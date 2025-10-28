import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s')

project_name = "congress_vote_analysis"

# --- folder + file definitions ---
file_list = [

    # ───── Root level ─────
    ".gitignore",
    "README.md",
    "requirements.txt",
    "setup.py",
    "config/config.ini",

    # ───── Source code ─────
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/database/__init__.py",
    f"src/{project_name}/database/mysql_connection.py",
    f"src/{project_name}/database/migrations/__init__.py",
    f"src/{project_name}/database/migrations/create_tables.sql",

    f"src/{project_name}/etl/__init__.py",
    f"src/{project_name}/etl/bill_fetcher.py",
    f"src/{project_name}/etl/vote_fetcher.py",
    f"src/{project_name}/etl/bill_vote_merger.py",

    f"src/{project_name}/nlp/__init__.py",
    f"src/{project_name}/nlp/preprocess.py",
    f"src/{project_name}/nlp/tokenizer.py",

    f"src/{project_name}/ml/__init__.py",
    f"src/{project_name}/ml/train_model.py",
    f"src/{project_name}/ml/predict.py",

    # ───── Data folders ─────
    "data/raw/.gitkeep",
    "data/processed/.gitkeep",
    "data/mysql/.gitkeep",

    # ───── Notebooks ─────
    "notebooks/eda.ipynb",
    "notebooks/model_dev.ipynb",

    # ───── Logging ─────
    "logs/.gitkeep"
]

def create_project_structure():
    for filepath in file_list:
        filepath = Path(filepath)
        file_dir = filepath.parent

        if not file_dir.exists():
            logging.info(f"Creating directory: {file_dir}")
            file_dir.mkdir(parents=True, exist_ok=True)

        if not filepath.exists():
            logging.info(f"Creating file: {filepath}")
            with open(filepath, 'w') as f:
                pass  # creates empty file

    logging.info("✅ Project structure created successfully.")


if __name__ == "__main__":
    create_project_structure()
