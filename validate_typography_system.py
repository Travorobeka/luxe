#!/usr/bin/env python3
"""
Typography System Validation Script

This script validates the implementation of the three-tier typography system
in the Luxe Shopify theme. It checks for:
- Proper CSS variable implementation
- Correct heading class usage
- Settings schema validation
- File consistency
- Performance implications
"""

import os
import re
import json
import glob
from collections import defaultdict, Counter

class TypographyValidator:
    def __init__(self):
        self.results = {
            'css_variables': [],
            'heading_usage': [],
            'settings_validation': [],
            'file_consistency': [],
            'performance': [],
            'accessibility': [],
            'summary': {}
        }
        
        self.expected_css_vars = [
            '--font-main-heading-desktop',
            '--font-sub-heading-desktop', 
            '--font-body-text-desktop',
            '--font-weight-main-heading',
            '--font-weight-sub-heading',
            '--font-weight-body-text',
            '--line-height-main-heading-ratio',
            '--line-height-sub-heading-ratio',
            '--line-height-body-text-ratio'
        ]
        
        self.expected_classes = [
            'main-heading',
            'sub-heading', 
            'body-text'
        ]
        
        self.disruption_levels = ['gentle', 'moderate', 'aggressive', 'nuclear']
    
    def validate_css_variables(self):
        """Validate CSS variable implementation in style-tags.liquid"""
        print("🔍 Validating CSS variables...")
        
        try:
            with open('snippets/style-tags.liquid', 'r', encoding='utf-8') as f:
                content = f.read()
            
            found_vars = []
            missing_vars = []
            
            for var in self.expected_css_vars:
                if var in content:
                    found_vars.append(var)
                    self.results['css_variables'].append({
                        'type': 'success',
                        'message': f"Found CSS variable: {var}"
                    })
                else:
                    missing_vars.append(var)
                    self.results['css_variables'].append({
                        'type': 'error',
                        'message': f"Missing CSS variable: {var}"
                    })
            
            # Check for disruptive settings variables
            disruptive_vars = [
                '--enable-typography-disruption',
                '--disruption-level',
                '--override-utility-classes'
            ]
            
            for var in disruptive_vars:
                if var in content:
                    self.results['css_variables'].append({
                        'type': 'success',
                        'message': f"Found disruptive variable: {var}"
                    })
                else:
                    self.results['css_variables'].append({
                        'type': 'warning',
                        'message': f"Missing disruptive variable: {var}"
                    })
            
            return len(missing_vars) == 0
            
        except FileNotFoundError:
            self.results['css_variables'].append({
                'type': 'error',
                'message': "style-tags.liquid file not found"
            })
            return False
    
    def validate_heading_usage(self):
        """Validate heading element usage across all files"""
        print("🔍 Validating heading usage...")
        
        file_patterns = [
            'sections/*.liquid',
            'snippets/*.liquid', 
            'templates/*.liquid',
            'templates/*.json'
        ]
        
        heading_stats = {
            'total_headings': 0,
            'with_new_classes': 0,
            'without_new_classes': 0,
            'files_processed': 0
        }
        
        class_usage = Counter()
        legacy_usage = Counter()
        
        for pattern in file_patterns:
            for file_path in glob.glob(pattern):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    heading_stats['files_processed'] += 1
                    
                    # Find all heading elements
                    heading_pattern = r'<h[1-6][^>]*>'
                    headings = re.findall(heading_pattern, content, re.IGNORECASE)
                    
                    for heading in headings:
                        heading_stats['total_headings'] += 1
                        
                        # Check for new typography classes
                        has_new_class = False
                        for cls in self.expected_classes:
                            if cls in heading:
                                class_usage[cls] += 1
                                has_new_class = True
                        
                        if has_new_class:
                            heading_stats['with_new_classes'] += 1
                        else:
                            heading_stats['without_new_classes'] += 1
                            
                            # Track legacy usage
                            tag_match = re.search(r'<(h[1-6])', heading, re.IGNORECASE)
                            if tag_match:
                                legacy_usage[tag_match.group(1).lower()] += 1
                
                except Exception as e:
                    self.results['heading_usage'].append({
                        'type': 'error',
                        'message': f"Error processing {file_path}: {e}"
                    })
        
        # Report results
        self.results['heading_usage'].append({
            'type': 'info',
            'message': f"Processed {heading_stats['files_processed']} files"
        })
        
        self.results['heading_usage'].append({
            'type': 'info',
            'message': f"Found {heading_stats['total_headings']} total headings"
        })
        
        self.results['heading_usage'].append({
            'type': 'success' if heading_stats['with_new_classes'] > 0 else 'warning',
            'message': f"{heading_stats['with_new_classes']} headings with new classes"
        })
        
        if heading_stats['without_new_classes'] > 0:
            self.results['heading_usage'].append({
                'type': 'warning',
                'message': f"{heading_stats['without_new_classes']} headings without new classes"
            })
        
        # Report class usage
        for cls, count in class_usage.items():
            self.results['heading_usage'].append({
                'type': 'success',
                'message': f"Class '{cls}' used {count} times"
            })
        
        # Report legacy usage
        for tag, count in legacy_usage.items():
            self.results['heading_usage'].append({
                'type': 'warning',
                'message': f"Legacy {tag} without new class: {count} times"
            })
        
        return heading_stats['without_new_classes'] < heading_stats['with_new_classes']
    
    def validate_settings_schema(self):
        """Validate settings schema implementation"""
        print("🔍 Validating settings schema...")
        
        try:
            with open('config/settings_schema.json', 'r', encoding='utf-8') as f:
                schema = json.load(f)
            
            # Find typography section
            typography_section = None
            for section in schema:
                if section.get('name') == 'Typography':
                    typography_section = section
                    break
            
            if not typography_section:
                self.results['settings_validation'].append({
                    'type': 'error',
                    'message': "Typography section not found in settings schema"
                })
                return False
            
            # Check for three-tier settings
            three_tier_settings = [
                'main_heading_font_size',
                'sub_heading_font_size', 
                'body_font_size',
                'main_heading_font_weight',
                'sub_heading_font_weight',
                'body_font_weight'
            ]
            
            found_settings = []
            missing_settings = []
            
            settings_list = typography_section.get('settings', [])
            setting_ids = [s.get('id') for s in settings_list if 'id' in s]
            
            for setting in three_tier_settings:
                if setting in setting_ids:
                    found_settings.append(setting)
                    self.results['settings_validation'].append({
                        'type': 'success',
                        'message': f"Found setting: {setting}"
                    })
                else:
                    missing_settings.append(setting)
                    self.results['settings_validation'].append({
                        'type': 'error',
                        'message': f"Missing setting: {setting}"
                    })
            
            # Check for disruptive settings
            disruptive_settings = [
                'enable_typography_disruption',
                'disruption_level',
                'override_utility_classes'
            ]
            
            for setting in disruptive_settings:
                if setting in setting_ids:
                    self.results['settings_validation'].append({
                        'type': 'success',
                        'message': f"Found disruptive setting: {setting}"
                    })
                else:
                    self.results['settings_validation'].append({
                        'type': 'warning',
                        'message': f"Missing disruptive setting: {setting}"
                    })
            
            return len(missing_settings) == 0
            
        except FileNotFoundError:
            self.results['settings_validation'].append({
                'type': 'error',
                'message': "settings_schema.json file not found"
            })
            return False
        except json.JSONDecodeError as e:
            self.results['settings_validation'].append({
                'type': 'error',
                'message': f"Invalid JSON in settings_schema.json: {e}"
            })
            return False
    
    def validate_file_consistency(self):
        """Validate file consistency and required files"""
        print("🔍 Validating file consistency...")
        
        required_files = [
            'assets/typography-utilities.css',
            'assets/typography-enhanced-utilities.css',
            'snippets/style-tags.liquid',
            'snippets/typography-test-suite.liquid',
            'config/settings_schema.json'
        ]
        
        all_files_exist = True
        
        for file_path in required_files:
            if os.path.exists(file_path):
                self.results['file_consistency'].append({
                    'type': 'success',
                    'message': f"Found required file: {file_path}"
                })
            else:
                all_files_exist = False
                self.results['file_consistency'].append({
                    'type': 'error',
                    'message': f"Missing required file: {file_path}"
                })
        
        # Check if CSS files are referenced in theme.liquid
        try:
            with open('layout/theme.liquid', 'r', encoding='utf-8') as f:
                theme_content = f.read()
            
            css_files = [
                'typography-utilities.css',
                'typography-enhanced-utilities.css'
            ]
            
            for css_file in css_files:
                if css_file in theme_content:
                    self.results['file_consistency'].append({
                        'type': 'success',
                        'message': f"CSS file referenced in theme.liquid: {css_file}"
                    })
                else:
                    self.results['file_consistency'].append({
                        'type': 'warning',
                        'message': f"CSS file not referenced in theme.liquid: {css_file}"
                    })
        
        except FileNotFoundError:
            self.results['file_consistency'].append({
                'type': 'error',
                'message': "theme.liquid file not found"
            })
            all_files_exist = False
        
        return all_files_exist
    
    def validate_performance(self):
        """Validate performance implications"""
        print("🔍 Validating performance...")
        
        # Check CSS file sizes
        css_files = [
            'assets/typography-utilities.css',
            'assets/typography-enhanced-utilities.css'
        ]
        
        total_size = 0
        
        for css_file in css_files:
            if os.path.exists(css_file):
                size = os.path.getsize(css_file)
                total_size += size
                
                if size > 50000:  # 50KB
                    self.results['performance'].append({
                        'type': 'warning',
                        'message': f"{css_file} is large: {size/1024:.1f}KB"
                    })
                else:
                    self.results['performance'].append({
                        'type': 'success',
                        'message': f"{css_file} size OK: {size/1024:.1f}KB"
                    })
        
        self.results['performance'].append({
            'type': 'info',
            'message': f"Total typography CSS size: {total_size/1024:.1f}KB"
        })
        
        # Check for potential CSS conflicts
        try:
            with open('assets/typography-utilities.css', 'r', encoding='utf-8') as f:
                css_content = f.read()
            
            important_count = css_content.count('!important')
            
            if important_count > 50:
                self.results['performance'].append({
                    'type': 'warning',
                    'message': f"High !important usage: {important_count} instances"
                })
            else:
                self.results['performance'].append({
                    'type': 'success',
                    'message': f"Reasonable !important usage: {important_count} instances"
                })
        
        except FileNotFoundError:
            pass
        
        return total_size < 100000  # 100KB total
    
    def validate_accessibility(self):
        """Validate accessibility considerations"""
        print("🔍 Validating accessibility...")
        
        # Check for accessibility settings in schema
        try:
            with open('config/settings_schema.json', 'r', encoding='utf-8') as f:
                schema = json.load(f)
            
            accessibility_keywords = ['contrast', 'accessibility', 'a11y', 'wcag']
            accessibility_settings = 0
            
            schema_str = json.dumps(schema).lower()
            
            for keyword in accessibility_keywords:
                if keyword in schema_str:
                    accessibility_settings += 1
            
            if accessibility_settings > 0:
                self.results['accessibility'].append({
                    'type': 'success',
                    'message': f"Found {accessibility_settings} accessibility-related settings"
                })
            else:
                self.results['accessibility'].append({
                    'type': 'warning',
                    'message': "No accessibility-related settings found"
                })
        
        except FileNotFoundError:
            pass
        
        # Check for proper semantic heading structure in templates
        heading_hierarchy_issues = 0
        
        for file_path in glob.glob('sections/*.liquid'):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Simple check for heading hierarchy
                headings = re.findall(r'<h([1-6])', content, re.IGNORECASE)
                if headings:
                    levels = [int(h) for h in headings]
                    for i in range(1, len(levels)):
                        if levels[i] > levels[i-1] + 1:
                            heading_hierarchy_issues += 1
                            break
            
            except Exception:
                pass
        
        if heading_hierarchy_issues == 0:
            self.results['accessibility'].append({
                'type': 'success',
                'message': "No obvious heading hierarchy issues found"
            })
        else:
            self.results['accessibility'].append({
                'type': 'warning',
                'message': f"Potential heading hierarchy issues in {heading_hierarchy_issues} files"
            })
        
        return heading_hierarchy_issues == 0
    
    def generate_summary(self):
        """Generate validation summary"""
        print("📊 Generating summary...")
        
        total_tests = 0
        passed_tests = 0
        warnings = 0
        errors = 0
        
        for category, results in self.results.items():
            if category == 'summary':
                continue
                
            for result in results:
                total_tests += 1
                if result['type'] == 'success':
                    passed_tests += 1
                elif result['type'] == 'warning':
                    warnings += 1
                elif result['type'] == 'error':
                    errors += 1
        
        self.results['summary'] = {
            'total_tests': total_tests,
            'passed_tests': passed_tests,
            'warnings': warnings,
            'errors': errors,
            'success_rate': (passed_tests / total_tests * 100) if total_tests > 0 else 0
        }
    
    def run_validation(self):
        """Run all validation tests"""
        print("🚀 Starting Typography System Validation")
        print("=" * 50)
        
        validation_results = {
            'css_variables': self.validate_css_variables(),
            'heading_usage': self.validate_heading_usage(),
            'settings_schema': self.validate_settings_schema(),
            'file_consistency': self.validate_file_consistency(),
            'performance': self.validate_performance(),
            'accessibility': self.validate_accessibility()
        }
        
        self.generate_summary()
        
        return validation_results
    
    def print_results(self):
        """Print validation results"""
        print("\n📋 Validation Results")
        print("=" * 50)
        
        for category, results in self.results.items():
            if category == 'summary':
                continue
                
            print(f"\n{category.replace('_', ' ').title()}:")
            for result in results:
                icon = '✅' if result['type'] == 'success' else \
                       '⚠️' if result['type'] == 'warning' else \
                       '❌' if result['type'] == 'error' else 'ℹ️'
                print(f"  {icon} {result['message']}")
        
        # Print summary
        summary = self.results['summary']
        print(f"\n📊 Summary:")
        print(f"  Total tests: {summary['total_tests']}")
        print(f"  Passed: {summary['passed_tests']}")
        print(f"  Warnings: {summary['warnings']}")
        print(f"  Errors: {summary['errors']}")
        print(f"  Success rate: {summary['success_rate']:.1f}%")
        
        if summary['errors'] == 0 and summary['warnings'] <= 5:
            print("\n🎉 Typography system validation PASSED!")
        elif summary['errors'] == 0:
            print("\n⚠️ Typography system validation passed with warnings")
        else:
            print("\n❌ Typography system validation FAILED")
    
    def export_report(self, filename='typography-validation-report.json'):
        """Export validation report to JSON"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2)
        print(f"\n📄 Report exported to {filename}")

def main():
    validator = TypographyValidator()
    validation_results = validator.run_validation()
    validator.print_results()
    validator.export_report()
    
    # Return exit code based on results
    summary = validator.results['summary']
    if summary['errors'] > 0:
        return 1
    elif summary['warnings'] > 10:
        return 2
    else:
        return 0

if __name__ == "__main__":
    exit(main())

