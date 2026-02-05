from logic.normalizer import normalize


ALIASES = {

    "cristiano ronaldo": ["cr7", "cristiano", "ronaldo"],
    "lionel messi": ["messi", "leo", "lionel"],
    "neymar": ["neymar", "ney"],
    "kylian mbappe": ["mbappe", "kylian"],
    "erling haaland": ["haaland", "erling"]
}


def expand_aliases(correct_answer):

    correct_answer = normalize(correct_answer)

    if correct_answer in ALIASES:
        return [normalize(a) for a in ALIASES[correct_answer]]

    return [correct_answer]