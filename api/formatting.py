__author__ = 'Greg Ziegan'


def is_allowed_punctuation(symbol):
    return symbol in '!"$%&\'(),.:;?'


def get_formatted_previous_and_current_novel_tokens(previous_token, new_token, quote_punctuation_direction=None):

    if not previous_token:
        return None, new_token

    append_left = False
    capitalize = False
    if is_allowed_punctuation(new_token):
        if quote_punctuation_direction != 'RIGHT':
            append_left = True
    else:
        if previous_token == '"':
            append_left = True

        if previous_token in '.?!\"':
            capitalize = True

    updated_previous_token, updated_new_token = None, None
    if append_left:
        updated_previous_token = previous_token + new_token
    else:
        updated_previous_token, updated_new_token = previous_token[:], new_token[:]

    if capitalize:
        updated_new_token = updated_new_token.capitalize()

    return updated_previous_token, updated_new_token