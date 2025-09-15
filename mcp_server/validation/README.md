# MCP Tool Validation Framework

This directory contains a comprehensive validation and testing framework for MCP tools in the AbletonMCP project. It ensures all tools follow established patterns and work correctly.

## Overview

The validation framework provides:

- **Code Pattern Validation**: Ensures tools follow the established MCP tool patterns
- **Template Generation**: Generates new tool templates following best practices
- **Functional Testing**: Tests tool execution, error handling, and parameter validation
- **Documentation**: Comprehensive guidelines for MCP tool development

## Components

### Core Modules

- `validator.py` - Code pattern validation engine
- `template_generator.py` - Template generation for new tools
- `testing_framework.py` - Functional testing framework
- `MCP_TOOL_GUIDELINES.md` - Comprehensive development guidelines

### Scripts

- `validate_tools.py` - Validate tool patterns in source files
- `test_tools.py` - Run functional tests on tools
- `generate_template.py` - Generate new tool templates
- `run_validation_suite.py` - Complete validation suite

## Quick Start

### Validate Existing Tools

```bash
# Validate all tools in main.py
python mcp_server/validation/validate_tools.py

# Validate with verbose output
python mcp_server/validation/validate_tools.py --verbose

# Validate specific file
python mcp_server/validation/validate_tools.py --file path/to/file.py
```

### Test Tool Functionality

```bash
# Test all tools
python mcp_server/validation/test_tools.py

# Test specific tool
python mcp_server/validation/test_tools.py --tool play

# Verbose testing output
python mcp_server/validation/test_tools.py --verbose
```

### Generate New Tool Templates

```bash
# Show examples
python mcp_server/validation/generate_template.py --examples

# Generate handler-based tool
python mcp_server/validation/generate_template.py \
  --name create_effect_rack \
  --description "Create an effect rack on a track" \
  --handler track \
  --method create_effect_rack \
  --parameters "track_id:int:Target track index"

# Generate direct tool
python mcp_server/validation/generate_template.py \
  --name get_live_version \
  --description "Get Ableton Live version" \
  --direct
```

### Run Complete Validation Suite

```bash
# Complete validation (recommended for CI/CD)
python mcp_server/validation/run_validation_suite.py

# Quick validation (skip functional tests)
python mcp_server/validation/run_validation_suite.py --quick

# CI mode (exit on first failure)
python mcp_server/validation/run_validation_suite.py --ci
```

## Usage Examples

### Validating Tools During Development

```python
from mcp_server.validation import MCPToolValidator

# Validate your tools
validator = MCPToolValidator()
results = validator.validate_file("mcp_server/main.py")

if results["valid"]:
    print("✅ All tools are valid!")
else:
    print("❌ Validation failed:")
    print(validator.generate_report(results))
```

### Testing Tool Functionality

```python
import asyncio
from mcp_server.validation import MCPToolTestFramework

async def test_my_tools():
    tester = MCPToolTestFramework()
    
    # Test specific tool
    from mcp_server.main import play
    results = await tester.run_comprehensive_test(play)
    
    if results["overall_passed"]:
        print("✅ Tool passed all tests!")
    else:
        print("❌ Tool failed tests:")
        print(tester.generate_test_report(results))

asyncio.run(test_my_tools())
```

### Generating New Tools

```python
from mcp_server.validation import MCPToolTemplateGenerator
from mcp_server.validation.template_generator import ParameterInfo

generator = MCPToolTemplateGenerator()

# Generate a handler-based tool
template = generator.generate_handler_tool_template(
    name="mute_track",
    description="Mute or unmute a track",
    handler_name="track",
    handler_method="set_mute",
    parameters=[
        ParameterInfo("track_id", "int", description="Target track index"),
        ParameterInfo("muted", "bool", description="True to mute, False to unmute")
    ]
)

print(template)
```

## Integration with Development Workflow

### Pre-commit Hook

Add to `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: local
    hooks:
      - id: validate-mcp-tools
        name: Validate MCP Tools
        entry: python mcp_server/validation/run_validation_suite.py --ci
        language: python
        files: ^mcp_server/main\.py$
```

### CI/CD Pipeline

Add to your CI configuration:

```yaml
# GitHub Actions example
- name: Validate MCP Tools
  run: |
    python mcp_server/validation/run_validation_suite.py --ci
```

### Testing in pytest

```python
# In your test_mcp_tools.py
import pytest
from mcp_server.validation import MCPToolValidator

def test_mcp_tool_validation():
    validator = MCPToolValidator()
    results = validator.validate_file("mcp_server/main.py")
    
    assert results["valid"], f"MCP tools validation failed:\n{validator.generate_report(results)}"

@pytest.mark.asyncio
async def test_mcp_tool_functionality():
    from mcp_server.validation import MCPToolTestFramework
    from mcp_server.main import play, stop, set_tempo
    
    tester = MCPToolTestFramework()
    
    for tool in [play, stop, set_tempo]:
        results = await tester.run_comprehensive_test(tool)
        assert results["overall_passed"], f"Tool {tool.__name__} failed tests"
```

## Validation Rules

The validator checks for:

### Required Patterns
- `@mcp.tool()` decorator
- `async def` function declaration
- `-> str` return type annotation
- Proper error handling with try-except
- Initialization checks (`if not handlers:` or `ensure_initialized_async()`)
- Consistent error message format

### Best Practices
- Comprehensive docstrings with Args sections
- Type hints for all parameters
- Parameter validation with clear error messages
- Consistent result handling patterns

### Common Issues Detected
- Missing decorators or incorrect decorator format
- Sync functions (should be async)
- Missing error handling
- Inconsistent error message format
- Missing or incomplete docstrings
- No parameter validation
- Incorrect return types

## Tool Templates

The template generator provides several patterns:

### Simple Handler Tool
```python
@mcp.tool()
async def tool_name(param: str) -> str:
    """Tool description.
    
    Args:
        param: Parameter description
    """
    try:
        if not handlers:
            return "Error: Server not initialized"
        result = await handlers["handler_name"].method_name(param)
        return result[0]["text"] if result and "text" in result[0] else "Operation completed"
    except Exception as e:
        return f"Error: {str(e)}"
```

### Direct Tool
```python
@mcp.tool()
async def tool_name() -> str:
    """Tool description."""
    try:
        await ensure_initialized_async()
        if not ableton_tools:
            return "Error: Server initialization failed"
        result = await ableton_tools.method_name()
        return result.get("message", "Operation completed")
    except Exception as e:
        return f"Error: {str(e)}"
```

### Tool with Validation
```python
@mcp.tool()
async def tool_name(param: str, value: int) -> str:
    """Tool description.
    
    Args:
        param: Parameter description
        value: Value between 1 and 100
    """
    if param not in ["option1", "option2"]:
        return "Error: param must be 'option1' or 'option2'"
    
    if not 1 <= value <= 100:
        return "Error: value must be between 1 and 100"
    
    try:
        if not handlers:
            return "Error: Server not initialized"
        result = await handlers["handler_name"].method_name(param, value)
        return result[0]["text"] if result and "text" in result[0] else "Operation completed"
    except Exception as e:
        return f"Error: {str(e)}"
```

## Contributing

When adding new validation rules or test cases:

1. Update the `MCPToolValidator` class with new validation logic
2. Add corresponding test cases in `MCPToolTestFramework`
3. Update the guidelines in `MCP_TOOL_GUIDELINES.md`
4. Test your changes with the validation suite
5. Update examples and templates as needed

## Troubleshooting

### Common Issues

**Import Errors**: Make sure you're running scripts from the project root directory.

**Module Not Found**: Ensure the project root is in your Python path.

**Test Failures**: Check that mock objects in `testing_framework.py` match your tool's expectations.

**Validation Errors**: Review `MCP_TOOL_GUIDELINES.md` for required patterns.

### Getting Help

1. Check the guidelines: `MCP_TOOL_GUIDELINES.md`
2. Run validation with `--verbose` for detailed information
3. Look at existing tools in `main.py` for examples
4. Generate templates with `generate_template.py --examples`

## License

This validation framework is part of the AbletonMCP project and follows the same license terms.