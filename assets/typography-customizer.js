/**
 * Typography Customizer
 * Handles dynamic font loading and preview in theme editor
 */

class TypographyCustomizer {
  constructor() {
    this.googleFontsCache = new Map();
    this.loadedFonts = new Set();
    this.init();
  }

  init() {
    // Listen for theme editor events
    if (window.Shopify && window.Shopify.designMode) {
      document.addEventListener('shopify:section:load', () => this.updateTypography());
      document.addEventListener('shopify:section:select', () => this.updateTypography());
      this.setupFontPreview();
    }
  }

  setupFontPreview() {
    // Watch for changes in typography settings
    const observer = new MutationObserver(() => {
      this.updateTypography();
    });

    const targetNode = document.querySelector('[data-section-type="typography"]');
    if (targetNode) {
      observer.observe(targetNode, { childList: true, subtree: true });
    }
  }

  async loadGoogleFont(fontFamily, weights = '300,400,500,700') {
    const fontKey = `${fontFamily}:${weights}`;
    
    if (this.loadedFonts.has(fontKey)) {
      return;
    }

    const link = document.createElement('link');
    link.rel = 'stylesheet';
    const formattedFamily = fontFamily.replace(/ /g, '+');
    const formattedWeights = weights.split(',').map(w => w.trim()).join(';');
    link.href = `https://fonts.googleapis.com/css2?family=${formattedFamily}:wght@${formattedWeights}&display=swap`;
    
    document.head.appendChild(link);
    this.loadedFonts.add(fontKey);

    // Wait for font to load
    await document.fonts.ready;
  }

  async updateTypography() {
    const fontSource = this.getSettingValue('font_source');
    
    switch (fontSource) {
      case 'google':
        await this.applyGoogleFonts();
        break;
      case 'template':
        await this.applyFontTemplate();
        break;
      default:
        // Shopify or custom fonts are handled by the liquid template
        break;
    }

    this.applyAdvancedSettings();
  }

  async applyGoogleFonts() {
    const headingFont = this.getSettingValue('google_font_heading');
    const headingWeights = this.getSettingValue('google_font_heading_weights');
    const bodyFont = this.getSettingValue('google_font_body');
    const bodyWeights = this.getSettingValue('google_font_body_weights');

    if (headingFont) {
      await this.loadGoogleFont(headingFont, headingWeights);
      document.documentElement.style.setProperty('--font-stack-header', `'${headingFont}', sans-serif`);
    }

    if (bodyFont) {
      await this.loadGoogleFont(bodyFont, bodyWeights);
      document.documentElement.style.setProperty('--font-stack-body', `'${bodyFont}', sans-serif`);
    }
  }

  async applyFontTemplate() {
    const template = this.getSettingValue('font_template');
    const templates = {
      'modern_minimal': {
        heading: { family: 'Inter', weights: '400,500,600,700,800' },
        body: { family: 'Inter', weights: '300,400,500,600' }
      },
      'classic_serif': {
        heading: { family: 'Playfair Display', weights: '400,700,900' },
        body: { family: 'Source Sans Pro', weights: '300,400,600,700' }
      },
      'tech_modern': {
        heading: { family: 'Roboto', weights: '300,400,500,700,900' },
        body: { family: 'Roboto Mono', weights: '300,400,500,700' }
      },
      'elegant_fashion': {
        heading: { family: 'Cormorant Garamond', weights: '300,400,500,600,700' },
        body: { family: 'Montserrat', weights: '300,400,500,600' }
      },
      'playful_creative': {
        heading: { family: 'Fredoka', weights: '400,500,600,700' },
        body: { family: 'Open Sans', weights: '300,400,600,700' }
      },
      'professional_corporate': {
        heading: { family: 'Merriweather', weights: '300,400,700,900' },
        body: { family: 'Lato', weights: '300,400,700,900' }
      },
      'luxury_premium': {
        heading: { family: 'Bodoni Moda', weights: '400,500,600,700,800,900' },
        body: { family: 'Raleway', weights: '300,400,500,600,700' }
      },
      'clean_swiss': {
        heading: { family: 'Work Sans', weights: '300,400,500,600,700,800' },
        body: { family: 'Work Sans', weights: '300,400,500,600' }
      }
    };

    const selectedTemplate = templates[template];
    if (selectedTemplate) {
      await this.loadGoogleFont(selectedTemplate.heading.family, selectedTemplate.heading.weights);
      await this.loadGoogleFont(selectedTemplate.body.family, selectedTemplate.body.weights);
      
      document.documentElement.style.setProperty('--font-stack-header', `'${selectedTemplate.heading.family}', sans-serif`);
      document.documentElement.style.setProperty('--font-stack-body', `'${selectedTemplate.body.family}', sans-serif`);
    }
  }

  applyAdvancedSettings() {
    // Font smoothing
    if (this.getSettingValue('enable_font_smoothing')) {
      document.body.style.webkitFontSmoothing = 'antialiased';
      document.body.style.mozOsxFontSmoothing = 'grayscale';
    }

    // OpenType features
    if (this.getSettingValue('enable_opentype_features')) {
      const features = this.getSettingValue('opentype_features') || 'liga, kern';
      document.body.style.fontFeatureSettings = features;
    }

    // Responsive typography
    if (this.getSettingValue('enable_responsive_typography')) {
      const minScale = parseFloat(this.getSettingValue('responsive_scale_min') || 0.8);
      const maxScale = parseFloat(this.getSettingValue('responsive_scale_max') || 1.2);
      
      this.applyResponsiveScale(minScale, maxScale);
    }

    // Typography presets
    if (this.getSettingValue('enable_typography_presets')) {
      this.applyTypographyPreset(this.getSettingValue('typography_preset'));
    }
  }

  applyResponsiveScale(minScale, maxScale) {
    const viewportWidth = window.innerWidth;
    let scale = 1;

    if (viewportWidth <= 768) {
      scale = minScale;
    } else if (viewportWidth >= 1441) {
      scale = maxScale;
    }

    document.documentElement.style.setProperty('--typography-scale', scale);
  }

  applyTypographyPreset(preset) {
    const presets = {
      'compact': {
        baseSize: '14px',
        lineHeightMultiplier: 1.4,
        headingScale: 0.9,
        spacingScale: 0.8
      },
      'balanced': {
        baseSize: '16px',
        lineHeightMultiplier: 1.6,
        headingScale: 1,
        spacingScale: 1
      },
      'comfortable': {
        baseSize: '18px',
        lineHeightMultiplier: 1.8,
        headingScale: 1.2,
        spacingScale: 1.3
      },
      'accessible': {
        baseSize: '18px',
        lineHeightMultiplier: 1.75,
        headingScale: 1.15,
        spacingScale: 1.2
      }
    };

    const selectedPreset = presets[preset];
    if (selectedPreset) {
      document.documentElement.style.setProperty('--preset-base-size', selectedPreset.baseSize);
      document.documentElement.style.setProperty('--preset-line-height-multiplier', selectedPreset.lineHeightMultiplier);
      document.documentElement.style.setProperty('--preset-heading-scale', selectedPreset.headingScale);
      document.documentElement.style.setProperty('--preset-spacing-scale', selectedPreset.spacingScale);
    }
  }

  getSettingValue(settingId) {
    // This would normally interface with Shopify's theme editor API
    // For now, we'll read from data attributes or theme settings
    const element = document.querySelector(`[data-setting-id="${settingId}"]`);
    return element ? element.value : null;
  }

  // Font search functionality for Google Fonts
  async searchGoogleFonts(query) {
    const apiKey = this.getSettingValue('google_fonts_api_key');
    if (!apiKey) {
      console.warn('Google Fonts API key not provided');
      return [];
    }

    try {
      const response = await fetch(`https://www.googleapis.com/webfonts/v1/webfonts?key=${apiKey}&sort=popularity`);
      const data = await response.json();
      
      return data.items
        .filter(font => font.family.toLowerCase().includes(query.toLowerCase()))
        .slice(0, 10)
        .map(font => ({
          family: font.family,
          variants: font.variants,
          category: font.category
        }));
    } catch (error) {
      console.error('Error fetching Google Fonts:', error);
      return [];
    }
  }
}

// Initialize on DOM ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    window.typographyCustomizer = new TypographyCustomizer();
  });
} else {
  window.typographyCustomizer = new TypographyCustomizer();
}