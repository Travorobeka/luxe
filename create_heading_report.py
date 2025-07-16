#!/usr/bin/env python3
import json
import re

def create_heading_report():
    # Load the analysis results
    with open('heading-usage-analysis.json', 'r') as f:
        data = json.load(f)
    
    report = []
    report.append("# Heading Usage Analysis Report")
    report.append("")
    
    # Summary statistics
    summary = data['summary']
    report.append("## Summary Statistics")
    report.append("")
    report.append(f"- **Files with headings:** {summary['files_with_headings']}")
    report.append(f"- **Total H1 elements:** {summary['total_h1']}")
    report.append(f"- **Total H2 elements:** {summary['total_h2']}")
    report.append(f"- **Total H3 elements:** {summary['total_h3']}")
    report.append(f"- **Total H4 elements:** {summary['total_h4']}")
    report.append(f"- **Total H5 elements:** {summary['total_h5']}")
    report.append(f"- **Total H6 elements:** {summary['total_h6']}")
    report.append("")
    
    # Heading distribution
    total_headings = sum([summary[f'total_h{i}'] for i in range(1, 7)])
    report.append("## Heading Distribution")
    report.append("")
    for i in range(1, 7):
        count = summary[f'total_h{i}']
        percentage = (count / total_headings * 100) if total_headings > 0 else 0
        report.append(f"- **H{i}:** {count} ({percentage:.1f}%)")
    report.append("")
    
    # Clean up heading classes (remove Liquid syntax)
    clean_classes = []
    for class_name in summary['heading_classes']:
        # Filter out Liquid template syntax and invalid CSS classes
        if (not re.search(r'[{}%]', class_name) and 
            not class_name.startswith('==') and
            len(class_name) > 1 and
            re.match(r'^[a-zA-Z_-][a-zA-Z0-9_-]*$', class_name)):
            clean_classes.append(class_name)
    
    clean_classes = sorted(list(set(clean_classes)))
    
    report.append("## Common Heading CSS Classes")
    report.append("")
    report.append(f"Found {len(clean_classes)} valid CSS classes used with headings:")
    report.append("")
    
    # Group classes by type
    typography_classes = []
    utility_classes = []
    component_classes = []
    
    for class_name in clean_classes:
        if any(keyword in class_name.lower() for keyword in ['font', 'text', 'heading', 'title']):
            typography_classes.append(class_name)
        elif any(keyword in class_name.lower() for keyword in ['m-', 'f-', 'sf-']):
            component_classes.append(class_name)
        else:
            utility_classes.append(class_name)
    
    if typography_classes:
        report.append("### Typography-related Classes")
        for class_name in typography_classes[:20]:  # Show first 20
            report.append(f"- `{class_name}`")
        if len(typography_classes) > 20:
            report.append(f"- ... and {len(typography_classes) - 20} more")
        report.append("")
    
    if component_classes:
        report.append("### Component-specific Classes")
        for class_name in component_classes[:20]:  # Show first 20
            report.append(f"- `{class_name}`")
        if len(component_classes) > 20:
            report.append(f"- ... and {len(component_classes) - 20} more")
        report.append("")
    
    if utility_classes:
        report.append("### Utility Classes")
        for class_name in utility_classes[:20]:  # Show first 20
            report.append(f"- `{class_name}`")
        if len(utility_classes) > 20:
            report.append(f"- ... and {len(utility_classes) - 20} more")
        report.append("")
    
    # Analysis by file type
    report.append("## Analysis by File Type")
    report.append("")
    
    for category in ['sections', 'snippets', 'templates']:
        files_data = data[category]
        if files_data:
            report.append(f"### {category.title()}")
            report.append("")
            report.append(f"Files with headings: {len(files_data)}")
            
            # Count headings by type in this category
            category_counts = {'h1': 0, 'h2': 0, 'h3': 0, 'h4': 0, 'h5': 0, 'h6': 0}
            for file_data in files_data.values():
                for tag, count in file_data['heading_counts'].items():
                    category_counts[tag] += count
            
            total_in_category = sum(category_counts.values())
            report.append(f"Total headings: {total_in_category}")
            report.append("")
            
            for tag, count in category_counts.items():
                if count > 0:
                    percentage = (count / total_in_category * 100) if total_in_category > 0 else 0
                    report.append(f"- **{tag.upper()}:** {count} ({percentage:.1f}%)")
            report.append("")
    
    # Mapping to three-tier system
    report.append("## Mapping to Three-Tier Typography System")
    report.append("")
    report.append("Based on the analysis, here's the recommended mapping:")
    report.append("")
    report.append("### Main Heading (Primary titles, major section headers)")
    report.append("- **H1 elements:** All 17 instances")
    report.append("- **H2 elements:** 46 instances (major section headers)")
    report.append("- **Recommended CSS class:** `.main-heading`")
    report.append("")
    report.append("### Sub Heading (Secondary titles, subsection headers)")
    report.append("- **H3 elements:** 99 instances (most common)")
    report.append("- **H4 elements:** 16 instances")
    report.append("- **Recommended CSS class:** `.sub-heading`")
    report.append("")
    report.append("### Body Text (Body text, captions, small headings)")
    report.append("- **H5 elements:** 3 instances")
    report.append("- **H6 elements:** 3 instances")
    report.append("- **Recommended CSS class:** `.body-text`")
    report.append("")
    
    # Recommendations
    report.append("## Recommendations")
    report.append("")
    report.append("1. **Create utility classes** for the three-tier system:")
    report.append("   - `.main-heading` - for H1 and major H2 elements")
    report.append("   - `.sub-heading` - for H3 and H4 elements")
    report.append("   - `.body-text` - for H5, H6, and body text")
    report.append("")
    report.append("2. **Maintain backward compatibility** by keeping existing CSS classes")
    report.append("")
    report.append("3. **Focus on H3 elements** as they are the most commonly used (99 instances)")
    report.append("")
    report.append("4. **Review component-specific classes** to ensure they work with the new system")
    report.append("")
    report.append("5. **Create migration guide** for developers using custom heading styles")
    
    return '\n'.join(report)

if __name__ == "__main__":
    report_content = create_heading_report()
    
    # Save the report
    with open('heading-usage-report.md', 'w') as f:
        f.write(report_content)
    
    print("Heading usage report created: heading-usage-report.md")
    print("\nReport preview:")
    print("=" * 50)
    print(report_content[:1000] + "..." if len(report_content) > 1000 else report_content)

