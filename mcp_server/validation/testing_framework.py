"""
MCP Tool Testing Framework

Provides testing utilities for validating MCP tool functionality.
"""

import asyncio
import inspect
import sys
from typing import Dict, Any, List, Optional, Callable, Tuple
from unittest.mock import AsyncMock, MagicMock, patch
import traceback


class MCPToolTestFramework:
    """Testing framework for MCP tools."""
    
    def __init__(self):
        """Initialize the testing framework."""
        self.test_results = []
        self.mock_handlers = {}
        self.mock_ableton_tools = None
        self.setup_mocks()
    
    def setup_mocks(self):
        """Set up mock objects for testing."""
        # Mock handlers
        self.mock_handlers = {
            "transport": AsyncMock(),
            "project": AsyncMock(),
            "track": AsyncMock(),
            "composition": AsyncMock(),
            "midi": AsyncMock(),
            "instruments": AsyncMock(),
            "effects": AsyncMock(),
            "samples": AsyncMock(),
        }
        
        # Mock ableton_tools
        self.mock_ableton_tools = AsyncMock()
        
        # Set up common return values
        self._setup_mock_returns()
    
    def _setup_mock_returns(self):
        """Set up default return values for mocks."""
        # Transport handler returns
        self.mock_handlers["transport"].play.return_value = [{"type": "text", "text": "▶️ Playback started"}]
        self.mock_handlers["transport"].stop.return_value = [{"type": "text", "text": "⏹️ Playback stopped"}]
        self.mock_handlers["transport"].set_tempo.return_value = [{"type": "text", "text": "🥁 Tempo set to 132 BPM"}]
        
        # Track handler returns
        self.mock_handlers["track"].create_track.return_value = [{"type": "text", "text": "Created audio track"}]
        
        # Composition handler returns
        self.mock_handlers["composition"].generate_chord_progression.return_value = [{"type": "text", "text": "Generated chord progression"}]
        self.mock_handlers["composition"].create_techno_song.return_value = [{"type": "text", "text": "Created techno song"}]
        
        # AbletonTools returns
        self.mock_ableton_tools.ping.return_value = {"message": "Connected to Ableton Live 11.3.21"}
        self.mock_ableton_tools.connect.return_value = True
        
    async def test_tool_registration(self, tool_function: Callable) -> Dict[str, Any]:
        """
        Test that a tool function is properly registered and decorated.
        
        Args:
            tool_function: The MCP tool function to test
            
        Returns:
            Test results dictionary
        """
        result = {
            "test_name": "tool_registration",
            "function_name": tool_function.__name__,
            "passed": True,
            "errors": [],
            "details": {}
        }
        
        try:
            # Check if function is async
            if not asyncio.iscoroutinefunction(tool_function):
                result["passed"] = False
                result["errors"].append("Function must be async")
            
            # Check return type annotation
            signature = inspect.signature(tool_function)
            if signature.return_annotation != str:
                result["passed"] = False
                result["errors"].append("Function must have return type annotation '-> str'")
            
            # Check for proper decorator (this is harder to test directly)
            if not hasattr(tool_function, '__annotations__'):
                result["errors"].append("Function should have type annotations")
            
            result["details"]["is_async"] = asyncio.iscoroutinefunction(tool_function)
            result["details"]["return_annotation"] = str(signature.return_annotation)
            result["details"]["parameters"] = list(signature.parameters.keys())
            
        except Exception as e:
            result["passed"] = False
            result["errors"].append(f"Registration test failed: {e}")
        
        return result
    
    async def test_tool_execution(self, tool_function: Callable, 
                                test_parameters: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Test basic execution of a tool function.
        
        Args:
            tool_function: The MCP tool function to test
            test_parameters: Parameters to pass to the function
            
        Returns:
            Test results dictionary
        """
        result = {
            "test_name": "tool_execution",
            "function_name": tool_function.__name__,
            "passed": True,
            "errors": [],
            "details": {}
        }
        
        try:
            # Prepare parameters
            if test_parameters is None:
                test_parameters = self._get_default_parameters(tool_function)
            
            # Mock global variables that tools depend on
            with patch('mcp_server.main.handlers', self.mock_handlers), \
                 patch('mcp_server.main.ableton_tools', self.mock_ableton_tools):
                
                # Execute the function
                if asyncio.iscoroutinefunction(tool_function):
                    execution_result = await tool_function(**test_parameters)
                else:
                    execution_result = tool_function(**test_parameters)
                
                # Validate result
                if not isinstance(execution_result, str):
                    result["passed"] = False
                    result["errors"].append(f"Function must return str, got {type(execution_result)}")
                
                result["details"]["return_value"] = execution_result
                result["details"]["parameters_used"] = test_parameters
                
        except Exception as e:
            result["passed"] = False
            result["errors"].append(f"Execution failed: {e}")
            result["details"]["exception"] = str(e)
            result["details"]["traceback"] = traceback.format_exc()
        
        return result
    
    async def test_error_handling(self, tool_function: Callable,
                                test_parameters: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Test error handling behavior of a tool function.
        
        Args:
            tool_function: The MCP tool function to test
            test_parameters: Parameters to pass to the function
            
        Returns:
            Test results dictionary
        """
        result = {
            "test_name": "error_handling", 
            "function_name": tool_function.__name__,
            "passed": True,
            "errors": [],
            "details": {}
        }
        
        try:
            # Test with mock handlers that raise exceptions
            error_handlers = {}
            for name, handler in self.mock_handlers.items():
                error_handler = AsyncMock()
                for attr_name in dir(handler):
                    if not attr_name.startswith('_'):
                        setattr(error_handler, attr_name, AsyncMock(side_effect=Exception("Test error")))
                error_handlers[name] = error_handler
            
            # Test with error-inducing mocks
            error_ableton_tools = AsyncMock()
            for attr_name in dir(self.mock_ableton_tools):
                if not attr_name.startswith('_'):
                    setattr(error_ableton_tools, attr_name, AsyncMock(side_effect=Exception("Test error")))
            
            if test_parameters is None:
                test_parameters = self._get_default_parameters(tool_function)
            
            with patch('mcp_server.main.handlers', error_handlers), \
                 patch('mcp_server.main.ableton_tools', error_ableton_tools):
                
                execution_result = await tool_function(**test_parameters)
                
                # Check that error is handled properly
                if not isinstance(execution_result, str):
                    result["passed"] = False
                    result["errors"].append("Function must return string even on error")
                elif not execution_result.startswith("Error:"):
                    result["passed"] = False
                    result["errors"].append("Error result should start with 'Error:'")
                
                result["details"]["error_return_value"] = execution_result
            
        except Exception as e:
            result["passed"] = False
            result["errors"].append(f"Error handling test failed: {e}")
            result["details"]["exception"] = str(e)
        
        return result
    
    async def test_parameter_validation(self, tool_function: Callable) -> Dict[str, Any]:
        """
        Test parameter validation for a tool function.
        
        Args:
            tool_function: The MCP tool function to test
            
        Returns:
            Test results dictionary
        """
        result = {
            "test_name": "parameter_validation",
            "function_name": tool_function.__name__,
            "passed": True,
            "errors": [],
            "details": {}
        }
        
        try:
            signature = inspect.signature(tool_function)
            validation_tests = []
            
            # Test invalid parameter values based on common patterns
            for param_name, param in signature.parameters.items():
                invalid_tests = self._get_invalid_parameter_tests(param_name, param)
                
                for invalid_value, expected_error in invalid_tests:
                    test_params = self._get_default_parameters(tool_function)
                    test_params[param_name] = invalid_value
                    
                    with patch('mcp_server.main.handlers', self.mock_handlers), \
                         patch('mcp_server.main.ableton_tools', self.mock_ableton_tools):
                        
                        try:
                            validation_result = await tool_function(**test_params)
                            
                            # Check if validation error was returned
                            if expected_error and not validation_result.startswith("Error:"):
                                result["errors"].append(
                                    f"Expected validation error for {param_name}={invalid_value}, "
                                    f"but got: {validation_result}"
                                )
                            
                            validation_tests.append({
                                "parameter": param_name,
                                "invalid_value": invalid_value,
                                "result": validation_result,
                                "expected_error": expected_error
                            })
                            
                        except Exception as e:
                            validation_tests.append({
                                "parameter": param_name,
                                "invalid_value": invalid_value,
                                "exception": str(e),
                                "expected_error": expected_error
                            })
            
            result["details"]["validation_tests"] = validation_tests
            
        except Exception as e:
            result["passed"] = False
            result["errors"].append(f"Parameter validation test failed: {e}")
        
        return result
    
    def _get_default_parameters(self, tool_function: Callable) -> Dict[str, Any]:
        """Get default parameters for testing a function."""
        signature = inspect.signature(tool_function)
        params = {}
        
        for param_name, param in signature.parameters.items():
            if param.default != inspect.Parameter.empty:
                continue  # Use default value
            
            # Provide test values based on parameter name and type
            if param.annotation == int:
                if 'track' in param_name.lower():
                    params[param_name] = 0
                elif 'clip' in param_name.lower():
                    params[param_name] = 0
                elif 'bpm' in param_name.lower():
                    params[param_name] = 120
                elif 'length' in param_name.lower() or 'bar' in param_name.lower():
                    params[param_name] = 8
                else:
                    params[param_name] = 1
            elif param.annotation == float:
                if 'bpm' in param_name.lower():
                    params[param_name] = 132.0
                else:
                    params[param_name] = 1.0
            elif param.annotation == str:
                if 'key' in param_name.lower():
                    params[param_name] = "Am"
                elif 'genre' in param_name.lower():
                    params[param_name] = "techno"
                elif 'type' in param_name.lower():
                    params[param_name] = "audio"
                elif 'name' in param_name.lower():
                    params[param_name] = "Test"
                else:
                    params[param_name] = "test_value"
            elif param.annotation == bool:
                params[param_name] = True
            else:
                # Try to provide a sensible default
                params[param_name] = None
        
        return params
    
    def _get_invalid_parameter_tests(self, param_name: str, param: inspect.Parameter) -> List[Tuple[Any, bool]]:
        """Get invalid parameter test cases."""
        invalid_tests = []
        
        # Common invalid values based on parameter names and types
        if 'bpm' in param_name.lower():
            invalid_tests.extend([
                (50, True),   # Too low
                (250, True),  # Too high
                (-10, True),  # Negative
            ])
        elif 'track_type' in param_name.lower():
            invalid_tests.extend([
                ("invalid", True),
                ("", True),
                (123, True),
            ])
        elif 'genre' in param_name.lower():
            invalid_tests.extend([
                ("invalid_genre", True),
                ("", True),
                (123, True),
            ])
        elif param.annotation == int:
            invalid_tests.extend([
                (-1, True),   # Negative (often invalid for indices)
                ("not_int", True),  # Wrong type
            ])
        
        return invalid_tests
    
    async def run_comprehensive_test(self, tool_function: Callable,
                                   test_parameters: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Run comprehensive tests on a tool function.
        
        Args:
            tool_function: The MCP tool function to test
            test_parameters: Optional parameters for testing
            
        Returns:
            Comprehensive test results
        """
        comprehensive_result = {
            "function_name": tool_function.__name__,
            "overall_passed": True,
            "test_results": {},
            "summary": {}
        }
        
        # Run all test types
        tests = [
            self.test_tool_registration(tool_function),
            self.test_tool_execution(tool_function, test_parameters),
            self.test_error_handling(tool_function, test_parameters),
            self.test_parameter_validation(tool_function),
        ]
        
        results = await asyncio.gather(*tests, return_exceptions=True)
        
        passed_count = 0
        total_count = len(tests)
        
        for i, test_result in enumerate(results):
            if isinstance(test_result, Exception):
                test_name = f"test_{i}"
                comprehensive_result["test_results"][test_name] = {
                    "passed": False,
                    "errors": [str(test_result)]
                }
                comprehensive_result["overall_passed"] = False
            else:
                test_name = test_result["test_name"]
                comprehensive_result["test_results"][test_name] = test_result
                
                if test_result["passed"]:
                    passed_count += 1
                else:
                    comprehensive_result["overall_passed"] = False
        
        comprehensive_result["summary"] = {
            "total_tests": total_count,
            "passed_tests": passed_count,
            "failed_tests": total_count - passed_count,
            "success_rate": passed_count / total_count if total_count > 0 else 0
        }
        
        return comprehensive_result
    
    def generate_test_report(self, test_results: Dict[str, Any]) -> str:
        """Generate a human-readable test report."""
        report = []
        report.append(f"MCP Tool Test Report: {test_results['function_name']}")
        report.append("=" * 60)
        
        summary = test_results["summary"]
        overall_status = "✅ PASSED" if test_results["overall_passed"] else "❌ FAILED"
        report.append(f"Overall Status: {overall_status}")
        report.append(f"Tests: {summary['passed_tests']}/{summary['total_tests']} passed " +
                     f"({summary['success_rate']:.1%} success rate)")
        report.append("")
        
        for test_name, result in test_results["test_results"].items():
            status = "✅ PASSED" if result["passed"] else "❌ FAILED"
            report.append(f"{test_name}: {status}")
            
            if result.get("errors"):
                for error in result["errors"]:
                    report.append(f"  ❌ {error}")
            
            if result.get("details"):
                for key, value in result["details"].items():
                    if key not in ["traceback"]:  # Skip verbose details
                        report.append(f"  ℹ️ {key}: {value}")
            
            report.append("")
        
        return "\n".join(report)