from unittest.mock import MagicMock

import pytest

from automata.core.agent.tools.symbol_search import SymbolSearchTool
from automata.core.base.tool import Tool


@pytest.fixture
def symbol_search_tool_builder():
    symbol_search_mock = MagicMock()
    return SymbolSearchTool(symbol_search=symbol_search_mock)


def test_init(symbol_search_tool_builder):
    assert isinstance(symbol_search_tool_builder.symbol_search, MagicMock)


def test_build(symbol_search_tool_builder):
    tools = symbol_search_tool_builder.build()
    assert len(tools) == 4
    for tool in tools:
        assert isinstance(tool, Tool)


def test_symbol_rank_search(symbols, symbol_search_tool_builder):
    symbol_search_tool_builder.symbol_search.symbol_rank_search = MagicMock(
        return_value=[(symbols[0], 1)]
    )

    tools = symbol_search_tool_builder.build()
    for tool in tools:
        if tool.name == "symbol-rank-search":
            assert tool.func(("module.path", "symbol")) == symbols[0]


def test_symbol_references(symbol_search_tool_builder):
    symbol_search_tool_builder.symbol_search.symbol_references = MagicMock(
        # TODO - replace with real symbol ref if that remains return type in the manager
        return_value={"ref": "Found references"}
    )

    tools = symbol_search_tool_builder.build()
    for tool in tools:
        if tool.name == "symbol-references":
            assert tool.func(("module.path", "symbol")) == "ref:Found references"


def test_retrieve_source_code_by_symbol(symbol_search_tool_builder):
    symbol_search_tool_builder.symbol_search.retrieve_source_code_by_symbol = MagicMock(
        return_value="Source code"
    )

    tools = symbol_search_tool_builder.build()
    for tool in tools:
        if tool.name == "retrieve-source-code-by-symbol":
            assert tool.func(("module.path", "symbol")) == "Source code"


def test_exact_search(symbol_search_tool_builder):
    symbol_search_tool_builder.symbol_search.exact_search = MagicMock(
        return_value={"symbol": "Exact match found"}
    )

    tools = symbol_search_tool_builder.build()
    for tool in tools:
        if tool.name == "exact-search":
            assert tool.func(("module.path", "pattern")) == "symbol:Exact match found"


def test_process_query(symbol_search_tool_builder):
    symbol_search_tool_builder.symbol_search.process_query = MagicMock(
        return_value="Processed query"
    )

    tools = symbol_search_tool_builder.build()
    for tool in tools:
        if tool.name == "process-query":
            assert tool.func(("module.path", "query")) == "Processed query"
