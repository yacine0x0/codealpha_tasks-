import os
import shutil

source = input("Source folder: ").strip() or "source_images"
dest = input("Destination folder: ").strip() or "jpg_archive"

if not os.path.isdir(source):
    print(f"Error: '{source}' is not a valid directory.")
    exit(1)

os.makedirs(dest, exist_ok=True)

moved = 0
for filename in os.listdir(source):
    if filename.lower().endswith(".jpg"):
        src_path = os.path.join(source, filename)
        if os.path.isfile(src_path):
            shutil.move(src_path, os.path.join(dest, filename))
            print(f"Moved: {filename}")
            moved += 1

print(f"\nDone. {moved} .jpg file(s) moved to '{dest}'.")
