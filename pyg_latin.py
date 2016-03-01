def pyg_latin():
    words = input("Input Sentence:").lower().split()
    for word in words:
        first = word[0]
        if (first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u' or first == 'A' or first == 'E' or first == 'I' or first == 'O' or first == 'U'):
            print(word[1:] + "s" + "ay", end = " ")
        else:
            print(word[1:] + word[0] + "ay", end = " ")
    print ()

pyg_latin()