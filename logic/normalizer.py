import unicodedata
import re


def normalize(text):

    text = text.lower().strip()

    # eliminar tildes
    text = ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )

    # eliminar emojis y símbolos raros
    text = re.sub(r'[^\w\s]', '', text)

    return text