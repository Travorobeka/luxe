# Heading Usage Analysis Report

## Summary Statistics

- **Files with headings:** 98
- **Total H1 elements:** 17
- **Total H2 elements:** 46
- **Total H3 elements:** 99
- **Total H4 elements:** 16
- **Total H5 elements:** 3
- **Total H6 elements:** 3

## Heading Distribution

- **H1:** 17 (9.2%)
- **H2:** 46 (25.0%)
- **H3:** 99 (53.8%)
- **H4:** 16 (8.7%)
- **H5:** 3 (1.6%)
- **H6:** 3 (1.6%)

## Common Heading CSS Classes

Found 79 valid CSS classes used with headings:

### Typography-related Classes
- `body-text`
- `font-medium`
- `gift-card__heading`
- `heading_color`
- `heading_size`
- `heading_text_size`
- `m-account__title`
- `m-account__title--medium`
- `m-activate-account__heading`
- `m-age-verifier__subtitle`
- `m-age-verifier__title`
- `m-article-card__title`
- `m-article__title`
- `m-cart-drawer__title`
- `m-collage-tab--heading`
- `m-collection-banner__title`
- `m-collection-card__title`
- `m-collection-page-header__title`
- `m-collection-showcase__heading`
- `m-complementary-products__heading`
- ... and 39 more

### Component-specific Classes
- `form-field--message`
- `m-accordion--item-button`
- `m-collapsible--button`
- `m-scroll-trigger`

### Utility Classes
- `animated`
- `animation_effect`
- `class`
- `else`
- `endif`
- `footer_id`
- `h1`
- `h2`
- `h3`
- `h4`
- `h5`
- `h6`
- `if`
- `main-product__block`
- `strip_newlines`
- `use_accordion`

## Analysis by File Type

### Sections

Files with headings: 58
Total headings: 103

- **H1:** 10 (9.7%)
- **H2:** 37 (35.9%)
- **H3:** 50 (48.5%)
- **H4:** 6 (5.8%)

### Snippets

Files with headings: 38
Total headings: 79

- **H1:** 6 (7.6%)
- **H2:** 9 (11.4%)
- **H3:** 48 (60.8%)
- **H4:** 10 (12.7%)
- **H5:** 3 (3.8%)
- **H6:** 3 (3.8%)

### Templates

Files with headings: 2
Total headings: 2

- **H1:** 1 (50.0%)
- **H3:** 1 (50.0%)

## Mapping to Three-Tier Typography System

Based on the analysis, here's the recommended mapping:

### Main Heading (Primary titles, major section headers)
- **H1 elements:** All 17 instances
- **H2 elements:** 46 instances (major section headers)
- **Recommended CSS class:** `.main-heading`

### Sub Heading (Secondary titles, subsection headers)
- **H3 elements:** 99 instances (most common)
- **H4 elements:** 16 instances
- **Recommended CSS class:** `.sub-heading`

### Body Text (Body text, captions, small headings)
- **H5 elements:** 3 instances
- **H6 elements:** 3 instances
- **Recommended CSS class:** `.body-text`

## Recommendations

1. **Create utility classes** for the three-tier system:
   - `.main-heading` - for H1 and major H2 elements
   - `.sub-heading` - for H3 and H4 elements
   - `.body-text` - for H5, H6, and body text

2. **Maintain backward compatibility** by keeping existing CSS classes

3. **Focus on H3 elements** as they are the most commonly used (99 instances)

4. **Review component-specific classes** to ensure they work with the new system

5. **Create migration guide** for developers using custom heading styles