#!/usr/bin/env python3
"""
MCP Tool Template Generator Script

This script generates templates for new MCP tools following established patterns.

Usage:
    python generate_template.py --name my_tool --handler transport --method my_method
    python generate_template.py --name ping_live --direct
    python generate_template.py --examples
"""

import argparse
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from mcp_server.validation import MCPToolTemplateGenerator
from mcp_server.validation.template_generator import ParameterInfo


def main():
    parser = argparse.ArgumentParser(description="Generate MCP tool templates")
    parser.add_argument(
        "--name", "-n",
        required=False,
        help="Name of the tool function"
    )
    parser.add_argument(
        "--description", "-d",
        help="Description of what the tool does"
    )
    parser.add_argument(
        "--handler",
        help="Handler name (transport, track, composition, etc.)"
    )
    parser.add_argument(
        "--method", "-m",
        help="Handler method name"
    )
    parser.add_argument(
        "--direct",
        action="store_true",
        help="Generate direct ableton_tools template"
    )
    parser.add_argument(
        "--examples",
        action="store_true",
        help="Show example templates"
    )
    parser.add_argument(
        "--parameters",
        help="Parameters in format: name:type:description,name:type:default:description"
    )
    
    args = parser.parse_args()
    
    generator = MCPToolTemplateGenerator()
    
    if args.examples:
        show_examples(generator)
        return
    
    if not args.name:
        parser.error("Tool name is required (use --name)")
    
    if not args.description:
        args.description = f"{args.name.replace('_', ' ').title()}"
    
    # Parse parameters
    parameters = []
    if args.parameters:
        param_specs = args.parameters.split(',')
        for spec in param_specs:
            parts = spec.split(':')
            if len(parts) < 3:
                print(f"Warning: Invalid parameter spec '{spec}', expected 'name:type:description' or 'name:type:default:description'")
                continue
            
            name = parts[0].strip()
            type_hint = parts[1].strip()
            
            if len(parts) == 3:
                # name:type:description
                description = parts[2].strip()
                default = None
            else:
                # name:type:default:description
                default = parts[2].strip()
                description = parts[3].strip()
            
            parameters.append(ParameterInfo(
                name=name,
                type_hint=type_hint,
                default=default,
                description=description
            ))
    
    # Generate template
    if args.direct:
        template = generator.generate_direct_tool_template(
            args.name,
            args.description,
            parameters
        )
    elif args.handler and args.method:
        template = generator.generate_handler_tool_template(
            args.name,
            args.description,
            args.handler,
            args.method,
            parameters
        )
    else:
        print("Error: Either --direct or both --handler and --method must be specified")
        sys.exit(1)
    
    print(f"# Generated MCP Tool Template: {args.name}")
    print("# Copy this into your main.py file")
    print()
    print(template)


def show_examples(generator):
    """Show example templates."""
    examples = generator.generate_example_tools()
    
    print("MCP Tool Template Examples")
    print("=" * 50)
    
    for example_name, template in examples.items():
        print(f"\n## Example: {example_name.replace('_', ' ').title()}")
        print("-" * 40)
        print(template)
        print()
    
    print("Common Parameter Templates:")
    print("-" * 30)
    common_params = generator.get_common_parameter_templates()
    for param_name, param_info in common_params.items():
        print(f"{param_name}: {param_info.type_hint} - {param_info.description}")
        if param_info.default:
            print(f"  Default: {param_info.default}")
        if param_info.validation:
            print(f"  Validation: {param_info.validation}")
        print()


if __name__ == "__main__":
    main()