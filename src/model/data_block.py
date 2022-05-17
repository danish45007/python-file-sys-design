from dataclasses import dataclass


@dataclass
class DataBlock:
    start: int
    is_occupied:bool