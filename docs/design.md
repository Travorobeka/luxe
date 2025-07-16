# Design Document

## Overview

This design document outlines the approach for simplifying the Minimog theme's typography system from the current complex six-level heading structure (H1-H6) to a streamlined three-tier system. The current theme has extensive typography customization options with individual controls for each heading level, which creates complexity and inconsistency. The new system will provide a cleaner, more maintainable approach while preserving visual hierarchy and design flexibility.

## Architecture

### Current State Analysis

Based on the theme analysis, the current typography system includes:

- **Settings Schema**: Individual controls for H1-H6 with font size, weight, line height, and letter spacing
- **Font Sources**: Support for Shopify fonts, Google Fonts, and custom fonts
- **Usage Patterns**: Inconsistent heading usage across sections with class-based sizing (h1, h2, h3, h4, h5, h6)
- **Configuration Complexity**: Over 30 individual typography settings creating maintenance overhead

### Target Architecture

The new three-tier system will consist of:

1. **Main Heading** - Primary page/section titles (replaces H1-H2 usage)
2. **Sub Heading** - Secondary titles and section headers (replaces H3-H4 usage)  
3. **Body Text** - All paragraph content and minor labels (replaces H5-H6 and body text)

## Components and Interfaces

### Typography Settings Schema

The simplified settings will include:

```json
{
  "name": "Typography",
  "settings": [
    {
      "type": "header",
      "content": "FONT SOURCE SELECTION"
    },
    {
      "type": "select",
      "id": "typography_source",
      "label": "Font Source",
      "options": ["shopify", "google_fonts", "custom_fonts"],
      "default": "shopify"
    },
    {
      "type": "header", 
      "content": "MAIN HEADING"
    },
    {
      "type": "range",
      "id": "main_heading_font_size",
      "label": "Font Size",
      "default": 42,
      "min": 24,
      "max": 80,
      "unit": "px"
    },
    {
      "type": "select",
      "id": "main_heading_font_weight", 
      "label": "Font Weight",
      "default": "700",
      "options": ["400", "500", "600", "700", "800"]
    },
    {
      "type": "header",
      "content": "SUB HEADING"
    },
    {
      "type": "range",
      "id": "sub_heading_font_size",
      "label": "Font Size", 
      "default": 24,
      "min": 18,
      "max": 48,
      "unit": "px"
    },
    {
      "type": "select",
      "id": "sub_heading_font_weight",
      "label": "Font Weight",
      "default": "600", 
      "options": ["400", "500", "600", "700"]
    }
  ]
}
```

### CSS Variable System

New CSS custom properties will be defined:

```css
:root {
  /* Main Heading */
  --font-size-main-heading: {{ settings.main_heading_font_size | default: 42 }}px;
  --font-weight-main-heading: {{ settings.main_heading_font_weight | default: 700 }};
  --line-height-main-heading: 1.2;
  
  /* Sub Heading */
  --font-size-sub-heading: {{ settings.sub_heading_font_size | default: 24 }}px;
  --font-weight-sub-heading: {{ settings.sub_heading_font_weight | default: 600 }};
  --line-height-sub-heading: 1.3;
  
  /* Body Text (existing) */
  --font-size-body: {{ settings.body_font_size | default: 16 }}px;
  --font-weight-body: {{ settings.body_font_weight | default: 400 }};
  --line-height-body: {{ settings.body_line_height | default: 1.6 }};
}
```

### CSS Classes

Standardized classes will replace the current heading size classes:

```css
.main-heading {
  font-size: var(--font-size-main-heading);
  font-weight: var(--font-weight-main-heading);
  line-height: var(--line-height-main-heading);
  font-family: var(--font-stack-header);
}

.sub-heading {
  font-size: var(--font-size-sub-heading);
  font-weight: var(--font-weight-sub-heading);
  line-height: var(--line-height-sub-heading);
  font-family: var(--font-stack-header);
}

.body-text {
  font-size: var(--font-size-body);
  font-weight: var(--font-weight-body);
  line-height: var(--line-height-body);
  font-family: var(--font-stack-body);
}
```

## Data Models

### Heading Mapping Strategy

Current heading usage will be mapped to the new system:

| Current Usage | New Class | Semantic HTML | Use Case |
|---------------|-----------|---------------|----------|
| H1, H2 classes | `.main-heading` | `<h1>`, `<h2>` | Page titles, major section headers |
| H3, H4 classes | `.sub-heading` | `<h3>`, `<h4>` | Subsection titles, card headers |
| H5, H6 classes | `.body-text` | `<h5>`, `<h6>`, `<p>` | Minor labels, small text |

### Section Settings Migration

Section settings will be simplified from multiple heading size options to three choices:

```json
{
  "type": "select",
  "id": "heading_style",
  "label": "Heading Style",
  "options": [
    {
      "value": "main-heading",
      "label": "Main Heading"
    },
    {
      "value": "sub-heading", 
      "label": "Sub Heading"
    },
    {
      "value": "body-text",
      "label": "Body Text"
    }
  ],
  "default": "main-heading"
}
```

## Error Handling

### Backward Compatibility

To ensure smooth transition:

1. **Legacy Class Support**: Maintain existing h1-h6 classes temporarily with deprecation warnings
2. **Fallback Values**: Provide sensible defaults if new settings are not configured
3. **Migration Path**: Create utility to automatically update existing section configurations

### Validation

- Ensure font sizes remain within accessible ranges (minimum 14px)
- Validate font weight availability for selected font families
- Check contrast ratios meet WCAG guidelines

## Testing Strategy

### Visual Regression Testing

1. **Before/After Screenshots**: Capture all page types with current and new typography
2. **Cross-Browser Testing**: Verify consistency across major browsers
3. **Responsive Testing**: Ensure typography scales properly on mobile devices

### Accessibility Testing

1. **Screen Reader Testing**: Verify semantic HTML structure is preserved
2. **Contrast Testing**: Ensure text meets WCAG AA standards
3. **Font Size Testing**: Verify readability at different zoom levels

### Performance Testing

1. **Font Loading**: Measure impact of simplified font loading
2. **CSS Size**: Compare stylesheet size before and after changes
3. **Render Performance**: Test page rendering speed with new typography

### User Acceptance Testing

1. **Theme Customization**: Test admin interface for typography settings
2. **Content Creation**: Verify editors can achieve desired visual hierarchy
3. **Migration Testing**: Test upgrade path from current to new system

## Implementation Phases

### Phase 1: Foundation
- Update settings schema with new typography options
- Create CSS variable system and utility classes
- Implement backward compatibility layer

### Phase 2: Core Updates  
- Update critical sections (header, footer, main content areas)
- Migrate product and collection templates
- Update reusable snippets

### Phase 3: Comprehensive Migration
- Update remaining sections and templates
- Remove deprecated classes and settings
- Optimize CSS and remove unused code

### Phase 4: Testing & Refinement
- Comprehensive testing across all page types
- Performance optimization
- Documentation updates