# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the **Minimog 5.7.0 Shopify Theme** - a highly customizable, performance-optimized Shopify theme built for modern e-commerce stores. The theme follows Shopify's Online Store 2.0 architecture with sections everywhere, app blocks, and dynamic sections.

## Development Commands

### Shopify Theme Development
```bash
# Push theme to Shopify store
shopify theme push

# Start local development with hot-reload
shopify theme dev

# Pull latest theme from Shopify store
shopify theme pull
```

### Git Workflow
Always stage, commit, and push changes to GitHub after significant work:
```bash
git add .
git commit -m "Description of changes"
git push origin master
```

## Architecture & Structure

### Core Architecture
- **Shopify OS 2.0 Compliant**: Built for sections everywhere, app blocks, and dynamic sections
- **Modular Design**: Heavily uses reusable snippets and modular section architecture
- **Performance-Optimized**: Critical CSS, deferred JS, optimized images, and browser caching

### Key Directories
- `/assets/` - CSS, JS, and image files for theme functionality
- `/config/` - Theme configuration files (settings_schema.json, settings_data.json)
- `/layout/` - Main theme structure (theme.liquid, password.liquid)
- `/sections/` - Reusable sections for the theme (header, footer, product templates)
- `/snippets/` - Reusable code blocks used across sections and templates
- `/templates/` - Page templates in JSON format with section configurations
- `/locales/` - Translation files for internationalization

### Theme Organization
- **Header System**: Complex header with drawer navigation, mega menus, and mobile optimization
- **Product Architecture**: Multiple product layouts with bundles, quick view, and variant handling
- **Collection System**: Advanced filtering, sorting, and display options
- **Responsive Design**: Mobile-first approach with extensive breakpoint management

## Key Development Guidelines

### Liquid Development
- Use `{% render %}` instead of `{% include %}` for scope isolation
- Always use lowercase, hyphenated handles
- Implement proper whitespace control with hyphens in tags
- Use correct Liquid operators (`==`, `!=`, `contains`, `and`, `or`)
- Implement proper variable assignment with `{% assign %}` or `{% capture %}`

### Code Quality Standards
- Follow the comprehensive guidelines in `project_instructions.md`
- Maintain OS 2.0 compliance for all new sections
- Use modular, reusable snippet design patterns
- Implement proper input sanitization and security practices

### Performance Requirements
- Optimize images and implement lazy loading
- Use browser caching strategies
- Implement critical CSS for above-the-fold content
- Defer non-critical JavaScript loading

### Theme Customization Areas
Based on `read.md`, the theme supports extensive customization:
- **Drawer Navigation**: Width, background, padding, animations, and close icon customization
- **Menu System**: Button styling, typography, expandable submenus with accordion functionality
- **Product Sections**: Image management, aspect ratios, and responsive controls
- **Social Integration**: Configurable social media icons and links
- **Accessibility**: Focus management, scroll locking, and animation preferences

### Pre-deployment Checklist
- Run Shopify Theme Check for validation
- Test on development store across multiple devices
- Verify all breakpoints and responsive behavior
- Check accessibility compliance
- Validate performance metrics
- Test all custom functionality

## File Naming & Structure Conventions

### Assets Organization
- CSS files follow component-based naming (e.g., `header.css`, `product.css`)
- JS files mirror their CSS counterparts with matching functionality
- Vendor files are clearly separated and prefixed appropriately

### Section Architecture
- Main sections in `/sections/` directory
- Template-specific sections follow clear naming patterns
- Customer account sections organized in `/templates/customers/`
- Product sections support multiple layout variations

### Snippet Usage
- Component snippets prefixed with `component-`
- Form snippets prefixed with `form-`
- Icon snippets use consistent `icon-` prefix
- Product-related snippets clearly identified

## Typography System

### Three-Tier Typography Structure (Updated January 2025)
The theme now uses a simplified three-tier typography system instead of the previous six-level H1-H6 structure:

#### 1. Main Heading (.main-heading)
- **Purpose**: Primary page titles, logo text, hero headings
- **Default**: 42px (desktop), 34px (tablet), 29px (mobile)
- **Usage**: Apply to H1 elements and primary content headings

#### 2. Sub Heading (.sub-heading)
- **Purpose**: Section headers, product titles, article headings
- **Default**: 24px (desktop), 20px (tablet), 18px (mobile)
- **Usage**: Apply to H2-H4 elements and secondary content headings

#### 3. Body Text (.body-text)
- **Purpose**: Content text, complementary headings, small sections
- **Default**: 16px (all devices)
- **Usage**: Apply to H5-H6 elements, paragraph text, and captions

### Implementation Guidelines
```liquid
<!-- Primary page title -->
<h1 class="main-heading">{{ page.title }}</h1>

<!-- Section header -->
<h2 class="sub-heading">{{ section.settings.title }}</h2>

<!-- Product title in cards -->
<h3 class="product-title sub-heading">{{ product.title }}</h3>

<!-- Small section heading -->
<h4 class="body-text">{{ block.settings.subtitle }}</h4>
```

### Typography Testing
Use the typography test suite for visual validation:
```liquid
{% render 'typography-test-suite' %}
```

### Backward Compatibility
All legacy H1-H6 classes continue to work through CSS variable mapping. The system maintains full backward compatibility while providing a cleaner structure for new development.

## Testing & Validation

Since this is a Shopify theme, testing should focus on:
- Theme functionality across different Shopify store configurations
- Cross-browser compatibility testing
- Mobile responsiveness validation
- Performance testing with Shopify's tools
- Accessibility compliance verification
- Typography system validation using the test suite

## Important Notes

- This theme is maintained in the `luxe` repository
- Always test changes on a development store before deployment
- Follow Shopify's theme development best practices
- Maintain backward compatibility with existing customizations
- Document all custom functionality and theme setting changes