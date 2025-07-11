 **Purpose:**
This file defines comprehensive guidelines and rules for developing Shopify themes, ensuring code quality, maintainability, and best practices throughout your project.
**Key Contents:**
- **Theme Architecture Best Practices**
  - **Online Store 2.0 Compliance:**
    - Build themes compatible with OS 2.0 (sections everywhere, app blocks, dynamic sections).
  - **Modular Design:**
    - Use reusable snippets and modular section design.
- **Liquid Development Guidelines**
  - **Handles:**
    - Always use lowercase, hyphenated handles.
  - **Operators:**
    - Use correct Liquid operators (`==`, `!=`, `>`, `<`, `>=`, `<=`, `and`, `or`, `contains`).
  - **Data Types:**
    - Work with String, Number, Boolean, Nil, Array, and EmptyDrop.
  - **Variable Assignment:**
    - Use `{% assign %}` or `{% capture %}`.
- **Liquid Tag Usage**
  - **Whitespace Control:**
    - Use hyphens in tags to strip whitespace for clean HTML.
  - **Control Flow:**
    - Use `{% if %}`, `{% elsif %}`, `{% else %}`, `{% endif %}`, `{% unless %}`, `{% case %}`, `{% when %}`.
  - **Iteration:**
    - Use `{% for %}` with `{% else %}` for empty collections, `{% paginate %}` for long lists, `{% break %}`, `{% continue %}`, `{% cycle %}`.
  - **Theme-Specific Tags:**
    - Prefer `{% render %}` over `{% include %}` for scope isolation.
- **Shopify Objects & Filters**
  - Reference key Shopify objects (product, collection, cart, etc.).
  - Use Shopify’s built-in filters for colors, URLs, and more.
- **Security Best Practices**
  - Input sanitization and safe output.
- **Performance Monitoring**
  - Optimize images, use browser caching, implement critical CSS, defer non-critical JS.
- **Theme Deployment Workflow**
  - **Pre-deployment Checklist:**
    - Run Theme Check, test on dev store, verify breakpoints, check accessibility, validate performance.
  - **Post-deployment Tasks:**
    - Monitor logs, check analytics, gather feedback, plan improvements.
  - **Automated Git Workflow:**
    - Always stage, commit, and push changes to GitHub after significant work.
    - **Documentation Requirements**
  - Document all custom functionality, maintain a changelog, create setup instructions, and document theme settings.
- **Continuous Improvement**
  - Regular code reviews, performance audits, accessibility and security updates.
**How to Use:**
Follow these rules for every theme customization, section, snippet, or asset you create or modify. Always push your changes to Shopify and GitHub as part of your workflow.