from abc import ABC, abstractmethod
from typing import BinaryIO

class IStorage(ABC):
    @abstractmethod
    def save_file(self, filename: str, content: bytes) -> str:
        """Saves a file and returns its path or URL"""
        pass

    @abstractmethod
    def get_file(self, filename: str) -> bytes:
        """Retrieves a file's binary content"""
        pass

    @abstractmethod
    def delete_file(self, filename: str) -> bool:
        """Deletes a file"""
        pass
