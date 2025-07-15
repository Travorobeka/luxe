{% doc %}
  @prompt
  Create a beautiful, minimal footer section with clean typography, subtle spacing, and modern design elements. Include
  areas for company information, navigation links, social media icons, and copyright text. Use a simple color scheme and
  ensure the footer is responsive across all devices., use shopify's native payment icons, add a newsletter signup form
  section with differnt footer customisations to pick from and edit/chnage,, use the native menus and also make it a
  drop dwon, add payment icons in the bottom bar on the same line as the copright text and shrink the icon size, fix the
  newsletter signup form. its not working. and the payment icons are not displaying Liquid error
  (temp/ai_gen_block_af788a6 line 245): Invalid form type "aogqrc2l6ck5vr1czbaigenblockaf788a6qxclxj", must be one of
  ["product", "storefront_password", "contact", "customer_login", "create_customer", "recover_customer_password",
  "reset_customer_password", "guest_login", "currency", "activate_customer_password", "customer_address", "new_comment",
  "customer", "localization", "cart"]
{% enddoc %}
{% assign ai_gen_id = block.id | replace: '_', '' | downcase %}

{% style %}
  .ai-footer-{{ ai_gen_id }} {
    padding: {{ block.settings.padding_top }}px 0 {{ block.settings.padding_bottom }}px;
    background-color: {{ block.settings.background_color }};
    color: {{ block.settings.text_color }};
    font-size: {{ block.settings.text_size }}px;
    line-height: 1.5;
  }

  .ai-footer-container-{{ ai_gen_id }} {
    max-width: {{ block.settings.container_width }}px;
    margin: 0 auto;
    padding: 0 20px;
  }

  .ai-footer-grid-{{ ai_gen_id }} {
    display: grid;
    {% case block.settings.column_width_mode %}
      {% when 'even' %}
        grid-template-columns: repeat({{ block.settings.columns }}, 1fr);
      {% when 'custom' %}
        grid-template-columns:
          {% if block.settings.columns == '2' %}
            {{ block.settings.column1_width }} {{ block.settings.column2_width }};
          {% elsif block.settings.columns == '3' %}
            {{ block.settings.column1_width }} {{ block.settings.column2_width }} {{ block.settings.column3_width }};
          {% else %}
            {{ block.settings.column1_width }} {{ block.settings.column2_width }} {{ block.settings.column3_width }} {{ block.settings.column4_width }};
          {% endif %}
      {% when 'auto' %}
        grid-template-columns: repeat({{ block.settings.columns }}, auto);
      {% when 'fluid' %}
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      {% else %}
        grid-template-columns: repeat({{ block.settings.columns }}, 1fr);
    {% endcase %}
    gap: {{ block.settings.column_spacing }}px;
    margin-bottom: {{ block.settings.section_spacing }}px;
    justify-content: {{ block.settings.column_horizontal_align }};
    align-items: {{ block.settings.column_vertical_align }};
  }
  .ai-footer-column-{{ ai_gen_id }}:nth-child(1) { padding: {{ block.settings.column1_padding }}px; }
  .ai-footer-column-{{ ai_gen_id }}:nth-child(2) { padding: {{ block.settings.column2_padding }}px; }
  .ai-footer-column-{{ ai_gen_id }}:nth-child(3) { padding: {{ block.settings.column3_padding }}px; }
  .ai-footer-column-{{ ai_gen_id }}:nth-child(4) { padding: {{ block.settings.column4_padding }}px; }

  .ai-footer-column-{{ ai_gen_id }} {
    display: flex;
    flex-direction: column;
  }

  .ai-footer-title-{{ ai_gen_id }} {
    font-size: {{ block.settings.heading_size }}px;
    font-weight: 500;
    margin-top: 0;
    margin-bottom: 20px;
    color: {{ block.settings.heading_color }};
  }

  .ai-footer-nav-{{ ai_gen_id }} {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin: 0;
    padding: 0;
    list-style: none;
    opacity: 1;
    max-height: 1000px;
    transition: none;
  }

  .ai-footer-nav-{{ ai_gen_id }}.fade {
    transition: opacity 0.3s;
    opacity: 0;
    max-height: 0;
    pointer-events: none;
  }

  .ai-footer-nav-{{ ai_gen_id }}.fade.active {
    opacity: 1;
    max-height: 1000px;
    pointer-events: auto;
  }

  .ai-footer-nav-{{ ai_gen_id }}.slide {
    transition: max-height 0.4s cubic-bezier(0.4,0,0.2,1), opacity 0.3s;
    max-height: 0;
    opacity: 0;
    overflow: hidden;
    pointer-events: none;
  }

  .ai-footer-nav-{{ ai_gen_id }}.slide.active {
    max-height: 1000px;
    opacity: 1;
    pointer-events: auto;
  }

  .ai-footer-nav-item-{{ ai_gen_id }} a {
    text-decoration: none;
    color: {{ block.settings.text_color }};
    transition: color 0.2s ease;
  }

  .ai-footer-nav-item-{{ ai_gen_id }} a:hover {
    color: {{ block.settings.link_hover_color }};
  }

  .ai-footer-company-info-{{ ai_gen_id }} {
    margin-bottom: 20px;
  }

  .ai-footer-social-{{ ai_gen_id }} {
    display: flex;
    gap: {{ block.settings.social_icon_spacing }}px;
    margin-top: 20px;
  }

  .ai-footer-social-link-{{ ai_gen_id }} {
    display: flex;
    align-items: center;
    justify-content: center;
    width: {{ block.settings.social_icon_size }}px;
    height: {{ block.settings.social_icon_size }}px;
    border-radius: {{ block.settings.social_icon_border_radius }}px;
    background-color: {{ block.settings.social_bg_color }};
    color: {{ block.settings.social_icon_color }};
    transition: all {{ block.settings.social_hover_transition }}s ease;
  }

  .ai-footer-social-link-{{ ai_gen_id }}:hover {
    background-color: {{ block.settings.social_hover_bg_color }};
    color: {{ block.settings.social_hover_icon_color }};
    {% if block.settings.social_hover_scale > 1 %}
    transform: scale({{ block.settings.social_hover_scale }});
    {% endif %}
    {% if block.settings.social_hover_rotate != 0 %}
    transform: rotate({{ block.settings.social_hover_rotate }}deg);
    {% endif %}
  }

  .ai-footer-social-icon-{{ ai_gen_id }} {
    width: {{ block.settings.social_icon_inner_size }}px;
    height: {{ block.settings.social_icon_inner_size }}px;
  }

  .ai-footer-bottom-{{ ai_gen_id }} {
    display: flex;
    align-items: center;
    padding-top: 20px;
    border-top: 1px solid {{ block.settings.border_color }};
    justify-content:
      {% case block.settings.footer_bottom_alignment %}
        {% when 'left' %} flex-start;
        {% when 'center' %} center;
        {% when 'right' %} flex-end;
        {% when 'space-between' %} space-between;
        {% when 'space-around' %} space-around;
        {% else %} flex-start;
      {% endcase %}
  }

  .ai-footer-copyright-{{ ai_gen_id }} {
    font-size: {{ block.settings.copyright_size }}px;
  }

  .ai-footer-payment-{{ ai_gen_id }} {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    align-items: center;
  }

  .ai-footer-payment-{{ ai_gen_id }} svg {
    width: {{ block.settings.payment_icon_size }}px;
    height: auto;
  }

  .ai-footer-newsletter-{{ ai_gen_id }} {
    margin-bottom: 30px;
  }

  .ai-footer-newsletter-form-{{ ai_gen_id }} {
    display: flex;
    flex-direction: {{ block.settings.newsletter_layout }};
    gap: 10px;
    margin-top: 15px;
  }

  .ai-footer-newsletter-input-{{ ai_gen_id }} {
    flex: 1;
    min-width: 0;
    padding: 12px 15px;
    border: 1px solid {{ block.settings.newsletter_input_border }};
    border-radius: {{ block.settings.newsletter_border_radius }}px;
    background-color: {{ block.settings.newsletter_input_bg }};
    color: {{ block.settings.newsletter_input_color }};
  }

  .ai-footer-newsletter-input-{{ ai_gen_id }}::placeholder {
    color: {{ block.settings.newsletter_input_color }};
    opacity: 0.7;
  }

  .ai-footer-newsletter-button-{{ ai_gen_id }} {
    padding: 12px 20px;
    border: none;
    border-radius: {{ block.settings.newsletter_border_radius }}px;
    background-color: {{ block.settings.newsletter_button_bg }};
    color: {{ block.settings.newsletter_button_color }};
    cursor: pointer;
    font-weight: 500;
    transition: background-color 0.2s ease;
    white-space: nowrap;
  }

  .ai-footer-newsletter-button-{{ ai_gen_id }}:hover {
    background-color: {{ block.settings.newsletter_button_hover_bg }};
  }

  .ai-footer-newsletter-text-{{ ai_gen_id }} {
    margin-top: 0;
    margin-bottom: 15px;
  }

  .ai-footer-newsletter-error-{{ ai_gen_id }} {
    color: #d82c0d;
    font-size: 13px;
    margin-bottom: 10px;
  }

  .ai-footer-newsletter-success-{{ ai_gen_id }} {
    color: #008060;
    font-size: 13px;
    margin-bottom: 10px;
  }

  .ai-footer-menu-toggle-{{ ai_gen_id }} {
    display: none;
    background: none;
    border: none;
    padding: 0;
    margin: 0;
    cursor: pointer;
    position: absolute;
    right: 0;
    top: 0;
    width: 24px;
    height: 24px;
    color: {{ block.settings.heading_color }};
  }

  .ai-footer-menu-wrapper-{{ ai_gen_id }} {
    position: relative;
  }

  .ai-footer-menu-heading-{{ ai_gen_id }} {
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: relative;
  }

  .ai-footer-bottom-group-{{ ai_gen_id }} {
    display: flex;
    align-items: center;
    gap: 20px;
  }

  @media screen and (max-width: 767px) {
    .ai-footer-grid-{{ ai_gen_id }} {
      grid-template-columns: repeat({{ block.settings.columns_mobile }}, 1fr);
      gap: 0;
    }

    .ai-footer-column-{{ ai_gen_id }} {
      margin-bottom: 20px;
    }

    .ai-footer-menu-toggle-{{ ai_gen_id }} {
      display: block;
    }

    .ai-footer-menu-heading-{{ ai_gen_id }} {
      cursor: pointer;
      padding-right: 30px;
    }

    .ai-footer-nav-{{ ai_gen_id }} {
      display: none;
      padding-bottom: 15px;
    }

    .ai-footer-nav-{{ ai_gen_id }}.active {
      display: flex;
    }

    .ai-footer-bottom-{{ ai_gen_id }} {
      flex-direction: column;
      gap: 15px;
      text-align: center;
      justify-content: center !important;
    }

    .ai-footer-bottom-group-{{ ai_gen_id }} {
      flex-direction: column;
      gap: 15px;
    }

    .ai-footer-newsletter-form-{{ ai_gen_id }} {
      flex-direction: column;
    }
  }

  .ai-footer-newsletter-input-group {
    display: flex;
    align-items: stretch;
  }
  .ai-footer-newsletter-input-group-wrapper-{{ ai_gen_id }} {
    display: flex;
    width: 100%;
  }
  .ai-footer-newsletter-input-group-wrapper-{{ ai_gen_id }} .ai-footer-newsletter-input-{{ ai_gen_id }} {
    border-top-right-radius: 0 !important;
    border-bottom-right-radius: 0 !important;
    flex: 1;
  }
  .ai-footer-newsletter-input-group-wrapper-{{ ai_gen_id }} .ai-footer-newsletter-button-{{ ai_gen_id }} {
    border-top-left-radius: 0 !important;
    border-bottom-left-radius: 0 !important;
    margin-left: -1px;
    min-width: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0 16px;
  }
  .ai-footer-newsletter-button-icon-arrow svg,
  .ai-footer-newsletter-button-icon-plus svg,
  .ai-footer-newsletter-button-icon-custom svg {
    display: inline-block;
    vertical-align: middle;
  }

  .ai-footer-menu-heading-{{ ai_gen_id }} {
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: relative;
  }
  .ai-footer-menu-toggle-{{ ai_gen_id }} svg {
    display: inline-block;
    vertical-align: middle;
  }

  @media screen and (min-width: 768px) {
    .ai-footer-nav-{{ ai_gen_id }} {
      display: flex !important;
      flex-direction: column;
    }
  }

  {% comment %} Newsletter Title Customization {% endcomment %}
  .ai-footer-newsletter-title-{{ ai_gen_id }} {
    text-transform: {{ block.settings.newsletter_title_transform }};
    font-weight: {{ block.settings.newsletter_title_weight }};
    font-size: {{ block.settings.newsletter_title_size }}px;
    background: {{ block.settings.menu_bg_color }};
    border-radius: {{ block.settings.menu_border_radius }}px;
    padding: 8px 20px 8px 0;
    display: inline-block;
  }

  {% comment %} Company Title Customization {% endcomment %}
  .ai-footer-company-title-{{ ai_gen_id }} {
    text-transform: {{ block.settings.company_title_transform }};
    font-weight: {{ block.settings.company_title_weight }};
    font-size: {{ block.settings.company_title_size }}px;
    background: {{ block.settings.menu_bg_color }};
    border-radius: {{ block.settings.menu_border_radius }}px;
    padding: 8px 16px;
    display: inline-block;
  }

  {% comment %} Menu Title Customization {% endcomment %}
  .ai-footer-menu-title-{{ ai_gen_id }} {
    text-transform: {{ block.settings.menu_title_transform }};
    font-weight: {{ block.settings.menu_title_weight }};
    font-size: {{ block.settings.menu_title_size }}px;
    background: {{ block.settings.menu_bg_color }};
    border-radius: {{ block.settings.menu_border_radius }}px;
    padding: {{ block.settings.menu_padding_y }}px {{ block.settings.menu_padding_x }}px;
    display: inline-block;
  }

  .ai-footer-menu-toggle-{{ ai_gen_id }}:focus {
    outline: none;
    box-shadow: none;
  }
{% endstyle %}

<footer class="ai-footer-{{ ai_gen_id }}" {{ block.shopify_attributes }}>
  <div class="ai-footer-container-{{ ai_gen_id }}">
    {% if block.settings.show_newsletter %}
      <div
        class="ai-footer-newsletter-{{ ai_gen_id }} ai-footer-newsletter-layout-{{ block.settings.newsletter_layout }} ai-footer-newsletter-align-{{ block.settings.newsletter_align }}"
        style="
          {% if block.settings.newsletter_bg_image != blank %}background-image: url('{{ block.settings.newsletter_bg_image | img_url: 'master' }}'); background-size: cover; background-position: center;{% endif %}
          padding: {{ block.settings.newsletter_section_padding }}px;
          margin-bottom: {{ block.settings.newsletter_section_margin }}px;
        "
      >
        <h3 class="ai-footer-title-{{ ai_gen_id }} ai-footer-newsletter-title-{{ ai_gen_id }}">
          {{ block.settings.newsletter_title }}
        </h3>
        <p class="ai-footer-newsletter-text-{{ ai_gen_id }}">{{ block.settings.newsletter_text }}</p>
        {% form 'customer' %}
          {% if form.errors %}
            <div class="ai-footer-newsletter-error-{{ ai_gen_id }}">
              {{ block.settings.newsletter_error_message | default: form.errors | default_errors }}
            </div>
          {% endif %}
          {% if form.posted_successfully? %}
            <div class="ai-footer-newsletter-success-{{ ai_gen_id }}">
              {{ block.settings.newsletter_success_message }}
            </div>
          {% else %}
            <input type="hidden" name="contact[tags]" value="newsletter">
            <div class="ai-footer-newsletter-form-{{ ai_gen_id }} ai-footer-newsletter-form-style-{{ block.settings.newsletter_input_style }} ai-footer-newsletter-button-style-{{ block.settings.newsletter_button_style }}{% if block.settings.newsletter_button_inside_input %} ai-footer-newsletter-input-group{% endif %}">
              {% if block.settings.newsletter_show_name %}
                <input
                  type="text"
                  name="contact[first_name]"
                  class="ai-footer-newsletter-input-{{ ai_gen_id }}"
                  placeholder="Your name"
                  style="border-radius: {% if block.settings.newsletter_input_style == 'pill' %}999px{% elsif block.settings.newsletter_input_style == 'rounded' %}{{ block.settings.newsletter_border_radius }}px{% else %}0{% endif %};"
                >
              {% endif %}
              {% if block.settings.newsletter_button_inside_input %}
                <div class="ai-footer-newsletter-input-group-wrapper-{{ ai_gen_id }}">
                  <input
                    type="email"
                    name="contact[email]"
                    id="newsletter-{{ ai_gen_id }}"
                    class="ai-footer-newsletter-input-{{ ai_gen_id }}"
                    value="{{ form.email }}"
                    placeholder="{{ block.settings.newsletter_placeholder }}"
                    required
                    style="border-radius: {% if block.settings.newsletter_input_style == 'pill' %}999px{% elsif block.settings.newsletter_input_style == 'rounded' %}{{ block.settings.newsletter_border_radius }}px{% else %}0{% endif %};"
                  >
                  <button
                    type="submit"
                    class="ai-footer-newsletter-button-{{ ai_gen_id }} ai-footer-newsletter-button-icon-{{ block.settings.newsletter_button_icon }}"
                    name="commit"
                    style="
                      border-radius: {% if block.settings.newsletter_input_style == 'pill' %}999px{% elsif block.settings.newsletter_input_style == 'rounded' %}{{ block.settings.newsletter_border_radius }}px{% else %}0{% endif %};
                      {% if block.settings.newsletter_button_style == 'outline' %}
                        background: none; border: 2px solid {{ block.settings.newsletter_button_bg }}; color: {{ block.settings.newsletter_button_bg }};
                      {% elsif block.settings.newsletter_button_style == 'ghost' %}
                        background: none; border: none; color: {{ block.settings.newsletter_button_bg }};
                      {% endif %}
                    "
                  >
                    {% if block.settings.newsletter_button_icon == 'arrow' %}
                      <svg width="20" height="20" fill="none" viewBox="0 0 20 20">
                        <path d="M5 10h10m0 0l-4-4m4 4l-4 4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                      </svg>
                    {% elsif block.settings.newsletter_button_icon == 'plus' %}
                      <svg width="20" height="20" fill="none" viewBox="0 0 20 20">
                        <path d="M10 5v10m5-5H5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                      </svg>
                    {% elsif block.settings.newsletter_button_icon == 'custom'
                      and block.settings.newsletter_button_custom_svg != blank
                    %}
                      <svg width="20" height="20" fill="none" viewBox="0 0 20 20">
                        {{ block.settings.newsletter_button_custom_svg }}
                      </svg>
                    {% else %}
                      {{ block.settings.newsletter_button_text }}
                    {% endif %}
                  </button>
                </div>
              {% else %}
                <input
                  type="email"
                  name="contact[email]"
                  id="newsletter-{{ ai_gen_id }}"
                  class="ai-footer-newsletter-input-{{ ai_gen_id }}"
                  value="{{ form.email }}"
                  placeholder="{{ block.settings.newsletter_placeholder }}"
                  required
                  style="border-radius: {% if block.settings.newsletter_input_style == 'pill' %}999px{% elsif block.settings.newsletter_input_style == 'rounded' %}{{ block.settings.newsletter_border_radius }}px{% else %}0{% endif %};"
                >
                <button
                  type="submit"
                  class="ai-footer-newsletter-button-{{ ai_gen_id }} ai-footer-newsletter-button-icon-{{ block.settings.newsletter_button_icon }}"
                  name="commit"
                  style="
                    border-radius: {% if block.settings.newsletter_input_style == 'pill' %}999px{% elsif block.settings.newsletter_input_style == 'rounded' %}{{ block.settings.newsletter_border_radius }}px{% else %}0{% endif %};
                    {% if block.settings.newsletter_button_style == 'outline' %}
                      background: none; border: 2px solid {{ block.settings.newsletter_button_bg }}; color: {{ block.settings.newsletter_button_bg }};
                    {% elsif block.settings.newsletter_button_style == 'ghost' %}
                      background: none; border: none; color: {{ block.settings.newsletter_button_bg }};
                    {% endif %}
                  "
                >
                  {% if block.settings.newsletter_button_icon == 'arrow' %}
                    <svg width="20" height="20" fill="none" viewBox="0 0 20 20">
                      <path d="M5 10h10m0 0l-4-4m4 4l-4 4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                  {% elsif block.settings.newsletter_button_icon == 'plus' %}
                    <svg width="20" height="20" fill="none" viewBox="0 0 20 20">
                      <path d="M10 5v10m5-5H5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                  {% elsif block.settings.newsletter_button_icon == 'custom'
                    and block.settings.newsletter_button_custom_svg != blank
                  %}
                    <svg width="20" height="20" fill="none" viewBox="0 0 20 20">
                      {{ block.settings.newsletter_button_custom_svg }}
                    </svg>
                  {% else %}
                    {{ block.settings.newsletter_button_text }}
                  {% endif %}
                </button>
              {% endif %}
            </div>
          {% endif %}
        {% endform %}
      </div>
    {% endif %}

    <div class="ai-footer-grid-{{ ai_gen_id }}">
      <!-- Company Info Column -->
      {% if block.settings.show_company_info %}
        <div class="ai-footer-column-{{ ai_gen_id }}">
          {% if block.settings.company_display_option == 'title_only'
            or block.settings.company_display_option == 'both'
          %}
            <h3
              class="ai-footer-title-{{ ai_gen_id }} ai-footer-company-title-{{ ai_gen_id }}"
              style="background: {{ block.settings.menu_bg_color }}; border-radius: {{ block.settings.menu_border_radius }}px; padding: 8px 16px; display: inline-block;"
            >
              {{ block.settings.company_title }}
            </h3>
          {% endif %}
          {% if block.settings.company_logo != blank
            and block.settings.company_display_option == 'logo_only'
            or block.settings.company_display_option == 'both'
          %}
            <div
              class="ai-footer-company-logo-{{ ai_gen_id }}"
              style="text-align: {{ block.settings.company_logo_align }}; margin: {{ block.settings.company_logo_margin }}px 0; padding: 16px;"
            >
              <img
                src="{{ block.settings.company_logo | img_url: 'master' }}"
                alt="{{ block.settings.company_title }}"
                style="
                  max-width: {{ block.settings.company_logo_size }}px;
                  height: auto;
                  border-radius: {{ block.settings.company_logo_border_radius }}px;
                  display: inline-block;
                "
              >
            </div>
          {% endif %}
          <div
            class="ai-footer-company-info-{{ ai_gen_id }}"
            style="background: {{ block.settings.menu_bg_color }}; border-radius: {{ block.settings.menu_border_radius }}px; padding: 16px; margin-bottom: 0;"
          >
            {{ block.settings.company_info }}
            {% if block.settings.show_social_icons %}
              <div class="ai-footer-social-{{ ai_gen_id }}">
                {% if block.settings.show_facebook and block.settings.facebook_link != blank %}
                  <a
                    href="{{ block.settings.facebook_link }}"
                    class="ai-footer-social-link-{{ ai_gen_id }}"
                    aria-label="Facebook"
                  >
                    <svg class="ai-footer-social-icon-{{ ai_gen_id }}" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M12 2.04C6.5 2.04 2 6.53 2 12.06C2 17.06 5.66 21.21 10.44 21.96V14.96H7.9V12.06H10.44V9.85C10.44 7.34 11.93 5.96 14.22 5.96C15.31 5.96 16.45 6.15 16.45 6.15V8.62H15.19C13.95 8.62 13.56 9.39 13.56 10.18V12.06H16.34L15.89 14.96H13.56V21.96C18.34 21.21 22 17.06 22 12.06C22 6.53 17.5 2.04 12 2.04Z"/>
                    </svg>
                  </a>
                {% endif %}
                {% if block.settings.show_twitter and block.settings.twitter_link != blank %}
                  <a
                    href="{{ block.settings.twitter_link }}"
                    class="ai-footer-social-link-{{ ai_gen_id }}"
                    aria-label="Twitter"
                  >
                    <svg class="ai-footer-social-icon-{{ ai_gen_id }}" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M22.46 6C21.69 6.35 20.86 6.58 20 6.69C20.88 6.16 21.56 5.32 21.88 4.31C21.05 4.81 20.13 5.16 19.16 5.36C18.37 4.5 17.26 4 16 4C13.65 4 11.73 5.92 11.73 8.29C11.73 8.63 11.77 8.96 11.84 9.27C8.28 9.09 5.11 7.38 3 4.79C2.63 5.42 2.42 6.16 2.42 6.94C2.42 8.43 3.17 9.75 4.33 10.5C3.62 10.5 2.96 10.3 2.38 10V10.03C2.38 12.11 3.86 13.85 5.82 14.24C5.46 14.34 5.08 14.39 4.69 14.39C4.42 14.39 4.15 14.36 3.89 14.31C4.43 16 6 17.26 7.89 17.29C6.43 18.45 4.58 19.13 2.56 19.13C2.22 19.13 1.88 19.11 1.54 19.07C3.44 20.29 5.7 21 8.12 21C16 21 20.33 14.46 20.33 8.79C20.33 8.6 20.33 8.42 20.32 8.23C21.16 7.63 21.88 6.87 22.46 6Z"/>
                    </svg>
                  </a>
                {% endif %}
                {% if block.settings.show_instagram and block.settings.instagram_link != blank %}
                  <a
                    href="{{ block.settings.instagram_link }}"
                    class="ai-footer-social-link-{{ ai_gen_id }}"
                    aria-label="Instagram"
                  >
                    <svg class="ai-footer-social-icon-{{ ai_gen_id }}" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M12 2C14.717 2 15.056 2.01 16.122 2.06C17.187 2.11 17.912 2.277 18.55 2.525C19.21 2.779 19.766 3.123 20.322 3.678C20.8305 4.1779 21.224 4.78259 21.475 5.45C21.722 6.087 21.89 6.813 21.94 7.878C21.987 8.944 22 9.283 22 12C22 14.717 21.99 15.056 21.94 16.122C21.89 17.187 21.722 17.912 21.475 18.55C21.2247 19.2178 20.8311 19.8226 20.322 20.322C19.822 20.8303 19.2173 21.2238 18.55 21.475C17.913 21.722 17.187 21.89 16.122 21.94C15.056 21.987 14.717 22 12 22C9.283 22 8.944 21.99 7.878 21.94C6.813 21.89 6.088 21.722 5.45 21.475C4.78233 21.2245 4.17753 20.8309 3.678 20.322C3.16941 19.8222 2.77593 19.2175 2.525 18.55C2.277 17.913 2.11 17.187 2.06 16.122C2.013 15.056 2 14.717 2 12C2 9.283 2.01 8.944 2.06 7.878C2.11 6.812 2.277 6.088 2.525 5.45C2.77524 4.78218 3.1688 4.17732 3.678 3.678C4.17767 3.16923 4.78243 2.77573 5.45 2.525C6.088 2.277 6.812 2.11 7.878 2.06C8.944 2.013 9.283 2 12 2ZM12 7C10.6739 7 9.40215 7.52678 8.46447 8.46447C7.52678 9.40215 7 10.6739 7 12C7 13.3261 7.52678 14.5979 8.46447 15.5355C9.40215 16.4732 10.6739 17 12 17C13.3261 17 14.5979 16.4732 15.5355 15.5355C16.4732 14.5979 17 13.3261 17 12C17 10.6739 16.4732 9.40215 15.5355 8.46447C14.5979 7.52678 13.3261 7 12 7ZM18.5 6.75C18.5 6.41848 18.3683 6.10054 18.1339 5.86612C17.8995 5.6317 17.5815 5.5 17.25 5.5C16.9185 5.5 16.6005 5.6317 16.3661 5.86612C16.1317 6.10054 16 6.41848 16 6.75C16 7.08152 16.1317 7.39946 16.3661 7.63388C16.6005 7.8683 16.9185 8 17.25 8C17.5815 8 17.8995 7.8683 18.1339 7.63388C18.3683 7.39946 18.5 7.08152 18.5 6.75ZM12 9C12.7956 9 13.5587 9.31607 14.1213 9.87868C14.6839 10.4413 15 11.2044 15 12C15 12.7956 14.6839 13.5587 14.1213 14.1213C13.5587 14.6839 12.7956 15 12 15C11.2044 15 10.4413 14.6839 9.87868 14.1213C9.31607 13.5587 9 12.7956 9 12C9 11.2044 9.31607 10.4413 9.87868 9.87868C10.4413 9.31607 11.2044 9 12 9Z"/>
                    </svg>
                  </a>
                {% endif %}
                {% if block.settings.show_pinterest and block.settings.pinterest_link != blank %}
                  <a
                    href="{{ block.settings.pinterest_link }}"
                    class="ai-footer-social-link-{{ ai_gen_id }}"
                    aria-label="Pinterest"
                  >
                    <svg class="ai-footer-social-icon-{{ ai_gen_id }}" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M9.04 21.54C10.21 21.83 10.97 22 12 22C17.5 22 22 17.5 22 12C22 6.5 17.5 2 12 2C6.5 2 2 6.5 2 12C2 14.87 3.23 17.43 5.16 19.22C5.07 18.67 5 18.1 5 17.5C5 16.25 5.27 9.5 10.25 9.5C11.25 9.5 12.22 10.5 12.22 11.77C12.22 13.04 11.5 14.3 11.5 15.57C11.5 16.84 12.72 17.89 13.97 17.89C16.4 17.89 17.48 15.4 17.48 13.38C17.48 10.41 15.18 8.18 12.06 8.18C8.94 8.18 6.24 10.18 6.24 14.18C6.24 15.18 6.63 16.33 7.21 17C7.33 17.14 7.36 17.36 7.29 17.56L6.97 18.5C6.86 18.74 6.64 18.85 6.39 18.73C4.93 18.08 4 15.91 4 14.19C4 10.14 7.5 7.06 12.25 7.06C16.18 7.06 20 9.45 20 13.38C20 17.5 17.35 19.86 14.15 19.86C13.78 19.86 13.41 19.83 13.05 19.75L11.97 18.63C11.56 20.61 10.5 21.54 9.04 21.54Z"/>
                    </svg>
                  </a>
                {% endif %}
                {% if block.settings.show_youtube and block.settings.youtube_link != blank %}
                  <a
                    href="{{ block.settings.youtube_link }}"
                    class="ai-footer-social-link-{{ ai_gen_id }}"
                    aria-label="YouTube"
                  >
                    <svg class="ai-footer-social-icon-{{ ai_gen_id }}" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M10 15L15.19 12L10 9V15ZM21.56 7.17C21.69 7.64 21.78 8.27 21.84 9.07C21.91 9.87 21.94 10.56 21.94 11.16L22 12C22 14.19 21.84 15.8 21.56 16.83C21.31 17.73 20.73 18.31 19.83 18.56C19.36 18.69 18.5 18.78 17.18 18.84C15.88 18.91 14.69 18.94 13.59 18.94L12 19C7.81 19 5.2 18.84 4.17 18.56C3.27 18.31 2.69 17.73 2.44 16.83C2.31 16.36 2.22 15.73 2.16 14.93C2.09 14.13 2.06 13.44 2.06 12.84L2 12C2 9.81 2.16 8.2 2.44 7.17C2.69 6.27 3.27 5.69 4.17 5.44C4.64 5.31 5.5 5.22 6.82 5.16C8.12 5.09 9.31 5.06 10.41 5.06L12 5C16.19 5 18.8 5.16 19.83 5.44C20.73 5.69 21.31 6.27 21.56 7.17Z"/>
                    </svg>
                  </a>
                {% endif %}
              </div>
            {% endif %}
          </div>
        </div>
      {% endif %}

      <!-- Menu Column 1 -->
      {% if block.settings.menu1 != blank and block.settings.show_menu1 %}
        <div class="ai-footer-column-{{ ai_gen_id }}">
          <div class="ai-footer-menu-wrapper-{{ ai_gen_id }}" data-menu-id="menu1-{{ ai_gen_id }}">
            {% assign menu1_display_title = block.settings.menu1_title
              | default: linklists[block.settings.menu1].title
            %}
            <div
              class="ai-footer-menu-heading-{{ ai_gen_id }}"
              style="border-radius: {{ block.settings.menu_border_radius }}px;{% if menu1_display_title != blank %} background: {{ block.settings.menu_bg_color }};{% endif %} margin: {{ block.settings.menu_margin_y }}px {{ block.settings.menu_margin_x }}px; min-width: {% if block.settings.menu_min_width > 0 %}{{ block.settings.menu_min_width }}px{% else %}initial{% endif %}; max-width: {% if block.settings.menu_max_width > 0 %}{{ block.settings.menu_max_width }}px{% else %}initial{% endif %};"
            >
              <h3 class="ai-footer-title-{{ ai_gen_id }}{% if menu1_display_title != blank %} ai-footer-menu-title-{{ ai_gen_id }}{% endif %}">
                {{ menu1_display_title }}
              </h3>
              <button
                class="ai-footer-menu-toggle-{{ ai_gen_id }}"
                aria-expanded="false"
                aria-controls="footer-menu1-{{ ai_gen_id }}"
              >
                {% if block.settings.menu_icon == 'arrow' %}
                  <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2">
                    <polyline points="6 9 12 15 18 9"></polyline>
                  </svg>
                {% elsif block.settings.menu_icon == 'plus' %}
                  <span class="plus-icon" style="display:inline-block;">
                    <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2">
                      <line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/>
                    </svg>
                  </span>
                  <span class="dash-icon" style="display:none;">
                    <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2">
                      <line x1="5" y1="12" x2="19" y2="12"/>
                    </svg>
                  </span>
                {% elsif block.settings.menu_icon == 'custom' and block.settings.menu_icon_custom_svg != blank %}
                  <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2">
                    {{ block.settings.menu_icon_custom_svg }}
                  </svg>
                {% endif %}
              </button>
            </div>
            <ul
              id="footer-menu1-{{ ai_gen_id }}"
              class="ai-footer-nav-{{ ai_gen_id }}{% if block.settings.menu1 != blank %} active{% endif %}{% if block.settings.menu_dropdown_animation != 'none' %} {{ block.settings.menu_dropdown_animation }}{% endif %}"
            >
              {% for link in linklists[block.settings.menu1].links %}
                <li class="ai-footer-nav-item-{{ ai_gen_id }}">
                  <a href="{{ link.url }}">{{ link.title }}</a>
                </li>
              {% endfor %}
            </ul>
          </div>
        </div>
      {% endif %}

      <!-- Menu Column 2 -->
      {% if block.settings.menu2 != blank and block.settings.show_menu2 %}
        <div class="ai-footer-column-{{ ai_gen_id }}">
          <div class="ai-footer-menu-wrapper-{{ ai_gen_id }}" data-menu-id="menu2-{{ ai_gen_id }}">
            {% assign menu2_display_title = block.settings.menu2_title
              | default: linklists[block.settings.menu2].title
            %}
            <div
              class="ai-footer-menu-heading-{{ ai_gen_id }}"
              style="border-radius: {{ block.settings.menu_border_radius }}px;{% if menu2_display_title != blank %} background: {{ block.settings.menu_bg_color }};{% endif %} margin: {{ block.settings.menu_margin_y }}px {{ block.settings.menu_margin_x }}px; min-width: {% if block.settings.menu_min_width > 0 %}{{ block.settings.menu_min_width }}px{% else %}initial{% endif %}; max-width: {% if block.settings.menu_max_width > 0 %}{{ block.settings.menu_max_width }}px{% else %}initial{% endif %};"
            >
              <h3 class="ai-footer-title-{{ ai_gen_id }}{% if menu2_display_title != blank %} ai-footer-menu-title-{{ ai_gen_id }}{% endif %}">
                {{ menu2_display_title }}
              </h3>
              <button
                class="ai-footer-menu-toggle-{{ ai_gen_id }}"
                aria-expanded="false"
                aria-controls="footer-menu2-{{ ai_gen_id }}"
              >
                {% if block.settings.menu_icon == 'arrow' %}
                  <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2">
                    <polyline points="6 9 12 15 18 9"></polyline>
                  </svg>
                {% elsif block.settings.menu_icon == 'plus' %}
                  <span class="plus-icon" style="display:inline-block;">
                    <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2">
                      <line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/>
                    </svg>
                  </span>
                  <span class="dash-icon" style="display:none;">
                    <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2">
                      <line x1="5" y1="12" x2="19" y2="12"/>
                    </svg>
                  </span>
                {% elsif block.settings.menu_icon == 'custom' and block.settings.menu_icon_custom_svg != blank %}
                  <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2">
                    {{ block.settings.menu_icon_custom_svg }}
                  </svg>
                {% endif %}
              </button>
            </div>
            <ul
              id="footer-menu2-{{ ai_gen_id }}"
              class="ai-footer-nav-{{ ai_gen_id }}{% if block.settings.menu2 != blank %} active{% endif %}{% if block.settings.menu_dropdown_animation != 'none' %} {{ block.settings.menu_dropdown_animation }}{% endif %}"
            >
              {% for link in linklists[block.settings.menu2].links %}
                <li class="ai-footer-nav-item-{{ ai_gen_id }}">
                  <a href="{{ link.url }}">{{ link.title }}</a>
                </li>
              {% endfor %}
            </ul>
          </div>
        </div>
      {% endif %}

      <!-- Menu Column 3 -->
      {% if block.settings.menu3 != blank and block.settings.show_menu3 %}
        <div class="ai-footer-column-{{ ai_gen_id }}">
          <div class="ai-footer-menu-wrapper-{{ ai_gen_id }}" data-menu-id="menu3-{{ ai_gen_id }}">
            {% assign menu3_display_title = block.settings.menu3_title
              | default: linklists[block.settings.menu3].title
            %}
            <div
              class="ai-footer-menu-heading-{{ ai_gen_id }}"
              style="border-radius: {{ block.settings.menu_border_radius }}px;{% if menu3_display_title != blank %} background: {{ block.settings.menu_bg_color }};{% endif %} margin: {{ block.settings.menu_margin_y }}px {{ block.settings.menu_margin_x }}px; min-width: {% if block.settings.menu_min_width > 0 %}{{ block.settings.menu_min_width }}px{% else %}initial{% endif %}; max-width: {% if block.settings.menu_max_width > 0 %}{{ block.settings.menu_max_width }}px{% else %}initial{% endif %};"
            >
              <h3 class="ai-footer-title-{{ ai_gen_id }}{% if menu3_display_title != blank %} ai-footer-menu-title-{{ ai_gen_id }}{% endif %}">
                {{ menu3_display_title }}
              </h3>
              <button
                class="ai-footer-menu-toggle-{{ ai_gen_id }}"
                aria-expanded="false"
                aria-controls="footer-menu3-{{ ai_gen_id }}"
              >
                {% if block.settings.menu_icon == 'arrow' %}
                  <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2">
                    <polyline points="6 9 12 15 18 9"></polyline>
                  </svg>
                {% elsif block.settings.menu_icon == 'plus' %}
                  <span class="plus-icon" style="display:inline-block;">
                    <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2">
                      <line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/>
                    </svg>
                  </span>
                  <span class="dash-icon" style="display:none;">
                    <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2">
                      <line x1="5" y1="12" x2="19" y2="12"/>
                    </svg>
                  </span>
                {% elsif block.settings.menu_icon == 'custom' and block.settings.menu_icon_custom_svg != blank %}
                  <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2">
                    {{ block.settings.menu_icon_custom_svg }}
                  </svg>
                {% endif %}
              </button>
            </div>
            <ul
              id="footer-menu3-{{ ai_gen_id }}"
              class="ai-footer-nav-{{ ai_gen_id }}{% if block.settings.menu3 != blank %} active{% endif %}{% if block.settings.menu_dropdown_animation != 'none' %} {{ block.settings.menu_dropdown_animation }}{% endif %}"
            >
              {% for link in linklists[block.settings.menu3].links %}
                <li class="ai-footer-nav-item-{{ ai_gen_id }}">
                  <a href="{{ link.url }}">{{ link.title }}</a>
                </li>
              {% endfor %}
            </ul>
          </div>
        </div>
      {% endif %}

      <!-- Contact Column -->
      {% if block.settings.show_contact %}
        <div class="ai-footer-column-{{ ai_gen_id }}">
          <div class="ai-footer-menu-wrapper-{{ ai_gen_id }}" data-menu-id="contact-{{ ai_gen_id }}">
            <div
              class="ai-footer-menu-heading-{{ ai_gen_id }}"
              style="border-radius: {{ block.settings.menu_border_radius }}px;{% if block.settings.contact_title != blank %} background: {{ block.settings.menu_bg_color }};{% endif %}"
            >
              <h3 class="ai-footer-title-{{ ai_gen_id }}{% if block.settings.contact_title != blank %} ai-footer-menu-title-{{ ai_gen_id }}{% endif %}">
                {{ block.settings.contact_title }}
              </h3>
              <button
                class="ai-footer-menu-toggle-{{ ai_gen_id }}"
                aria-expanded="false"
                aria-controls="footer-contact-{{ ai_gen_id }}"
              >
                {% if block.settings.menu_icon == 'arrow' %}
                  <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2">
                    <polyline points="6 9 12 15 18 9"></polyline>
                  </svg>
                {% elsif block.settings.menu_icon == 'plus' %}
                  <span class="plus-icon" style="display:inline-block;">
                    <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2">
                      <line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/>
                    </svg>
                  </span>
                  <span class="dash-icon" style="display:none;">
                    <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2">
                      <line x1="5" y1="12" x2="19" y2="12"/>
                    </svg>
                  </span>
                {% elsif block.settings.menu_icon == 'custom' and block.settings.menu_icon_custom_svg != blank %}
                  <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2">
                    {{ block.settings.menu_icon_custom_svg }}
                  </svg>
                {% endif %}
              </button>
            </div>
            <div
              id="footer-contact-{{ ai_gen_id }}"
              class="ai-footer-nav-{{ ai_gen_id }} active{% if block.settings.menu_dropdown_animation != 'none' %} {{ block.settings.menu_dropdown_animation }}{% endif %}"
            >
              <div
                class="ai-footer-company-info-{{ ai_gen_id }}"
                style="background: {{ block.settings.menu_bg_color }}; border-radius: {{ block.settings.menu_border_radius }}px; padding: 16px; margin-bottom: 0;"
              >
                {{ block.settings.contact_info }}
              </div>
            </div>
          </div>
        </div>
      {% endif %}
    </div>

    <div class="ai-footer-bottom-{{ ai_gen_id }}">
      <div class="ai-footer-bottom-group-{{ ai_gen_id }}">
        <div class="ai-footer-copyright-{{ ai_gen_id }}">
          {{ block.settings.copyright_text }}
        </div>

        {% if block.settings.show_payment_icons %}
          <div class="ai-footer-payment-{{ ai_gen_id }}">
            {% for type in shop.enabled_payment_types %}
              {{ type | payment_type_svg_tag: class: 'ai-footer-payment-icon' }}
            {% endfor %}
          </div>
        {% endif %}
      </div>
    </div>
  </div>
</footer>

<script>
  (function() {
    const menuToggles = document.querySelectorAll('.ai-footer-menu-toggle-{{ ai_gen_id }}');

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

    const menuHeadings = document.querySelectorAll('.ai-footer-menu-heading-{{ ai_gen_id }}');

    menuHeadings.forEach(heading => {
      heading.addEventListener('click', function(event) {
        // Only toggle if the click is on the heading, icon, or button (not on a link inside the menu)
        const wrapper = this.closest('.ai-footer-menu-wrapper-{{ ai_gen_id }}');
        const toggle = wrapper.querySelector('.ai-footer-menu-toggle-{{ ai_gen_id }}');
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
        document.querySelectorAll('.ai-footer-nav-{{ ai_gen_id }}').forEach(menu => {
          menu.classList.add('active');
        });

        document.querySelectorAll('.ai-footer-menu-toggle-{{ ai_gen_id }}').forEach(toggle => {
          toggle.setAttribute('aria-expanded', 'true');
        });
      }
      // Set correct plus/dash icon on resize
      document.querySelectorAll('.ai-footer-menu-toggle-{{ ai_gen_id }}').forEach(toggle => {
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
      document.querySelectorAll('.ai-footer-menu-toggle-{{ ai_gen_id }}').forEach(toggle => {
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
      document.querySelectorAll('.ai-footer-menu-wrapper-{{ ai_gen_id }}').forEach(wrapper => {
        const toggle = wrapper.querySelector('.ai-footer-menu-toggle-{{ ai_gen_id }}');
        const menu = wrapper.querySelector('.ai-footer-nav-{{ ai_gen_id }}');
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
</script>

{% schema %}
{
  "name": "Enhanced Footer",
  "tag": null,
  "class": "section",
  "settings": [
    {
      "type": "header",
      "content": "Layout"
    },
    {
      "type": "range",
      "id": "container_width",
      "min": 800,
      "max": 1600,
      "step": 50,
      "unit": "px",
      "label": "Container width",
      "default": 1200
    },
    {
      "type": "select",
      "id": "columns",
      "label": "Columns",
      "options": [
        {
          "value": "2",
          "label": "2"
        },
        {
          "value": "3",
          "label": "3"
        },
        {
          "value": "4",
          "label": "4"
        }
      ],
      "default": "4"
    },
    {
      "type": "select",
      "id": "columns_mobile",
      "label": "Columns on mobile",
      "options": [
        {
          "value": "1",
          "label": "1"
        },
        {
          "value": "2",
          "label": "2"
        }
      ],
      "default": "1"
    },
    {
      "type": "range",
      "id": "column_spacing",
      "min": 10,
      "max": 100,
      "step": 5,
      "unit": "px",
      "label": "Column spacing",
      "default": 40
    },
    {
      "type": "range",
      "id": "section_spacing",
      "min": 10,
      "max": 100,
      "step": 5,
      "unit": "px",
      "label": "Section spacing",
      "default": 40
    },
    {
      "type": "range",
      "id": "padding_top",
      "min": 20,
      "max": 120,
      "step": 10,
      "unit": "px",
      "label": "Padding top",
      "default": 60
    },
    {
      "type": "range",
      "id": "padding_bottom",
      "min": 20,
      "max": 120,
      "step": 10,
      "unit": "px",
      "label": "Padding bottom",
      "default": 60
    },
    {
      "type": "header",
      "content": "Colors"
    },
    {
      "type": "color",
      "id": "background_color",
      "label": "Background color",
      "default": "#f7f7f7"
    },
    {
      "type": "color",
      "id": "text_color",
      "label": "Text color",
      "default": "#333333"
    },
    {
      "type": "color",
      "id": "heading_color",
      "label": "Heading color",
      "default": "#000000"
    },
    {
      "type": "color",
      "id": "link_hover_color",
      "label": "Link hover color",
      "default": "#000f9f"
    },
    {
      "type": "color",
      "id": "border_color",
      "label": "Border color",
      "default": "#e5e5e5"
    },
    {
      "type": "color",
      "id": "social_bg_color",
      "label": "Social icon background",
      "default": "#eeeeee"
    },
    {
      "type": "color",
      "id": "social_icon_color",
      "label": "Social icon color",
      "default": "#333333"
    },
    {
      "type": "color",
      "id": "social_hover_bg_color",
      "label": "Social hover background",
      "default": "#000000"
    },
    {
      "type": "color",
      "id": "social_hover_icon_color",
      "label": "Social hover icon color",
      "default": "#ffffff"
    },
    {
      "type": "header",
      "content": "Typography"
    },
    {
      "type": "range",
      "id": "heading_size",
      "min": 14,
      "max": 28,
      "step": 1,
      "unit": "px",
      "label": "Heading size",
      "default": 16
    },
    {
      "type": "range",
      "id": "text_size",
      "min": 12,
      "max": 18,
      "step": 1,
      "unit": "px",
      "label": "Text size",
      "default": 14
    },
    {
      "type": "range",
      "id": "copyright_size",
      "min": 10,
      "max": 16,
      "step": 1,
      "unit": "px",
      "label": "Copyright text size",
      "default": 12
    },
    {
      "type": "header",
      "content": "Newsletter"
    },
    {
      "type": "checkbox",
      "id": "show_newsletter",
      "label": "Show newsletter signup",
      "default": true
    },
    {
      "type": "text",
      "id": "newsletter_title",
      "label": "Newsletter title",
      "default": "Subscribe to our newsletter"
    },
    {
      "type": "select",
      "id": "newsletter_title_transform",
      "label": "Newsletter title text transform",
      "options": [
        { "value": "none", "label": "None" },
        { "value": "uppercase", "label": "Uppercase" },
        { "value": "lowercase", "label": "Lowercase" },
        { "value": "capitalize", "label": "Capitalize" }
      ],
      "default": "none"
    },
    {
      "type": "select",
      "id": "newsletter_title_weight",
      "label": "Newsletter title font weight",
      "options": [
        { "value": "400", "label": "Normal" },
        { "value": "500", "label": "Medium" },
        { "value": "600", "label": "Semi-bold" },
        { "value": "700", "label": "Bold" }
      ],
      "default": "500"
    },
    {
      "type": "range",
      "id": "newsletter_title_size",
      "label": "Newsletter title font size",
      "min": 12,
      "max": 32,
      "step": 1,
      "unit": "px",
      "default": 18
    },
    {
      "type": "text",
      "id": "newsletter_text",
      "label": "Newsletter text",
      "default": "Sign up for exclusive offers, original stories, events and more."
    },
    {
      "type": "text",
      "id": "newsletter_placeholder",
      "label": "Email placeholder text",
      "default": "Your email address"
    },
    {
      "type": "text",
      "id": "newsletter_button_text",
      "label": "Button text",
      "default": "Subscribe"
    },
    {
      "type": "select",
      "id": "newsletter_layout",
      "label": "Newsletter layout",
      "options": [
        { "value": "row", "label": "Horizontal" },
        { "value": "column", "label": "Vertical" },
        { "value": "boxed", "label": "Boxed/Card" },
        { "value": "centered", "label": "Centered" },
        { "value": "inline", "label": "Inline with text" },
        { "value": "split", "label": "Split (image/text)" }
      ],
      "default": "row"
    },
    {
      "type": "checkbox",
      "id": "newsletter_show_name",
      "label": "Show name field",
      "default": false
    },
    {
      "type": "select",
      "id": "newsletter_align",
      "label": "Newsletter alignment",
      "options": [
        { "value": "left", "label": "Left" },
        { "value": "center", "label": "Center" },
        { "value": "right", "label": "Right" }
      ],
      "default": "left"
    },
    {
      "type": "image_picker",
      "id": "newsletter_bg_image",
      "label": "Newsletter background image"
    },
    {
      "type": "text",
      "id": "newsletter_success_message",
      "label": "Custom success message",
      "default": "Thank you for subscribing to our newsletter!"
    },
    {
      "type": "text",
      "id": "newsletter_error_message",
      "label": "Custom error message",
      "default": "There was an error. Please try again."
    },
    {
      "type": "select",
      "id": "newsletter_input_style",
      "label": "Input style",
      "options": [
        { "value": "rounded", "label": "Rounded" },
        { "value": "square", "label": "Square" },
        { "value": "pill", "label": "Pill" }
      ],
      "default": "rounded"
    },
    {
      "type": "select",
      "id": "newsletter_button_style",
      "label": "Button style",
      "options": [
        { "value": "solid", "label": "Solid" },
        { "value": "outline", "label": "Outline" },
        { "value": "ghost", "label": "Ghost" }
      ],
      "default": "solid"
    },
    {
      "type": "select",
      "id": "newsletter_button_icon",
      "label": "Button icon",
      "options": [
        { "value": "none", "label": "None" },
        { "value": "arrow", "label": "Arrow" },
        { "value": "plus", "label": "Plus" },
        { "value": "custom", "label": "Custom SVG" }
      ],
      "default": "none"
    },
    {
      "type": "text",
      "id": "newsletter_button_custom_svg",
      "label": "Custom SVG (inline, no <svg> tag)",
      "default": "<path d='M5 10h10m0 0l-4-4m4 4l-4 4' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/>"
    },
    {
      "type": "checkbox",
      "id": "newsletter_button_inside_input",
      "label": "Show button inside text field",
      "default": false
    },
    {
      "type": "range",
      "id": "newsletter_section_padding",
      "min": 0,
      "max": 60,
      "step": 2,
      "unit": "px",
      "label": "Newsletter section padding",
      "default": 20
    },
    {
      "type": "range",
      "id": "newsletter_section_margin",
      "min": 0,
      "max": 60,
      "step": 2,
      "unit": "px",
      "label": "Newsletter section margin",
      "default": 0
    },
    {
      "type": "header",
      "content": "Company Information"
    },
    {
      "type": "checkbox",
      "id": "show_company_info",
      "label": "Show company info column",
      "default": true
    },
    {
      "type": "select",
      "id": "company_display_option",
      "label": "Company header display",
      "options": [
        { "value": "title_only", "label": "Title only" },
        { "value": "logo_only", "label": "Logo only" },
        { "value": "both", "label": "Both title and logo" }
      ],
      "default": "title_only"
    },
    {
      "type": "text",
      "id": "company_title",
      "label": "Company title",
      "default": "About Us"
    },
    {
      "type": "image_picker",
      "id": "company_logo",
      "label": "Company logo"
    },
    {
      "type": "range",
      "id": "company_logo_size",
      "label": "Logo size",
      "min": 50,
      "max": 300,
      "step": 10,
      "unit": "px",
      "default": 150
    },
    {
      "type": "select",
      "id": "company_logo_align",
      "label": "Logo alignment",
      "options": [
        { "value": "left", "label": "Left" },
        { "value": "center", "label": "Center" },
        { "value": "right", "label": "Right" }
      ],
      "default": "left"
    },
    {
      "type": "range",
      "id": "company_logo_margin",
      "label": "Logo margin",
      "min": 0,
      "max": 40,
      "step": 2,
      "unit": "px",
      "default": 20
    },
    {
      "type": "range",
      "id": "company_logo_border_radius",
      "label": "Logo border radius",
      "min": 0,
      "max": 50,
      "step": 1,
      "unit": "px",
      "default": 0
    },
    {
      "type": "select",
      "id": "company_title_transform",
      "label": "Company title text transform",
      "options": [
        { "value": "none", "label": "None" },
        { "value": "uppercase", "label": "Uppercase" },
        { "value": "lowercase", "label": "Lowercase" },
        { "value": "capitalize", "label": "Capitalize" }
      ],
      "default": "none"
    },
    {
      "type": "select",
      "id": "company_title_weight",
      "label": "Company title font weight",
      "options": [
        { "value": "400", "label": "Normal" },
        { "value": "500", "label": "Medium" },
        { "value": "600", "label": "Semi-bold" },
        { "value": "700", "label": "Bold" }
      ],
      "default": "500"
    },
    {
      "type": "range",
      "id": "company_title_size",
      "label": "Company title font size",
      "min": 12,
      "max": 32,
      "step": 1,
      "unit": "px",
      "default": 18
    },
    {
      "type": "richtext",
      "id": "company_info",
      "label": "Company information",
      "default": "<p>We're dedicated to providing quality products and exceptional service to our customers. Our mission is to make your shopping experience enjoyable and hassle-free.</p>"
    },
    {
      "type": "header",
      "content": "Footer Menus"
    },
    {
      "type": "select",
      "id": "menu_icon",
      "label": "Menu heading icon",
      "options": [
        { "value": "arrow", "label": "Arrow" },
        { "value": "plus", "label": "Plus" },
        { "value": "custom", "label": "Custom SVG" },
        { "value": "none", "label": "None" }
      ],
      "default": "arrow"
    },
    {
      "type": "text",
      "id": "menu_icon_custom_svg",
      "label": "Custom SVG for menu icon (inline, no <svg> tag)",
      "default": "<path d='M5 10h10m0 0l-4-4m4 4l-4 4' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/>"
    },
    {
      "type": "select",
      "id": "menu_dropdown_animation",
      "label": "Menu dropdown animation",
      "options": [
        { "value": "none", "label": "None" },
        { "value": "fade", "label": "Fade" },
        { "value": "slide", "label": "Slide" }
      ],
      "default": "none"
    },
    {
      "type": "range",
      "id": "menu_padding_y",
      "label": "Menu vertical padding",
      "min": 0,
      "max": 40,
      "step": 0.5,
      "unit": "px",
      "default": 4
    },
    {
      "type": "range",
      "id": "menu_padding_x",
      "label": "Menu horizontal padding",
      "min": 0,
      "max": 40,
      "step": 0.5,
      "unit": "px",
      "default": 0
    },
    {
      "type": "range",
      "id": "menu_border_radius",
      "label": "Menu border radius",
      "min": 0,
      "max": 32,
      "step": 1,
      "unit": "px",
      "default": 0
    },
    {
      "type": "color",
      "id": "menu_bg_color",
      "label": "Menu background color",
      "default": "#ffffff"
    },
    {
      "type": "range",
      "id": "menu_margin_y",
      "label": "Menu vertical margin",
      "min": 0,
      "max": 40,
      "step": 1,
      "unit": "px",
      "default": 0
    },
    {
      "type": "range",
      "id": "menu_margin_x",
      "label": "Menu horizontal margin",
      "min": 0,
      "max": 40,
      "step": 1,
      "unit": "px",
      "default": 0
    },
    {
      "type": "range",
      "id": "menu_min_width",
      "label": "Menu min width",
      "min": 0,
      "max": 400,
      "step": 10,
      "unit": "px",
      "default": 0
    },
    {
      "type": "range",
      "id": "menu_max_width",
      "label": "Menu max width",
      "min": 0,
      "max": 800,
      "step": 10,
      "unit": "px",
      "default": 0
    },
    {
      "type": "link_list",
      "id": "menu1",
      "label": "Menu 1",
      "default": "footer"
    },
    {
      "type": "checkbox",
      "id": "show_menu1",
      "label": "Show Menu 1 column",
      "default": true
    },
    {
      "type": "text",
      "id": "menu1_title",
      "label": "Menu 1 custom title (optional)",
      "default": "Menu 1"
    },
    {
      "type": "link_list",
      "id": "menu2",
      "label": "Menu 2"
    },
    {
      "type": "checkbox",
      "id": "show_menu2",
      "label": "Show Menu 2 column",
      "default": true
    },
    {
      "type": "text",
      "id": "menu2_title",
      "label": "Menu 2 custom title (optional)",
      "default": "Menu 2"
    },
    {
      "type": "link_list",
      "id": "menu3",
      "label": "Menu 3"
    },
    {
      "type": "checkbox",
      "id": "show_menu3",
      "label": "Show Menu 3 column",
      "default": true
    },
    {
      "type": "text",
      "id": "menu3_title",
      "label": "Menu 3 custom title (optional)",
      "default": "Menu 3"
    },
    {
      "type": "select",
      "id": "menu_title_transform",
      "label": "Menu title text transform",
      "options": [
        { "value": "none", "label": "None" },
        { "value": "uppercase", "label": "Uppercase" },
        { "value": "lowercase", "label": "Lowercase" },
        { "value": "capitalize", "label": "Capitalize" }
      ],
      "default": "none"
    },
    {
      "type": "select",
      "id": "menu_title_weight",
      "label": "Menu title font weight",
      "options": [
        { "value": "400", "label": "Normal" },
        { "value": "500", "label": "Medium" },
        { "value": "600", "label": "Semi-bold" },
        { "value": "700", "label": "Bold" }
      ],
      "default": "500"
    },
    {
      "type": "range",
      "id": "menu_title_size",
      "label": "Menu title font size",
      "min": 12,
      "max": 32,
      "step": 1,
      "unit": "px",
      "default": 18
    },
    {
      "type": "header",
      "content": "Contact Information"
    },
    {
      "type": "checkbox",
      "id": "show_contact",
      "label": "Show contact column",
      "default": true
    },
    {
      "type": "text",
      "id": "contact_title",
      "label": "Title",
      "default": "Contact Us"
    },
    {
      "type": "richtext",
      "id": "contact_info",
      "label": "Contact information",
      "default": "<p>123 Main Street<br>New York, NY 10001<br>United States<br><br>Email: hello@example.com<br>Phone: (123) 456-7890</p>"
    },
    {
      "type": "header",
      "content": "Social Media"
    },
    {
      "type": "checkbox",
      "id": "show_social_icons",
      "label": "Show social icons in bottom bar",
      "default": true
    },
    {
      "type": "range",
      "id": "social_icon_size",
      "label": "Social icon container size",
      "min": 24,
      "max": 60,
      "step": 2,
      "unit": "px",
      "default": 36
    },
    {
      "type": "range",
      "id": "social_icon_inner_size",
      "label": "Social icon inner size",
      "min": 12,
      "max": 32,
      "step": 1,
      "unit": "px",
      "default": 18
    },
    {
      "type": "range",
      "id": "social_icon_spacing",
      "label": "Space between icons",
      "min": 5,
      "max": 30,
      "step": 1,
      "unit": "px",
      "default": 15
    },
    {
      "type": "range",
      "id": "social_icon_border_radius",
      "label": "Icon border radius",
      "min": 0,
      "max": 50,
      "step": 1,
      "unit": "px",
      "default": 18
    },
    {
      "type": "range",
      "id": "social_hover_transition",
      "label": "Hover transition speed",
      "min": 0.1,
      "max": 1.0,
      "step": 0.1,
      "unit": "s",
      "default": 0.2
    },
    {
      "type": "range",
      "id": "social_hover_scale",
      "label": "Hover scale effect",
      "min": 1.0,
      "max": 1.5,
      "step": 0.1,
      "default": 1.0
    },
    {
      "type": "range",
      "id": "social_hover_rotate",
      "label": "Hover rotation (degrees)",
      "min": 0,
      "max": 360,
      "step": 5,
      "default": 0
    },
    {
      "type": "checkbox",
      "id": "show_facebook",
      "label": "Show Facebook icon",
      "default": true
    },
    {
      "type": "url",
      "id": "facebook_link",
      "label": "Facebook"
    },
    {
      "type": "checkbox",
      "id": "show_twitter",
      "label": "Show Twitter icon",
      "default": true
    },
    {
      "type": "url",
      "id": "twitter_link",
      "label": "Twitter"
    },
    {
      "type": "checkbox",
      "id": "show_instagram",
      "label": "Show Instagram icon",
      "default": true
    },
    {
      "type": "url",
      "id": "instagram_link",
      "label": "Instagram"
    },
    {
      "type": "checkbox",
      "id": "show_pinterest",
      "label": "Show Pinterest icon",
      "default": true
    },
    {
      "type": "url",
      "id": "pinterest_link",
      "label": "Pinterest"
    },
    {
      "type": "checkbox",
      "id": "show_youtube",
      "label": "Show YouTube icon",
      "default": true
    },
    {
      "type": "url",
      "id": "youtube_link",
      "label": "YouTube"
    },
    {
      "type": "header",
      "content": "Bottom Bar"
    },
    {
      "type": "richtext",
      "id": "copyright_text",
      "label": "Copyright text",
      "default": "<p>© 2023 Your Store. All rights reserved.</p>"
    },
    {
      "type": "checkbox",
      "id": "show_payment_icons",
      "label": "Show payment icons",
      "default": true
    },
    {
      "type": "range",
      "id": "payment_icon_size",
      "min": 20,
      "max": 60,
      "step": 2,
      "unit": "px",
      "label": "Payment icon size",
      "default": 30
    },
    {
      "type": "select",
      "id": "footer_bottom_alignment",
      "label": "Footer bottom alignment (copyright & payment icons)",
      "options": [
        { "value": "left", "label": "Left" },
        { "value": "center", "label": "Center" },
        { "value": "right", "label": "Right" },
        { "value": "space-between", "label": "Space between" },
        { "value": "space-around", "label": "Space around" }
      ],
      "default": "left"
    },
    {
      "type": "header",
      "content": "Advanced Column Layout (Desktop)"
    },
    {
      "type": "select",
      "id": "column_width_mode",
      "label": "Column width mode",
      "options": [
        { "value": "even", "label": "Even (default)" },
        { "value": "custom", "label": "Custom (set per column)" },
        { "value": "auto", "label": "Auto (content-based)" },
        { "value": "fluid", "label": "Fluid (auto-fit/minmax)" }
      ],
      "default": "even"
    },
    {
      "type": "text",
      "id": "column1_width",
      "label": "Column 1 width (e.g. 1fr, 200px, 20%)",
      "default": "1fr"
    },
    {
      "type": "text",
      "id": "column2_width",
      "label": "Column 2 width",
      "default": "1fr"
    },
    {
      "type": "text",
      "id": "column3_width",
      "label": "Column 3 width",
      "default": "1fr"
    },
    {
      "type": "text",
      "id": "column4_width",
      "label": "Column 4 width",
      "default": "1fr"
    },
    {
      "type": "select",
      "id": "column_horizontal_align",
      "label": "Column horizontal alignment",
      "options": [
        { "value": "start", "label": "Left" },
        { "value": "center", "label": "Center" },
        { "value": "end", "label": "Right" },
        { "value": "space-between", "label": "Space between" },
        { "value": "space-around", "label": "Space around" }
      ],
      "default": "start"
    },
    {
      "type": "select",
      "id": "column_vertical_align",
      "label": "Column vertical alignment",
      "options": [
        { "value": "start", "label": "Top" },
        { "value": "center", "label": "Center" },
        { "value": "end", "label": "Bottom" },
        { "value": "stretch", "label": "Stretch" }
      ],
      "default": "start"
    },
    {
      "type": "range",
      "id": "column1_padding",
      "label": "Column 1 padding (px)",
      "min": 0,
      "max": 60,
      "step": 2,
      "default": 0
    },
    {
      "type": "range",
      "id": "column2_padding",
      "label": "Column 2 padding (px)",
      "min": 0,
      "max": 60,
      "step": 2,
      "default": 0
    },
    {
      "type": "range",
      "id": "column3_padding",
      "label": "Column 3 padding (px)",
      "min": 0,
      "max": 60,
      "step": 2,
      "default": 0
    },
    {
      "type": "range",
      "id": "column4_padding",
      "label": "Column 4 padding (px)",
      "min": 0,
      "max": 60,
      "step": 2,
      "default": 0
    }
  ],
  "presets": [
    {
      "name": "Enhanced Footer"
    }
  ]
}
{% endschema %}
