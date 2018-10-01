from nose.tools import *
from ex48 import parser


def test_peek():
    assert_equal(parser.peek([]), None)
    assert_equal(parser.peek([('direction', 'north')]), 'direction')


def test_match():
    assert_equal(parser.match([], 'what is that'), None)
    assert_equal(parser.match([('oh', 'run'), ('direction', 'up')], 'oh'),
                 ('oh', 'run'))
    assert_equal(parser.match([('aiyo', 'aiya'), ('direction', 'up')], 'verb'),
                 None)


def test_skip():
    raw_word_list = [('oh', 'run'), ('oh', 'go'), ('direction', 'up')]
    parser.skip(raw_word_list, 'oh')
    assert_equal(raw_word_list, [('direction', 'up')])


def test_parse_verb():
    raw_word_list = [('stop', 'run'), ('verb', 'go'), ('direction', 'up')]
    assert_equal(parser.parse_verb(raw_word_list), ('verb', 'go'))

    expected_error_message = "Expected a verb next."
    error_word_list = [('stop', 'run'), ('oh', 'go'), ('direction', 'up')]
    with assert_raises(parser.ParserError) as error:
        assert_equal(parser.parse_verb(error_word_list), ('oh', 'go'))
    assert_equal(error.exception.message, expected_error_message)


def test_parse_object():
    raw_word_list = [('noun', 'gogo'), ('direction', 'up')]
    assert_equal(parser.parse_object(raw_word_list), ('noun', 'gogo'))

    expected_error_message = "Expected a noun or direction next."
    error_word_list = [('oh', 'go'), ('direction', 'up')]
    with assert_raises(parser.ParserError) as error:
        assert_equal(parser.parse_object(error_word_list), ('oh', 'go'))
    assert_equal(error.exception.message, expected_error_message)


def test_parse_subject():
    raw_word_list = [('stop', 'run'), ('noun', 'gogo'), ('direction', 'up')]
    assert_equal(parser.parse_subject(raw_word_list), ('noun', 'gogo'))

    player_word_list = [('verb', 'run'), ('noun', 'gogo'), ('direction', 'up')]
    assert_equal(parser.parse_subject(player_word_list), ('noun', 'player'))

    expected_error_message = "Expected a verb next."
    error_word_list = [('stop', 'run'), ('oh', 'go'), ('direction', 'up')]
    with assert_raises(parser.ParserError) as error:
        assert_equal(parser.parse_subject(error_word_list), ('oh', 'go'))
    assert_equal(error.exception.message, expected_error_message)


def test_parse_sentence():
    input_x = [('verb', 'run'), ('direction', 'up')]
    sentence_x = parser.parse_sentence(input_x)
    assert_equal(sentence_x.subject, 'player')
    assert_equal(sentence_x.verb, 'run')
    assert_equal(sentence_x.object, 'up')

    input_xx = [('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'honey')]
    sentence_xx = parser.parse_sentence(input_xx)
    assert_equal(sentence_xx.subject, 'bear')
    assert_equal(sentence_xx.verb, 'eat')
    assert_equal(sentence_xx.object, 'honey')
