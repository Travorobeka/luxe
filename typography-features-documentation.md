# Enterprise Typography Customization Features

## Overview

This Shopify theme now includes enterprise-level typography customization features that provide advanced control over fonts, including Google Fonts integration, professional font pairing templates, and advanced typography settings.

## Features

### 1. Font Source Selection

Choose from multiple font sources:
- **Shopify Fonts**: Use Shopify's built-in font library
- **Google Fonts**: Access thousands of Google Fonts
- **Custom Fonts**: Upload and use your own font files
- **Font Pairing Templates**: Professional pre-configured font combinations

### 2. Google Fonts Integration

- Enter any Google Font name to use it in your theme
- Specify custom font weights for both headings and body text
- Optional API key support for advanced features
- Automatic font loading optimization

### 3. Font Pairing Templates

Professional font combinations that work well together:

1. **Modern Minimal** - Inter + Inter
   - Clean, modern sans-serif for all text
   - Perfect for minimalist designs

2. **Classic Editorial** - Playfair Display + Source Sans Pro
   - Elegant serif headings with readable sans-serif body
   - Great for blogs and editorial content

3. **Tech Modern** - Roboto + Roboto Mono
   - Technical and clean appearance
   - Ideal for tech/software companies

4. **Elegant Fashion** - Cormorant Garamond + Montserrat
   - Sophisticated serif with modern sans-serif
   - Perfect for fashion and luxury brands

5. **Playful Creative** - Fredoka + Open Sans
   - Fun, rounded headings with clean body text
   - Great for creative agencies and children's brands

6. **Professional Corporate** - Lato + Merriweather
   - Trustworthy and readable combination
   - Ideal for corporate and professional services

7. **Luxury Premium** - Bodoni Moda + Raleway
   - High-contrast serif with elegant sans-serif
   - Perfect for luxury and premium brands

8. **Clean Swiss** - Work Sans + Work Sans
   - Consistent, clean typography throughout
   - Great for modern, minimalist designs

### 4. Advanced Typography Settings

#### Font Loading Optimization
- **Font Loading Strategy**: Control how fonts are displayed while loading
  - Auto: Browser decides
  - Block: Hide text until font loads
  - Swap: Show fallback, then swap
  - Fallback: Quick swap with short block period
  - Optional: Use font only if already cached

- **Preload Critical Fonts**: Improves performance by loading fonts early

#### Responsive Typography
- **Enable Responsive Typography**: Automatically adjust font sizes based on screen size
- **Scale Factors**: Set minimum and maximum scale factors for different screen sizes

#### Typography Presets
- **Compact**: Smaller sizes, tighter spacing for information-dense layouts
- **Balanced**: Default sizing for most use cases
- **Comfortable**: Larger sizes, relaxed spacing for better readability
- **Accessible**: WCAG AAA compliant sizing for maximum accessibility

#### OpenType Features
- Enable advanced typography features like ligatures
- Custom OpenType feature settings (liga, kern, calt, etc.)
- Variable font support for smoother weight transitions

### 5. Additional Features

- **Font Smoothing**: Improves font rendering on screens
- **Variable Fonts**: Enable smoother weight transitions and smaller file sizes
- **Fluid Typography**: Responsive font sizes that scale smoothly with viewport
- **Dark Mode Adjustments**: Automatic contrast adjustments for dark themes
- **Print Optimization**: Specific typography settings for printed pages

## Usage Instructions

### Setting Up Google Fonts

1. Navigate to **Theme Settings > Typography**
2. Select "Google fonts" from the **Font source** dropdown
3. Enter the exact Google Font name for headings (e.g., "Roboto", "Open Sans")
4. Enter the font weights you want to load (e.g., "300,400,700")
5. Repeat for body font
6. Save your settings

### Using Font Templates

1. Navigate to **Theme Settings > Typography**
2. Select "Font pairing templates" from the **Font source** dropdown
3. Choose a template from the **Select font pairing** dropdown
4. Save your settings

### Enabling Advanced Features

1. Scroll to the **Advanced Typography** section
2. Enable desired features:
   - Font smoothing for better rendering
   - Responsive typography for automatic scaling
   - Typography presets for quick style changes
   - OpenType features for professional typography

### Performance Optimization

1. Enable **Preload critical fonts** for faster loading
2. Choose appropriate **Font loading strategy** based on your needs
3. Use **Variable fonts** when available for better performance

## CSS Classes Available

The following utility classes are available for use in your theme:

### Fluid Typography
- `.fluid-text-xs` to `.fluid-text-5xl` - Responsive font sizes

### Font Pairing Styles
- `.font-pairing-modern-minimal`
- `.font-pairing-classic-serif`
- `.font-pairing-elegant-fashion`
- `.font-pairing-luxury-premium`

### Typography Features
- `.drop-cap-enabled` - Enable drop caps for first letter
- `.text-balance` - Better text wrapping
- `.optical-alignment-enabled` - Hanging punctuation
- `.high-contrast-mode` - Improved contrast
- `.dyslexia-friendly` - Accessibility mode

## Theme Editor Integration

When in the theme editor:
- Typography changes preview in real-time
- Font loading indicator shows loading progress
- Debug mode available for troubleshooting

## Browser Support

- All modern browsers (Chrome, Firefox, Safari, Edge)
- Graceful fallbacks for older browsers
- Progressive enhancement for advanced features

## Performance Considerations

- Google Fonts are loaded asynchronously
- Only requested font weights are loaded
- Fonts are cached for improved performance
- Variable fonts reduce file size when available

## Troubleshooting

### Fonts Not Loading
1. Check font name spelling (must match Google Fonts exactly)
2. Verify font weights are available for chosen font
3. Clear browser cache and reload

### Performance Issues
1. Reduce number of font weights loaded
2. Enable font preloading
3. Use "optional" loading strategy for non-critical fonts

### Display Issues
1. Enable font smoothing for better rendering
2. Check responsive typography scale factors
3. Test with different typography presets