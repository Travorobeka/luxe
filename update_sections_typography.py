#!/usr/bin/env python3
import os
import re
import glob

def update_section_typography():
    """
    Update sections to use the new three-tier typography system
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
    
    # Get all section files
    section_files = glob.glob('sections/*.liquid')
    
    results = {
        'updated_files': [],
        'total_changes': 0,
        'errors': []
    }
    
    for file_path in section_files:
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

def update_snippets_typography():
    """
    Update snippets to use the new three-tier typography system
    """
    
    # Get all snippet files
    snippet_files = glob.glob('snippets/*.liquid')
    
    results = {
        'updated_files': [],
        'total_changes': 0,
        'errors': []
    }
    
    # Same heading updates as sections
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
    
    for file_path in snippet_files:
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

if __name__ == "__main__":
    print("🚀 Starting Typography System Update")
    print("=" * 50)
    
    print("\n📁 Updating Sections...")
    section_results = update_section_typography()
    
    print("\n📁 Updating Snippets...")
    snippet_results = update_snippets_typography()
    
    print("\n📊 Summary:")
    print(f"Sections updated: {len(section_results['updated_files'])}")
    print(f"Snippets updated: {len(snippet_results['updated_files'])}")
    print(f"Total changes: {section_results['total_changes'] + snippet_results['total_changes']}")
    
    if section_results['errors'] or snippet_results['errors']:
        print(f"Errors: {len(section_results['errors']) + len(snippet_results['errors'])}")
        for error in section_results['errors'] + snippet_results['errors']:
            print(f"  - {error}")
    
    print("\n✅ Typography system update complete!")
    print("🎯 All heading elements now use the three-tier typography system")
    print("📝 Check the updated files and test the theme in Shopify admin")

