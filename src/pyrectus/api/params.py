from __future__ import annotations
from abc import ABC
from typing import Literal, TypedDict

from httpx import QueryParams

__all__ = ['Fields', 'Filter', 'Search', 'Sort', 'Limit', 'Offset', ]

FilterOp = Literal[
    '_eq',
    '_neq',
    '_lt',
    '_lte',
    '_gt',
    '_gte',
    '_in',
    '_nin',
    '_null',
    '_nnull',
    '_contains',
    '_ncontains',
    '_icontains',
    '_nicontains',
    '_starts_with',
    '_istarts_with',
    '_nstarts_with',
    '_nistarts_with',
    '_ends_with',
    '_iends_with',
    '_nends_with',
    '_niends_with',
    '_between',
    '_nbetween',
    '_empty',
    '_nempty',
    '_intersects',
    '_nintersects',
    '_intersects_bbox',
    '_nintersects_bbox',
    '_regex',
    '_some',
    '_none',
]

LogicOp = Literal['_and', '_or']

FieldFunctions = Literal['year', 'month', 'week', 'day', 'weekday', 'hour', 'minute', 'second', 'count']
AggregationFunc = Literal['count', 'countDistinct', 'sum', 'sumDistinct', 'avg', 'avgDistinct', 'min', 'max']

class DirectusParameter(ABC):
    def __call__(self) -> dict[str, str]: ...

class CurrentUser: ...

class CurrentRole: ...

class Now: ...

class Fields: ...

class Follow: ...

class Filter(DirectusParameter):
    def __init__(self, field: str, op: FilterOp):
        self.field = field
        self.op = op
    

class Search(DirectusParameter): ...

class Sort(DirectusParameter): ...

class Limit(DirectusParameter): ...

class Offset(DirectusParameter): ...

class Page(DirectusParameter): ...
    
class Aggregate(DirectusParameter):
    def __init__(self, func: AggregationFunc, *fields: Literal['*'] | str) -> None:
        self.func = func
        self.fields = fields
    
    def __call__(self) -> dict[str, str]:
        return {f'agregate[{self.func}]': ','.join(self.fields)}

class GroupBy(DirectusParameter): ...

class Deep(DirectusParameter): ...

class Alias(DirectusParameter): ...

class Export(DirectusParameter): ...

class Version(DirectusParameter): ...

class VersionRaw(DirectusParameter): ...

class Backlink(DirectusParameter): ...

class Meta(DirectusParameter): ...

# Root param object that compiles all built parameters
class Params(TypedDict, total=False):
    fields: Fields
    filter: Filter
    search: Search
    sort: Sort
    limit: Limit
    offset: Offset
    page: Page
    aggregate: Aggregate
    groupBy: GroupBy
    deep: Deep
    alias: Alias
    export: Export
    version: Version | VersionRaw
    backlink: Backlink
    

def parse_params(params: Params) -> QueryParams:
    qp = QueryParams()
    
    for _, v in params.items():
        v: DirectusParameter
        qp.update(v())
    
    return qp