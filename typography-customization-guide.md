# Typography Customization Guide

## Overview

This Shopify theme now includes comprehensive typography customization features that allow you to control the appearance of all text elements throughout your store. These settings override any hardcoded typography styles in sections, snippets, and templates.

## Typography Hierarchy

The typography system is organized into three main categories:

1. **Headings (H1-H2)**: Primary page titles and major section headings
2. **Subheadings (H3-H4)**: Secondary titles and subsection headings
3. **Description/Text (H5-H6, P, SPAN)**: Body text, descriptions, and general content

## Accessing Typography Settings

1. Go to your Shopify Admin
2. Navigate to **Online Store > Themes**
3. Click **Customize** on your active theme
4. Go to **Theme Settings > Typography**
5. Scroll down to find the **COMPREHENSIVE TYPOGRAPHY CUSTOMIZATION** section

## Available Settings

### For Each Typography Category

Each category (Headings, Subheadings, Description/Text) includes the following customization options:

1. **Font Size**: Control the size of the text
   - H1: 20-120px
   - H2: 20-100px
   - H3: 14-80px
   - H4: 14-60px
   - H5: 12-40px
   - H6: 12-36px
   - Base text: 14-20px

2. **Font Weight**: Choose from 9 weight options
   - 100 (Thin)
   - 200 (Extra-light)
   - 300 (Light)
   - 400 (Regular)
   - 500 (Medium)
   - 600 (Semi-bold)
   - 700 (Bold)
   - 800 (Extra-bold)
   - 900 (Black)

3. **Letter Spacing**: Adjust the space between characters
   - Headings: -5px to 10px
   - Subheadings: -5px to 10px
   - Text: -2px to 5px

4. **Text Transform**: Control capitalization
   - None (default)
   - UPPERCASE
   - lowercase
   - Capitalize

5. **Text Alignment**: Set text alignment
   - Left
   - Center
   - Right
   - Justify

6. **Padding**: Control spacing above and below text
   - Top padding: 0-50px (varies by category)
   - Bottom padding: 0-50px (varies by category)

### Typography Override Settings

1. **Enable Typography Override**: Toggle to activate/deactivate the override system
2. **Override Priority**: Choose how styles are applied
   - Normal: Uses CSS specificity
   - Important: Uses !important declarations (recommended)

## How It Works

### Override System

When enabled, the typography override system:

1. Applies your custom settings to ALL matching elements throughout the theme
2. Overrides any hardcoded styles in sections, snippets, and templates
3. Maintains consistency across your entire store

### Elements Affected

The system automatically applies settings to:

- All heading tags (h1-h6)
- Paragraphs and spans
- Product titles and descriptions
- Section headings
- Card content
- Navigation text
- Footer content
- Form labels
- List items
- Table cells

### Responsive Behavior

Typography automatically adjusts for different screen sizes:

- **Mobile (< 750px)**: Font sizes reduced by 10-20%
- **Desktop**: Uses your configured sizes
- **Large screens (> 1920px)**: Font sizes increased by 5-10%

## Best Practices

### 1. Maintain Hierarchy

Ensure your font sizes create a clear visual hierarchy:
- H1 should be the largest
- Each subsequent heading level should be smaller
- Body text should be easily readable

### 2. Consider Readability

- Use appropriate line height for body text (1.5-1.8x font size)
- Avoid extreme letter spacing values
- Test on multiple devices

### 3. Brand Consistency

- Choose font weights that match your brand personality
- Use text transform sparingly (uppercase can reduce readability)
- Maintain consistent alignment patterns

### 4. Performance

- The override system uses CSS custom properties for optimal performance
- Changes apply instantly without page reload
- No JavaScript required for basic functionality

## Troubleshooting

### Changes Not Appearing

1. Ensure "Enable typography override" is checked
2. Clear your browser cache
3. Check that "Override priority" is set to "Important"

### Specific Elements Not Updating

Some third-party apps or custom code may use inline styles. In these cases:
1. Contact the app developer
2. Use the utility classes provided (see below)

### Utility Classes

For manual override of specific elements, use these classes:

- `.force-heading-style`: Apply heading typography
- `.force-subheading-style`: Apply subheading typography
- `.force-text-style`: Apply text typography

Example:
```html
<div class="force-heading-style">This will use heading typography</div>
```

## Advanced Usage

### Custom CSS

You can reference the CSS variables in your custom CSS:

```css
.my-custom-element {
  font-size: var(--heading-font-size-h1);
  font-weight: var(--heading-font-weight);
  letter-spacing: var(--heading-letter-spacing);
}
```

### Available CSS Variables

- `--heading-font-size-h1`
- `--heading-font-size-h2`
- `--subheading-font-size-h3`
- `--subheading-font-size-h4`
- `--text-font-size-h5`
- `--text-font-size-h6`
- `--text-font-size-base`
- And many more...

## Support

For additional help or to report issues with the typography customization system, please contact your theme developer or Shopify support.