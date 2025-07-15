class MFooter extends HTMLElement {
  constructor() {
    super();
    this.init();
  }

  init() {
    const mobileAccordion = this.querySelector(".m-footer--accordion");
    const mobileStickyBar = document.querySelector(".m-mobile-sticky-bar");

    if (mobileAccordion) {
      if (MinimogTheme.config.mqlMobile) {
        this.acc = new MinimogLibs.Accordion(mobileAccordion, { presetContentHeight: true, onload: true });
      }
      document.addEventListener("matchMobile", () => {
        this.acc = new MinimogLibs.Accordion(mobileAccordion, { presetContentHeight: true, onload: true });
      });
    }

    // Set mobile stickybar height
    if (mobileStickyBar) {
      document.documentElement.style.setProperty("--mobile-sticky-bar-height", `${mobileStickyBar.offsetHeight}px`);
      document.addEventListener("matchMobile", () => {
        document.documentElement.style.setProperty("--mobile-sticky-bar-height", `${mobileStickyBar.offsetHeight}px`);
      });
      document.addEventListener("unmatchMobile", () => {
        document.documentElement.style.setProperty("--mobile-sticky-bar-height", `${mobileStickyBar.offsetHeight}px`);
      });
    }
  }
}
customElements.define("m-footer", MFooter);

// Enhanced Footer JS (from footer.md)
(function() {
  const menuToggles = document.querySelectorAll('.ai-footer-menu-toggle');

  menuToggles.forEach(toggle => {
    toggle.addEventListener('click', function(event) {
      const menuId = this.getAttribute('aria-controls');
      const menu = document.getElementById(menuId);
      const isExpanded = this.getAttribute('aria-expanded') === 'true';

      this.setAttribute('aria-expanded', !isExpanded);
      menu.classList.toggle('active');
      event.stopPropagation && event.stopPropagation();

      // Toggle plus/dash icon for plus style (ALWAYS update based on new state)
      if (this.querySelector('.plus-icon') && this.querySelector('.dash-icon')) {
        const nowExpanded = this.getAttribute('aria-expanded') === 'true';
        if (nowExpanded) {
          this.querySelector('.plus-icon').style.display = 'none';
          this.querySelector('.dash-icon').style.display = 'inline-block';
        } else {
          this.querySelector('.plus-icon').style.display = 'inline-block';
          this.querySelector('.dash-icon').style.display = 'none';
        }
      }
    });
  });

  const menuHeadings = document.querySelectorAll('.ai-footer-menu-heading');

  menuHeadings.forEach(heading => {
    heading.addEventListener('click', function(event) {
      // Only toggle if the click is on the heading, icon, or button (not on a link inside the menu)
      const wrapper = this.closest('.ai-footer-menu-wrapper');
      const toggle = wrapper.querySelector('.ai-footer-menu-toggle');
      // Only toggle on mobile (<= 767px)
      if (window.innerWidth <= 767) {
        if (toggle && (event.target === toggle || toggle.contains(event.target) || this.contains(event.target))) {
          toggle.click();
        }
      }
    });
  });

  window.addEventListener('resize', function() {
    if (window.innerWidth > 767) {
      document.querySelectorAll('.ai-footer-nav').forEach(menu => {
        menu.classList.add('active');
      });

      document.querySelectorAll('.ai-footer-menu-toggle').forEach(toggle => {
        toggle.setAttribute('aria-expanded', 'true');
      });
    }
    // Set correct plus/dash icon on resize
    document.querySelectorAll('.ai-footer-menu-toggle').forEach(toggle => {
      const isExpanded = toggle.getAttribute('aria-expanded') === 'true';
      if (toggle.querySelector('.plus-icon') && toggle.querySelector('.dash-icon')) {
        if (isExpanded) {
          toggle.querySelector('.plus-icon').style.display = 'none';
          toggle.querySelector('.dash-icon').style.display = 'inline-block';
        } else {
          toggle.querySelector('.plus-icon').style.display = 'inline-block';
          toggle.querySelector('.dash-icon').style.display = 'none';
        }
      }
    });
  });
  // Set correct plus/dash icon on page load
  document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.ai-footer-menu-toggle').forEach(toggle => {
      const isExpanded = toggle.getAttribute('aria-expanded') === 'true';
      if (toggle.querySelector('.plus-icon') && toggle.querySelector('.dash-icon')) {
        if (isExpanded) {
          toggle.querySelector('.plus-icon').style.display = 'none';
          toggle.querySelector('.dash-icon').style.display = 'inline-block';
        } else {
          toggle.querySelector('.plus-icon').style.display = 'inline-block';
          toggle.querySelector('.dash-icon').style.display = 'none';
        }
      }
    });
  });

  // Helper to set menu and icon state
  function setMenuAndIconState() {
    const isMobile = window.innerWidth <= 767;
    document.querySelectorAll('.ai-footer-menu-wrapper').forEach(wrapper => {
      const toggle = wrapper.querySelector('.ai-footer-menu-toggle');
      const menu = wrapper.querySelector('.ai-footer-nav');
      if (!toggle || !menu) return;
      if (isMobile) {
        // Collapse by default on mobile
        menu.classList.remove('active');
        toggle.setAttribute('aria-expanded', 'false');
      } else {
        // Expand by default on desktop
        menu.classList.add('active');
        toggle.setAttribute('aria-expanded', 'true');
      }
      // Set correct icon
      const isExpanded = toggle.getAttribute('aria-expanded') === 'true';
      if (toggle.querySelector('.plus-icon') && toggle.querySelector('.dash-icon')) {
        if (isExpanded) {
          toggle.querySelector('.plus-icon').style.display = 'none';
          toggle.querySelector('.dash-icon').style.display = 'inline-block';
        } else {
          toggle.querySelector('.plus-icon').style.display = 'inline-block';
          toggle.querySelector('.dash-icon').style.display = 'none';
        }
      }
    });
  }
  // On load
  document.addEventListener('DOMContentLoaded', setMenuAndIconState);
  // On resize
  window.addEventListener('resize', setMenuAndIconState);
})();
