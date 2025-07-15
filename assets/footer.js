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
// --- Dynamic Responsive Breakpoints for Footer Grid ---
document.addEventListener('DOMContentLoaded', function() {
  const footerGrids = document.querySelectorAll('[class*="footer-grid-"][data-responsive-breakpoints]');

  function parseBreakpoints(breakpointsStr) {
    // Example: "1200:4,900:3,600:2" => [{width:1200,cols:4},...]
    return breakpointsStr.split(',').map(bp => {
      const [width, cols] = bp.split(':');
      return { width: parseInt(width.trim(), 10), cols: parseInt(cols.trim(), 10) };
    }).sort((a, b) => b.width - a.width); // Descending order
  }

  function applyResponsiveColumns(grid, breakpoints) {
    const width = window.innerWidth;
    let applied = false;
    for (const bp of breakpoints) {
      if (width <= bp.width) {
        grid.style.gridTemplateColumns = `repeat(${bp.cols}, 1fr)`;
        applied = true;
      }
    }
    if (!applied && grid.dataset.defaultColumns) {
      grid.style.gridTemplateColumns = grid.dataset.defaultColumns;
    }
  }

  footerGrids.forEach(grid => {
    const breakpointsStr = grid.getAttribute('data-responsive-breakpoints');
    const breakpoints = parseBreakpoints(breakpointsStr);
    // Store the default columns style
    grid.dataset.defaultColumns = grid.style.gridTemplateColumns;

    function updateGridColumns() {
      applyResponsiveColumns(grid, breakpoints);
    }

    window.addEventListener('resize', updateGridColumns);
    updateGridColumns();
  });
});
