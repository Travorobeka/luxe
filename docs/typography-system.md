# Unified Typography System

## Overview

The Unified Typography System combines all typography functionality into a single, comprehensive system that provides:

- **Three-tier typography system** (Main Heading, Sub Heading, Body Text)
- **Responsive typography** with fluid scaling
- **Accessibility features** for better user experience
- **Performance optimizations** for faster loading
- **Legacy compatibility** for existing code
- **Utility classes** and modifiers for flexibility

## Files

### Core Files
- `assets/typography.css` - Main typography styles and system
- `assets/typography.js` - JavaScript functionality and dynamic updates
- `config/settings_schema.json` - Theme customizer settings

### Removed Files
- `assets/typography-utilities.css` - Merged into `typography.css`

## Three-Tier System

### 1. Main Heading
- **Usage**: Primary page titles, hero sections, major section headers
- **Replaces**: H1, H2 elements
- **CSS Class**: `.main-heading`
- **Default Size**: 42px
- **Default Weight**: 700 (Bold)

### 2. Sub Heading
- **Usage**: Secondary titles, section headers, card titles
- **Replaces**: H3, H4 elements
- **CSS Class**: `.sub-heading`
- **Default Size**: 24px
- **Default Weight**: 600 (Semi-bold)

### 3. Body Text
- **Usage**: Paragraphs, descriptions, minor labels
- **Replaces**: H5, H6, body text
- **CSS Class**: `.body-text`
- **Default Size**: 16px
- **Default Weight**: 400 (Regular)

## CSS Custom Properties

The system uses CSS custom properties for easy customization:

```css
:root {
  /* Font Stacks */
  --font-stack-header: var(--type_header_font, 'Helvetica Neue', Helvetica, Arial, sans-serif);
  --font-stack-body: var(--type_body_font, 'Helvetica Neue', Helvetica, Arial, sans-serif);
  
  /* Three-Tier System Variables */
  --font-size-main-heading: var(--main_heading_font_size, 42px);
  --font-size-sub-heading: var(--sub_heading_font_size, 24px);
  --font-size-body-text: var(--body_font_size, 16px);
  
  --font-weight-main-heading: var(--main_heading_font_weight, 700);
  --font-weight-sub-heading: var(--sub_heading_font_weight, 600);
  --font-weight-body-text: var(--body_font_weight, 400);
  
  --line-height-main-heading: var(--main_heading_line_height, 1.2);
  --line-height-sub-heading: var(--sub_heading_line_height, 1.3);
  --line-height-body-text: var(--body_line_height, 1.5);
  
  --letter-spacing-main-heading: var(--main_heading_letter_spacing, 0px);
  --letter-spacing-sub-heading: var(--sub_heading_letter_spacing, 0px);
  --letter-spacing-body-text: var(--body_letter_spacing, 0px);
}
```

## Responsive Typography

### Breakpoint System
- **Desktop**: Default sizes
- **Tablet** (≤1023px): 85-95% of desktop sizes
- **Mobile** (≤767px): 70-90% of desktop sizes

### Fluid Typography
When enabled, typography scales smoothly between breakpoints using CSS `clamp()`:

```css
.main-heading {
  font-size: clamp(
    calc(var(--font-size-main-heading) * var(--mobile-typography-scale)),
    5vw,
    var(--font-size-main-heading)
  );
}
```

## Utility Classes

### Size Modifiers
```css
.main-heading--large    /* 120% of base size */
.main-heading--small    /* 80% of base size */
.sub-heading--large     /* 120% of base size */
.sub-heading--small     /* 80% of base size */
.body-text--large       /* 112.5% of base size */
.body-text--small       /* 87.5% of base size */
```

### Weight Modifiers
```css
.typography--light      /* 300 */
.typography--normal     /* 400 */
.typography--medium     /* 500 */
.typography--semibold   /* 600 */
.typography--bold       /* 700 */
.typography--extrabold  /* 800 */
```

### Color Modifiers
```css
.typography--muted      /* Secondary text color */
.typography--accent     /* Button color */
.typography--inverse    /* Background color */
```

### Text Transform Modifiers
```css
.typography--uppercase
.typography--lowercase
.typography--capitalize
```

### Text Alignment Modifiers
```css
.typography--left
.typography--center
.typography--right
.typography--justify
```

## Accessibility Features

### Reduced Motion Support
Automatically detects `prefers-reduced-motion` and disables animations:

```css
@media (prefers-reduced-motion: reduce) {
  .main-heading,
  .sub-heading,
  .body-text {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

### High Contrast Support
Enhances contrast for users with `prefers-contrast: high`:

```css
@media (prefers-contrast: high) {
  .main-heading,
  .sub-heading,
  .body-text {
    color: #000000 !important;
  }
}
```

### Font Loading Optimization
Uses `font-display: swap` for better performance:

```css
.main-heading, .sub-heading, .body-text {
  font-display: swap;
}
```

## JavaScript Integration

### TypographySystem Class
```javascript
// Initialize the system
window.TypographySystem = new TypographySystem();

// Update settings dynamically
window.TypographySystem.updateSettings({
  'font-size-main-heading': '48px',
  'font-weight-main-heading': '800'
});

// Apply typography class to element
window.TypographySystem.applyTypographyClass(element, 'main-heading');

// Get current settings
const settings = window.TypographySystem.getCurrentSettings();
```

### Global API
```javascript
// Update settings
window.MinimogTypography.updateSettings(settings);

// Get settings
const currentSettings = window.MinimogTypography.getSettings();

// Apply class to element
window.MinimogTypography.applyClass(element, 'main-heading');
```

### Events
```javascript
// Listen for font loading
window.addEventListener('typography:fonts-loaded', (event) => {
  console.log('Fonts loaded at:', event.detail.timestamp);
});

// Listen for typography updates
window.addEventListener('typography:updated', (event) => {
  console.log('Typography updated:', event.detail.settings);
});
```

## Migration Guide

### From H1-H6 System
Replace individual heading elements with unified classes:

```html
<!-- Old -->
<h1>Page Title</h1>
<h2>Section Title</h2>
<h3>Subsection Title</h3>

<!-- New -->
<h1 class="main-heading">Page Title</h1>
<h2 class="main-heading">Section Title</h2>
<h3 class="sub-heading">Subsection Title</h3>
```

### From Legacy Font Classes
Replace legacy font size classes:

```html
<!-- Old -->
<div class="font-size--large">Large Text</div>
<div class="font-size--medium">Medium Text</div>
<div class="font-size--small">Small Text</div>

<!-- New -->
<div class="main-heading">Large Text</div>
<div class="sub-heading">Medium Text</div>
<div class="body-text">Small Text</div>
```

## Performance Considerations

### Font Loading
- Uses `font-display: swap` for faster perceived loading
- Preloads critical fonts when enabled
- Falls back gracefully for older browsers

### CSS Optimization
- Minimal CSS with utility classes
- Efficient selectors and specificity
- Optimized for critical rendering path

### JavaScript Performance
- Lazy loading of non-critical features
- Debounced resize handlers
- Efficient DOM queries and updates

## Browser Support

### CSS Features
- **CSS Custom Properties**: IE11+ (with polyfill)
- **CSS Grid**: IE11+ (with polyfill)
- **CSS clamp()**: Chrome 79+, Firefox 75+, Safari 13.1+
- **font-display**: Chrome 60+, Firefox 58+, Safari 11.1+

### JavaScript Features
- **Intersection Observer**: Chrome 51+, Firefox 55+, Safari 12.1+
- **Font Loading API**: Chrome 35+, Firefox 41+, Safari 10+
- **matchMedia**: All modern browsers

## Troubleshooting

### Common Issues

1. **Fonts not loading**
   - Check font URLs in theme settings
   - Verify font-display settings
   - Check browser console for errors

2. **Typography not updating**
   - Verify CSS custom properties are set
   - Check JavaScript console for errors
   - Ensure theme customizer is working

3. **Responsive issues**
   - Check viewport meta tag
   - Verify media query breakpoints
   - Test on actual devices

### Debug Mode
Enable typography debugging:

```javascript
window.TypographySystem.enableDebugging();
```

This will:
- Add visual indicators to typography elements
- Log current settings to console
- Show CSS custom property values

## Best Practices

### Content Structure
- Use semantic HTML elements
- Apply appropriate typography classes
- Maintain consistent hierarchy

### Performance
- Minimize font file sizes
- Use font subsetting when possible
- Optimize critical rendering path

### Accessibility
- Maintain sufficient color contrast
- Use appropriate font sizes
- Respect user preferences

### Maintenance
- Keep typography system updated
- Test across different devices
- Monitor performance metrics 