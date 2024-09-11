import os
import shutil

# Define the file extensions for each category
FILE_CATEGORIES = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".tiff"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov", ".wmv"],
    "Music": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "Archives": [".zip", ".tar", ".gz", ".7z", ".rar"],
    "Programs": [".exe", ".msi", ".sh", ".bat", ".jar", ".py"],
    "Others": []  # Files that don't match any category
}


# Function to create folders for each category if they don't exist
def create_folders(directory):
    for category in FILE_CATEGORIES:
        category_folder = os.path.join(directory, category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)


# Function to sort files
def sort_files(directory):
    create_folders(directory)  # Create category folders if they don't exist

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        _, extension = os.path.splitext(filename)

        # Move file to its corresponding folder
        moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if extension.lower() in extensions:
                category_folder = os.path.join(directory, category)
                shutil.move(file_path, os.path.join(category_folder, filename))
                print(f"Moved {filename} to {category}")
                moved = True
                break

        # If the file doesn't match any category, move it to the "Others" folder
        if not moved:
            others_folder = os.path.join(directory, "Others")
            shutil.move(file_path, os.path.join(others_folder, filename))
            print(f"Moved {filename} to Others")


# Main function
if __name__ == "__main__":
    # Enter the directory you want to sort
    target_directory = input("Enter the path to the directory you want to sort: ")

    # Verify the directory exists
    if os.path.exists(target_directory):
        sort_files(target_directory)
        print("File sorting completed!")
    else:
        print(f"The directory {target_directory} does not exist.")
