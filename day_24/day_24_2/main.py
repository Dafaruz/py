

name_2_replace = "[name]"
with open("./Input/Names/invited_names.txt") as names:

    for name in names:
        name = name.replace("\n", "")
        with open(f"./Output/ReadyToSend/letter for {name}.txt", mode="w") as n_file:
            with open("./Input/Letters/starting_letter.txt", mode="r") as file:
                content = file.read()
                content = content.replace(name_2_replace, name)
                n_file.write(content)
                