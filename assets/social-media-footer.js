class SocialMediaFooter {
  constructor() {
    this.init();
  }

  init() {
    this.setupEventListeners();
    this.setupIntersectionObserver();
  }

  setupEventListeners() {
    // Add click tracking for analytics
    const socialIcons = document.querySelectorAll('.social-media-footer-icon');
    
    socialIcons.forEach(icon => {
      icon.addEventListener('click', (e) => {
        this.trackSocialClick(e);
      });
    });

    // Add keyboard navigation support
    socialIcons.forEach(icon => {
      icon.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          icon.click();
        }
      });
    });
  }

  setupIntersectionObserver() {
    // Animate icons when they come into view
    const observerOptions = {
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('social-media-footer-icon--visible');
        }
      });
    }, observerOptions);

    const socialIcons = document.querySelectorAll('.social-media-footer-icon');
    socialIcons.forEach(icon => {
      observer.observe(icon);
    });
  }

  trackSocialClick(event) {
    const platform = this.getPlatformFromElement(event.currentTarget);
    const url = event.currentTarget.href;
    
    // Track social media clicks for analytics
    if (typeof gtag !== 'undefined') {
      gtag('event', 'social_click', {
        'event_category': 'social_media',
        'event_label': platform,
        'value': 1
      });
    }

    // Track with Facebook Pixel if available
    if (typeof fbq !== 'undefined') {
      fbq('track', 'CustomEvent', {
        event_name: 'social_media_click',
        platform: platform,
        url: url
      });
    }

    // Log to console for debugging
    console.log(`Social media click tracked: ${platform} - ${url}`);
  }

  getPlatformFromElement(element) {
    const classList = element.classList;
    
    if (classList.contains('social-media-footer-icon--facebook')) return 'facebook';
    if (classList.contains('social-media-footer-icon--instagram')) return 'instagram';
    if (classList.contains('social-media-footer-icon--twitter')) return 'twitter';
    if (classList.contains('social-media-footer-icon--linkedin')) return 'linkedin';
    if (classList.contains('social-media-footer-icon--youtube')) return 'youtube';
    if (classList.contains('social-media-footer-icon--tiktok')) return 'tiktok';
    if (classList.contains('social-media-footer-icon--pinterest')) return 'pinterest';
    if (classList.contains('social-media-footer-icon--whatsapp')) return 'whatsapp';
    if (classList.contains('social-media-footer-icon--spotify')) return 'spotify';
    
    return 'unknown';
  }

  // Method to update icon colors dynamically
  updateIconColors(primaryColor, hoverColor) {
    const socialSection = document.querySelector('.social-media-footer-section');
    if (socialSection) {
      socialSection.style.setProperty('--social-icon-color', primaryColor);
      socialSection.style.setProperty('--social-icon-hover-color', hoverColor);
    }
  }

  // Method to update icon size dynamically
  updateIconSize(size) {
    const socialSection = document.querySelector('.social-media-footer-section');
    if (socialSection) {
      socialSection.style.setProperty('--social-icon-size', `${size}px`);
    }
  }

  // Method to update spacing dynamically
  updateIconSpacing(spacing) {
    const socialSection = document.querySelector('.social-media-footer-section');
    if (socialSection) {
      socialSection.style.setProperty('--social-spacing', `${spacing}px`);
    }
  }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  new SocialMediaFooter();
});

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
  module.exports = SocialMediaFooter;
}