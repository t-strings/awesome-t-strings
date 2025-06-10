#!/usr/bin/env python3
"""
Link validation script for Awesome T-Strings.
Checks all links in markdown files for accessibility.
"""

import re
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path
from typing import List, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed

# Regular expression to find markdown links
LINK_PATTERN = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

# User agent to avoid being blocked
USER_AGENT = 'Mozilla/5.0 (compatible; awesome-t-strings-link-checker/1.0)'

# Timeout for requests (seconds)
TIMEOUT = 20

# Number of concurrent requests
MAX_WORKERS = 3

# Rate limiting delay (seconds)
RATE_LIMIT_DELAY = 0.5


def find_links(file_path: Path) -> List[Tuple[str, str, int]]:
    """Extract all links from a markdown file."""
    links = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            for match in LINK_PATTERN.finditer(line):
                text, url = match.groups()
                # Skip anchor links and relative paths
                if not url.startswith(('#', '/', '..')):
                    links.append((text, url, line_num))
    
    return links


def check_link(url: str) -> Tuple[str, bool, str]:
    """Check if a URL is accessible."""
    # Skip non-HTTP(S) URLs
    if not url.startswith(('http://', 'https://')):
        return url, True, "Skipped (not HTTP/HTTPS)"
    
    try:
        request = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            if response.status == 200:
                return url, True, f"OK ({response.status})"
            else:
                return url, False, f"HTTP {response.status}"
    except urllib.error.HTTPError as e:
        return url, False, f"HTTP {e.code}"
    except urllib.error.URLError as e:
        return url, False, f"URL Error: {e.reason}"
    except Exception as e:
        return url, False, f"Error: {str(e)}"


def validate_markdown_file(file_path: Path) -> List[dict]:
    """Validate all links in a markdown file."""
    print(f"\nChecking {file_path}...")
    links = find_links(file_path)
    
    if not links:
        print(f"  No links found.")
        return []
    
    print(f"  Found {len(links)} links to check.")
    
    results = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # Submit all link checks
        future_to_link = {
            executor.submit(check_link, url): (text, url, line_num)
            for text, url, line_num in links
        }
        
        # Process results as they complete
        for future in as_completed(future_to_link):
            text, url, line_num = future_to_link[future]
            checked_url, is_valid, message = future.result()
            
            result = {
                'file': str(file_path),
                'line': line_num,
                'text': text,
                'url': url,
                'valid': is_valid,
                'message': message
            }
            results.append(result)
            
            # Print progress
            status = "✓" if is_valid else "✗"
            print(f"  {status} Line {line_num}: {text} - {message}")
            
            # Rate limiting to be respectful
            time.sleep(RATE_LIMIT_DELAY)
    
    return results


def main():
    """Main function to validate all markdown files."""
    # Find all markdown files
    repo_root = Path(__file__).parent.parent
    markdown_files = list(repo_root.glob('**/*.md'))
    
    # Exclude some directories
    exclude_dirs = {'.git', 'node_modules', 'venv', '.venv'}
    markdown_files = [
        f for f in markdown_files 
        if not any(excluded in f.parts for excluded in exclude_dirs)
    ]
    
    print(f"Found {len(markdown_files)} markdown files to check.")
    
    # Check all files
    all_results = []
    for file_path in markdown_files:
        results = validate_markdown_file(file_path)
        all_results.extend(results)
    
    # Summary
    print("\n" + "="*50)
    print("SUMMARY")
    print("="*50)
    
    total_links = len(all_results)
    broken_links = [r for r in all_results if not r['valid']]
    
    print(f"Total links checked: {total_links}")
    print(f"Valid links: {total_links - len(broken_links)}")
    print(f"Broken links: {len(broken_links)}")
    
    if broken_links:
        print("\nBROKEN LINKS:")
        for result in broken_links:
            print(f"  {result['file']}:{result['line']} - {result['text']} ({result['url']})")
            print(f"    Error: {result['message']}")
        
        return 1  # Exit with error
    else:
        print("\nAll links are valid! ✨")
        return 0


if __name__ == '__main__':
    sys.exit(main())