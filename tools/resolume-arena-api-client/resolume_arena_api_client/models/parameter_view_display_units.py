from enum import Enum


class ParameterViewDisplayUnits(str, Enum):
    BEATS = "beats"
    DECIBELS = "decibels"
    DEGREES = "degrees"
    FRACTIONS = "fractions"
    FRAMES_PER_SECOND = "frames_per_second"
    INTEGER = "integer"
    MILLISECONDS = "milliseconds"
    PERCENT = "percent"
    REAL = "real"
    SECONDS = "seconds"

    def __str__(self) -> str:
        return str(self.value)
