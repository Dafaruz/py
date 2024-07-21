
##########################################
#          list of alphabet             #
##########################################
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction=""

##########################################
#          encryption function           #
##########################################

def enctypt(text ,shift):
    text_list=list(text)
    for position_in_text in range(len(text)):
        alphabet_shifted=alphabet.index(text_list[position_in_text])

        alphabet_shifted+=shift
        if alphabet_shifted> len(alphabet):                  # loop for encode
                alphabet_shifted-=len(alphabet)
        elif alphabet_shifted<(-1*len(alphabet)):            # loop for decode
            alphabet_shifted+=len(alphabet)

        text_list[position_in_text]=alphabet[alphabet_shifted]           # asing to the list
    scramble_word=''.join(text_list)                                     # convert list to string

    if shift>0:
        print("your enc word is: \n")
        print(scramble_word)
    else:
        print("your decrip word is: \n")
        print(scramble_word)

#######################################################
#  if statement to understand what user want to do   #
#######################################################
while direction!="exit":                               # a loop for the user interfance
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction=='encrypt':
        enctypt(text ,shift)

    if direction=="decode":
        enctypt(text ,(-1*shift))

#################################################################################################
