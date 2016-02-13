def codeword(phrase):
    result = ("")
    for letter in phrase:
        if letter.isupper() == True:
            result = result + letter
    print(result)
codeword("How are you? Eh, ok. Low or Lower? Ohhh.")

