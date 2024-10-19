#!/usr/bin/env python3
# type: ignore

import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# try:
#   donuts_per_guest = donuts / guests
# except ZeroDivisionError:
#   logging.exception("DonutCalculationError")

def lire(nom_fichier):
  logger.info(f'Reading file {nom_fichier}')
  f = open(nom_fichier, 'r')
  f_content = f.read()
  f.close()
  return f_content

def ecrire(nom_fichier, texte):
  logger.info(f'Writting file {nom_fichier}')
  f = open(nom_fichier, 'w')
  f.write(texte)
  
def minuscules(texte):
  return texte.lower()

# def shift_enc(plain_text, key):


# def shift_dec(cipher_text, key):


# def compter_lettres_minuscules(texte):


# def compter_lettres_majuscules(texte):


# def max_lettres(freq_lettres):


# def chaine_en_mots(texte):


# def compter_mots(mots):


# max_mot_1(freq_mots):


# def francais(texte):


# def break_shift(cipher_text):


# def lire_clef_subst(nom_fichier):


# def ecrire_clef_subst(nom_fichier, clef):


# def subst_enc(plain_text, key):


# def subst_dec_key(key):


# def subst_dec(cipher_text, key):


# def break_subst(cipher_text):


# def lire_clef_poly(nom_fichier):


# def ecrire_clef_poly(nom_fichier, clef):


# def poly_enc(plain_text, key):


# def poly_dec_key(key):


# def poly_dec(cipher_text, key):
