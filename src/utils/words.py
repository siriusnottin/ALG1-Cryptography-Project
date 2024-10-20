def chaine_en_mots(texte):
    return texte.split(' ')

def compter_mots(mots):
    words = mots
    words_freq = {word: 0 for word in words}
    for word in words:
        words_freq[word] += 1
    return words_freq

def max_mot_1(freq_mots):
    pass
