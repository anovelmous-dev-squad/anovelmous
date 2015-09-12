__author__ = 'Greg Ziegan'

from api.formatting import format_bigram

WORD = 'hey'
PUNCTUATION = '!'
QUOTATION = '"'

def test_word_then_punctuation():
    token1, token2 = format_bigram(WORD, PUNCTUATION)
    assert token1 == WORD + PUNCTUATION
    assert token2 is None

def test_word_then_quotation():
    token1, token2 = format_bigram(WORD, QUOTATION)
    assert token1 == WORD
    assert token2 == QUOTATION

def test_word_then_quotation_append():
    token1, token2 = format_bigram(WORD, QUOTATION, append_quotation=True)
    assert token1 == WORD + QUOTATION
    assert token2 is None

def test_quotation_then_word():
    token1, token2 = format_bigram(QUOTATION, WORD)
    assert token1 == QUOTATION + WORD.capitalize()
    assert token2 is None

def test_quotation_then_word_append():
    # Specifying True/False here should make no difference
    token1, token2 = format_bigram(QUOTATION, WORD, append_quotation=True)
    assert token1 == QUOTATION + WORD.capitalize()
    assert token2 is None
