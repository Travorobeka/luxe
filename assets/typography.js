/**
 * Modular Typography System JavaScript
 * Handles dynamic typography features and accessibility
 */

class TypographySystem {
  constructor() {
    this.init();
  }

  init() {
    this.setupAccessibilityFeatures();
    this.setupPerformanceOptimizations();
    this.setupResponsiveHandling();
  }

  /**
   * Setup accessibility features
   */
  setupAccessibilityFeatures() {
    // Monitor for changes in user preferences
    if (window.matchMedia) {
      // Reduced motion preference
      const reduceMotionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
      this.handleReducedMotion(reduceMotionQuery);
      reduceMotionQuery.addEventListener('change', this.handleReducedMotion);

      // High contrast preference
      const highContrastQuery = window.matchMedia('(prefers-contrast: high)');
      this.handleHighContrast(highContrastQuery);
      highContrastQuery.addEventListener('change', this.handleHighContrast);
    }
  }

  /**
   * Handle reduced motion preference
   */
  handleReducedMotion(e) {
    const root = document.documentElement;
    if (e.matches) {
      root.style.setProperty('--animation-duration', '0.01ms');
      root.style.setProperty('--transition-duration', '0.01ms');
    } else {
      root.style.removeProperty('--animation-duration');
      root.style.removeProperty('--transition-duration');
    }
  }

  /**
   * Handle high contrast preference
   */
  handleHighContrast(e) {
    const root = document.documentElement;
    if (e.matches) {
      root.classList.add('high-contrast');
    } else {
      root.classList.remove('high-contrast');
    }
  }

  /**
   * Setup performance optimizations
   */
  setupPerformanceOptimizations() {
    // Font loading optimization
    if ('fonts' in document) {
      document.fonts.addEventListener('loadingdone', () => {
        document.documentElement.classList.add('fonts-loaded');
      });
    }

    // Optimize text rendering for critical text
    this.optimizeCriticalText();
  }

  /**
   * Optimize critical text rendering
   */
  optimizeCriticalText() {
    const criticalElements = document.querySelectorAll('h1, h2, .product-card__title, .price');
    criticalElements.forEach(element => {
      element.style.fontDisplay = 'swap';
    });
  }

  /**
   * Setup responsive typography handling
   */
  setupResponsiveHandling() {
    // Handle viewport changes for better responsive typography
    let resizeTimer;
    window.addEventListener('resize', () => {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(() => {
        this.updateViewportUnits();
      }, 100);
    });
  }

  /**
   * Update viewport units for better responsive scaling
   */
  updateViewportUnits() {
    const vh = window.innerHeight * 0.01;
    const vw = window.innerWidth * 0.01;
    document.documentElement.style.setProperty('--vh', `${vh}px`);
    document.documentElement.style.setProperty('--vw', `${vw}px`);
  }

  /**
   * Utility method to dynamically adjust font sizes
   */
  adjustFontSize(element, size) {
    if (element && size) {
      element.style.fontSize = `${size}px`;
    }
  }

  /**
   * Utility method to check if text is readable
   */
  checkReadability(element) {
    if (!element) return false;
    
    const computedStyle = window.getComputedStyle(element);
    const fontSize = parseFloat(computedStyle.fontSize);
    const lineHeight = parseFloat(computedStyle.lineHeight);
    
    // Basic readability checks
    return fontSize >= 14 && lineHeight >= fontSize * 1.2;
  }

  /**
   * Public method to update typography settings
   */
  updateSettings(settings) {
    const root = document.documentElement;
    
    Object.keys(settings).forEach(key => {
      const cssVar = `--${key.replace(/_/g, '-')}`;
      root.style.setProperty(cssVar, settings[key]);
    });
  }
}

// Initialize typography system when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  window.TypographySystem = new TypographySystem();
});

// Expose for theme customizer integration
window.MinimogTypography = {
  system: window.TypographySystem,
  updateSettings: (settings) => {
    if (window.TypographySystem) {
      window.TypographySystem.updateSettings(settings);
    }
  }
};