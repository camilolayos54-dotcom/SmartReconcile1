# Deliverable 4: Design System & UI Kit [GLOBAL]

**Project:** SmartReconcile  
**Document ID:** D4-DESIGN-SYSTEM-UI-KIT  
**Phase:** 4 — System Modeling (Track A)  

---

## 1. Corporate Brand Identity & Palette (Bancolombia-Inspired)

The design system adopts a modern, high-contrast, charismatic financial palette inspired by enterprise banking standards (Bancolombia aesthetic):

```
Primary Navy/Charcoal: #0B192C (Deep, stable corporate base)
Accent Electric Yellow: #FFD200 (Bancolombia Yellow - High visibility highlights & primary badges)
Action Crimson Red:     #E11D48 (Vibrant Action & Error state highlights)
Success Emerald:        #10B981 (Matched status & positive metric indicators)
Warning Amber:          #F59E0B (Discrepancy alerts & unverified tags)
Dark Slate Surface:     #1E293B (Card containers & sidebar background)
Light Slate Surface:    #F8FAFC (Body background in Light Mode)
```

## 2. Tailwind CSS Color Tokens Configuration

```javascript
// tailwind.config.js
module.exports = {
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        brand: {
          navy: '#0B192C',
          dark: '#070F1E',
          yellow: '#FFD200',
          yellowHover: '#E6BC00',
          crimson: '#E11D48',
          crimsonHover: '#BE123C',
          emerald: '#10B981',
          amber: '#F59E0B',
          slate: '#1E293B',
          bgLight: '#F8FAFC',
        }
      },
      fontFamily: {
        sans: ['Inter', 'Roboto', 'sans-serif'],
        mono: ['JetBrains Mono', 'Fira Code', 'monospace'],
      }
    }
  }
}
```

## 3. Atomic Design Components Catalog

### A. Atoms
- **`Button`:**
  - `Primary`: `bg-brand-yellow text-brand-navy hover:bg-brand-yellowHover font-bold rounded-lg px-6 py-2.5 shadow-md`
  - `ActionRed`: `bg-brand-crimson text-white hover:bg-brand-crimsonHover font-bold rounded-lg px-6 py-2.5`
  - `Secondary`: `bg-brand-slate text-white border border-gray-700 hover:bg-gray-800 rounded-lg px-6 py-2.5`
- **`Badge`:**
  - `MATCHED`: `bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 px-3 py-1 rounded-full text-xs font-semibold`
  - `DISCREPANCY`: `bg-amber-500/10 text-amber-400 border border-amber-500/30 px-3 py-1 rounded-full text-xs font-semibold`
  - `ACTION_REQUIRED`: `bg-rose-500/10 text-rose-400 border border-rose-500/30 px-3 py-1 rounded-full text-xs font-semibold`
- **`Input`:** `bg-brand-dark text-white border border-gray-700 focus:border-brand-yellow focus:ring-1 focus:ring-brand-yellow rounded-lg px-4 py-2`

### B. Moléculas
- **`MetricCard`:** Container (`bg-brand-slate p-6 rounded-xl border border-gray-800 shadow-lg`) featuring Yellow Accent Icon, Large Monospace Value, and Trend Indicator.
- **`ReasoningCard`:** Dark Container with Yellow Border Accent (`border-l-4 border-brand-yellow bg-gray-900/80 p-4 rounded-r-lg`), markdown step-by-step text, and confidence score pill.

### C. Organisms
- **`AppHeaderNavbar`:** Fixed top header (`bg-brand-navy border-b border-gray-800 text-white`) with Bancolombia Yellow logo accent, tenant switcher, base currency selector, and WebSocket status indicator.
- **`SidebarNavigation`:** Collapsible left sidebar (`bg-brand-dark text-gray-300 border-r border-gray-800`) with active routes highlighted in yellow border-left.
