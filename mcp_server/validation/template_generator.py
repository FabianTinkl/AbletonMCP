"""
MCP Tool Template Generator

Generates code templates for new MCP tools following established patterns.
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass


@dataclass
class ParameterInfo:
    """Information about a function parameter."""
    name: str
    type_hint: str
    default: Optional[str] = None
    description: str = ""
    validation: Optional[str] = None


@dataclass
class ToolTemplate:
    """Template for generating MCP tool functions."""
    name: str
    description: str
    parameters: List[ParameterInfo]
    handler_name: Optional[str] = None
    handler_method: Optional[str] = None
    use_lazy_init: bool = False
    additional_validation: List[str] = None


class MCPToolTemplateGenerator:
    """Generates MCP tool function templates."""
    
    def __init__(self):
        """Initialize the template generator."""
        self.base_template = '''@mcp.tool()
async def {function_name}({parameters}) -> str:
    """{description}
    
    Args:
{parameter_docs}
    """
{validation_code}
    try:
{initialization_check}
{main_logic}
{result_handling}
    except Exception as e:
        return f"Error: {{str(e)}}"'''

        self.parameter_template = "{name}: {type_hint}{default}"
        self.doc_template = "        {name}: {description}"
        
    def generate_tool(self, template: ToolTemplate) -> str:
        """
        Generate a complete MCP tool function from template.
        
        Args:
            template: The tool template configuration
            
        Returns:
            Generated function source code
        """
        # Generate parameter list
        parameters = self._generate_parameters(template.parameters)
        
        # Generate parameter documentation
        parameter_docs = self._generate_parameter_docs(template.parameters)
        
        # Generate validation code
        validation_code = self._generate_validation_code(template)
        
        # Generate initialization check
        initialization_check = self._generate_initialization_check(template)
        
        # Generate main logic
        main_logic = self._generate_main_logic(template)
        
        # Generate result handling
        result_handling = self._generate_result_handling(template)
        
        return self.base_template.format(
            function_name=template.name,
            description=template.description,
            parameters=parameters,
            parameter_docs=parameter_docs,
            validation_code=validation_code,
            initialization_check=initialization_check,
            main_logic=main_logic,
            result_handling=result_handling
        )
    
    def _generate_parameters(self, parameters: List[ParameterInfo]) -> str:
        """Generate the parameter list for the function signature."""
        param_strs = []
        for param in parameters:
            default_str = f" = {param.default}" if param.default is not None else ""
            param_str = self.parameter_template.format(
                name=param.name,
                type_hint=param.type_hint,
                default=default_str
            )
            param_strs.append(param_str)
        
        return ", ".join(param_strs)
    
    def _generate_parameter_docs(self, parameters: List[ParameterInfo]) -> str:
        """Generate the Args section of the docstring."""
        if not parameters:
            return "        (No parameters)"
            
        docs = []
        for param in parameters:
            doc_str = self.doc_template.format(
                name=param.name,
                description=param.description
            )
            docs.append(doc_str)
        
        return "\n".join(docs)
    
    def _generate_validation_code(self, template: ToolTemplate) -> str:
        """Generate parameter validation code."""
        if not template.additional_validation:
            return ""
        
        validation_lines = []
        for validation in template.additional_validation:
            validation_lines.append(f"    {validation}")
        
        return "\n".join(validation_lines) + "\n"
    
    def _generate_initialization_check(self, template: ToolTemplate) -> str:
        """Generate initialization check code."""
        if template.use_lazy_init:
            return '''        await ensure_initialized_async()
        if not ableton_tools:
            return "Error: Server initialization failed"'''
        else:
            return '''        if not handlers:
            return "Error: Server not initialized"'''
    
    def _generate_main_logic(self, template: ToolTemplate) -> str:
        """Generate the main logic for the tool."""
        if template.handler_name and template.handler_method:
            # Generate handler-based logic
            param_names = [p.name for p in template.parameters]
            param_args = ", ".join(param_names)
            
            return f'''        result = await handlers["{template.handler_name}"].{template.handler_method}({param_args})'''
        else:
            # Generate direct ableton_tools logic
            param_names = [p.name for p in template.parameters]
            param_args = ", ".join(param_names)
            method_name = template.name  # Assume method matches function name
            
            return f'''        result = await ableton_tools.{method_name}({param_args})
        return result.get("message", "{template.description} completed")'''
    
    def _generate_result_handling(self, template: ToolTemplate) -> str:
        """Generate result handling code."""
        if template.handler_name:
            return '''        return result[0]["text"] if result and "text" in result[0] else f"{} completed"'''.format(template.description)
        else:
            return ""  # Handled in main logic for direct tools
    
    def generate_handler_tool_template(self, name: str, description: str, 
                                     handler_name: str, handler_method: str,
                                     parameters: List[ParameterInfo] = None,
                                     validation: List[str] = None) -> str:
        """
        Generate a template for a handler-based tool.
        
        Args:
            name: Function name
            description: Tool description
            handler_name: Name of the handler to use
            handler_method: Method to call on the handler
            parameters: List of parameters
            validation: Additional validation rules
            
        Returns:
            Generated function source code
        """
        template = ToolTemplate(
            name=name,
            description=description,
            parameters=parameters or [],
            handler_name=handler_name,
            handler_method=handler_method,
            use_lazy_init=False,
            additional_validation=validation
        )
        
        return self.generate_tool(template)
    
    def generate_direct_tool_template(self, name: str, description: str,
                                    parameters: List[ParameterInfo] = None,
                                    validation: List[str] = None) -> str:
        """
        Generate a template for a direct ableton_tools tool.
        
        Args:
            name: Function name
            description: Tool description
            parameters: List of parameters
            validation: Additional validation rules
            
        Returns:
            Generated function source code
        """
        template = ToolTemplate(
            name=name,
            description=description,
            parameters=parameters or [],
            handler_name=None,
            handler_method=None,
            use_lazy_init=True,
            additional_validation=validation
        )
        
        return self.generate_tool(template)
    
    def get_common_parameter_templates(self) -> Dict[str, ParameterInfo]:
        """Get commonly used parameter templates."""
        return {
            "track_id": ParameterInfo(
                name="track_id",
                type_hint="int",
                description="Target track index"
            ),
            "clip_slot": ParameterInfo(
                name="clip_slot",
                type_hint="int", 
                description="Clip slot index"
            ),
            "bpm": ParameterInfo(
                name="bpm",
                type_hint="float",
                description="Tempo in beats per minute (60-200)",
                validation="if not 60 <= bpm <= 200:\n        return \"Error: BPM must be between 60 and 200\""
            ),
            "track_type": ParameterInfo(
                name="track_type",
                type_hint="str",
                description="Type of track to create (audio, midi, return)",
                validation='if track_type not in ["audio", "midi", "return"]:\n        return "Error: track_type must be \'audio\', \'midi\', or \'return\'"'
            ),
            "name": ParameterInfo(
                name="name",
                type_hint="Optional[str]",
                default="None",
                description="Optional name"
            ),
            "key": ParameterInfo(
                name="key",
                type_hint="str",
                description="Musical key (e.g., 'C', 'Am', 'F#')"
            ),
            "genre": ParameterInfo(
                name="genre", 
                type_hint="str",
                description="Genre style (techno, industrial, house, minimal)",
                validation='if genre not in ["techno", "industrial", "house", "minimal"]:\n        return "Error: genre must be one of: techno, industrial, house, minimal"'
            ),
            "length": ParameterInfo(
                name="length",
                type_hint="int",
                default="4",
                description="Length in bars (4-64)",
                validation="if not 4 <= length <= 64:\n        return \"Error: length must be between 4 and 64 bars\""
            ),
        }
    
    def generate_example_tools(self) -> Dict[str, str]:
        """Generate example tools showing different patterns."""
        common_params = self.get_common_parameter_templates()
        examples = {}
        
        # Example 1: Simple transport tool (direct)
        examples["simple_direct"] = self.generate_direct_tool_template(
            name="record",
            description="Start recording in Ableton Live",
            parameters=[],
        )
        
        # Example 2: Handler-based tool with validation
        examples["handler_with_validation"] = self.generate_handler_tool_template(
            name="create_audio_track",
            description="Create a new audio track",
            handler_name="track",
            handler_method="create_track", 
            parameters=[
                ParameterInfo("track_type", "str", default='"audio"', description="Type of track (audio)"),
                common_params["name"]
            ]
        )
        
        # Example 3: Complex tool with multiple parameters and validation
        examples["complex_tool"] = self.generate_handler_tool_template(
            name="generate_bass_line",
            description="Generate a bass line with specific characteristics",
            handler_name="composition",
            handler_method="generate_bass_line",
            parameters=[
                common_params["key"],
                common_params["genre"],
                common_params["length"],
                ParameterInfo("note_density", "str", default='"medium"', 
                            description="Note density (sparse, medium, dense)",
                            validation='if note_density not in ["sparse", "medium", "dense"]:\n        return "Error: note_density must be \'sparse\', \'medium\', or \'dense\'"'),
            ],
            validation=[
                'if genre not in ["techno", "industrial", "house", "minimal"]:',
                '    return "Error: genre must be one of: techno, industrial, house, minimal"',
                'if not 4 <= length <= 64:',
                '    return "Error: length must be between 4 and 64 bars"',
                'if note_density not in ["sparse", "medium", "dense"]:',
                '    return "Error: note_density must be \'sparse\', \'medium\', or \'dense\'"'
            ]
        )
        
        return examples