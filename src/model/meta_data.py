from dataclasses import dataclass
from typing import List
import uuid

from model.data_block import DataBlock

@dataclass
class MetaData:
    UUID:uuid
    file_name:str
    data_block: List[DataBlock]
    size:int
    