# Typography Enhancements - Minimog Theme

## Overview

The Minimog theme now includes comprehensive typography enhancements with Google Fonts integration, curated font pairings, and advanced typography controls.

## New Features

### 1. Google Fonts Integration

- **Enable Google Fonts**: Toggle to activate Google Fonts loading
- **Font Preloading**: Optimized font loading with preconnect and preload
- **Font Display Swap**: Improves loading performance with fallback fonts

### 2. Curated Font Pairings

Choose from professionally curated font combinations:

#### Elegant Classic (Playfair Display + Nunito)
- **Best for**: Luxury brands, sophisticated designs, fashion
- **Heading**: Playfair Display (serif)
- **Body**: Nunito (sans-serif)
- **Mood**: Sophisticated, elegant, timeless

#### Modern SaaS (Inter + Inter)
- **Best for**: Tech companies, SaaS platforms, modern applications
- **Heading**: Inter (sans-serif)
- **Body**: Inter (sans-serif)
- **Mood**: Clean, modern, professional

#### Creative Bold (Oswald + Open Sans)
- **Best for**: Creative agencies, bold branding, marketing
- **Heading**: Oswald (sans-serif, condensed)
- **Body**: Open Sans (sans-serif)
- **Mood**: Bold, impactful, creative

#### Luxury Serif (Cormorant Garamond + Lato)
- **Best for**: Premium brands, luxury goods, editorial
- **Heading**: Cormorant Garamond (serif)
- **Body**: Lato (sans-serif)
- **Mood**: Luxurious, refined, classic

#### Minimalist Clean (Poppins + Poppins)
- **Best for**: Minimal designs, clean aesthetics, modern brands
- **Heading**: Poppins (sans-serif)
- **Body**: Poppins (sans-serif)
- **Mood**: Clean, minimal, friendly

#### Editorial Classic (Merriweather + Open Sans)
- **Best for**: Blogs, editorial content, news sites
- **Heading**: Merriweather (serif)
- **Body**: Open Sans (sans-serif)
- **Mood**: Readable, editorial, trustworthy

#### Tech Modern (Roboto + Roboto)
- **Best for**: Tech companies, Android apps, modern interfaces
- **Heading**: Roboto (sans-serif)
- **Body**: Roboto (sans-serif)
- **Mood**: Modern, technical, reliable

#### Artistic Creative (Montserrat + Source Sans Pro)
- **Best for**: Creative portfolios, art galleries, design studios
- **Heading**: Montserrat (sans-serif)
- **Body**: Source Sans Pro (sans-serif)
- **Mood**: Artistic, creative, versatile

#### Boutique Fashion (Crimson Text + Lato)
- **Best for**: Fashion brands, boutiques, lifestyle
- **Heading**: Crimson Text (serif)
- **Body**: Lato (sans-serif)
- **Mood**: Fashion-forward, elegant, boutique

#### Startup Friendly (Work Sans + Work Sans)
- **Best for**: Startups, modern businesses, tech companies
- **Heading**: Work Sans (sans-serif)
- **Body**: Work Sans (sans-serif)
- **Mood**: Approachable, modern, friendly

### 3. Typography Scales

Mathematical relationships for harmonious font sizing:

- **Minor Second (1.067)**: Subtle size differences
- **Major Second (1.125)**: Gentle progression
- **Minor Third (1.2)**: Balanced scaling (default)
- **Major Third (1.25)**: Noticeable differences
- **Perfect Fourth (1.333)**: Strong hierarchy
- **Augmented Fourth (1.414)**: Bold scaling
- **Perfect Fifth (1.5)**: Dramatic differences
- **Golden Ratio (1.618)**: Natural, pleasing proportions

### 4. Line Height Controls

- **Body Line Height Ratio**: Controls spacing for body text (default: 1.6)
- **Heading Line Height Ratio**: Controls spacing for headings (default: 1.2)

## Implementation Details

### File Structure

```
snippets/
├── font-face.liquid           # Enhanced font loading system
├── typography-preview.liquid  # Typography preview component
└── style-tags.liquid         # Enhanced CSS variables

config/
└── settings_schema.json      # New typography settings
```

### CSS Variables Generated

The system generates comprehensive CSS variables:

```css
/* Font Families */
--font-stack-header: 'Playfair Display', serif;
--font-stack-body: 'Nunito', sans-serif;

/* Font Sizes (responsive) */
--font-h1-desktop: 48px;
--font-h1-tablet: 34px;
--font-h1-mobile: 29px;
/* ... continues for h2-h6 */

/* Line Heights */
--line-height-body: 26px;
--line-height-h1: 58px;
--line-height-h2: 40px;
/* ... continues for h3-h6 */

/* Ratios */
--line-height-body-ratio: 1.6;
--line-height-heading-ratio: 1.2;
```

### Google Fonts URL Generation

The system automatically generates optimized Google Fonts URLs:

```liquid
https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400,500,600,700&family=Nunito:wght@300,400,500,600&display=swap
```

### Performance Optimizations

1. **Preconnect**: DNS resolution for Google Fonts
2. **Font Display Swap**: Fallback fonts while loading
3. **Selective Loading**: Only loads requested weights
4. **Combining Fonts**: Single request for multiple font families

## Usage Instructions

### 1. Enable Google Fonts

1. Go to Theme Settings → Typography
2. Enable "Google Fonts" checkbox
3. Choose a font pairing preset or select "Custom Selection"

### 2. Custom Font Selection

For custom fonts:
1. Set Font Pairing Preset to "Custom Selection"
2. Enter heading font name (e.g., "Playfair Display")
3. Enter body font name (e.g., "Nunito")
4. Specify font weights (e.g., "400,500,600,700")

### 3. Typography Scale

1. Choose a typography scale from the dropdown
2. Scales automatically calculate font sizes based on your base font size
3. Maintains consistent proportions across all headings

### 4. Line Height Control

1. Adjust body line height ratio (1.2 - 2.0)
2. Adjust heading line height ratio (1.0 - 1.8)
3. Values automatically calculate pixel line heights

## Preview System

Use the typography preview snippet to see changes:

```liquid
{% render 'typography-preview' %}
```

This displays:
- Current settings overview
- Font size hierarchy (H1-H6)
- Body text samples
- Font pairing information

## Best Practices

### Font Pairing Guidelines

1. **Contrast**: Pair serif headings with sans-serif body text (or vice versa)
2. **Hierarchy**: Ensure clear visual hierarchy between headings and body
3. **Readability**: Prioritize readability for body text
4. **Brand Alignment**: Choose fonts that match your brand personality

### Typography Scale Selection

- **Minor scales** (1.067-1.125): Subtle, professional
- **Medium scales** (1.2-1.333): Balanced, versatile
- **Large scales** (1.414-1.618): Bold, dramatic

### Line Height Recommendations

- **Body text**: 1.4-1.6 for optimal readability
- **Headings**: 1.1-1.3 for tight, impactful spacing
- **Small text**: 1.3-1.5 for better legibility

## Browser Support

- **Modern browsers**: Full support for Google Fonts and CSS variables
- **Legacy browsers**: Graceful fallback to system fonts
- **Font loading**: Progressive enhancement with font-display: swap

## Performance Considerations

1. **Font Loading**: Optimized with preconnect and preload
2. **Selective Weights**: Only loads necessary font weights
3. **Caching**: Google Fonts are cached across sites
4. **Fallbacks**: Immediate rendering with system fonts

## Troubleshooting

### Common Issues

1. **Fonts not loading**: Check internet connection and Google Fonts API
2. **Slow loading**: Reduce number of font weights loaded
3. **Layout shifts**: Ensure font-display: swap is enabled
4. **Typography scale not working**: Verify Google Fonts are enabled

### Debug Mode

Add this to any page to see current typography settings:

```liquid
{% render 'typography-preview' %}
```

## Migration from Previous Version

Existing typography settings are preserved:
- Shopify fonts continue to work
- Custom uploaded fonts remain functional
- Google Fonts are additive enhancement

## Future Enhancements

Planned features:
- Font subset optimization
- Variable font support
- Additional font pairings
- Advanced typography controls
- Performance monitoring

## Support

For questions or issues:
1. Check the typography preview for current settings
2. Verify Google Fonts are enabled
3. Test with different font pairings
4. Consult browser developer tools for CSS variables