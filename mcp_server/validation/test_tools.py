#!/usr/bin/env python3
"""
MCP Tool Testing Script

This script runs comprehensive tests on MCP tools to ensure they function correctly.

Usage:
    python test_tools.py                        # Test all tools in main.py
    python test_tools.py --tool play            # Test specific tool
    python test_tools.py --verbose              # Verbose output
"""

import argparse
import asyncio
import importlib
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from mcp_server.validation import MCPToolTestFramework


async def test_all_tools(module_name="mcp_server.main", verbose=False):
    """Test all MCP tools in a module."""
    try:
        module = importlib.import_module(module_name)
    except ImportError as e:
        print(f"Error: Could not import module {module_name}: {e}")
        return False
    
    tester = MCPToolTestFramework()
    all_passed = True
    
    # Find all functions with @mcp.tool() decorator
    mcp_tools = []
    for name in dir(module):
        obj = getattr(module, name)
        if callable(obj) and hasattr(obj, '__name__') and asyncio.iscoroutinefunction(obj):
            # Check if it's likely an MCP tool (this is a heuristic)
            if name not in ['init_server', 'ensure_initialized', 'ensure_initialized_async']:
                mcp_tools.append((name, obj))
    
    print(f"Found {len(mcp_tools)} potential MCP tools to test")
    print("=" * 60)
    
    for tool_name, tool_func in mcp_tools:
        print(f"\nTesting {tool_name}...")
        try:
            results = await tester.run_comprehensive_test(tool_func)
            
            if verbose:
                report = tester.generate_test_report(results)
                print(report)
            else:
                status = "✅ PASSED" if results["overall_passed"] else "❌ FAILED"
                summary = results["summary"]
                print(f"{tool_name}: {status} ({summary['passed_tests']}/{summary['total_tests']} tests passed)")
                
                # Show errors even in non-verbose mode
                if not results["overall_passed"]:
                    for test_name, test_result in results["test_results"].items():
                        if not test_result["passed"] and test_result.get("errors"):
                            print(f"  {test_name}:")
                            for error in test_result["errors"]:
                                print(f"    ❌ {error}")
            
            if not results["overall_passed"]:
                all_passed = False
                
        except Exception as e:
            print(f"❌ FAILED: Exception during testing: {e}")
            all_passed = False
    
    print("\n" + "=" * 60)
    overall_status = "✅ ALL TESTS PASSED" if all_passed else "❌ SOME TESTS FAILED"
    print(f"Overall Result: {overall_status}")
    
    return all_passed


async def test_specific_tool(module_name, tool_name, verbose=False):
    """Test a specific MCP tool."""
    try:
        module = importlib.import_module(module_name)
    except ImportError as e:
        print(f"Error: Could not import module {module_name}: {e}")
        return False
    
    if not hasattr(module, tool_name):
        print(f"Error: Tool '{tool_name}' not found in module {module_name}")
        return False
    
    tool_func = getattr(module, tool_name)
    
    if not asyncio.iscoroutinefunction(tool_func):
        print(f"Error: '{tool_name}' is not an async function")
        return False
    
    tester = MCPToolTestFramework()
    
    print(f"Testing {tool_name}...")
    print("=" * 40)
    
    try:
        results = await tester.run_comprehensive_test(tool_func)
        report = tester.generate_test_report(results)
        print(report)
        return results["overall_passed"]
        
    except Exception as e:
        print(f"❌ FAILED: Exception during testing: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Test MCP tools")
    parser.add_argument(
        "--tool", "-t",
        help="Test specific tool function"
    )
    parser.add_argument(
        "--module", "-m",
        default="mcp_server.main",
        help="Module to import tools from (default: mcp_server.main)"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Verbose output with detailed test results"
    )
    
    args = parser.parse_args()
    
    async def run_tests():
        if args.tool:
            success = await test_specific_tool(args.module, args.tool, args.verbose)
        else:
            success = await test_all_tools(args.module, args.verbose)
        
        return success
    
    try:
        success = asyncio.run(run_tests())
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\nTesting interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()