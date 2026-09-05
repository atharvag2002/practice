
import os

def get_file_size(file_path):
    size = os.path.getsize(file_path)
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"


def main():
    # Example usage - would need actual file path
    print("This function returns file size in human-readable format")
    print("Usage: get_file_size('path/to/file')")


if __name__ == "__main__":
    main()
