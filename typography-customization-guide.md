# Typography Customization Guide - Streamlined Version

## Overview

This Shopify theme includes a comprehensive yet streamlined typography customization system that provides powerful control over all text elements while maintaining simplicity and performance.

## Key Features

### 1. **Unified Typography Control**
- Single location for all typography settings
- Intelligent inheritance system reduces redundancy
- Global settings that cascade throughout the theme

### 2. **Smart Defaults**
- "Inherit" options prevent unnecessary overrides
- Responsive scaling built-in
- Performance-optimized CSS output

### 3. **Flexible Override System**
- Enable/disable global overrides
- Option to force override inline styles
- Utility classes for exceptions

## Accessing Typography Settings

1. Go to **Online Store > Themes**
2. Click **Customize**
3. Navigate to **Theme Settings > Typography**
4. Scroll to **ADVANCED TYPOGRAPHY CUSTOMIZATION**

## Settings Structure

### Font Sizes
All heading sizes (H1-H6) are controlled in the main typography section:
- **H1-H4**: Already present in original settings
- **H5-H6**: Added for complete control

### Global Typography Styles
Universal settings that apply to all text:
- **Text Transform**: Apply uppercase, lowercase, or capitalize globally
- **Text Alignment**: Set default alignment (with "inherit" option)

### Heading Styles (H1-H4)
Applies to all heading elements:
- **Font Weight**: With "Use font default" option
- **Letter Spacing**: -2px to 5px
- **Text Transform**: Can inherit from global or override

### Body Text Styles
Controls paragraphs and general text:
- **Font Weight Override**: Only when needed
- **Letter Spacing**: Subtle adjustments (-1px to 2px)

### Spacing
Simplified spacing controls:
- **Space below headings**: Universal heading margin
- **Space between paragraphs**: Consistent paragraph spacing

### Override Controls
- **Enable global typography override**: Master on/off switch
- **Override inline styles**: Use with caution for stubborn elements

## How It Works

### Inheritance Hierarchy

1. **Global Settings** → Apply to all elements
2. **Category Settings** → Override globals for specific element types
3. **Element Defaults** → Fallback to theme/browser defaults

### Smart CSS Generation

The system only generates CSS for:
- Settings that differ from defaults
- Non-"inherit" values
- Enabled override options

This results in smaller CSS files and better performance.

### Responsive Behavior

Automatic adjustments:
- **Mobile**: 15% reduction in font sizes
- **Large screens**: 10% increase for headings
- **Spacing**: Proportional scaling

## Best Practices

### 1. Start with Globals
Set global text transform and alignment first, then override only where needed.

### 2. Use "Inherit" Wisely
Leave settings on "inherit" unless you specifically need to change them.

### 3. Test Responsively
Always preview on mobile, tablet, and desktop to ensure readability.

### 4. Avoid Over-Styling
Less is more - too many customizations can harm readability and brand consistency.

## Utility Classes

For manual control in specific situations:

```html
<!-- Force heading style -->
<div class="force-heading-style">Styled like a heading</div>

<!-- Force body style -->
<div class="force-body-style">Styled like body text</div>

<!-- Reset all typography -->
<div class="typography-reset">Back to defaults</div>
```

## Troubleshooting

### Settings Not Applying

1. Check "Enable global typography override" is ON
2. Clear browser cache
3. Verify the element isn't using inline styles

### Inline Styles Not Overriding

1. Enable "Override inline styles" (use sparingly)
2. Use utility classes for specific elements
3. Contact app developers for third-party content

### Performance Issues

1. Disable unused features
2. Use "inherit" for unchanged values
3. Minimize use of "Override inline styles"

## CSS Variables Reference

Access these in custom CSS:

```css
/* Global */
--global-text-transform
--global-text-align

/* Headings */
--heading-font-weight
--heading-letter-spacing
--heading-text-transform
--heading-margin-bottom

/* Body Text */
--body-font-weight
--body-letter-spacing
--paragraph-margin-bottom

/* Font Sizes */
--heading-font-size-h1 through h6
--text-font-size-base
--text-line-height
```

## Migration from Previous Version

If upgrading from the complex version:
1. Previous font size settings are preserved
2. Simplified controls replace repetitive options
3. Better performance with same flexibility

## Support

For assistance with the typography system, please refer to your theme documentation or contact Shopify support.