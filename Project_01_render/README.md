# ALG1 Project_01

## Description

Authors: Alexandre, Sirius

## Project Structure

```
Text Files:
- Les_Miserables.txt
- Les_Miserables_decalage.txt
- double_key.txt
- fichier_clé_poly.txt
- key_shift.txt
- key_subst_2.txt
- shift_cipher_text.txt
- shift_plan_text.txt

Markdown File:
- README.md

PDF File:
- Rapport.pdf

Python Script:
- crypto.py

Requirements File:
- requirements.txt

```

## More info

Tried to setup a better structure for the project, with a more modular approach.
And with some testing, but it's not working and complete yet.

Link to the updated repo: [ALG1-Cryptography-Project](https://github.com/siriusnottin/ALG1-Cryptography-Project/tree/dev)

And since Git and I have a love-hate relationship, here's a link to a commit with the actual tests: [commit](https://github.com/siriusnottin/ALG1-Cryptography-Project/commit/470ce7604dbbec7b0ef0c474c70310e9d3a9b453#diff-dd72c48ca0bd1801ba8f0d11f73481cfa3b51beaa7d802ac8fb19ee414254d35)

## Development

### Requirements

- Python 3.12.7
- Pip
- Pyenv

### Setup

```bash
# setup virtualenv using pyenv
pyenv virtualenv 3.12.7 alg1
pyenv activate alg1

# install dependencies
pip install -r requirements.txt
```

### Running

```bash
python crypto.py
```
