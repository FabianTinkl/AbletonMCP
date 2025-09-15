#!/usr/bin/env python3
"""
MCP Tool Validation Script

This script validates all MCP tools in the main.py file to ensure they follow
the established patterns and conventions.

Usage:
    python validate_tools.py                    # Validate main.py
    python validate_tools.py --file path.py     # Validate specific file
    python validate_tools.py --verbose          # Verbose output
"""

import argparse
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from mcp_server.validation import MCPToolValidator


def main():
    parser = argparse.ArgumentParser(description="Validate MCP tools")
    parser.add_argument(
        "--file", "-f",
        default="mcp_server/main.py",
        help="Python file to validate (default: mcp_server/main.py)"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Verbose output with detailed information"
    )
    parser.add_argument(
        "--json", "-j",
        action="store_true",
        help="Output results in JSON format"
    )
    
    args = parser.parse_args()
    
    # Resolve file path
    file_path = Path(args.file)
    if not file_path.is_absolute():
        file_path = project_root / file_path
    
    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    
    # Run validation
    validator = MCPToolValidator()
    results = validator.validate_file(str(file_path))
    
    if args.json:
        import json
        print(json.dumps(results, indent=2))
    else:
        # Generate and print report
        report = validator.generate_report(results)
        print(report)
        
        if args.verbose:
            print("\nDetailed Results:")
            print("-" * 40)
            for func_name, func_results in results.get("functions", {}).items():
                print(f"\n{func_name}:")
                if func_results.get("errors"):
                    print("  Errors:")
                    for error in func_results["errors"]:
                        print(f"    - {error}")
                if func_results.get("warnings"):
                    print("  Warnings:")
                    for warning in func_results["warnings"]:
                        print(f"    - {warning}")
                if func_results.get("suggestions"):
                    print("  Suggestions:")
                    for suggestion in func_results["suggestions"]:
                        print(f"    - {suggestion}")
    
    # Exit with error code if validation failed
    if not results.get("valid", False):
        sys.exit(1)


if __name__ == "__main__":
    main()