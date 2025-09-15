#!/usr/bin/env python3
"""
Complete MCP Tool Validation Suite

This script runs both validation and testing on all MCP tools.

Usage:
    python run_validation_suite.py              # Run complete validation
    python run_validation_suite.py --quick      # Skip comprehensive testing
    python run_validation_suite.py --ci         # CI mode (exit on failure)
"""

import argparse
import asyncio
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from mcp_server.validation import MCPToolValidator, MCPToolTestFramework
import importlib


async def run_validation_suite(quick=False, ci_mode=False):
    """Run the complete validation suite."""
    print("🔍 MCP Tool Validation Suite")
    print("=" * 50)
    
    all_passed = True
    
    # Step 1: Code Validation
    print("\n📝 Step 1: Code Pattern Validation")
    print("-" * 35)
    
    validator = MCPToolValidator()
    main_py_path = project_root / "mcp_server" / "main.py"
    
    if not main_py_path.exists():
        print(f"❌ Error: main.py not found at {main_py_path}")
        return False
    
    validation_results = validator.validate_file(str(main_py_path))
    validation_report = validator.generate_report(validation_results)
    print(validation_report)
    
    if not validation_results["valid"]:
        all_passed = False
        if ci_mode:
            print("💥 Validation failed in CI mode, stopping")
            return False
    
    # Step 2: Functional Testing (unless quick mode)
    if not quick:
        print("\n🧪 Step 2: Functional Testing")
        print("-" * 30)
        
        try:
            # Import the module
            module = importlib.import_module("mcp_server.main")
            tester = MCPToolTestFramework()
            
            # Find MCP tools
            mcp_tools = []
            for name in dir(module):
                obj = getattr(module, name)
                if callable(obj) and hasattr(obj, '__name__') and asyncio.iscoroutinefunction(obj):
                    # Skip utility functions
                    if name not in ['init_server', 'ensure_initialized', 'ensure_initialized_async']:
                        mcp_tools.append((name, obj))
            
            print(f"Found {len(mcp_tools)} tools to test")
            
            failed_tools = []
            for tool_name, tool_func in mcp_tools:
                print(f"  Testing {tool_name}...", end="")
                try:
                    results = await tester.run_comprehensive_test(tool_func)
                    if results["overall_passed"]:
                        print(" ✅")
                    else:
                        print(" ❌")
                        failed_tools.append(tool_name)
                        all_passed = False
                        
                        # Show summary of failures
                        summary = results["summary"]
                        print(f"    Failed: {summary['failed_tests']}/{summary['total_tests']} tests")
                        
                except Exception as e:
                    print(f" ❌ (Exception: {e})")
                    failed_tools.append(tool_name)
                    all_passed = False
            
            if failed_tools:
                print(f"\n❌ Failed tools: {', '.join(failed_tools)}")
                if ci_mode:
                    print("💥 Testing failed in CI mode, stopping")
                    return False
            else:
                print("\n✅ All tools passed functional testing")
        
        except ImportError as e:
            print(f"❌ Could not import main module: {e}")
            all_passed = False
            if ci_mode:
                return False
    
    # Step 3: Summary
    print("\n📊 Validation Suite Summary")
    print("-" * 30)
    
    validation_status = "✅ PASSED" if validation_results["valid"] else "❌ FAILED"
    print(f"Code Validation: {validation_status}")
    
    if not quick:
        testing_status = "✅ PASSED" if not failed_tools else "❌ FAILED"
        print(f"Functional Testing: {testing_status}")
    else:
        print("Functional Testing: ⏭️ SKIPPED (quick mode)")
    
    overall_status = "✅ PASSED" if all_passed else "❌ FAILED"
    print(f"\nOverall Result: {overall_status}")
    
    if all_passed:
        print("\n🎉 All validation checks passed!")
        print("Your MCP tools are ready for deployment.")
    else:
        print("\n⚠️ Some validation checks failed.")
        print("Please review the errors above and fix them before deploying.")
    
    return all_passed


def main():
    parser = argparse.ArgumentParser(description="Run MCP tool validation suite")
    parser.add_argument(
        "--quick",
        action="store_true",
        help="Skip comprehensive functional testing"
    )
    parser.add_argument(
        "--ci",
        action="store_true", 
        help="CI mode: exit immediately on first failure"
    )
    
    args = parser.parse_args()
    
    try:
        success = asyncio.run(run_validation_suite(args.quick, args.ci))
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\nValidation interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"Fatal error during validation: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()