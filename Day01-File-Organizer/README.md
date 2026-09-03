# CLI File Organizer

A Python command-line tool that automatically organizes files into categorized folders based on their file extensions.

## Features

- Organizes files recursively through subdirectories
- Flattens files into category folders in the selected directory
- Supports a wide range of file extensions
- Places unknown file types into an `Other` folder
- Prevents filename collisions by generating unique filenames
- Supports a `--dry-run` mode to preview changes without moving files
- Validates that the provided path exists and is a directory
- Uses command-line arguments through `argparse`

## Categories

Files are organized into categories such as:

- Images
- Videos
- Audio
- Documents
- Spreadsheets
- Presentations
- Archives
- Code
- Web
- Data
- Disk Images
- Programs
- 3D
- Subtitles
- Other

## Usage

Run the program by providing the directory you want to organize:

```bash
python organizer.py <directory>
```

For example:

```bash
python organizer.py Downloads
```

To preview what the program would do without moving any files:

```bash
python organizer.py Downloads --dry-run
```

## Technologies

- Python
- pathlib
- argparse
- Git / GitHub

## Project Purpose

This project was built as a practical Python exercise to learn filesystem manipulation, command-line interfaces, error handling, recursion, and writing a small utility from scratch.