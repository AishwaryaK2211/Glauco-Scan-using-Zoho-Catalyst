import os
from app.interfaces.storage_interface import IStorage

class LocalStorage(IStorage):
    def __init__(self, base_dir: str = "./storage"):
        self.base_dir = base_dir
        os.makedirs(self.base_dir, exist_ok=True)
        os.makedirs(os.path.join(self.base_dir, "uploads"), exist_ok=True)
        os.makedirs(os.path.join(self.base_dir, "heatmaps"), exist_ok=True)
        os.makedirs(os.path.join(self.base_dir, "reports"), exist_ok=True)

    def save_file(self, filename: str, content: bytes, folder: str = "uploads") -> str:
        filepath = os.path.join(self.base_dir, folder, filename)
        with open(filepath, "wb") as f:
            f.write(content)
        return filepath

    def get_file(self, filepath: str) -> bytes:
        with open(filepath, "rb") as f:
            return f.read()

    def delete_file(self, filepath: str) -> bool:
        if os.path.exists(filepath):
            os.remove(filepath)
            return True
        return False
