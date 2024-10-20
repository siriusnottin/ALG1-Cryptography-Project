def chaine_en_lettres(texte):
    return list(texte)

def compter_lettres(lettres):
    letters = lettres
    letters_freq = {letter: 0 for letter in letters}
    for letter in letters:
        letters_freq[letter] += 1
    return letters_freq

def max_lettre_1(freq_lettres):
    pass
