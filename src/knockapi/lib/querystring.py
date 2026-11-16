from __future__ import annotations

from typing import List, Tuple, Mapping
from typing_extensions import override

from .._qs import Params, Querystring
from .._types import NotGiven, ArrayFormat, NestedFormat, not_given


class KnockQuerystring(Querystring):
    @override
    def stringify_items(
        self,
        params: Params,
        *,
        array_format: ArrayFormat | NotGiven = not_given,
        nested_format: NestedFormat | NotGiven = not_given,
    ) -> List[Tuple[str, str]]:
        # Provider options are literal dotted query names in Knock's API.
        # Explicit dotted options (including pagination cursors) take precedence.
        query_options = params.get("query_options")
        if isinstance(query_options, Mapping):
            params = {
                **{
                    f"query_options.{key}": value
                    for key, value in query_options.items()
                },
                **{
                    key: value
                    for key, value in params.items()
                    if key != "query_options"
                },
            }
        return super().stringify_items(
            params, array_format=array_format, nested_format=nested_format
        )
