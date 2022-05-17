from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

from model.data_block import DataBlock


class MemoryService(ABC):
    
    @abstractmethod
    def create_data_block(self) -> None:
        pass
    
    @abstractmethod
    def write_data_into_block(self,file_content:str) -> List[DataBlock]:
        pass
    
    @abstractmethod
    def read_data_from_block(self,size:int,data_block:List[DataBlock]) -> str:
        pass
    
    @abstractmethod
    def delete_block(self,data_block:List[DataBlock]) -> None:
        pass
    
    @abstractmethod
    def update_block(self,data_block:List[DataBlock],prev_file_size:int,new_file_content:str) -> List[DataBlock]:
        pass
    


class ConcreteMemorySerice(MemoryService):
    '''
        pre-defined data related to memory and memory-segmentation
    '''
    block_size:int = 5 # size of each memory segment
    memory_size: int
    memory: List[str] 
    data_block:List[DataBlock]
    
    def __init__(self,memory_size:int) -> None:
        self.memory = List[None]*memory_size
        self.memory_size = memory_size
        self.data_block = List[DataBlock]
        self.create_data_block()
    
    def create_data_block(self) -> None:
        if self.memory_size == 0:
            raise RuntimeError('Invalid Memory Size Passed(0 value error)')
        else:
            no_of_blocks:int = self.memory_size // self.block_size
            # initialize the memory with data blocks of size block_size
            for i in range(no_of_blocks):
                pass
                
    