# Typography System Migration Guide

## Quick Start Migration

### 1. Enable the New System

1. Go to **Theme Settings > Typography > Disruptive Typography Overrides**
2. Enable **Typography Disruption**
3. Set **Disruption Level** to **Aggressive**
4. Enable all override options:
   - ✅ Override Utility Classes
   - ✅ Override Component Styles  
   - ✅ Override Semantic Elements

### 2. Configure Three-Tier Settings

1. Go to **Theme Settings > Typography**
2. Configure **Main Heading** (replaces H1, H2):
   - Font size: 42px (recommended)
   - Font weight: 700 (bold)
   - Line height: 1.2
3. Configure **Sub Heading** (replaces H3, H4):
   - Font size: 24px (recommended)
   - Font weight: 600 (semi-bold)
   - Line height: 1.3
4. Configure **Body Text** (replaces H5, H6, P):
   - Font size: 16px (recommended)
   - Font weight: 400 (normal)
   - Line height: 1.6

### 3. Test and Validate

1. Enable **Show Typography Indicators** in theme editor
2. Preview your store to see changes
3. Run validation: `python3 validate_typography_system.py`
4. Check the test suite in theme editor

## Detailed Migration Steps

### Step 1: Backup Current Settings

Before migrating, document your current typography settings:

```json
{
  "h1_font_size": "48px",
  "h2_font_size": "36px", 
  "h3_font_size": "28px",
  "h4_font_size": "24px",
  "h5_font_size": "20px",
  "h6_font_size": "16px"
}
```

### Step 2: Map to Three-Tier System

Convert your existing settings to the new system:

| Old Setting | New Setting | Recommended Value |
|-------------|-------------|-------------------|
| H1, H2 Font Size | Main Heading Font Size | Largest of H1/H2 |
| H3, H4 Font Size | Sub Heading Font Size | Largest of H3/H4 |
| H5, H6 Font Size | Body Text Font Size | Body font size |

### Step 3: Update Custom CSS

#### Before (Legacy System)
```css
h1 { font-size: 48px; color: #333; }
h2 { font-size: 36px; color: #333; }
h3 { font-size: 28px; color: #666; }
h4 { font-size: 24px; color: #666; }
h5 { font-size: 20px; color: #999; }
h6 { font-size: 16px; color: #999; }
```

#### After (Three-Tier System)
```css
.main-heading { 
  font-size: 48px; 
  color: #333; 
}

.sub-heading { 
  font-size: 28px; 
  color: #666; 
}

.body-text { 
  font-size: 16px; 
  color: #999; 
}
```

### Step 4: Update Template Code

#### Manual Updates (Recommended)

Update your liquid templates to use the new classes:

```html
<!-- Before -->
<h1>{{ page.title }}</h1>
<h3>{{ section.settings.heading }}</h3>

<!-- After -->
<h1 class="main-heading" data-typography="main-heading">{{ page.title }}</h1>
<h3 class="sub-heading" data-typography="sub-heading">{{ section.settings.heading }}</h3>
```

#### Automatic Updates

The system automatically updates most headings, but manual updates provide better control.

### Step 5: Handle Edge Cases

#### Custom Components

For custom components with specific typography needs:

```html
<!-- Use size variants -->
<h2 class="main-heading-lg">Large Hero Title</h2>
<h3 class="sub-heading-sm">Small Card Title</h3>

<!-- Use contextual classes -->
<h1 class="hero-heading">Hero Section</h1>
<h4 class="card-title">Product Card</h4>
```

#### Conflicting Styles

If existing styles conflict:

1. Increase disruption level to "Nuclear"
2. Add custom CSS to override settings
3. Use `!important` declarations

```css
/* In Typography Override CSS setting */
.my-special-heading {
  font-size: 64px !important;
  font-weight: 800 !important;
}
```

## Migration Scenarios

### Scenario 1: Minimal Changes

**Goal**: Keep existing design with minimal disruption

**Steps**:
1. Set disruption level to "Gentle"
2. Map existing font sizes to three-tier system
3. Disable override options you don't need
4. Test thoroughly

**Settings**:
- Disruption Level: Gentle
- Override Utility Classes: ❌
- Override Component Styles: ❌
- Override Semantic Elements: ✅

### Scenario 2: Complete Overhaul

**Goal**: Completely replace existing typography

**Steps**:
1. Set disruption level to "Nuclear"
2. Design new three-tier hierarchy
3. Enable all override options
4. Update custom CSS to use new classes

**Settings**:
- Disruption Level: Nuclear
- Override Utility Classes: ✅
- Override Component Styles: ✅
- Override Semantic Elements: ✅

### Scenario 3: Gradual Migration

**Goal**: Migrate section by section over time

**Steps**:
1. Start with disruption level "Moderate"
2. Update one section at a time
3. Use migration helper classes
4. Gradually increase disruption level

**Settings**:
- Disruption Level: Moderate
- Override Utility Classes: ✅
- Override Component Styles: ❌ (initially)
- Override Semantic Elements: ✅

## Common Migration Issues

### Issue 1: Typography Not Changing

**Symptoms**: Headings look the same after enabling system

**Causes**:
- Disruption level too low
- Custom CSS overriding new styles
- Browser cache

**Solutions**:
1. Increase disruption level to "Aggressive"
2. Clear browser cache
3. Check for conflicting custom CSS
4. Enable all override options

### Issue 2: Design Looks Broken

**Symptoms**: Layout issues, spacing problems

**Causes**:
- Font sizes too different from original
- Line height issues
- Missing responsive scaling

**Solutions**:
1. Adjust three-tier font sizes gradually
2. Fine-tune line heights
3. Test on mobile devices
4. Use size variants for specific cases

### Issue 3: Performance Issues

**Symptoms**: Slower page loading

**Causes**:
- Too many CSS overrides
- Large CSS files
- Inefficient selectors

**Solutions**:
1. Reduce disruption level
2. Disable unused size variants
3. Optimize custom CSS
4. Use CSS minification

### Issue 4: Accessibility Problems

**Symptoms**: Poor contrast, heading hierarchy issues

**Causes**:
- Incorrect color mapping
- Broken semantic structure
- Missing focus styles

**Solutions**:
1. Check contrast ratios
2. Validate heading hierarchy
3. Test with screen readers
4. Enable accessibility features

## Testing Checklist

### Visual Testing

- [ ] Homepage displays correctly
- [ ] Product pages use proper hierarchy
- [ ] Collection pages are consistent
- [ ] Blog posts maintain readability
- [ ] Cart and checkout pages work
- [ ] Mobile responsive design intact

### Functional Testing

- [ ] All headings are clickable (if linked)
- [ ] Search functionality works
- [ ] Navigation remains functional
- [ ] Forms submit properly
- [ ] Buttons are accessible

### Performance Testing

- [ ] Page load times acceptable
- [ ] CSS file sizes reasonable
- [ ] No console errors
- [ ] Smooth scrolling maintained
- [ ] Font loading optimized

### Accessibility Testing

- [ ] Proper heading hierarchy (H1 → H2 → H3)
- [ ] Sufficient color contrast
- [ ] Keyboard navigation works
- [ ] Screen reader compatibility
- [ ] Focus indicators visible

## Rollback Plan

If migration causes issues, you can rollback:

### Quick Rollback

1. Go to **Typography > Disruptive Typography Overrides**
2. Disable **Typography Disruption**
3. Clear browser cache
4. Test site functionality

### Complete Rollback

1. Disable typography disruption
2. Remove custom CSS from override settings
3. Restore original theme files (if modified)
4. Clear all caches

### Partial Rollback

1. Reduce disruption level to "Gentle"
2. Disable specific override options
3. Adjust three-tier settings
4. Test incrementally

## Advanced Migration

### Custom Theme Development

For developers creating custom themes:

```liquid
<!-- Use conditional classes -->
{% if settings.enable_typography_disruption %}
  <h1 class="main-heading">{{ title }}</h1>
{% else %}
  <h1 class="{{ legacy_class }}">{{ title }}</h1>
{% endif %}
```

### API Integration

For headless or API-driven implementations:

```javascript
// Check typography system status
const typographyEnabled = window.getComputedStyle(document.documentElement)
  .getPropertyValue('--enable-typography-disruption') === 'true';

if (typographyEnabled) {
  // Use three-tier classes
  element.className = 'main-heading';
} else {
  // Use legacy classes
  element.className = 'h1';
}
```

### Bulk Updates

For large sites with many customizations:

```bash
# Run bulk update script
python3 update_sections_typography.py
python3 update_templates_typography.py

# Validate changes
python3 validate_typography_system.py
```

## Post-Migration Optimization

### 1. Performance Optimization

- Remove unused CSS classes
- Optimize font loading
- Enable CSS minification
- Use CDN for font files

### 2. SEO Considerations

- Maintain proper heading hierarchy
- Keep important keywords in H1 tags
- Ensure content remains crawlable
- Test with SEO tools

### 3. User Experience

- Test with real users
- Monitor bounce rates
- Check conversion metrics
- Gather feedback

### 4. Maintenance

- Regular validation checks
- Monitor performance metrics
- Update documentation
- Train team members

## Support Resources

### Documentation
- [Typography System Documentation](TYPOGRAPHY_SYSTEM_DOCUMENTATION.md)
- [Validation Report](typography-validation-report.json)
- [Heading Usage Analysis](heading-usage-report.md)

### Tools
- Validation script: `validate_typography_system.py`
- Test suite: `snippets/typography-test-suite.liquid`
- Debug mode: Browser console tools

### Community
- Theme developer forums
- Shopify community
- Typography best practices guides

---

*This migration guide provides comprehensive steps for transitioning to the new three-tier typography system. Follow the steps carefully and test thoroughly to ensure a smooth migration.*

