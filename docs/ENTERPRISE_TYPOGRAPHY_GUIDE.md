# Enterprise Typography Features Guide

## Overview

This guide covers the enterprise-level typography features added to the Minimog theme. These features provide advanced customization capabilities for businesses requiring sophisticated typography control.

## Features Added

### 1. Advanced Typography Controls

#### Main Heading Customization
- **Font Size**: 24px - 80px range
- **Font Weight**: 400, 500, 600, 700, 800
- **Line Height**: 0.8x - 2.0x ratio
- **Letter Spacing**: -2px to +5px
- **Text Transform**: None, Uppercase, Lowercase, Capitalize
- **Text Decoration**: None, Underline, Overline, Line-through
- **Text Shadow**: Custom CSS text-shadow support
- **Responsive Scaling**: Separate mobile and tablet scale factors

#### Sub Heading Customization
- **Font Size**: 18px - 48px range
- **Font Weight**: 400, 500, 600, 700
- **Line Height**: 0.8x - 2.0x ratio
- **Letter Spacing**: -2px to +5px
- **Text Transform**: None, Uppercase, Lowercase, Capitalize
- **Text Decoration**: None, Underline, Overline, Line-through
- **Text Shadow**: Custom CSS text-shadow support
- **Responsive Scaling**: Separate mobile and tablet scale factors

#### Body Text Customization
- **Font Size**: 12px - 24px range
- **Font Weight**: 300, 400, 500, 600
- **Line Height**: 1.0x - 2.5x ratio
- **Letter Spacing**: -1px to +3px
- **Text Transform**: None, Uppercase, Lowercase, Capitalize

### 2. Typography Presets

Quick-apply presets for different brand aesthetics:

#### Modern Minimal
- Clean, light typography with generous spacing
- Main: 36px, Light (300), -0.5px letter spacing
- Sub: 20px, Regular (400), normal spacing
- Body: 16px, Regular (400), 1.6x line height

#### Elegant Serif
- Sophisticated serif styling with elegant proportions
- Main: 48px, Regular (400), -0.3px letter spacing
- Sub: 28px, Medium (500), 1.4x line height
- Body: 18px, Regular (400), 0.2px letter spacing

#### Bold Impact
- Strong, attention-grabbing typography
- Main: 56px, Extra Bold (800), uppercase, text shadow
- Sub: 32px, Bold (700), uppercase, subtle shadow
- Body: 16px, Medium (500), 0.3px letter spacing

#### Clean Corporate
- Professional, readable typography for business use
- Main: 40px, Semi Bold (600), -0.2px letter spacing
- Sub: 22px, Semi Bold (600), balanced spacing
- Body: 15px, Regular (400), 1.6x line height

#### Creative Artistic
- Expressive typography with decorative elements
- Main: 44px, Bold (700), capitalize, strong shadow
- Sub: 26px, Semi Bold (600), underline decoration
- Body: 17px, Regular (400), 0.1px letter spacing

### 3. Fluid Typography

#### Responsive Scaling
- **Mobile Scale Factor**: 0.5x - 1.2x (default: 0.8x)
- **Tablet Scale Factor**: 0.6x - 1.1x (default: 0.9x)
- **Custom Breakpoints**: Configurable min/max viewport widths

#### Fluid Typography Support
- **CSS Clamp**: Automatic scaling between breakpoints
- **Viewport Units**: Typography scales with screen size
- **Progressive Enhancement**: Fallback to fixed sizes if unsupported

### 4. Accessibility Features

#### User Preference Respect
- **Reduced Motion**: Disables animations for sensitive users
- **High Contrast**: Increases font weights for better readability
- **System Preferences**: Automatically adapts to user settings

#### WCAG Compliance
- **Contrast Ratio**: Configurable minimum contrast (3.0:1 - 7.0:1)
- **Font Weight**: Automatic adjustments for accessibility
- **Focus Management**: Improved keyboard navigation

### 5. Performance Optimizations

#### Font Loading Strategy
- **Font Display**: Configurable strategy (auto, block, swap, fallback, optional)
- **Loading Optimization**: Improved FOIT/FOUT handling
- **Critical Path**: Optimized above-the-fold typography

#### Resource Management
- **Conditional Loading**: Features load only when needed
- **CSS Variables**: Efficient property updates
- **Browser Caching**: Optimized asset delivery

## Implementation Guide

### Theme Settings Access

Navigate to **Theme Settings > Typography** to access enterprise features:

1. **Main Heading Customization** - Primary page titles and hero text
2. **Sub Heading Customization** - Section headers and secondary titles
3. **Body Text Customization** - Content text and small headings
4. **Typography Presets** - Quick-apply brand styles
5. **Advanced Typography Options** - Fluid typography and optimization

### CSS Variables Available

The system exposes these CSS variables for custom development:

```css
/* Main Heading */
--font-main-heading-desktop
--font-main-heading-tablet
--font-main-heading-mobile
--font-weight-main-heading
--line-height-main-heading-ratio
--letter-spacing-main-heading
--text-transform-main-heading
--text-decoration-main-heading
--text-shadow-main-heading

/* Sub Heading */
--font-sub-heading-desktop
--font-sub-heading-tablet
--font-sub-heading-mobile
--font-weight-sub-heading
--line-height-sub-heading-ratio
--letter-spacing-sub-heading
--text-transform-sub-heading
--text-decoration-sub-heading
--text-shadow-sub-heading

/* Body Text */
--font-body-text-desktop
--font-body-text-tablet
--font-body-text-mobile
--font-weight-body-text
--line-height-body-text-ratio
--letter-spacing-body-text
--text-transform-body-text

/* Advanced */
--enable-fluid-typography
--fluid-typography-min-width
--fluid-typography-max-width
--font-display-strategy
--accessibility-min-contrast
```

### JavaScript API

The typography system provides a JavaScript API for custom functionality:

```javascript
// Apply a preset programmatically
window.MinimogTypography.applyPreset('modern_minimal');

// Access preset definitions
const presets = window.MinimogTypography.presets;

// Listen for preset changes
document.addEventListener('typography-preset-applied', function(e) {
  console.log('Preset applied:', e.detail.preset);
});
```

## Best Practices

### 1. Typography Hierarchy

- **Main Heading**: Use sparingly for primary page elements
- **Sub Heading**: Section headers and important content
- **Body Text**: Regular content, captions, and small headings

### 2. Responsive Design

- Test all typography at different screen sizes
- Use appropriate scale factors for mobile and tablet
- Consider fluid typography for smooth scaling

### 3. Accessibility

- Maintain minimum contrast ratios (4.5:1 for normal text)
- Test with high contrast mode enabled
- Verify readability with screen readers

### 4. Performance

- Use font-display: swap for better loading performance
- Minimize the number of font weights loaded
- Test loading performance on slow connections

## Customization Examples

### Custom Preset Creation

```javascript
// Define a custom preset
const customPreset = {
  main_heading_font_size: 50,
  main_heading_font_weight: '600',
  main_heading_line_height: 1.1,
  main_heading_letter_spacing: -0.8,
  main_heading_text_transform: 'uppercase',
  // ... other properties
};

// Apply the custom preset
window.MinimogTypography.applyPreset('custom', customPreset);
```

### Dynamic Typography Updates

```javascript
// Update typography based on user interaction
function updateTypographyForDarkMode() {
  const root = document.documentElement;
  root.style.setProperty('--font-weight-main-heading', '700');
  root.style.setProperty('--text-shadow-main-heading', '2px 2px 4px rgba(255,255,255,0.1)');
}
```

## Testing & Validation

### Visual Testing

1. **Typography Test Suite**: Use `{% render 'typography-test-suite' %}` in templates
2. **Cross-Browser**: Test in Chrome, Firefox, Safari, Edge
3. **Device Testing**: Verify on mobile, tablet, and desktop
4. **Accessibility**: Test with screen readers and high contrast mode

### Performance Testing

1. **Font Loading**: Monitor FOIT/FOUT behavior
2. **Render Speed**: Measure time to first meaningful paint
3. **Memory Usage**: Check for CSS variable performance impact

## Troubleshooting

### Common Issues

1. **Preset Not Applying**: Check JavaScript console for errors
2. **Fluid Typography Not Working**: Verify browser support for CSS clamp()
3. **Accessibility Features Not Loading**: Ensure settings are properly configured

### Support Resources

- **Documentation**: Reference this guide and CLAUDE.md
- **CSS Variables**: Inspect element to verify variable values
- **JavaScript API**: Use browser console to test functionality

## Migration Notes

### From Basic Typography

All existing typography settings remain functional through backward compatibility mapping. Enterprise features are additive and don't break existing customizations.

### Settings Migration

- H1-H6 settings automatically map to three-tier system
- Existing customizations are preserved
- New features are opt-in and don't affect existing sites

## Future Enhancements

### Planned Features

1. **Font Pairing**: Automatic font combinations
2. **Typography Analytics**: Usage tracking and optimization
3. **AI-Powered Presets**: Dynamic preset generation
4. **Advanced Animations**: Typography-specific animations

### API Expansion

- Additional CSS variables for micro-typography
- Enhanced JavaScript API for theme integrations
- Shopify Plus features for enterprise customers

---

**Version**: 1.0  
**Updated**: January 2025  
**Compatibility**: Minimog 5.7.0+  
**Support**: Enterprise Typography Features