# Typography Test Checklist - Three-Tier System

## Overview
This checklist ensures the new three-tier typography system is working correctly across all components and devices.

## Test Environment Setup

### 1. Theme Settings Verification
- [ ] Navigate to Theme Settings > Typography
- [ ] Verify new three-tier settings are present:
  - [ ] Main Heading Font Size (default: 42px)
  - [ ] Main Heading Font Weight (default: 700)
  - [ ] Main Heading Line Height (default: 1.2)
  - [ ] Main Heading Letter Spacing (default: 0)
  - [ ] Sub Heading Font Size (default: 24px)
  - [ ] Sub Heading Font Weight (default: 600)
  - [ ] Sub Heading Line Height (default: 1.3)
  - [ ] Sub Heading Letter Spacing (default: 0)
  - [ ] Body Text Font Size (default: 16px)
  - [ ] Body Text Font Weight (default: 400)
  - [ ] Body Text Line Height (default: 1.6)
  - [ ] Body Text Letter Spacing (default: 0)

### 2. CSS Variables Test
Add this to any template to verify CSS variables are loaded:
```liquid
{% render 'typography-test-suite' %}
```

## Component Testing

### 3. Critical Sections
- [ ] **Page Titles** (`snippets/page-title.liquid`)
  - [ ] H1 element has `main-heading` class
  - [ ] Typography scales correctly on mobile/tablet
  - [ ] Color inheritance works properly
  
- [ ] **Header Logo** (`snippets/header-logo.liquid`)
  - [ ] Logo text uses `main-heading` class
  - [ ] H1 wrapper on homepage has `main-heading` class
  - [ ] Typography is consistent across devices

- [ ] **Section Headers** (`snippets/index-section-header.liquid`)
  - [ ] H2 elements have `sub-heading` class
  - [ ] Responsive scaling works correctly
  - [ ] Animation effects still function

- [ ] **Footer Headings** (`sections/footer.liquid`)
  - [ ] Newsletter title has `sub-heading` class
  - [ ] Company title has `sub-heading` class
  - [ ] Menu titles have `sub-heading` class
  - [ ] Contact title has `sub-heading` class

### 4. Product & Collection Components
- [ ] **Product Cards** (all 5 variants)
  - [ ] Product titles use `sub-heading` class
  - [ ] Typography hierarchy is maintained
  - [ ] Responsive behavior works correctly
  - [ ] Backward compatibility preserved

- [ ] **Collection Cards** (`snippets/collection-card.liquid`)
  - [ ] Collection titles use `sub-heading` class
  - [ ] All card styles (inside, outside, boxed) work
  - [ ] Hidden titles still have proper classes

- [ ] **Product Bundles** (`snippets/product-card-bundle.liquid`)
  - [ ] Bundle titles use `body-text` class
  - [ ] Typography fits within bundle layout

### 5. Reusable Snippets
- [ ] **Article Cards** (`snippets/article-card.liquid`)
  - [ ] Article titles use `sub-heading` class
  - [ ] Typography works in all view modes

- [ ] **Image Cards** (`snippets/image-card.liquid`)
  - [ ] Image card headings use `sub-heading` class
  - [ ] Typography overlays work correctly

- [ ] **Video Cards** (`snippets/video-card.liquid`)
  - [ ] Video card headings use `sub-heading` class
  - [ ] Typography overlays are readable

- [ ] **Main Product Blocks** (`snippets/main-product-blocks.liquid`)
  - [ ] Product titles use `main-heading` class
  - [ ] Complementary product headings use `body-text` class
  - [ ] Typography hierarchy is clear

## Responsive Testing

### 6. Mobile Testing (< 768px)
- [ ] Main headings scale down by ~30% (42px → ~29px)
- [ ] Sub headings scale down by ~25% (24px → ~18px)
- [ ] Body text remains consistent (16px)
- [ ] Line heights adjust appropriately
- [ ] Text remains readable at all sizes

### 7. Tablet Testing (768px - 1279px)
- [ ] Main headings scale down by ~20% (42px → ~34px)
- [ ] Sub headings scale down by ~15% (24px → ~20px)
- [ ] Body text remains consistent (16px)
- [ ] Typography fits well in tablet layouts

### 8. Desktop Testing (≥ 1280px)
- [ ] Main headings display at full size (42px default)
- [ ] Sub headings display at full size (24px default)
- [ ] Body text displays at full size (16px default)
- [ ] Typography hierarchy is clearly visible

## Backward Compatibility Testing

### 9. Legacy H1-H6 Classes
- [ ] H1 elements without new classes still work
- [ ] H2 elements without new classes still work
- [ ] H3 elements without new classes still work
- [ ] H4 elements without new classes still work
- [ ] H5 elements without new classes still work
- [ ] H6 elements without new classes still work

### 10. CSS Variable Mapping
- [ ] Legacy H1-H6 variables still function
- [ ] No broken styles in existing components
- [ ] Theme customizer changes apply correctly

## Performance Testing

### 11. Loading Performance
- [ ] Page load times remain acceptable
- [ ] CSS file size hasn't increased significantly
- [ ] No console errors related to typography
- [ ] Font loading works correctly

### 12. Theme Customizer Testing
- [ ] Typography changes apply immediately in customizer
- [ ] Preview updates correctly on setting changes
- [ ] Save functionality works properly
- [ ] Reset to defaults works correctly

## Cross-Browser Testing

### 13. Browser Compatibility
- [ ] Chrome: Typography renders correctly
- [ ] Firefox: Typography renders correctly
- [ ] Safari: Typography renders correctly
- [ ] Edge: Typography renders correctly
- [ ] Mobile Safari: Typography renders correctly
- [ ] Chrome Mobile: Typography renders correctly

## Accessibility Testing

### 14. Accessibility Compliance
- [ ] Heading hierarchy is semantic (H1 > H2 > H3...)
- [ ] Color contrast meets WCAG guidelines
- [ ] Typography is scalable with browser zoom
- [ ] Screen readers interpret headings correctly
- [ ] Focus indicators work with typography

## Final Validation

### 15. Visual Hierarchy Test
- [ ] Main headings are clearly the largest
- [ ] Sub headings are visually secondary
- [ ] Body text is appropriate for content
- [ ] Hierarchy is obvious without explanation

### 16. User Experience Test
- [ ] Typography feels cohesive across the site
- [ ] Reading experience is comfortable
- [ ] Navigation feels intuitive
- [ ] No typography-related confusion

## Testing Tools

### Development Tools
```html
<!-- Add to any template for visual testing -->
{% render 'typography-test-suite' %}
```

### Browser DevTools Commands
```javascript
// Check CSS variables are loaded
console.log(getComputedStyle(document.documentElement).getPropertyValue('--font-main-heading-desktop'));

// Test responsive scaling
window.addEventListener('resize', () => {
  console.log('Window width:', window.innerWidth);
});
```

### Validation Commands
```liquid
<!-- Check if classes are applied -->
{{ 'main-heading' | class_exists }}
{{ 'sub-heading' | class_exists }}
{{ 'body-text' | class_exists }}
```

## Test Results Documentation

### Issues Found
- [ ] Issue 1: Description and resolution
- [ ] Issue 2: Description and resolution
- [ ] Issue 3: Description and resolution

### Performance Metrics
- [ ] Page load time: ___ms
- [ ] CSS file size: ___KB
- [ ] Font loading time: ___ms

### Sign-off
- [ ] Developer testing complete
- [ ] QA testing complete
- [ ] Stakeholder approval received
- [ ] Ready for production deployment

---

**Test Completed By:** _______________  
**Date:** _______________  
**Environment:** _______________  
**Notes:** _______________