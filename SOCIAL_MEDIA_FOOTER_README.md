# Social Media Footer Component

A customizable social media footer component for Shopify themes with extensive customization options for padding, icon weight, size, type/style, and color.

## Features

### 🎨 **Comprehensive Customization**
- **Padding Control**: Adjust top, bottom, left, and right padding
- **Icon Size**: Customizable icon size from 16px to 48px
- **Icon Weight**: Normal, Bold, or Bolder font weights
- **Color Customization**: Primary and hover colors for icons
- **Background & Border**: Custom background colors, border width, color, and radius
- **Spacing**: Adjustable spacing between icons

### 📱 **Social Media Platforms**
- Facebook
- Instagram
- Twitter
- LinkedIn
- YouTube
- TikTok
- Pinterest
- WhatsApp
- Spotify

### ♿ **Accessibility Features**
- ARIA labels for screen readers
- Keyboard navigation support
- Focus states for accessibility
- High contrast mode support
- Reduced motion support for users with vestibular disorders

### 🎯 **Interactive Features**
- Platform-specific hover effects with brand colors
- Smooth animations and transitions
- Click tracking for analytics
- Intersection Observer for performance
- Responsive design for all devices

## Installation

1. **Add the section file**: Copy `sections/social-media-footer.liquid` to your theme's sections directory
2. **Add the CSS file**: Copy `assets/social-media-footer.css` to your theme's assets directory
3. **Add the JavaScript file**: Copy `assets/social-media-footer.js` to your theme's assets directory
4. **Update footer-group.json**: The section is already included in the footer group configuration

## Configuration

### Theme Settings Required

Make sure your theme has the following social media settings configured in the theme customizer:

```liquid
settings.social_facebook_link
settings.social_instagram_link
settings.social_twitter_link
settings.social_linkedin_link
settings.social_youtube_link
settings.social_tiktok_link
settings.social_pinterest_link
settings.social_whatsapp_link
settings.social_spotify_link
```

### Section Settings

The component includes extensive customization options:

#### Content Settings
- **Title**: Custom title for the social media section
- **Description**: Optional description text

#### Layout Settings
- **Container Type**: Default, Full width, or Container box
- **Alignment**: Left, Center, or Right alignment

#### Padding Settings
- **Padding Top**: 0-100px (5px increments)
- **Padding Bottom**: 0-100px (5px increments)
- **Padding Left**: 0-100px (5px increments)
- **Padding Right**: 0-100px (5px increments)

#### Icon Settings
- **Icon Size**: 16-48px (2px increments)
- **Icon Weight**: Normal, Bold, or Bolder
- **Icon Spacing**: 5-50px (5px increments)

#### Color Settings
- **Icon Color**: Primary color for icons
- **Icon Hover Color**: Color on hover
- **Background Color**: Section background color

#### Border Settings
- **Border Width**: 0-10px (1px increments)
- **Border Color**: Border color
- **Border Radius**: 0-50px (2px increments)

#### Platform Toggles
Individual checkboxes to show/hide each social media platform

## Usage Examples

### Basic Implementation

The component is automatically included in the footer and will display social media icons based on your theme settings.

### Custom Styling

You can customize the appearance through the theme customizer or by modifying the CSS variables:

```css
.social-media-footer-section {
  --social-padding-top: 30px;
  --social-padding-bottom: 30px;
  --social-icon-size: 28px;
  --social-icon-color: #333333;
  --social-icon-hover-color: #666666;
  --social-spacing: 20px;
}
```

### JavaScript API

The component provides a JavaScript API for dynamic updates:

```javascript
// Get the social media footer instance
const socialFooter = new SocialMediaFooter();

// Update colors dynamically
socialFooter.updateIconColors('#ff0000', '#cc0000');

// Update icon size
socialFooter.updateIconSize(32);

// Update spacing
socialFooter.updateIconSpacing(25);
```

## Customization Examples

### Minimal Design
```json
{
  "padding_top": 10,
  "padding_bottom": 10,
  "icon_size": 20,
  "icon_spacing": 10,
  "background_color": "transparent",
  "border_width": 0
}
```

### Bold Design
```json
{
  "padding_top": 40,
  "padding_bottom": 40,
  "icon_size": 32,
  "icon_weight": "bold",
  "icon_spacing": 25,
  "background_color": "#f5f5f5",
  "border_width": 2,
  "border_radius": 10
}
```

### Colorful Design
```json
{
  "icon_color": "#ffffff",
  "icon_hover_color": "#ff6b6b",
  "background_color": "#2c3e50",
  "border_radius": 20,
  "icon_size": 28
}
```

## Browser Support

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## Performance Features

- **Lazy Loading**: Icons animate in when they come into view
- **Optimized Animations**: Uses CSS transforms for smooth performance
- **Reduced Motion**: Respects user preferences for reduced motion
- **Intersection Observer**: Efficient scroll-based animations

## Analytics Integration

The component automatically tracks social media clicks for:

- Google Analytics (gtag)
- Facebook Pixel (fbq)
- Console logging for debugging

## Accessibility

- **ARIA Labels**: Each icon has proper accessibility labels
- **Keyboard Navigation**: Full keyboard support with Enter/Space activation
- **Focus States**: Clear focus indicators for keyboard users
- **High Contrast**: Special styling for high contrast mode
- **Screen Reader Support**: Proper semantic markup and labels

## Troubleshooting

### Icons Not Showing
1. Check that social media URLs are configured in theme settings
2. Verify that the platform checkboxes are enabled in section settings
3. Ensure the section is added to the footer group

### Styling Issues
1. Check that the CSS file is properly loaded
2. Verify CSS custom properties are being applied
3. Check for conflicting CSS rules

### JavaScript Errors
1. Ensure the JavaScript file is loaded
2. Check browser console for errors
3. Verify that the DOM is ready before initialization

## Contributing

To extend this component:

1. Add new social media platforms in the liquid template
2. Add corresponding CSS classes for hover effects
3. Update the JavaScript tracking methods
4. Add new customization options to the schema

## License

This component is part of the Shopify theme and follows the same licensing terms.