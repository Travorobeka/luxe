(function() {
  const menuToggles = document.querySelectorAll('.footer__menu-toggle');
  menuToggles.forEach(toggle => {
    toggle.addEventListener('click', function(event) {
      const menuId = this.getAttribute('aria-controls');
      const menu = document.getElementById(menuId);
      const isExpanded = this.getAttribute('aria-expanded') === 'true';
      this.setAttribute('aria-expanded', !isExpanded);
      menu.classList.toggle('active');
      event.stopPropagation && event.stopPropagation();
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
  const menuHeadings = document.querySelectorAll('.footer__menu-heading');
  menuHeadings.forEach(heading => {
    heading.addEventListener('click', function(event) {
      const wrapper = this.closest('.footer__menu-wrapper');
      const toggle = wrapper.querySelector('.footer__menu-toggle');
      if (window.innerWidth <= 767) {
        if (toggle && (event.target === toggle || toggle.contains(event.target) || this.contains(event.target))) {
          toggle.click();
        }
      }
    });
  });
  window.addEventListener('resize', function() {
    if (window.innerWidth > 767) {
      document.querySelectorAll('.footer__nav').forEach(menu => {
        menu.classList.add('active');
      });
      document.querySelectorAll('.footer__menu-toggle').forEach(toggle => {
        toggle.setAttribute('aria-expanded', 'true');
      });
    }
    document.querySelectorAll('.footer__menu-toggle').forEach(toggle => {
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
  document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.footer__menu-toggle').forEach(toggle => {
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
  function setMenuAndIconState() {
    const isMobile = window.innerWidth <= 767;
    document.querySelectorAll('.footer__menu-wrapper').forEach(wrapper => {
      const toggle = wrapper.querySelector('.footer__menu-toggle');
      const menu = wrapper.querySelector('.footer__nav');
      if (!toggle || !menu) return;
      if (isMobile) {
        menu.classList.remove('active');
        toggle.setAttribute('aria-expanded', 'false');
      } else {
        menu.classList.add('active');
        toggle.setAttribute('aria-expanded', 'true');
      }
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
  document.addEventListener('DOMContentLoaded', setMenuAndIconState);
  window.addEventListener('resize', setMenuAndIconState);
})();
