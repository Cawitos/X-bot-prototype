from collections import Counter


def filter_multiple_comments(comments):
    """
    Descalifica por completo a los usuarios que comentaron más de una vez
    en el hilo, sin importar si alguno de esos comentarios tiene la
    respuesta correcta. Útil cuando la dinámica prohíbe comentar 2 veces.
    """
    counter = Counter(c.username for c in comments)
    disqualified = {username for username, count in counter.items() if count > 1}

    filtered = [c for c in comments if c.username not in disqualified]

    return filtered, disqualified