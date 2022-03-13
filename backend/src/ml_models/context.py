from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Optional

import onnxruntime

_CONTEXT: Optional[Context] = None


class Attributes:
    def __init__(self, attributes_dict: Dict[str, Any]) -> None:
        self._attributes_dict = attributes_dict

    def get(self, attribute_id: str) -> Any:
        rv = self._get_attribute(attribute_id=attribute_id)
        return rv

    def _get_attribute(self, attribute_id: str) -> Any:
        attribute = self._attributes_dict.get(attribute_id, None)
        if attribute is None:
            err_msg = f"Invalid attribute: {attribute_id}, available attributes: {list(self._attributes_dict.keys())}"
            raise AttributeError(err_msg)
        return attribute


class Context:
    def __init__(self, clients: Attributes) -> None:
        self.clients = clients


def configure_context(root_path: Path, mnist_onnx_path: Path):
    global _CONTEXT

    mnist_path = str(root_path / mnist_onnx_path)
    mnist_session = onnxruntime.InferenceSession(mnist_path, None)

    client_dict = {
        "mnist": mnist_session,
    }

    client_attributes = Attributes(attributes_dict=client_dict)
    context = Context(clients=client_attributes)

    _CONTEXT = context


def get_context() -> Context:
    if _CONTEXT is None:
        raise ValueError("Context has not been initialised")
    return _CONTEXT
