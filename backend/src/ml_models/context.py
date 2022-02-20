from __future__ import annotations

import pathlib
from typing import Any, Dict, Optional

import onnxruntime

_CONTEXT: Optional[Context] = None
_ONNX_PATH = str(pathlib.Path(__file__).parent / "data/mnist.onnx")


class Attributes:
    def __init__(self, attributes_dict: Dict[str, Any]) -> None:
        self._attributes_dict = attributes_dict

    def __getitem__(self, attribute_id) -> Any:
        rv = self._get_attribute(attribute_id=attribute_id)
        return rv

    def __getattr__(self, attribute_id) -> Any:
        rv = self._get_attribute(attribute_id=attribute_id)
        return rv

    def _get_attribute(self, attribute_id: str) -> Any:
        attribute = self._attributes_dict.get(attribute_id, None)
        if attribute is None:
            err_msg = f"Invalid attribute: {attribute_id}, options are: {self.list()}"
            raise AttributeError(err_msg)
        return attribute

    def get(self, attribute_id: str, default=None) -> Any:
        try:
            rv = self._get_attribute(attribute_id=attribute_id)
        except AttributeError:
            rv = default
        return rv

    def list(self):
        rv = self._attributes_dict.keys()
        return rv


class Context:
    def __init__(self, resources: Attributes) -> None:
        self.resources = resources


def configure_context():
    global _CONTEXT

    mnist_model = _ONNX_PATH
    mnist_session = onnxruntime.InferenceSession(mnist_model, None)

    attributes_dict = {
        "mnist": mnist_session,
    }

    resources = Attributes(attributes_dict=attributes_dict)
    context = Context(resources=resources)

    _CONTEXT = context


def get_context() -> Context:
    if _CONTEXT is None:
        raise ValueError("Context has not been initialised")
    return _CONTEXT
