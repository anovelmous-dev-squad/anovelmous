__author__ = 'Greg Ziegan'


def is_allowed_punctuation(symbol):
    return symbol in '!"$%&\'(),.:;?'


def get_formatted_previous_and_current_novel_tokens(previous_token, new_token, quote_punctuation_direction=None):

    if not previous_token:
        return None, new_token

    append_left = False
    if is_allowed_punctuation(new_token):
        if quote_punctuation_direction != 'RIGHT':
            append_left = True
    else:
        if previous_token == '"':
            append_left = True

    if append_left:
        return previous_token + new_token, None
    else:
        return previous_token[:], new_token[:]
