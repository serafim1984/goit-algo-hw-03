import argparse
import shutil
from pathlib import Path

def parse_argv():
    parser = argparse.ArgumentParser('Sorting of files')
    parser.add_argument("-S", "--sourse", type = Path, required = True, help = "Initial folder")
    parser.add_argument('-O', '--output', type = Path, default = Path('output'), help = 'Sorted folder')
    
    return parser.parse_args()

def recursive_copy(src: Path, dst: Path):
    for item in src.iterdir():
        if item.is_dir():
            recursive_copy(item, dst)

        else:
            folder = dst / item.suffix

            try:
                folder.mkdir(exist_ok = True, parents = True)
            except FileExistsError:
                # Handle the case where the directory already exists (if needed)
                pass
            except PermissionError as e:
                print(f"Permission error creating directory: {e}")
                # Handle the error or exit gracefully
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                # Handle the error or exit gracefully

            try:
                shutil.copy2(item, folder)
            except shutil.Error as e:
                print(f"Error copying file: {e}")
            # Handle the error or skip the file
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
            # Handle the error or exit gracefully

def main():
    try:
        args = parse_argv()
    except argparse.ArgumentError as e:
        print(f'Error parsing command-line arguments: {e}')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    print(f'Entry arguments: {args}')
    recursive_copy(args.sourse, args.output)

if __name__ == '__main__':
    main()

