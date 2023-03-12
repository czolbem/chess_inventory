from enum import Enum


class RequiredPgnHeaders(Enum):
    EVENT = 'Event'
    SITE = 'Site'
    DATE = 'Date'
    ROUND = 'Round'
    WHITE = 'White'
    BLACK = 'Black'
    RESULT = 'Result'
