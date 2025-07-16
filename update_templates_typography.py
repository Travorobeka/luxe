#!/usr/bin/env python3
import os
import re
import glob
import json

def update_templates_typography():
    """
    Update template files to use the new three-tier typography system
    """
    
    # Define the mapping of heading patterns to new classes
    heading_updates = [
        # H1 and H2 -> Main Heading
        {
            'pattern': r'(<h[12][^>]*class="[^"]*?)(")',
            'replacement': r'\1 main-heading" data-typography="main-heading\2',
            'description': 'H1/H2 -> Main Heading'
        },
        {
            'pattern': r'(<h[12])(\s+class="[^"]*">)',
            'replacement': r'\1 class="main-heading" data-typography="main-heading"\2',
            'description': 'H1/H2 without main-heading class'
        },
        {
            'pattern': r'(<h[12])(\s*>)',
            'replacement': r'\1 class="main-heading" data-typography="main-heading"\2',
            'description': 'H1/H2 without any class'
        },
        
        # H3 and H4 -> Sub Heading
        {
            'pattern': r'(<h[34][^>]*class="[^"]*?)(")',
            'replacement': r'\1 sub-heading" data-typography="sub-heading\2',
            'description': 'H3/H4 -> Sub Heading'
        },
        {
            'pattern': r'(<h[34])(\s+class="[^"]*">)',
            'replacement': r'\1 class="sub-heading" data-typography="sub-heading"\2',
            'description': 'H3/H4 without sub-heading class'
        },
        {
            'pattern': r'(<h[34])(\s*>)',
            'replacement': r'\1 class="sub-heading" data-typography="sub-heading"\2',
            'description': 'H3/H4 without any class'
        },
        
        # H5 and H6 -> Body Text
        {
            'pattern': r'(<h[56][^>]*class="[^"]*?)(")',
            'replacement': r'\1 body-text" data-typography="body-text\2',
            'description': 'H5/H6 -> Body Text'
        },
        {
            'pattern': r'(<h[56])(\s+class="[^"]*">)',
            'replacement': r'\1 class="body-text" data-typography="body-text"\2',
            'description': 'H5/H6 without body-text class'
        },
        {
            'pattern': r'(<h[56])(\s*>)',
            'replacement': r'\1 class="body-text" data-typography="body-text"\2',
            'description': 'H5/H6 without any class'
        }
    ]
    
    # Get all template files
    template_files = glob.glob('templates/*.liquid') + glob.glob('templates/**/*.liquid', recursive=True)
    
    results = {
        'updated_files': [],
        'total_changes': 0,
        'errors': []
    }
    
    for file_path in template_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            file_changes = 0
            
            # Apply each heading update pattern
            for update in heading_updates:
                pattern = update['pattern']
                replacement = update['replacement']
                
                # Count matches before replacement
                matches = len(re.findall(pattern, content, re.IGNORECASE))
                if matches > 0:
                    content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
                    file_changes += matches
                    print(f"  {update['description']}: {matches} changes")
            
            # Only write if changes were made
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                results['updated_files'].append({
                    'file': file_path,
                    'changes': file_changes
                })
                results['total_changes'] += file_changes
                
                print(f"✅ Updated {file_path}: {file_changes} changes")
            
        except Exception as e:
            error_msg = f"Error processing {file_path}: {e}"
            results['errors'].append(error_msg)
            print(f"❌ {error_msg}")
    
    return results

def update_json_templates():
    """
    Update JSON template files that contain HTML with headings
    """
    
    # Get all JSON template files
    json_files = glob.glob('templates/*.json') + glob.glob('templates/**/*.json', recursive=True)
    
    results = {
        'updated_files': [],
        'total_changes': 0,
        'errors': []
    }
    
    # Heading patterns for JSON content (escaped)
    heading_updates = [
        # H1 and H2 -> Main Heading (in JSON strings)
        {
            'pattern': r'(<h[12][^>]*class=\\"[^"]*?)(\\")',
            'replacement': r'\1 main-heading\\" data-typography=\\"main-heading\2',
            'description': 'JSON H1/H2 -> Main Heading'
        },
        {
            'pattern': r'(<h[12])(\\s*>)',
            'replacement': r'\1 class=\\"main-heading\\" data-typography=\\"main-heading\\"\2',
            'description': 'JSON H1/H2 without class'
        },
        
        # H3 and H4 -> Sub Heading (in JSON strings)
        {
            'pattern': r'(<h[34][^>]*class=\\"[^"]*?)(\\")',
            'replacement': r'\1 sub-heading\\" data-typography=\\"sub-heading\2',
            'description': 'JSON H3/H4 -> Sub Heading'
        },
        {
            'pattern': r'(<h[34])(\\s*>)',
            'replacement': r'\1 class=\\"sub-heading\\" data-typography=\\"sub-heading\\"\2',
            'description': 'JSON H3/H4 without class'
        },
        
        # H5 and H6 -> Body Text (in JSON strings)
        {
            'pattern': r'(<h[56][^>]*class=\\"[^"]*?)(\\")',
            'replacement': r'\1 body-text\\" data-typography=\\"body-text\2',
            'description': 'JSON H5/H6 -> Body Text'
        },
        {
            'pattern': r'(<h[56])(\\s*>)',
            'replacement': r'\1 class=\\"body-text\\" data-typography=\\"body-text\\"\2',
            'description': 'JSON H5/H6 without class'
        }
    ]
    
    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            file_changes = 0
            
            # Apply each heading update pattern
            for update in heading_updates:
                pattern = update['pattern']
                replacement = update['replacement']
                
                # Count matches before replacement
                matches = len(re.findall(pattern, content, re.IGNORECASE))
                if matches > 0:
                    content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
                    file_changes += matches
                    print(f"  {update['description']}: {matches} changes")
            
            # Only write if changes were made
            if content != original_content:
                # Validate JSON before writing
                try:
                    json.loads(content)
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    results['updated_files'].append({
                        'file': file_path,
                        'changes': file_changes
                    })
                    results['total_changes'] += file_changes
                    
                    print(f"✅ Updated {file_path}: {file_changes} changes")
                except json.JSONDecodeError as e:
                    error_msg = f"JSON validation failed for {file_path}: {e}"
                    results['errors'].append(error_msg)
                    print(f"❌ {error_msg}")
            
        except Exception as e:
            error_msg = f"Error processing {file_path}: {e}"
            results['errors'].append(error_msg)
            print(f"❌ {error_msg}")
    
    return results

if __name__ == "__main__":
    print("🚀 Starting Template Typography Update")
    print("=" * 50)
    
    print("\n📁 Updating Liquid Templates...")
    liquid_results = update_templates_typography()
    
    print("\n📁 Updating JSON Templates...")
    json_results = update_json_templates()
    
    print("\n📊 Summary:")
    print(f"Liquid templates updated: {len(liquid_results['updated_files'])}")
    print(f"JSON templates updated: {len(json_results['updated_files'])}")
    print(f"Total changes: {liquid_results['total_changes'] + json_results['total_changes']}")
    
    if liquid_results['errors'] or json_results['errors']:
        print(f"Errors: {len(liquid_results['errors']) + len(json_results['errors'])}")
        for error in liquid_results['errors'] + json_results['errors']:
            print(f"  - {error}")
    
    print("\n✅ Template typography update complete!")
    print("🎯 All template heading elements now use the three-tier typography system")

