from phdictionary.requestor import Requester
from phdictionary.file_manager import FileManager


# Definition block
# {
def get_definition(word, number_of_examples=0, grammar_mark=False):
    r = Requester()
    if grammar_mark == False and number_of_examples == 0:
        return r.get_definition_1(word, number_of_examples, grammar_mark)[1:2]
    elif grammar_mark == True and number_of_examples == 0:
        return r.get_definition_1(word, number_of_examples, grammar_mark)[:2]
    elif number_of_examples != 0 and grammar_mark == False:
        return r.get_definition_1(word, number_of_examples, grammar_mark)[1:]
    return r.get_definition_1(word, number_of_examples, grammar_mark)


# }

# Translation block
# {

def get_french_english(word, number_of_examples=0, grammar_mark=False):
    try:
        r = Requester()
        if grammar_mark == False and number_of_examples == 0:
            return r.get_french_english_q(word, number_of_examples, grammar_mark)[1:2]
        elif grammar_mark == True and number_of_examples == 0:
            return r.get_french_english_q(word, number_of_examples, grammar_mark)[:2]
        elif number_of_examples != 0 and grammar_mark == False:
            return r.get_french_english_q(word, number_of_examples, grammar_mark)[1:]
        return r.get_french_english_q(word, number_of_examples, grammar_mark)
    except:
        print('Try again, something went wrong. It might be spelling')


def get_english_french(word, number_of_examples=0, grammar_mark=False):
    try:
        r = Requester()
        if grammar_mark == False and number_of_examples == 0:
            return r.get_eng_fr(word, number_of_examples, grammar_mark)[1:2]
        elif grammar_mark == True and number_of_examples == 0:
            return r.get_eng_fr(word, number_of_examples, grammar_mark)[:2]
        elif number_of_examples != 0 and grammar_mark == False:
            return r.get_eng_fr(word, number_of_examples, grammar_mark)[1:]
        return r.get_eng_fr(word, number_of_examples, grammar_mark)
    except:
        print('Try again, something went wrong. It might be spelling')


def get_french_russian(word, number_of_examples=0, ):
    r = Requester()
    return r.get_glosbe(word, number_of_examples, 'fr-ru')


def get_russian_french(word, number_of_examples=0):
    r = Requester()
    return r.get_glosbe(word, number_of_examples, 'ru-fr')


def get_russian_english(word, number_of_examples=0):
    r = Requester()
    return r.get_glosbe(word, number_of_examples, 'ru-en')


def get_english_russian(word, number_of_examples=0):
    r = Requester()
    return r.get_glosbe(word, number_of_examples, 'en-ru')


# }
# Synonym block
# {
def get_synonym(word, number_of_syn=1):
    try:
        r = Requester()
        return r.get_synonym(word, number_of_syn)
    except:
        print('Try again, something went wrong. It might be spelling')


# }
# Files block
# {
def get_french_english_from_file(file, number_of_examples=0):
    f = FileManager()
    return f.txt_french_english(file, number_of_examples)


def get_synonyms_from_file(file, number_of_syn=1):
    f = FileManager()
    return f.syn_txt(file, number_of_syn)


def get_definition_from_file(file, number_of_examples=0):
    f = FileManager()
    return f.definition(file, number_of_examples)


def get_english_french_from_file(file, number_of_examples=0):
    f = FileManager()
    return f.txt_english_french(file, number_of_examples)
# }
