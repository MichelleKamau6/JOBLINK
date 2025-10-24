# JobLink Design System

## Color Palette

### Primary Colors
- **Primary 50**: `#eff6ff` - Light background
- **Primary 500**: `#3b82f6` - Main brand color
- **Primary 600**: `#2563eb` - Primary buttons
- **Primary 700**: `#1d4ed8` - Hover states

### Secondary Colors
- **Secondary 50**: `#f8fafc` - Light backgrounds
- **Secondary 500**: `#64748b` - Text secondary
- **Secondary 600**: `#475569` - Text primary

### Status Colors
- **Success**: `#10b981` - Success states
- **Warning**: `#f59e0b` - Warning states
- **Error**: `#ef4444` - Error states
- **Info**: `#3b82f6` - Info states

## Typography

### Font Family
- Primary: `system-ui, -apple-system, sans-serif`
- Monospace: `ui-monospace, monospace`

### Font Sizes
- **xs**: 12px
- **sm**: 14px
- **base**: 16px
- **lg**: 18px
- **xl**: 20px
- **2xl**: 24px
- **3xl**: 30px
- **4xl**: 36px

## Components

### Buttons

#### Primary Button
```css
.btn-primary {
  @apply bg-primary-600 hover:bg-primary-700 text-white font-medium py-2 px-4 rounded-lg transition-colors;
}
```

#### Secondary Button
```css
.btn-secondary {
  @apply bg-secondary-100 hover:bg-secondary-200 text-secondary-700 font-medium py-2 px-4 rounded-lg transition-colors;
}
```

### Cards
```css
.card {
  @apply bg-white rounded-lg shadow-md p-6;
}
```

### Forms
- Input fields use Tailwind's form plugin
- Focus states use primary color
- Error states use red color scheme

## Spacing

- **xs**: 4px
- **sm**: 8px
- **md**: 16px
- **lg**: 24px
- **xl**: 32px
- **2xl**: 48px

## Breakpoints

- **sm**: 640px
- **md**: 768px
- **lg**: 1024px
- **xl**: 1280px
- **2xl**: 1536px

## Usage Guidelines

1. Use primary colors for main actions and branding
2. Use secondary colors for supporting elements
3. Maintain consistent spacing using the defined scale
4. Ensure proper contrast ratios for accessibility
5. Use semantic color names for status indicators

## Figma Integration

- Design tokens are mapped to Tailwind CSS classes
- Components are built to match Figma designs exactly
- Assets exported from Figma should be placed in `/docs/assets/`