from pathlib import Path
import argparse
import sys

def get_folder():
      parser = argparse.ArgumentParser()
      parser.add_argument("directory")
      parser.add_argument("--dry-run", action="store_true")
      args = parser.parse_args()
      return Path(args.directory), args.dry_run

def validate_folder(folder):
     if not folder.exists():
          sys.exit("No such folder found.")
     if not folder.is_dir():
          sys.exit("The given path is not that of a directory")

def get_unique_path(item,item_target):
            count=1
            new_path = item_target / item.name
            while new_path.exists():                       
                    new_item_name = item.stem + "_" + str(count) + item.suffix
                    count += 1
                    new_path= item_target / new_item_name
            return new_path
def organize_folder(folder, dry_run):
        categories = {
    # Images
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".webp": "Images",
    ".svg": "Images",
    ".ico": "Images",
    ".tif": "Images",
    ".tiff": "Images",
    ".heic": "Images",
    ".heif": "Images",
    ".raw": "Images",
    ".cr2": "Images",
    ".nef": "Images",
    ".arw": "Images",

    # Videos
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",
    ".wmv": "Videos",
    ".flv": "Videos",
    ".webm": "Videos",
    ".m4v": "Videos",
    ".mpeg": "Videos",
    ".mpg": "Videos",
    ".3gp": "Videos",

    # Audio
    ".mp3": "Audio",
    ".wav": "Audio",
    ".flac": "Audio",
    ".aac": "Audio",
    ".ogg": "Audio",
    ".wma": "Audio",
    ".m4a": "Audio",
    ".opus": "Audio",
    ".aiff": "Audio",

    # Documents
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".odt": "Documents",
    ".rtf": "Documents",
    ".txt": "Documents",
    ".tex": "Documents",

    # Spreadsheets
    ".xls": "Spreadsheets",
    ".xlsx": "Spreadsheets",
    ".csv": "Spreadsheets",
    ".ods": "Spreadsheets",
    ".tsv": "Spreadsheets",

    # Presentations
    ".ppt": "Presentations",
    ".pptx": "Presentations",
    ".odp": "Presentations",
    ".key": "Presentations",

    # Archives / compressed files
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",
    ".bz2": "Archives",
    ".xz": "Archives",
    ".tar.gz": "Archives",
    ".tar.bz2": "Archives",
    ".tar.xz": "Archives",
    # Source code / programming
    ".py": "Code",
    ".js": "Code",
    ".ts": "Code",
    ".jsx": "Code",
    ".tsx": "Code",
    ".java": "Code",
    ".c": "Code",
    ".cpp": "Code",
    ".h": "Code",
    ".hpp": "Code",
    ".cs": "Code",
    ".go": "Code",
    ".rs": "Code",
    ".rb": "Code",
    ".php": "Code",
    ".swift": "Code",
    ".kt": "Code",
    ".kts": "Code",
    ".scala": "Code",
    ".hs": "Code",
    ".fs": "Code",
    ".fsx": "Code",
    ".lua": "Code",
    ".r": "Code",
    ".sql": "Code",
    ".sh": "Code",
    ".bat": "Code",
    ".ps1": "Code",
    # Web
    ".html": "Web",
    ".htm": "Web",
    ".css": "Web",
    ".scss": "Web",
    ".sass": "Web",
    ".less": "Web",
    # Data / configuration
    ".json": "Data",
    ".xml": "Data",
    ".yaml": "Data",
    ".yml": "Data",
    ".toml": "Data",
    ".ini": "Data",
    ".cfg": "Data",
    ".conf": "Data",
    ".log": "Data",
    # Disk images
    ".iso": "Disk Images",
    ".img": "Disk Images",
    ".dmg": "Disk Images",
    ".vhd": "Disk Images",
    ".vhdx": "Disk Images",
    # Executables / installers
    ".exe": "Programs",
    ".msi": "Programs",
    ".app": "Programs",
    ".apk": "Programs",
    ".deb": "Programs",
    ".rpm": "Programs",
    # 3D / CAD
    ".obj": "3D",
    ".fbx": "3D",
    ".stl": "3D",
    ".blend": "3D",
    ".dae": "3D",
    ".3ds": "3D",
    # Subtitles
    ".sub": "Subtitles",
}
        destination_folders = set(categories.values()) | {"Other"}
        for item in folder.rglob("*"):
                    if item.parent.name in destination_folders:
                           continue
                    if item.is_file():
                        category = categories.get(item.suffix,"Other")
                        item_target = folder / category
                        new_path= get_unique_path(item,item_target)
                        if dry_run:
                                print(f"{item.name}  ->   {new_path}")
                        else:
                            item_target.mkdir(exist_ok=True)
                            item.move(new_path)   
                                    

folder,dry_run = get_folder()
validate_folder(folder)
organize_folder(folder,dry_run)








