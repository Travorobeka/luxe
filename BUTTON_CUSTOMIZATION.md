# Advanced Button Customization

This document explains the comprehensive button customization features added to your Shopify theme.

## Overview

The advanced button system provides extensive control over button appearance and behavior:
- Size and padding customization
- Shadow and hover effects
- Gradient backgrounds and borders
- Loading states and animations
- Icon support and positioning
- Multiple button variants and styles

## Features

### 1. Button Sizes & Padding
- **Horizontal Padding**: Adjust left/right padding (10-60px)
- **Vertical Padding**: Adjust top/bottom padding (5-25px)
- **Minimum Width**: Set minimum button width or auto

### 2. Shadows & Effects
- **Shadow Styles**: None, Small, Medium, Large, Extra Large, Inner, or Custom
- **Custom Shadow**: Define your own CSS box-shadow
- **Hover Lift**: Buttons can lift up on hover
- **Hover Scale**: Scale buttons on hover (0.9-1.1x)

### 3. Borders
- **Border Styles**: Solid, Dashed, Dotted, Double, or None
- **Gradient Borders**: Enable colorful gradient borders
- **Custom Gradient**: Define your own gradient colors

### 4. Backgrounds
- **Gradient Backgrounds**: Enable gradient button backgrounds
- **Hover Effects**: Darken, Lighten, Invert, Slide fill, or Pulse
- **Animated Backgrounds**: Shifting gradient animations

### 5. Icons
- **Icon Animation**: Animate icons on hover
- **Icon Position**: Place icons left or right
- **Icon Spacing**: Adjust space between icon and text

### 6. Loading States
- **Loading Spinner**: Show spinner when loading
- **Loading Styles**: Spinner, Dots, Pulse, or Progress bar
- **Automatic Detection**: Forms automatically show loading on submit

### 7. Secondary Buttons
- **Ghost Style**: Transparent background with border
- **Opacity Control**: Adjust secondary button opacity

### 8. Animations
- **Click Animations**: Ripple, Pulse, Bounce, or Shake
- **Transition Duration**: Control animation speed (100-600ms)

### 9. Disabled State
- **Opacity**: Control disabled button appearance
- **Cursor**: Show not-allowed cursor on disabled buttons

## Usage

### Theme Customizer
1. Go to **Online Store > Themes > Customize**
2. Navigate to **Theme Settings > Typography**
3. Scroll to **Advanced Button Customization**
4. Adjust settings as needed
5. Save changes

### CSS Classes

#### Button Sizes
- `.m-button--xs` - Extra small button
- `.m-button--sm` - Small button
- `.m-button--lg` - Large button
- `.m-button--xl` - Extra large button

#### Button Variants
- `.m-button--primary` - Primary button (default)
- `.m-button--secondary` - Secondary button
- `.m-button--ghost` - Ghost/outline button
- `.m-button--text` - Text-only button
- `.m-button--link` - Link-style button

#### Button Shapes
- `.m-button--pill` - Rounded pill shape
- `.m-button--square` - Square corners

#### Effects
- `.m-button--3d` - 3D pressed effect
- `.m-button--glow` - Glowing effect
- `.m-button--gradient` - Gradient background
- `.m-button--gradient-border` - Gradient border
- `.m-button--animated-bg` - Animated gradient

#### Hover Effects
- `.m-button--slide-fill` - Slide fill on hover
- `.m-button--pulse` - Pulse effect on hover

#### Click Animations
- `.m-button--ripple` - Ripple effect on click
- `.m-button--bounce` - Bounce on click
- `.m-button--shake` - Shake on click

#### Loading States
- `.m-button--loading` - Show loading state
- `.m-button--loading-spinner` - Spinner style
- `.m-button--loading-dots` - Dots style
- `.m-button--loading-progress` - Progress bar style

#### Special Buttons
- `.m-button--icon-only` - Icon-only button
- `.m-button--toggle` - Toggle button
- `.m-button--split` - Split button
- `.m-button--fab` - Floating action button
- `.m-button--responsive` - Full width on mobile

## JavaScript API

### Button Utilities

```javascript
// Create a button programmatically
const button = ButtonUtils.createButton({
  text: 'Click Me',
  variant: 'primary',
  size: 'lg',
  icon: 'arrow-right',
  onClick: () => console.log('Clicked!')
});

// Show success state
ButtonUtils.showSuccess(button, 'Added to cart!', 3000);

// Show error state
ButtonUtils.showError(button, 'Out of stock', 3000);

// Set loading state
buttonHandler.setButtonLoading(button, true);
```

### Event Handling

```javascript
// Toggle button events
button.addEventListener('toggle', (e) => {
  console.log('Toggle state:', e.detail.active);
});

// Button group events
buttonGroup.addEventListener('change', (e) => {
  console.log('Selected:', e.detail.value);
});
```

## Examples

### Gradient Button
```html
<button class="m-button m-button--primary m-button--gradient">
  Gradient Button
</button>
```

### Icon Button with Animation
```html
<button class="m-button m-button--text-with-icon" data-icon-animation="true">
  Shop Now
  <svg class="icon"><!-- Arrow icon --></svg>
</button>
```

### Loading Button
```html
<button class="m-button m-button--loading m-button--loading-spinner">
  Loading...
</button>
```

### Button Group
```html
<div class="m-button-group" data-toggle="true">
  <button class="m-button is-active" data-value="option1">Option 1</button>
  <button class="m-button" data-value="option2">Option 2</button>
  <button class="m-button" data-value="option3">Option 3</button>
</div>
```

### Toggle Button
```html
<button class="m-button m-button--toggle" aria-pressed="false">
  Toggle Me
</button>
```

### 3D Button
```html
<button class="m-button m-button--primary m-button--3d">
  Press Me
</button>
```

### Ghost Button with Hover Effect
```html
<button class="m-button m-button--ghost m-button--slide-fill">
  Learn More
</button>
```

### Floating Action Button
```html
<button class="m-button m-button--primary m-button--fab">
  <svg class="icon"><!-- Plus icon --></svg>
</button>
```

## Advanced Features

### Custom Ripple Color
```css
.m-button--custom-ripple .ripple-effect {
  background: rgba(255, 0, 0, 0.5);
}
```

### Responsive Button
```html
<button class="m-button m-button--responsive m-button--responsive-icon-only">
  <svg class="icon"><!-- Icon --></svg>
  <span>Add to Cart</span>
</button>
```

### Split Button
```html
<div class="m-button m-button--split">
  <span>Add to Cart</span>
  <span class="icon">▼</span>
</div>
```

## Accessibility

All button enhancements maintain accessibility:
- Proper focus states with visible outlines
- ARIA attributes for toggle buttons
- Disabled state handling
- High contrast mode support
- Keyboard navigation support

## Performance

- CSS animations use GPU acceleration
- JavaScript is lightweight and efficient
- Loading states prevent multiple submissions
- Deferred loading for non-critical features

## Browser Support

All features work in modern browsers:
- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers

Some advanced effects gracefully degrade in older browsers.

## Troubleshooting

### Buttons Not Animating
- Check if animations are enabled in theme settings
- Verify JavaScript is loaded
- Check browser console for errors

### Gradient Not Showing
- Ensure gradient is enabled in customizer
- Check gradient color syntax
- Verify no conflicting CSS

### Loading State Stuck
- Check form submission handling
- Verify timeout is set
- Look for JavaScript errors

---

Last updated: [Current Date]
Version: 1.0.0