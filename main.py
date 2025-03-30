import asyncio
import aiofiles
import aiofiles.os
import aiofiles.ospath
import shutil
import argparse
import logging
from pathlib import Path
from typing import List
import os

# Configure error logging
logging.basicConfig(filename='file_sorter_errors.log',
                    level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')


async def read_folder(source: Path) -> List[Path]:
    """Recursively collect all file paths in the source directory."""
    files = []
    loop = asyncio.get_event_loop()
    try:
        entries = await loop.run_in_executor(None, lambda: list(os.scandir(source)))
        for entry in entries:
            path = source / entry.name
            if entry.is_dir():
                files.extend(await read_folder(path))
            elif entry.is_file():
                files.append(path)
    except Exception as e:
        logging.error(f"Failed to read folder {source}: {e}")
    return files


async def copy_file(file_path: Path, dest: Path):
    """Copy file to destination subfolder based on its extension."""
    try:
        ext = file_path.suffix[1:] or "no_extension"
        dest_folder = dest / ext
        await aiofiles.os.makedirs(dest_folder, exist_ok=True)
        dest_path = dest_folder / file_path.name

        # Use thread pool for blocking IO operation
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, shutil.copy2, file_path, dest_path)
    except Exception as e:
        logging.error(f"Failed to copy {file_path} to {dest_folder}: {e}")


async def main(source: Path, dest: Path):
    all_files = await read_folder(source)
    tasks = [copy_file(file_path, dest) for file_path in all_files]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Asynchronously sort files by extension.")
    parser.add_argument("source", type=str, help="Source folder path")
    parser.add_argument("destination", type=str, help="Destination folder path")
    args = parser.parse_args()

    source_path = Path(args.source).resolve()
    dest_path = Path(args.destination).resolve()

    asyncio.run(main(source_path, dest_path))
