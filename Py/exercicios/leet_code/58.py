def lengthOfLastWord(frase):
    frase = frase.strip().split()
    
    last_word = frase[-1]
    #print(len(last_word))
    return len(last_word)


lengthOfLastWord("luffy is still joyboy")