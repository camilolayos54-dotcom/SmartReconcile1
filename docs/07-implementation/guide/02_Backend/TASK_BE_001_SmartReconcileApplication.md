# TASK BE-001 — `SmartReconcileApplication.java`

**Módulo:** `backend-core/src/main/java/com/smartreconcile/`  
**Tipo de archivo:** Entry point de la aplicación Spring Boot (Java 21)  
**Prioridad:** CRÍTICA — Debe ser el primer archivo Java. Sin él no arranca nada.  
**Depende de:** `pom.xml` (TASK BE-002), `application.yml` (TASK BE-003)  
**Bloquea:** Todos los demás archivos del backend Java. Nada puede ejecutarse, compilarse ni testearse si este archivo no existe.  

---

## 1. Propósito

Este archivo es el **único punto de entrada** de la JVM para el servicio `backend-core`. Su responsabilidad es exactamente una: inicializar el contexto de Spring Boot y delegar todo el control al framework. No contiene lógica de negocio. No hace consultas. No expone endpoints. Es el equivalente al `main()` de C pero para un servidor empresarial.

Cuando ejecutas `java -jar backend-core.jar`, la JVM busca la clase con el método `main` declarado en el `MANIFEST.MF`, y esa clase es esta.

---

## 2. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear la estructura de directorios de Maven

Navega a la carpeta `backend-core/`. Spring Boot exige que el código fuente Java viva dentro de una estructura de paquetes estándar de Maven. Debes crear la cadena de directorios anidados `src/main/java/com/smartreconcile/`.

- **Por qué:** Maven y el compilador de Java necesitan esta estructura para resolver los paquetes. Si la ruta no coincide con la declaración `package` dentro del archivo `.java`, la compilación falla.
- **Detalle importante:** El nombre del paquete final debe ser `smartreconcile` en minúsculas, sin guiones ni mayúsculas. Esto define el paquete raíz que Spring Boot escaneará automáticamente para detectar componentes, controladores y repositorios.

### Paso 2: Crear el archivo físico

Dentro de la carpeta `com/smartreconcile/`, crea un nuevo archivo llamado `SmartReconcileApplication.java`.

- **Por qué PascalCase:** Java exige que el nombre de la clase pública coincida exactamente con el nombre del archivo. Si el archivo se llama `SmartReconcileApplication.java`, la clase dentro debe llamarse `SmartReconcileApplication`. Si no coinciden, el compilador lanza un error fatal.

### Paso 3: Declarar el paquete

La primera línea del archivo debe declarar el paquete al que pertenece: `com.smartreconcile`.

- **Por qué:** Esto le dice al compilador de Java dónde ubicar esta clase en el classpath. Spring Boot usa esta declaración de paquete como punto de anclaje para el escaneo de componentes (`@ComponentScan`). Todos los subpaquetes (como `com.smartreconcile.engine`, `com.smartreconcile.api`) serán detectados automáticamente porque son hijos de este paquete.
- **Consecuencia si falla:** Si el paquete está mal escrito o no coincide con la ruta de carpetas, los beans de subpaquetes no se detectan. Verás errores como `No qualifying bean of type` en tiempo de arranque.

### Paso 4: Añadir las importaciones necesarias

Después de la declaración del paquete, deja una línea en blanco y añade las importaciones de Spring Boot. Necesitas cuatro imports:

1. **`SpringApplication`** (del paquete `org.springframework.boot`): Es la clase utilitaria que arranca el contexto de Spring. La usarás en el método `main`.
2. **`@SpringBootApplication`** (del paquete `org.springframework.boot.autoconfigure`): Es una meta-anotación que combina tres cosas: `@Configuration` (marca la clase como fuente de configuración), `@EnableAutoConfiguration` (activa la autoconfiguración de Spring Boot basada en las dependencias del classpath), y `@ComponentScan` (escanea automáticamente los subpaquetes del paquete actual).
3. **`@EnableJpaAuditing`** (del paquete `org.springframework.data.jpa.repository.config`): Habilita la funcionalidad de auditoría automática de JPA. Esto permite que las anotaciones `@CreatedDate` y `@LastModifiedDate` en las entidades se llenen automáticamente con la fecha actual al persistir o actualizar registros.
4. **`@EnableScheduling`** (del paquete `org.springframework.scheduling.annotation`): Habilita el soporte para métodos anotados con `@Scheduled`. SmartReconcile usará tareas programadas (por ejemplo, limpieza de tokens JWT expirados, reintento de discrepancias fallidas).

### Paso 5: Declarar las anotaciones a nivel de clase

Justo encima de la declaración de la clase, coloca las tres anotaciones en este orden:
1. `@SpringBootApplication` — Obligatoria. Sin ella, Spring Boot no arranca.
2. `@EnableScheduling` — Necesaria para que cualquier `@Scheduled` funcione en el futuro.
3. `@EnableJpaAuditing` — Necesaria para que `created_at` y `updated_at` se llenen automáticamente en las entidades JPA.

- **Por qué ponerlas aquí y no en otra clase:** La convención de Spring Boot es centralizar estas anotaciones de bootstrap en la clase principal para máxima visibilidad. Técnicamente podrían estar en una clase `@Configuration` separada, pero dispersarlas dificulta que alguien nuevo entienda qué funcionalidades están habilitadas en el proyecto.

### Paso 6: Declarar la clase y el método `main`

Declara una clase pública con el mismo nombre que el archivo. Dentro, define el método `main` con la firma estándar de Java: `public static void main(String[] args)`.

Dentro del método `main`, invoca `SpringApplication.run()` pasándole dos argumentos:
1. **La propia clase** (`SmartReconcileApplication.class`): Spring necesita saber cuál es la clase de configuración raíz.
2. **`args`** (los argumentos de línea de comandos): Es crítico pasar `args` porque en entornos de producción y CI/CD (Docker, Kubernetes, Railway) se inyectan propiedades vía argumentos de línea de comandos (ej: `--spring.profiles.active=prod`). Si no pasas `args`, esas propiedades se ignoran silenciosamente.

- **Por qué la clase debe ser `public`:** `SpringApplication.run()` necesita instanciar esta clase internamente. Si no es pública, el framework no puede accederla desde fuera del paquete.

---

## 3. Condiciones que debe cumplir (Checklist de Verificación)

| # | Condición | Consecuencia si falla |
|---|-----------|----------------------|
| 1 | Package declarado como `com.smartreconcile` | Los beans de subpaquetes no son detectados por `@ComponentScan`. Error: `No qualifying bean` |
| 2 | Anotación `@SpringBootApplication` presente | La aplicación no arranca. Error fatal en contexto de Spring |
| 3 | Anotación `@EnableScheduling` presente | Los métodos `@Scheduled` no se ejecutan nunca |
| 4 | Anotación `@EnableJpaAuditing` presente | Los campos `created_at` y `updated_at` quedan `null` en todas las entidades |
| 5 | Clase declarada como `public` | `SpringApplication.run()` no puede instanciarla |
| 6 | Método `main` con firma exacta `public static void main(String[] args)` | La JVM no puede iniciar el proceso |
| 7 | `SpringApplication.run()` pasa `args` como segundo parámetro | Propiedades de línea de comandos ignoradas en Docker/Kubernetes |
| 8 | Ninguna lógica de negocio dentro de la clase | Viola el principio de responsabilidad única |
| 9 | Nombre del archivo coincide exactamente con el nombre de la clase | Error de compilación: `public class must match file name` |

---

## 4. Errores comunes a evitar

1. **Olvidar pasar `args` a `SpringApplication.run()`:** Escribir `.run(SmartReconcileApplication.class)` sin `args`. Docker y Kubernetes inyectan propiedades por línea de comandos; sin `args`, se ignoran.
2. **Poner `@EnableJpaAuditing` en una clase `JpaConfig.java` separada:** Funciona técnicamente, pero dispersa la configuración de bootstrap y reduce la visibilidad.
3. **Agregar lógica de inicialización aquí (ej: cargar datos seed):** Si necesitas ejecutar algo al arranque, crea un `@Bean` de tipo `CommandLineRunner` en una clase separada. No contamines este archivo.
4. **Usar `com.smart_reconcile` o `com.SmartReconcile` como paquete:** Java es case-sensitive. El paquete debe ser todo en minúsculas: `com.smartreconcile`.

---

## 5. Cómo verificar que funciona correctamente

1. Asegúrate de que `pom.xml` (TASK BE-002) y `application.yml` (TASK BE-003) ya estén creados, y que PostgreSQL y Redis estén corriendo localmente (vía Docker Compose).
2. En tu terminal, sitúate en la raíz del proyecto backend: `cd backend-core/`.
3. Ejecuta la aplicación usando el Maven Wrapper: `./mvnw spring-boot:run`.
4. **Salida esperada en consola:** Verás el banner de Spring Boot en arte ASCII y una línea que dice:
   ```
   Started SmartReconcileApplication in X.XXX seconds (process running for X.XXX)
   ```
   Si ves ese mensaje, la tarea está completa.

---

*Próxima tarea: TASK BE-002 — `pom.xml` (Dependencias Maven del proyecto Java)*
