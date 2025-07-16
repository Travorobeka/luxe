#!/usr/bin/env python3
import os
import re
import json

def analyze_heading_usage():
    results = {
        'sections': {},
        'snippets': {},
        'templates': {},
        'summary': {
            'total_h1': 0,
            'total_h2': 0,
            'total_h3': 0,
            'total_h4': 0,
            'total_h5': 0,
            'total_h6': 0,
            'heading_classes': set(),
            'files_with_headings': 0
        }
    }
    
    # Patterns to match heading elements and classes
    heading_pattern = r'<(h[1-6])[^>]*>(.*?)</\1>'
    heading_class_pattern = r'class=["\']([^"\']*)["\']'
    
    def analyze_file(filepath, category):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            headings = re.findall(heading_pattern, content, re.IGNORECASE | re.DOTALL)
            if headings:
                results['summary']['files_with_headings'] += 1
                
            file_data = {
                'headings': [],
                'heading_counts': {'h1': 0, 'h2': 0, 'h3': 0, 'h4': 0, 'h5': 0, 'h6': 0}
            }
            
            for tag, inner_content in headings:
                tag_lower = tag.lower()
                file_data['heading_counts'][tag_lower] += 1
                results['summary'][f'total_{tag_lower}'] += 1
                
                # Extract classes if present in the heading tag
                heading_tag_pattern = f'<{tag}[^>]*>'
                heading_tag_match = re.search(heading_tag_pattern, content, re.IGNORECASE)
                classes = []
                if heading_tag_match:
                    tag_content = heading_tag_match.group(0)
                    class_matches = re.findall(heading_class_pattern, tag_content)
                    for class_match in class_matches:
                        classes.extend(class_match.split())
                        results['summary']['heading_classes'].update(class_match.split())
                
                file_data['headings'].append({
                    'tag': tag_lower,
                    'content': inner_content.strip()[:100],  # First 100 chars
                    'classes': classes
                })
            
            if file_data['headings']:
                results[category][os.path.basename(filepath)] = file_data
                
        except Exception as e:
            print(f'Error analyzing {filepath}: {e}')
    
    # Analyze sections
    sections_dir = 'sections'
    if os.path.exists(sections_dir):
        for filename in os.listdir(sections_dir):
            if filename.endswith('.liquid'):
                analyze_file(os.path.join(sections_dir, filename), 'sections')
    
    # Analyze snippets
    snippets_dir = 'snippets'
    if os.path.exists(snippets_dir):
        for filename in os.listdir(snippets_dir):
            if filename.endswith('.liquid'):
                analyze_file(os.path.join(snippets_dir, filename), 'snippets')
    
    # Analyze templates
    templates_dir = 'templates'
    if os.path.exists(templates_dir):
        for root, dirs, files in os.walk(templates_dir):
            for filename in files:
                if filename.endswith('.liquid'):
                    analyze_file(os.path.join(root, filename), 'templates')
    
    # Convert set to list for JSON serialization
    results['summary']['heading_classes'] = list(results['summary']['heading_classes'])
    
    return results

if __name__ == "__main__":
    # Run analysis
    analysis_results = analyze_heading_usage()
    
    # Save results to JSON file
    with open('heading-usage-analysis.json', 'w') as f:
        json.dump(analysis_results, f, indent=2)
    
    print('Heading usage analysis complete!')
    print(f"Files with headings: {analysis_results['summary']['files_with_headings']}")
    print(f"Total H1: {analysis_results['summary']['total_h1']}")
    print(f"Total H2: {analysis_results['summary']['total_h2']}")
    print(f"Total H3: {analysis_results['summary']['total_h3']}")
    print(f"Total H4: {analysis_results['summary']['total_h4']}")
    print(f"Total H5: {analysis_results['summary']['total_h5']}")
    print(f"Total H6: {analysis_results['summary']['total_h6']}")
    print(f"Unique heading classes found: {len(analysis_results['summary']['heading_classes'])}")
    
    # Show some examples of heading classes
    if analysis_results['summary']['heading_classes']:
        print("\nSample heading classes found:")
        for i, class_name in enumerate(sorted(analysis_results['summary']['heading_classes'])[:10]):
            print(f"  - {class_name}")
        if len(analysis_results['summary']['heading_classes']) > 10:
            print(f"  ... and {len(analysis_results['summary']['heading_classes']) - 10} more")

