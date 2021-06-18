from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
print(BASE_DIR2)
