import builtins
from conjure_python_client import ConjureBeanType, ConjureDecoder, ConjureEncoder, ConjureFieldDefinition, Service
from typing import Any, Dict, List

class SimpleNestedService(Service):

    def test_endpoint(self, string):
        # type: (str) -> str

        _headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        } # type: Dict[str, Any]

        _params = {
        } # type: Dict[str, Any]

        _path_params = {
        } # type: Dict[str, Any]

        _json = ConjureEncoder().default(string) # type: Any

        _path = '/catalog/testEndpoint'
        _path = _path.format(**_path_params)

        _response = self._request( # type: ignore
            'POST',
            self._uri + _path,
            params=_params,
            headers=_headers,
            json=_json)

        _decoder = ConjureDecoder()
        return _decoder.decode(_response.json(), str)

class SimpleObject(ConjureBeanType):

    @builtins.classmethod
    def _fields(cls):
        # type: () -> Dict[str, ConjureFieldDefinition]
        return {
            'string': ConjureFieldDefinition('string', str)
        }

    __slots__ = ['_string'] # type: List[str]

    def __init__(self, string):
        # type: (str) -> None
        self._string = string

    @builtins.property
    def string(self):
        # type: () -> str
        return self._string

