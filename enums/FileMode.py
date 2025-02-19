from enum import Enum


class FileMode(Enum):
    r = "r"
    w = "w"
    r += "r+"
