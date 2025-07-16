class MFooter extends HTMLElement {
  constructor() {
    super();
    this.init();
  }

  init() {
    const mobileStickyBar = document.querySelector(".m-mobile-sticky-bar");

    // Set mobile sticky bar height for enhanced footer
    if (mobileStickyBar) {
      this.setMobileStickyBarHeight(mobileStickyBar);
      
      // Listen for resize events
      window.addEventListener('resize', () => {
        this.setMobileStickyBarHeight(mobileStickyBar);
      });
      
      // Legacy mobile event support
      document.addEventListener("matchMobile", () => {
        this.setMobileStickyBarHeight(mobileStickyBar);
      });
      
      document.addEventListener("unmatchMobile", () => {
        this.setMobileStickyBarHeight(mobileStickyBar);
      });
    }
  }

  setMobileStickyBarHeight(mobileStickyBar) {
    document.documentElement.style.setProperty(
      "--mobile-sticky-bar-height", 
      `${mobileStickyBar.offsetHeight}px`
    );
  }
}

// Support both old and enhanced footer systems
customElements.define("m-footer", MFooter);

// Enhanced footer specific functionality
document.addEventListener('DOMContentLoaded', function() {
  // Add any global footer enhancements here
  const footers = document.querySelectorAll('[class*="footer-"]');
  
  footers.forEach(footer => {
    // Add enhanced footer class for styling hooks
    footer.classList.add('enhanced-footer');
    
    // Support for smooth scrolling to footer
    const footerLinks = document.querySelectorAll('a[href="#footer"]');
    footerLinks.forEach(link => {
      link.addEventListener('click', (e) => {
        e.preventDefault();
        footer.scrollIntoView({ behavior: 'smooth' });
      });
    });
  });
});

// Social icon click tracking (if enabled in settings)
document.addEventListener('DOMContentLoaded', function() {
  function attachSocialTracking() {
    if (window.theme && window.theme.settings && window.theme.settings.social_enable_tracking) {
      document.querySelectorAll('.social-media-links--item').forEach(function(link) {
        link.addEventListener('click', function() {
          var social = link.getAttribute('aria-label') || link.href;
          if (window.dataLayer) {
            window.dataLayer.push({event: 'social_click', social: social});
          }
        });
      });
    }
  }
  attachSocialTracking();
  // Re-attach if social links are dynamically updated
  const observer = new MutationObserver(attachSocialTracking);
  document.querySelectorAll('.social-media-links').forEach(function(el) {
    observer.observe(el, { childList: true, subtree: true });
  });
});
