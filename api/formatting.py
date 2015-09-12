__author__ = 'Greg Ziegan'


def is_allowed_punctuation(symbol):
    return symbol in '!"$%&\'(),.:;?'


def format_bigram(token1, token2, append_quotation=False):
    if not token1:
        return None, token2

    append, capitalize = False, False
    if token2 == '\"':
        if append_quotation:
            append = True
    elif token1 in '.?!\"' and not is_allowed_punctuation(token2):
        capitalize = True
        append = True
    elif is_allowed_punctuation(token2):
        append = True

    formatted_token1, formatted_token2 = None, None
    if capitalize:
        token2 = token2.capitalize()

    if append:
        formatted_token1 = token1 + token2
    else:
        formatted_token1, formatted_token2 = token1[:], token2[:]

    return formatted_token1, formatted_token2
