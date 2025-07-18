# Advanced Typography Customization

This document explains the new typography customization features added to your Shopify theme.

## Overview

The advanced typography system provides extensive control over your store's text appearance, including:
- Advanced font settings
- Paragraph and text styling
- Mobile-optimized typography
- Special effects and utilities
- Performance optimizations

## Features

### 1. Paragraph Settings
- **Paragraph Spacing**: Control the space between paragraphs (8-32px)
- **First Line Indent**: Add indentation to the first line of paragraphs (0-50px)

### 2. Heading Customization
- **Text Transform**: Apply uppercase, lowercase, capitalize, or none to all headings
- **Font Style**: Choose between normal or italic for headings
- **Line Height**: Adjust heading line height with a multiplier (1.0-2.0)
- **Text Shadow**: Enable and customize text shadows on headings

### 3. Link Styling
- **Decoration Options**:
  - None: No underline
  - Underline: Always underlined
  - Underline on Hover: Only underlined when hovered
- **Bold Links**: Option to make all links bold

### 4. Small Text & Captions
- **Small Text Size**: Control size for small text elements (10-16px)
- **Caption Size**: Set specific size for image captions (10-14px)
- **Caption Transform**: Apply text transform to captions

### 5. Mobile Typography
- **Font Scale**: Scale all fonts on mobile devices (0.7-1.1x)
- **Line Height Reduction**: Optionally reduce line height on mobile for better fit

### 6. Special Effects
- **Drop Caps**: Enable large first letters in article paragraphs
- **Drop Cap Size**: Control the size of drop caps (2-5x line height)

## Usage

### Theme Customizer
1. Go to **Online Store > Themes > Customize**
2. Navigate to **Theme Settings > Typography**
3. Scroll to **Advanced Typography** section
4. Adjust settings as needed
5. Save changes

### CSS Utility Classes

The system includes utility classes for manual typography control:

#### Text Transform
- `.text-uppercase` - UPPERCASE text
- `.text-lowercase` - lowercase text
- `.text-capitalize` - Capitalize Text
- `.text-normal` - Normal text

#### Font Weight
- `.font-thin` - Weight 100
- `.font-light` - Weight 300
- `.font-normal` - Weight 400
- `.font-medium` - Weight 500
- `.font-semibold` - Weight 600
- `.font-bold` - Weight 700
- `.font-extrabold` - Weight 800
- `.font-black` - Weight 900

#### Letter Spacing
- `.letter-spacing-tight` - Tight spacing
- `.letter-spacing-normal` - Normal spacing
- `.letter-spacing-wide` - Wide spacing
- `.letter-spacing-wider` - Wider spacing
- `.letter-spacing-widest` - Widest spacing

#### Line Height
- `.leading-none` - Line height 1
- `.leading-tight` - Line height 1.25
- `.leading-snug` - Line height 1.375
- `.leading-normal` - Line height 1.5
- `.leading-relaxed` - Line height 1.625
- `.leading-loose` - Line height 2

#### Text Shadow
- `.text-shadow-sm` - Small shadow
- `.text-shadow` - Default shadow
- `.text-shadow-md` - Medium shadow
- `.text-shadow-lg` - Large shadow
- `.text-shadow-none` - No shadow

#### Other Utilities
- `.hyphens-auto` - Automatic hyphenation
- `.break-words` - Break long words
- `.whitespace-nowrap` - Prevent text wrapping

### Responsive Classes

Add responsive prefixes for different screen sizes:
- `md:` - Tablet and up (≥768px)
- `lg:` - Desktop and up (≥1024px)

Example: `md:text-uppercase lg:font-bold`

## JavaScript API

Access typography utilities via JavaScript:

```javascript
// Apply optimal line length to custom elements
TypographyUtils.applyOptimalLineLength('.my-content');

// Enable hyphenation
TypographyUtils.enableHyphenation('.my-text p');

// Balance heading text
TypographyUtils.balanceHeadings();
```

## Performance

The typography system includes several performance optimizations:
- Deferred CSS loading
- Font display swap for faster text rendering
- Optimized font loading strategies
- Minimal JavaScript footprint

## Accessibility

Built-in accessibility features:
- Respects user preferences for reduced motion
- High contrast mode support
- Print-friendly styles
- Proper semantic markup

## Browser Support

All features work in modern browsers:
- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers

Some advanced features (like text-wrap: balance) gracefully degrade in older browsers.

## Troubleshooting

### Fonts Not Loading
- Check custom font URLs are correct
- Ensure font files are in supported formats (WOFF, WOFF2)
- Verify font weights match your settings

### Drop Caps Not Showing
- Enable drop caps in theme settings
- Ensure content has proper paragraph tags
- Check for conflicting CSS

### Mobile Scaling Issues
- Adjust mobile font scale setting
- Test on actual devices, not just browser DevTools
- Check for viewport meta tag

## Examples

### Custom Drop Cap Style
```css
.custom-drop-cap:first-letter {
  color: rgb(var(--color-accent));
  font-size: 4em;
  float: left;
  margin-right: 0.1em;
}
```

### Responsive Typography
```html
<h2 class="text-uppercase md:text-normal lg:text-capitalize">
  Responsive Heading
</h2>
```

### Optimal Reading Experience
```html
<article class="rte hyphens-auto">
  <p class="drop-cap">Your article content...</p>
</article>
```

## Support

For issues or questions:
1. Check theme documentation
2. Review browser console for errors
3. Contact theme support with specific details

---

Last updated: [Current Date]
Version: 1.0.0