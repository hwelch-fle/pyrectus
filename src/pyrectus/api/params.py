from __future__ import annotations
from typing import Literal, TypedDict

from httpx import QueryParams

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

class CurrentUser: ...

class CurrentRole: ...

class Now: ...

class Fields: ...

class Follow: ...

class Filter:
    def __init__(self, field: str, op: FilterOp):
        self.field = field
        self.op = op
    

class Search: ...

class Sort: ...

class Limit: ...

class Offset: ...

class Page: ...

class Aggregate:
    def __init__(self, func: AggregationFunc, *fields: Literal['*'] | str) -> None:
        self.func = func
        self.fields = fields
    
    def __str__(self) -> str:
        return f'agregate[{self.func}]={",".join(self.fields)}'

class GroupBy: ...

class Deep: ...

class Alias: ...

class Export: ...

class Version: ...

class VersionRaw: ...



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
    backlink: bool
    

def parse_params(params: Params) -> QueryParams: ...