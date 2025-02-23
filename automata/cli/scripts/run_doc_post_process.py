import logging
import os

from automata.config.config_types import ConfigCategory
from automata.core.coding.py_coding.writer import PyDocWriter
from automata.core.database.vector import JSONVectorDatabase
from automata.core.utils import config_fpath, root_py_fpath

logger = logging.getLogger(__name__)


def main(*args, **kwargs) -> str:
    """
    Update the symbol code embedding based on the specified SCIP index file.
    """
    doc_writer = PyDocWriter(root_py_fpath())

    embedding_path = os.path.join(
        config_fpath(), ConfigCategory.SYMBOL.value, "symbol_doc_embedding_l2.json"
    )

    embedding_db = JSONVectorDatabase(embedding_path)

    symbols = embedding_db.get_all_symbols()

    docs = {symbol: embedding_db.get(symbol) for symbol in symbols}

    doc_writer.write_documentation(docs, symbols, os.path.join(root_py_fpath(), "docs"))  # type: ignore
    return "Success"
