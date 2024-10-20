# ALG1 : Projet Cryptographie

## Fichiers

chiffrés et déchiffrés, et les clefs :

1. Les_Miserables_decalage.txt
2. shift_plain_text.txt
3. key_subst.txt
4. Les_Miserables_substitution.txt 5. key_subst_2.txt
6. Les_Miserables_substitution_2.txt 7. subst_plain_text.txt
8. double_key.txt
9. Les_Miserables_polyalphabet.txt
10. key_poly.txt

Le but de ce projet est de mettre en place un chiffrement par décalage et de le casser, puis un chiffrement par substitution monoalphabétique et de le casser, et finalement mettre en place un chiffrement par substitution polyalphabétique.

Pour tous les chiffrements, le texte d’origine non chiffré est appelé texte clair ou plain text en anglais. Le texte chiffré est appelé texte chiffré ou cipher text en anglais. Par convention, on affichera toujours le texte clair en minuscules et le texte chiffré en majuscules.

## Chiffrement par décalage

Le chiffrement par décalage consiste en un décalage de l’alphabet. Si on considère une clef qui vaut 3, ce qui équivaut au chiffrement de César, alors le chiffré de chaque lettre sera la 3ème lettre à sa droite. La Table 1 montre la correspondance entre les lettres claires et les lettres chiffrées suivant le chiffrement de César. La Table 2 montre la correspondance pour le déchiffrement de César.

| a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C |

[^1]: Table 1: Chiffrement César.

| A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| x | y | z | a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w |

[^2]: Table 2: Déchiffrement César.

