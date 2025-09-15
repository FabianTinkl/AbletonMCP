# MCP Tool Development Guidelines

This document provides comprehensive guidelines for developing MCP tools that follow the established patterns in the AbletonMCP project.

## Table of Contents

1. [Overview](#overview)
2. [Standard MCP Tool Pattern](#standard-mcp-tool-pattern)
3. [Tool Structure Requirements](#tool-structure-requirements)
4. [Handler-Based vs Direct Tools](#handler-based-vs-direct-tools)
5. [Parameter Validation](#parameter-validation)
6. [Error Handling](#error-handling)
7. [Testing Tools](#testing-tools)
8. [Common Patterns](#common-patterns)
9. [Examples](#examples)
10. [Validation and Testing](#validation-and-testing)

## Overview

MCP (Model Context Protocol) tools in this project follow specific patterns to ensure consistency, reliability, and maintainability. All tools must:

- Use the FastMCP framework with `@mcp.tool()` decorator
- Be async functions with `-> str` return type annotation
- Implement proper error handling
- Follow established initialization patterns
- Include comprehensive docstrings with Args sections

## Standard MCP Tool Pattern

Every MCP tool follows this basic structure:

```python
@mcp.tool()
async def tool_name(parameter: type, optional_param: Optional[type] = None) -> str:
    """Brief description of what the tool does.
    
    Args:
        parameter: Description of the parameter
        optional_param: Description of optional parameter
    """
    # Parameter validation (if needed)
    if validation_condition:
        return "Error: validation message"
    
    try:
        # Initialization check
        if not handlers:  # or ensure_initialized_async()
            return "Error: Server not initialized"
        
        # Main logic
        result = await handlers["handler_name"].method_name(parameters)
        
        # Result handling
        return result[0]["text"] if result and "text" in result[0] else "Default message"
        
    except Exception as e:
        return f"Error: {str(e)}"
```

## Tool Structure Requirements

### 1. Function Signature

```python
@mcp.tool()
async def function_name(param1: Type1, param2: Optional[Type2] = None) -> str:
```

**Requirements:**
- `@mcp.tool()` decorator (exactly this format)
- `async def` (all MCP tools must be async)
- Type hints for all parameters
- `-> str` return type annotation
- Optional parameters must use `Optional[Type]` and have default values

### 2. Docstring Format

```python
"""Brief one-line description of the tool's purpose.
    
Args:
    param1: Description of parameter including valid values/ranges
    param2: Description of optional parameter (default: value)
"""
```

**Requirements:**
- Brief description on the first line
- `Args:` section for functions with parameters
- Document parameter constraints and valid values
- Note default values for optional parameters

### 3. Parameter Validation

```python
# Validate enums/choices
if param not in ["choice1", "choice2", "choice3"]:
    return "Error: param must be one of: choice1, choice2, choice3"

# Validate ranges
if not min_val <= param <= max_val:
    return f"Error: param must be between {min_val} and {max_val}"

# Validate types (if not enforced by type hints)
if not isinstance(param, expected_type):
    return f"Error: param must be of type {expected_type}"
```

### 4. Initialization Check

Choose one pattern based on your tool type:

```python
# For handler-based tools
if not handlers:
    return "Error: Server not initialized"

# For direct ableton_tools access
await ensure_initialized_async()
if not ableton_tools:
    return "Error: Server initialization failed"
```

### 5. Error Handling

```python
try:
    # Main tool logic here
    result = await some_operation()
    return process_result(result)
except Exception as e:
    return f"Error: {str(e)}"
```

## Handler-Based vs Direct Tools

### Handler-Based Tools (Recommended)

Most tools should use handlers for better organization and separation of concerns:

```python
@mcp.tool()
async def create_track(track_type: str, name: Optional[str] = None) -> str:
    """Create a new track in Ableton Live.
    
    Args:
        track_type: Type of track to create (audio, midi, return)
        name: Optional name for the track
    """
    if track_type not in ["audio", "midi", "return"]:
        return "Error: track_type must be 'audio', 'midi', or 'return'"
        
    try:
        if not handlers:
            return "Error: Server not initialized"
        result = await handlers["track"].create_track(track_type, name)
        return result[0]["text"] if result and "text" in result[0] else f"Created {track_type} track"
    except Exception as e:
        return f"Error: {str(e)}"
```

### Direct Tools (For Simple Operations)

Simple operations can access ableton_tools directly:

```python
@mcp.tool()
async def ping() -> str:
    """Test connection to Ableton Live."""
    try:
        await ensure_initialized_async()
        if not ableton_tools:
            return "Error: Server initialization failed"
        result = await ableton_tools.ping()
        return result.get("message", "Ping completed")
    except Exception as e:
        return f"Error: {str(e)}"
```

## Parameter Validation

### Common Validation Patterns

```python
# BPM validation
if not 60 <= bpm <= 200:
    return "Error: BPM must be between 60 and 200"

# Genre validation
if genre not in ["techno", "industrial", "house", "minimal"]:
    return "Error: genre must be one of: techno, industrial, house, minimal"

# Length validation
if not 4 <= length <= 64:
    return "Error: length must be between 4 and 64 bars"

# Track type validation
if track_type not in ["audio", "midi", "return"]:
    return "Error: track_type must be 'audio', 'midi', or 'return'"

# Note density validation
if note_density not in ["sparse", "medium", "dense"]:
    return "Error: note_density must be 'sparse', 'medium', or 'dense'"
```

### Validation Best Practices

1. **Validate Early**: Check parameters before any async operations
2. **Clear Error Messages**: Use descriptive error messages with valid options
3. **Consistent Format**: All error messages start with "Error: "
4. **Document Constraints**: Include valid values/ranges in docstrings

## Error Handling

### Standard Error Handling Pattern

```python
try:
    # Initialization check
    if not handlers:
        return "Error: Server not initialized"
    
    # Main operation
    result = await handlers["handler"].method()
    
    # Success path
    return result[0]["text"] if result and "text" in result[0] else "Operation completed"
    
except Exception as e:
    return f"Error: {str(e)}"
```

### Error Handling Best Practices

1. **Wrap All Operations**: Use try-except around the entire tool logic
2. **Specific Initialization Errors**: Handle initialization failures specifically
3. **Consistent Error Format**: All errors return strings starting with "Error: "
4. **Preserve Stack Traces**: Use `str(e)` to include exception details
5. **No Re-raising**: Always return error strings, never re-raise exceptions

## Testing Tools

### Using the Validation Framework

```python
from mcp_server.validation import MCPToolValidator, MCPToolTestFramework

# Validate tool structure
validator = MCPToolValidator()
results = validator.validate_file("path/to/main.py")
print(validator.generate_report(results))

# Test tool functionality
tester = MCPToolTestFramework()
test_results = await tester.run_comprehensive_test(your_tool_function)
print(tester.generate_test_report(test_results))
```

## Common Patterns

### 1. Transport Controls

```python
@mcp.tool()
async def play() -> str:
    """Start playback in Ableton Live."""
    try:
        if not handlers:
            return "Error: Server not initialized"
        result = await handlers["transport"].play()
        return result[0]["text"] if result and "text" in result[0] else "Playback started"
    except Exception as e:
        return f"Error: {str(e)}"
```

### 2. Track Management

```python
@mcp.tool()
async def create_track(track_type: str, name: Optional[str] = None) -> str:
    """Create a new track in Ableton Live.
    
    Args:
        track_type: Type of track to create (audio, midi, return)
        name: Optional name for the track
    """
    if track_type not in ["audio", "midi", "return"]:
        return "Error: track_type must be 'audio', 'midi', or 'return'"
        
    try:
        if not handlers:
            return "Error: Server not initialized"
        result = await handlers["track"].create_track(track_type, name)
        return result[0]["text"] if result and "text" in result[0] else f"Created {track_type} track"
    except Exception as e:
        return f"Error: {str(e)}"
```

### 3. Music Generation

```python
@mcp.tool()
async def generate_chord_progression(key: str, genre: str, length: int = 8) -> str:
    """Generate a chord progression for a specific genre and key.
    
    Args:
        key: Musical key (e.g., 'C', 'Am', 'F#')
        genre: Genre style (techno, industrial, house, minimal)
        length: Number of bars for the progression (4-64)
    """
    if genre not in ["techno", "industrial", "house", "minimal"]:
        return "Error: genre must be one of: techno, industrial, house, minimal"
    
    if not 4 <= length <= 64:
        return "Error: length must be between 4 and 64 bars"
        
    try:
        if not handlers:
            return "Error: Server not initialized"
        result = await handlers["composition"].generate_chord_progression(key, genre, length)
        return result[0]["text"] if result and "text" in result[0] else f"Generated {length}-bar chord progression in {key} {genre}"
    except Exception as e:
        return f"Error: {str(e)}"
```

## Examples

### Simple Tool (No Parameters)

```python
@mcp.tool()
async def stop() -> str:
    """Stop playback in Ableton Live."""
    try:
        if not handlers:
            return "Error: Server not initialized"
        result = await handlers["transport"].stop()
        return result[0]["text"] if result and "text" in result[0] else "Playback stopped"
    except Exception as e:
        return f"Error: {str(e)}"
```

### Tool with Required Parameters

```python
@mcp.tool()
async def set_tempo(bpm: float) -> str:
    """Set the tempo (BPM) of the current Live set.
    
    Args:
        bpm: Tempo in beats per minute (60-200)
    """
    if not 60 <= bpm <= 200:
        return "Error: BPM must be between 60 and 200"
    
    try:
        if not handlers:
            return "Error: Server not initialized"
        result = await handlers["transport"].set_tempo(bpm)
        return result[0]["text"] if result and "text" in result[0] else f"Tempo set to {bpm} BPM"
    except Exception as e:
        return f"Error: {str(e)}"
```

### Tool with Optional Parameters

```python
@mcp.tool()
async def create_midi_clip(track_id: int, clip_slot: int, scale_name: str = "natural_minor", 
                          root_note: str = "A", length_bars: int = 4, genre: str = "techno") -> str:
    """Create a MIDI clip with scale constraints and music theory integration.
    
    Args:
        track_id: Target track index
        clip_slot: Clip slot index
        scale_name: Musical scale (default: natural_minor)
        root_note: Root note (default: A)
        length_bars: Clip length in bars (default: 4)
        genre: Genre for style (default: techno)
    """
    try:
        if not handlers:
            return "Error: Server not initialized"
        result = await handlers["midi"].create_midi_clip(
            track_id, clip_slot, scale_name, root_note, length_bars, genre
        )
        return result[0]["text"] if result and "text" in result[0] else f"Created MIDI clip in {root_note} {scale_name}"
    except Exception as e:
        return f"Error: {str(e)}"
```

## Validation and Testing

### Running Validation

```python
# Validate all tools in main.py
from mcp_server.validation import MCPToolValidator

validator = MCPToolValidator()
results = validator.validate_file("/path/to/mcp_server/main.py")
print(validator.generate_report(results))
```

### Running Tests

```python
# Test specific tool
from mcp_server.validation import MCPToolTestFramework
import asyncio

async def test_my_tool():
    tester = MCPToolTestFramework()
    results = await tester.run_comprehensive_test(play)  # your tool function
    print(tester.generate_test_report(results))

asyncio.run(test_my_tool())
```

### Continuous Integration

Add validation and testing to your development workflow:

```python
# In your test suite
def test_mcp_tools():
    validator = MCPToolValidator()
    results = validator.validate_file("mcp_server/main.py")
    assert results["valid"], f"MCP tools validation failed: {validator.generate_report(results)}"
```

## Common Pitfalls to Avoid

1. **Missing Decorator**: Always include `@mcp.tool()` decorator
2. **Wrong Return Type**: Must return `str`, not dictionaries or other types
3. **Sync Functions**: All MCP tools must be `async def`
4. **Missing Error Handling**: Always wrap main logic in try-except
5. **Inconsistent Error Format**: All errors should start with "Error: "
6. **No Initialization Check**: Always check if handlers/ableton_tools are available
7. **Missing Docstrings**: Document all functions, especially the Args section
8. **No Parameter Validation**: Validate parameters before processing
9. **Ignoring Type Hints**: Use proper type annotations for all parameters
10. **Complex Return Logic**: Keep result handling simple and consistent

## Summary

Following these guidelines ensures that all MCP tools in the project:

- Work reliably with the FastMCP framework
- Provide consistent user experience
- Handle errors gracefully
- Are easy to test and maintain
- Follow established project patterns

Use the validation and testing frameworks provided to verify that your tools meet these requirements before deploying them.