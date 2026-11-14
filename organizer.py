# File Organizer - Task 3
# I made this to clean my messy folder
# It puts each file into a separate folder based on its type

import os
import shutil

print("=== Automated File Organizer ===")
print("")

# Ask the user which folder to clean
folder = input("Which folder do you want to clean? Enter full path (Press Enter to use Test_Folder): ")

if folder == "":
    folder = "Test_Folder"

# If the folder does not exist, show a message
if not os.path.exists(folder):
    print("Folder not found:", folder)
    print("First create Test_Folder and put some files in it.")
else:
    # This tells which file will go into which folder
    file_types = {
        ".pdf": "Documents",
        ".docx": "Documents",
        ".txt": "Documents",
        ".xlsx": "Documents",
        ".jpg": "Images",
        ".jpeg": "Images",
        ".png": "Images",
        ".mp4": "Videos",
        ".mkv": "Videos",
        ".mp3": "Music",
        ".zip": "Archives",
        ".rar": "Archives",
        ".py": "Code",
        ".js": "Code",
        ".html": "Code"
    }

    moved = 0
    skipped = 0

    # Look at everything inside the folder
    files = os.scandir(folder)

    for item in files:
        # Only pick files, leave folders alone
        if item.is_file():
            name = item.name
            # Get the last part of the file, like .pdf .jpg
            _, ext = os.path.splitext(name)
            ext = ext.lower()

            # If we know this type, make its folder
            if ext in file_types:
                category = file_types[ext]
                new_folder = os.path.join(folder, category)

                # If the folder is not created yet, create it
                if not os.path.exists(new_folder):
                    os.mkdir(new_folder)
                    print(f"New folder created: {category}")

                old_path = os.path.join(folder, name)
                new_path = os.path.join(new_folder, name)

                # If a file with this name already exists, change the name
                try:
                    # Move the file into the new folder
                    if os.path.exists(new_path):
                        # Add (1) to the name so the old one is not deleted
                        base, extension = os.path.splitext(name)
                        name = base + " (1)" + extension
                        new_path = os.path.join(new_folder, name)

                    shutil.move(old_path, new_path)
                    print(f"Moved: {item.name} -> {category}/")
                    moved = moved + 1

                except PermissionError:
                    print(f"Permission denied, skipped: {name}")
                    skipped = skipped + 1

                except FileExistsError:
                    print(f"Already exists: {name}")
                    skipped = skipped + 1

                except Exception as e:
                    print(f"Problem in {name}: {e}")
                    skipped = skipped + 1
            else:
                print(f"Skipped, unknown file type: {name}")
                skipped = skipped + 1

    print("")
    print("--- Summary ---")
    print("Total files moved:", moved)
    print("Total files skipped:", skipped)
    print("Done! Folder is clean.")