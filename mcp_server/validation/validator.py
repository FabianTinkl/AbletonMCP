"""
MCP Tool Validator

Validates that MCP tools follow the established patterns in this project.
"""

import ast
import inspect
import re
from typing import List, Dict, Any, Optional, Tuple
from pathlib import Path
import importlib.util


class MCPToolValidator:
    """Validates MCP tools against project conventions."""
    
    def __init__(self):
        """Initialize the validator with established patterns."""
        self.required_patterns = {
            "decorator": "@mcp.tool()",
            "return_type": "-> str",
            "async_function": "async def",
            "lazy_init_check": "ensure_initialized_async()",
            "handlers_check": "if not handlers:",
            "error_handling": "except Exception as e:",
            "error_return": 'return f"Error: {str(e)}"',
            "docstring_args": "Args:",
        }
        
        self.validation_rules = [
            self._validate_decorator,
            self._validate_return_type,
            self._validate_async_function,
            self._validate_docstring,
            self._validate_parameter_types,
            self._validate_error_handling,
            self._validate_initialization_check,
            self._validate_handler_access,
        ]
        
    def validate_tool_function(self, func_source: str, func_name: str) -> Dict[str, Any]:
        """
        Validate a single MCP tool function.
        
        Args:
            func_source: The source code of the function
            func_name: Name of the function
            
        Returns:
            Dictionary with validation results
        """
        results = {
            "function_name": func_name,
            "valid": True,
            "errors": [],
            "warnings": [],
            "suggestions": []
        }
        
        # Parse the function source
        try:
            tree = ast.parse(func_source)
        except SyntaxError as e:
            results["valid"] = False
            results["errors"].append(f"Syntax error: {e}")
            return results
            
        # Find the function definition
        func_node = None
        for node in ast.walk(tree):
            if isinstance(node, ast.AsyncFunctionDef) and node.name == func_name:
                func_node = node
                break
            elif isinstance(node, ast.FunctionDef) and node.name == func_name:
                func_node = node
                break
                
        if not func_node:
            results["valid"] = False
            results["errors"].append(f"Function {func_name} not found in parsed AST")
            return results
        
        # Apply validation rules
        for rule in self.validation_rules:
            try:
                rule(func_source, func_node, results)
            except Exception as e:
                results["warnings"].append(f"Validation rule failed: {e}")
                
        return results
    
    def _validate_decorator(self, source: str, node: ast.FunctionDef, results: Dict[str, Any]):
        """Validate that the function has the correct @mcp.tool() decorator."""
        if "@mcp.tool()" not in source:
            results["valid"] = False
            results["errors"].append("Missing @mcp.tool() decorator")
            
        # Check for correct decorator placement
        if node.decorator_list:
            decorator_found = False
            for decorator in node.decorator_list:
                if (isinstance(decorator, ast.Call) and 
                    isinstance(decorator.func, ast.Attribute) and
                    decorator.func.attr == "tool"):
                    decorator_found = True
                    break
            if not decorator_found:
                results["warnings"].append("@mcp.tool() decorator not found in AST")
    
    def _validate_return_type(self, source: str, node: ast.FunctionDef, results: Dict[str, Any]):
        """Validate that the function returns str."""
        if "-> str" not in source:
            results["valid"] = False
            results["errors"].append("Function must have return type annotation '-> str'")
            
        # Additional check for return type in AST
        if node.returns:
            if not (isinstance(node.returns, ast.Name) and node.returns.id == "str"):
                results["errors"].append("Return type must be 'str'")
    
    def _validate_async_function(self, source: str, node: ast.FunctionDef, results: Dict[str, Any]):
        """Validate that the function is async."""
        if not isinstance(node, ast.AsyncFunctionDef):
            results["valid"] = False
            results["errors"].append("MCP tools must be async functions")
    
    def _validate_docstring(self, source: str, node: ast.FunctionDef, results: Dict[str, Any]):
        """Validate docstring format and Args section."""
        if not ast.get_docstring(node):
            results["warnings"].append("Function should have a docstring")
            return
            
        docstring = ast.get_docstring(node)
        
        # Check for Args section if function has parameters (excluding self)
        params = [arg.arg for arg in node.args.args if arg.arg != 'self']
        if params and "Args:" not in docstring:
            results["errors"].append("Function with parameters must have 'Args:' section in docstring")
        
        # Check that all parameters are documented
        if "Args:" in docstring:
            for param in params:
                if f"{param}:" not in docstring:
                    results["warnings"].append(f"Parameter '{param}' not documented in Args section")
    
    def _validate_parameter_types(self, source: str, node: ast.FunctionDef, results: Dict[str, Any]):
        """Validate parameter type hints."""
        for arg in node.args.args:
            if arg.arg != 'self' and not arg.annotation:
                results["warnings"].append(f"Parameter '{arg.arg}' should have type annotation")
    
    def _validate_error_handling(self, source: str, node: ast.FunctionDef, results: Dict[str, Any]):
        """Validate error handling patterns."""
        has_try_except = False
        has_error_return = False
        
        for n in ast.walk(node):
            if isinstance(n, ast.Try):
                has_try_except = True
            if (isinstance(n, ast.Return) and 
                isinstance(n.value, ast.JoinedStr)):  # f-string
                # Check if it's an error return
                if any("Error:" in str(part.s) if hasattr(part, 's') else False 
                       for part in n.value.values if hasattr(part, 's')):
                    has_error_return = True
        
        if not has_try_except:
            results["errors"].append("Function should have try-except error handling")
        
        if has_try_except and not has_error_return:
            results["warnings"].append("Error handling should return formatted error message")
    
    def _validate_initialization_check(self, source: str, node: ast.FunctionDef, results: Dict[str, Any]):
        """Validate lazy initialization pattern."""
        # For tools that don't use handlers, they should use ensure_initialized_async()
        if "ensure_initialized_async()" in source:
            return  # Good pattern
        elif "if not handlers:" in source:
            return  # Also acceptable pattern
        else:
            results["warnings"].append("Consider adding initialization check (ensure_initialized_async() or handlers check)")
    
    def _validate_handler_access(self, source: str, node: ast.FunctionDef, results: Dict[str, Any]):
        """Validate handler access pattern."""
        if 'handlers[' in source:
            # Should have initialization check
            if "if not handlers:" not in source:
                results["errors"].append("Handler access should include 'if not handlers:' check")
            
            # Should have error return for uninitialized handlers
            if 'return "Error: Server not initialized"' not in source:
                results["errors"].append("Should return 'Error: Server not initialized' when handlers not available")
    
    def validate_file(self, file_path: str) -> Dict[str, Any]:
        """
        Validate all MCP tools in a Python file.
        
        Args:
            file_path: Path to the Python file to validate
            
        Returns:
            Dictionary with validation results for all functions
        """
        results = {
            "file_path": file_path,
            "valid": True,
            "functions": {},
            "summary": {"total": 0, "valid": 0, "invalid": 0}
        }
        
        try:
            with open(file_path, 'r') as f:
                source = f.read()
        except Exception as e:
            results["valid"] = False
            results["error"] = f"Could not read file: {e}"
            return results
        
        # Find all functions with @mcp.tool() decorator
        mcp_functions = self._find_mcp_tools(source)
        
        for func_name, func_source in mcp_functions.items():
            func_results = self.validate_tool_function(func_source, func_name)
            results["functions"][func_name] = func_results
            results["summary"]["total"] += 1
            
            if func_results["valid"]:
                results["summary"]["valid"] += 1
            else:
                results["summary"]["invalid"] += 1
                results["valid"] = False
        
        return results
    
    def _find_mcp_tools(self, source: str) -> Dict[str, str]:
        """Find all functions with @mcp.tool() decorator."""
        functions = {}
        lines = source.split('\n')
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Look for @mcp.tool() decorator
            if line == "@mcp.tool()":
                # Find the function definition
                func_start = i
                while i < len(lines) and not lines[i].strip().startswith("async def "):
                    i += 1
                
                if i < len(lines):
                    # Extract function name
                    func_line = lines[i].strip()
                    match = re.match(r'async def (\w+)', func_line)
                    if match:
                        func_name = match.group(1)
                        
                        # Find the end of the function
                        func_end = self._find_function_end(lines, i)
                        
                        # Extract the complete function source
                        func_source = '\n'.join(lines[func_start:func_end + 1])
                        functions[func_name] = func_source
            i += 1
        
        return functions
    
    def _find_function_end(self, lines: List[str], start_idx: int) -> int:
        """Find the end of a function definition."""
        # Find the actual function definition line
        func_line_idx = start_idx
        while func_line_idx < len(lines) and not lines[func_line_idx].strip().startswith("async def "):
            func_line_idx += 1
        
        if func_line_idx >= len(lines):
            return len(lines) - 1
            
        # Get the indentation level of the function definition
        func_indent = len(lines[func_line_idx]) - len(lines[func_line_idx].lstrip())
        
        i = func_line_idx + 1
        while i < len(lines):
            line = lines[i]
            if line.strip() == "":
                i += 1
                continue
            
            current_indent = len(line) - len(line.lstrip())
            # Function ends when we find a line at the same or lesser indent level
            if current_indent <= func_indent and line.strip():
                return i - 1
            
            i += 1
        
        return len(lines) - 1
    
    def generate_report(self, validation_results: Dict[str, Any]) -> str:
        """Generate a human-readable validation report."""
        report = []
        report.append(f"MCP Tool Validation Report")
        report.append("=" * 50)
        
        if "file_path" in validation_results:
            report.append(f"File: {validation_results['file_path']}")
            report.append(f"Overall Status: {'✅ VALID' if validation_results['valid'] else '❌ INVALID'}")
            
            summary = validation_results["summary"]
            report.append(f"Functions: {summary['total']} total, {summary['valid']} valid, {summary['invalid']} invalid")
            report.append("")
            
            for func_name, func_results in validation_results["functions"].items():
                report.append(f"Function: {func_name}")
                report.append(f"  Status: {'✅ Valid' if func_results['valid'] else '❌ Invalid'}")
                
                if func_results["errors"]:
                    report.append("  Errors:")
                    for error in func_results["errors"]:
                        report.append(f"    ❌ {error}")
                
                if func_results["warnings"]:
                    report.append("  Warnings:")
                    for warning in func_results["warnings"]:
                        report.append(f"    ⚠️ {warning}")
                
                if func_results["suggestions"]:
                    report.append("  Suggestions:")
                    for suggestion in func_results["suggestions"]:
                        report.append(f"    💡 {suggestion}")
                
                report.append("")
        
        return "\n".join(report)