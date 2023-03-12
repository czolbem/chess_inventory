from enum import Enum


class RequiredPgnHeaders(Enum):
    EVENT = 'Event'
    SITE = 'Site'
    DATE = 'Date'
    ROUND = 'Round'
    WHITE = 'White'
    BLACK = 'Black'
    RESULT = 'Result'


class OpeningPgnHeaders(Enum):
    ECO = 'ECO'
    OPENING = 'Opening'
    VARIATION = 'Variation'
    ECOT = 'ECOT'
    OPENINGT = 'OpeningT'
    VARIATIONT = 'VariationT'
