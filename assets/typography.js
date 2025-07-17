/**
 * UNIFIED TYPOGRAPHY SYSTEM - JavaScript
 * =====================================
 * 
 * This file provides JavaScript functionality for the unified typography system.
 * It handles dynamic updates, accessibility features, and performance optimizations.
 */

class TypographySystem {
  constructor() {
    this.init();
  }

  init() {
    this.setupAccessibilityFeatures();
    this.setupPerformanceOptimizations();
    this.setupResponsiveHandling();
    this.setupDynamicUpdates();
  }

  /**
   * Setup accessibility features
   */
  setupAccessibilityFeatures() {
    // Monitor for changes in user preferences
    if (window.matchMedia) {
      // Reduced motion preference
      const reduceMotionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
      this.handleReduceMotionChange(reduceMotionQuery);
      reduceMotionQuery.addEventListener('change', (e) => this.handleReduceMotionChange(e));

      // High contrast preference
      const highContrastQuery = window.matchMedia('(prefers-contrast: high)');
      this.handleHighContrastChange(highContrastQuery);
      highContrastQuery.addEventListener('change', (e) => this.handleHighContrastChange(e));
    }
  }

  /**
   * Handle reduced motion preference changes
   */
  handleReduceMotionChange(query) {
    if (query.matches) {
      document.documentElement.style.setProperty('--animation-duration', '0.01ms');
      document.documentElement.style.setProperty('--transition-duration', '0.01ms');
    } else {
      document.documentElement.style.removeProperty('--animation-duration');
      document.documentElement.style.removeProperty('--transition-duration');
    }
  }

  /**
   * Handle high contrast preference changes
   */
  handleHighContrastChange(query) {
    if (query.matches) {
      document.documentElement.style.setProperty('--color-heading', '0, 0, 0');
      document.documentElement.style.setProperty('--color-foreground', '0, 0, 0');
      document.documentElement.style.setProperty('--color-foreground-secondary', '0, 0, 0');
    } else {
      document.documentElement.style.removeProperty('--color-heading');
      document.documentElement.style.removeProperty('--color-foreground');
      document.documentElement.style.removeProperty('--color-foreground-secondary');
    }
  }

  /**
   * Setup performance optimizations
   */
  setupPerformanceOptimizations() {
    // Font loading optimization
    if ('fonts' in document) {
      document.fonts.ready.then(() => {
        this.onFontsLoaded();
      });
    }

    // Intersection Observer for typography animations
    if ('IntersectionObserver' in window) {
      this.setupTypographyAnimations();
    }
  }

  /**
   * Handle font loading completion
   */
  onFontsLoaded() {
    document.documentElement.classList.add('fonts-loaded');
    
    // Trigger custom event for other components
    window.dispatchEvent(new CustomEvent('typography:fonts-loaded', {
      detail: { timestamp: Date.now() }
    }));
  }

  /**
   * Setup typography animations
   */
  setupTypographyAnimations() {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('typography-animate');
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    });

    // Observe all typography elements
    document.querySelectorAll('.main-heading, .sub-heading, .body-text').forEach(el => {
      observer.observe(el);
    });
  }

  /**
   * Setup responsive handling
   */
  setupResponsiveHandling() {
    // Handle viewport changes
    let resizeTimeout;
    window.addEventListener('resize', () => {
      clearTimeout(resizeTimeout);
      resizeTimeout = setTimeout(() => {
        this.updateResponsiveTypography();
      }, 100);
    });

    // Initial responsive update
    this.updateResponsiveTypography();
  }

  /**
   * Update responsive typography based on viewport
   */
  updateResponsiveTypography() {
    const viewportWidth = window.innerWidth;
    const isMobile = viewportWidth <= 767;
    const isTablet = viewportWidth > 767 && viewportWidth <= 1023;
    const isDesktop = viewportWidth > 1023;

    document.documentElement.classList.toggle('typography-mobile', isMobile);
    document.documentElement.classList.toggle('typography-tablet', isTablet);
    document.documentElement.classList.toggle('typography-desktop', isDesktop);
  }

  /**
   * Setup dynamic updates
   */
  setupDynamicUpdates() {
    // Listen for theme customizer changes
    if (window.Shopify && window.Shopify.theme) {
      window.Shopify.theme.on('change', (event) => {
        if (event.target && event.target.sectionId === 'typography') {
          this.updateFromSettings(event.target.settings);
        }
      });
    }
  }

  /**
   * Update typography from settings
   */
  updateFromSettings(settings) {
    if (!settings) return;

    // Update CSS custom properties
    Object.keys(settings).forEach(key => {
      if (key.startsWith('main_heading_') || key.startsWith('sub_heading_') || key.startsWith('body_')) {
        const value = settings[key];
        const cssVar = this.convertSettingToCSSVar(key, value);
        if (cssVar) {
          document.documentElement.style.setProperty(cssVar.name, cssVar.value);
        }
      }
    });

    // Trigger update event
    window.dispatchEvent(new CustomEvent('typography:updated', {
      detail: { settings, timestamp: Date.now() }
    }));
  }

  /**
   * Convert setting key to CSS variable
   */
  convertSettingToCSSVar(key, value) {
    const mappings = {
      'main_heading_font_size': '--font-size-main-heading',
      'main_heading_font_weight': '--font-weight-main-heading',
      'main_heading_line_height': '--line-height-main-heading',
      'main_heading_letter_spacing': '--letter-spacing-main-heading',
      'sub_heading_font_size': '--font-size-sub-heading',
      'sub_heading_font_weight': '--font-weight-sub-heading',
      'sub_heading_line_height': '--line-height-sub-heading',
      'sub_heading_letter_spacing': '--letter-spacing-sub-heading',
      'body_font_size': '--font-size-body-text',
      'body_font_weight': '--font-weight-body-text',
      'body_line_height': '--line-height-body-text',
      'body_letter_spacing': '--letter-spacing-body-text'
    };

    const cssVarName = mappings[key];
    if (!cssVarName) return null;

    let cssValue = value;
    
    // Add units where needed
    if (key.includes('font_size')) {
      cssValue = `${value}px`;
    } else if (key.includes('letter_spacing')) {
      cssValue = `${value}px`;
    }

    return { name: cssVarName, value: cssValue };
  }

  /**
   * Apply typography class to element
   */
  applyTypographyClass(element, className) {
    if (!element || !className) return;

    // Remove existing typography classes
    element.classList.remove('main-heading', 'sub-heading', 'body-text');
    
    // Add new class
    element.classList.add(className);
  }

  /**
   * Get current typography settings
   */
  getCurrentSettings() {
    const root = document.documentElement;
    const computedStyle = getComputedStyle(root);
    
    return {
      'main_heading_font_size': this.extractNumericValue(computedStyle.getPropertyValue('--font-size-main-heading')),
      'main_heading_font_weight': computedStyle.getPropertyValue('--font-weight-main-heading'),
      'main_heading_line_height': computedStyle.getPropertyValue('--line-height-main-heading'),
      'main_heading_letter_spacing': this.extractNumericValue(computedStyle.getPropertyValue('--letter-spacing-main-heading')),
      'sub_heading_font_size': this.extractNumericValue(computedStyle.getPropertyValue('--font-size-sub-heading')),
      'sub_heading_font_weight': computedStyle.getPropertyValue('--font-weight-sub-heading'),
      'sub_heading_line_height': computedStyle.getPropertyValue('--line-height-sub-heading'),
      'sub_heading_letter_spacing': this.extractNumericValue(computedStyle.getPropertyValue('--letter-spacing-sub-heading')),
      'body_font_size': this.extractNumericValue(computedStyle.getPropertyValue('--font-size-body-text')),
      'body_font_weight': computedStyle.getPropertyValue('--font-weight-body-text'),
      'body_line_height': computedStyle.getPropertyValue('--line-height-body-text'),
      'body_letter_spacing': this.extractNumericValue(computedStyle.getPropertyValue('--letter-spacing-body-text'))
    };
  }

  /**
   * Extract numeric value from CSS value
   */
  extractNumericValue(cssValue) {
    const match = cssValue.match(/(\d+(?:\.\d+)?)/);
    return match ? parseFloat(match[1]) : 0;
  }

  /**
   * Enable typography debugging
   */
  enableDebugging() {
    document.documentElement.classList.add('typography-debug');
    
    // Log current settings
    console.log('Typography System Debug:', this.getCurrentSettings());
  }

  /**
   * Disable typography debugging
   */
  disableDebugging() {
    document.documentElement.classList.remove('typography-debug');
  }
}

// Initialize the typography system
document.addEventListener('DOMContentLoaded', () => {
  window.TypographySystem = new TypographySystem();
});

// Global API for backward compatibility
window.MinimogTypography = {
  updateSettings: (settings) => {
    if (window.TypographySystem) {
      window.TypographySystem.updateFromSettings(settings);
    }
  },
  
  getSettings: () => {
    if (window.TypographySystem) {
      return window.TypographySystem.getCurrentSettings();
    }
    return {};
  },
  
  applyClass: (element, className) => {
    if (window.TypographySystem) {
      window.TypographySystem.applyTypographyClass(element, className);
    }
  }
};

// Export for module systems
if (typeof module !== 'undefined' && module.exports) {
  module.exports = TypographySystem;
}