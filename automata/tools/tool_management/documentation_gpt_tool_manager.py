from typing import List

from automata.core.base.tool import Tool
from automata.tools.documentation_tools.documentation_gpt import DocumentationGPT
from automata.tools.tool_management.base_tool_manager import BaseToolManager


class DocumentationGPTToolManager(BaseToolManager):
    def __init__(self, **kwargs):
        """Initializes a DocumentationGPTToolManager object with the given inputs."""
        self.documentation_gpt: DocumentationGPT = kwargs.get("documentation_gpt")

    def build_tools(self) -> List[Tool]:
        """Initializes a DocumentationGPTToolManager object with the given inputs."""
        tools = [
            Tool(
                name="doc-gpt-lookup",
                func=lambda input_str: self._documentation_gpt_lookup(input_str),
                description="Vector search over the specified API documentation.",
                return_direct=False,
            ),
        ]
        return tools

    def build_tools_with_automata(self) -> List[Tool]:
        """Not implemented."""
        raise NotImplementedError

    def _documentation_gpt_lookup(self, input_text):
        """Lookup the documentation for the given input text."""
        result = self.documentation_gpt.run(input_text)
        return result
