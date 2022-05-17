from abc import ABC, abstractmethod
from typing import List

from model.data_block import DataBlock


class FileService(ABC):
    '''
        abstract method that creates a file into memory
        @args:
            file_name: str
            file_content: str
        @return type:
            List[BlockData]
    '''
    @abstractmethod
    def create(self,file_name:str,file_content:str) -> List[DataBlock]: 
        pass

    '''
        abstract method that reads the file content from memory
        @args:
            data_blocks: List[DataBlock]
            size: int
        @return type:
            str
    '''
    @abstractmethod
    def read(self,data_blocks:List[DataBlock],size:int) -> str:
        pass