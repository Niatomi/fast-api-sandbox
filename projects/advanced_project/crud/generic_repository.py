from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')

class GenericCrud(Generic[T]):
    
    @abstractmethod
    def create(T):
        pass
    
    @abstractmethod
    def read(T):
        pass
    
    @abstractmethod
    def update(T):
        pass
    
    @abstractmethod
    def delete(T):
        pass