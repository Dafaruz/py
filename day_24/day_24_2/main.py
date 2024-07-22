import  os

# Define the path to the file
file_path = "./Output/ReadyToSend/letter for"

# Check if the file exists
if os.path.exists(file_path):
    # Try to delete the file
    try:
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
    except OSError as e:
        print(f"Error: {e.strerror}")
else:
    print(f"File '{file_path}' does not exist.")

name_2_replace = "[name]"
with open("./Input/Names/invited_names.txt") as names:

    for name in names:
        name = name.replace("\n", "")
        with open(f"./Output/ReadyToSend/letter for {name}.txt", mode="w") as n_file:
            with open("./Input/Letters/starting_letter.txt", mode="r") as file:
                content = file.read()
                content = content.replace(name_2_replace, name)
                n_file.write(content)
                