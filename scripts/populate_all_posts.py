#!/usr/bin/env python3
"""
populate_all_posts.py - Populate the "All Posts" section in a/index.html

This script reads all posts from a/toc/chrono-data.json and generates
a complete table of all blog posts in the "All Posts" section.

Usage:
    python populate_all_posts.py
    python populate_all_posts.py --dry-run

Author: parametrix
Date: January 8, 2026
"""

import argparse
import html
import json
import re
import sys
from pathlib import Path

# Configuration
REPO_ROOT = Path(__file__).parent.parent
INDEX_FILE = REPO_ROOT / "a" / "index.html"
CHRONO_FILE = REPO_ROOT / "a" / "toc" / "chrono-data.json"


def generate_table_rows(posts):
    """
    Generate HTML table rows for all posts.
    
    Args:
        posts: List of post dictionaries from chrono-data.json
        
    Returns:
        str: HTML string containing all table rows
    """
    rows = []
    for post in posts:
        post_num = post.get('num', 0)
        date = post.get('date', '')
        title = post.get('title', '')
        filename = post.get('file', '')
        
        # Categories are not in chrono-data.json, so leave empty
        categories = ''
        
        # Format: <tr><td align="right">NUM</td><td>DATE</td><td><a href="file">Title</a>&nbsp;&nbsp;&nbsp;<a href="file">web</a>&nbsp;&nbsp;&nbsp;&nbsp;</td><td>CATEGORIES</td></tr>
        row = (
            f'<tr><td align="right">{html.escape(str(post_num))}</td>'
            f'<td>{html.escape(str(date))}</td>'
            f'<td><a href="{html.escape(filename, quote=True)}">{html.escape(title)}</a>'
            f'&nbsp;&nbsp;&nbsp;<a href="{html.escape(filename, quote=True)}">web</a>'
            f'&nbsp;&nbsp;&nbsp;&nbsp;</td>'
            f'<td>{html.escape(categories)}</td></tr>'
        )
        rows.append(row)
    
    return '\n'.join(rows)


def update_all_posts_table(table_rows_html, dry_run=False):
    """
    Update the "All Posts" table in index.html with generated rows.
    
    Args:
        table_rows_html: HTML string containing all table rows
        dry_run: If True, preview changes without writing
        
    Returns:
        bool: True if successful, False otherwise
    """
    if not INDEX_FILE.exists():
        print(f"Error: Index file not found: {INDEX_FILE}")
        return False
    
    content = INDEX_FILE.read_text(encoding='utf-8')
    
    # Pattern to find the "All Posts" table and replace its content
    # We want to match from the closing </tr> of the header row to the </table>
    # and replace everything in between with our generated rows
    pattern = r'(<h3>All Posts</h3>.*?<th>Categories</th>\s*</tr>)(.*?)(</table>)'
    
    match = re.search(pattern, content, flags=re.DOTALL)
    
    if not match:
        print("Error: Could not find 'All Posts' table in index.html")
        print("The table structure may have changed.")
        return False
    
    # Replace the middle group (empty space or old rows) with new rows
    new_content = content[:match.start(2)] + '\n' + table_rows_html + '\n' + content[match.end(2):]
    
    if dry_run:
        print("[DRY RUN] Would update 'All Posts' table in index.html")
        print(f"[DRY RUN] Generated {len(table_rows_html.splitlines())} table rows")
        print(f"[DRY RUN] Preview of first 3 rows:")
        for i, row in enumerate(table_rows_html.splitlines()[:3]):
            print(f"  {row}")
        if len(table_rows_html.splitlines()) > 3:
            print(f"  ... and {len(table_rows_html.splitlines()) - 3} more rows")
        return True
    else:
        INDEX_FILE.write_text(new_content, encoding='utf-8')
        print(f"Updated 'All Posts' table in index.html")
        print(f"Added {len(table_rows_html.splitlines())} table rows")
        return True


def populate_all_posts(dry_run=False):
    """
    Main function to populate the "All Posts" section.
    
    Args:
        dry_run: If True, preview changes without writing
        
    Returns:
        bool: True if successful, False otherwise
    """
    # Read chrono-data.json
    if not CHRONO_FILE.exists():
        print(f"Error: Chrono file not found: {CHRONO_FILE}")
        return False
    
    try:
        chrono_data = json.loads(CHRONO_FILE.read_text(encoding='utf-8'))
    except json.JSONDecodeError as e:
        print(f"Error: Could not parse chrono file: {e}")
        return False
    
    posts = chrono_data.get('posts', [])
    total_posts = len(posts)
    
    if total_posts == 0:
        print("Warning: No posts found in chrono-data.json")
        return False
    
    print(f"Found {total_posts} posts in chrono-data.json")
    
    # Generate table rows
    print("Generating HTML table rows...")
    table_rows_html = generate_table_rows(posts)
    
    # Update index.html
    print("Updating index.html...")
    success = update_all_posts_table(table_rows_html, dry_run)
    
    if success:
        print()
        if dry_run:
            print("[DRY RUN] Preview complete. No files were modified.")
            print("Run without --dry-run to apply changes.")
        else:
            print("Successfully populated 'All Posts' section!")
            print()
            print("Next steps:")
            print("  git add a/index.html")
            print('  git commit -m "Populate All Posts section with complete post listing"')
            print("  git push")
    
    return success


def main():
    parser = argparse.ArgumentParser(
        description="Populate the 'All Posts' section in a/index.html",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python populate_all_posts.py
  python populate_all_posts.py --dry-run

This script:
  - Reads all posts from a/toc/chrono-data.json
  - Generates HTML table rows for each post
  - Updates the empty "All Posts" table in a/index.html
  
The table includes: Post number, Date, Title (with links), and Categories (empty).
        """
    )
    
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without writing files"
    )
    
    args = parser.parse_args()
    
    success = populate_all_posts(dry_run=args.dry_run)
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
