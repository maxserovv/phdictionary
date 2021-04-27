from phdictionary.requestor import *
from phdictionary.file_manager import *


def get_definition(word, number_of_examples=0, grammar_mark=False):
    try:
        if grammar_mark == False and number_of_examples == 0:
            return get_definition_1(word, number_of_examples, grammar_mark)[1:2]
        elif grammar_mark == True and number_of_examples == 0:
            return get_definition_1(word, number_of_examples, grammar_mark)[:2]
        elif number_of_examples != 0 and grammar_mark == False:
            return get_definition_1(word, number_of_examples, grammar_mark)[1:]
        return get_definition_1(word, number_of_examples, grammar_mark)
    except:
        print('Try again, something went wrong. It might be spelling')

def get_french_english(word, number_of_examples=0, grammar_mark=False):
    try:
        if grammar_mark == False and number_of_examples == 0:
            return get_french_english_q(word, number_of_examples, grammar_mark)[1:2]
        elif grammar_mark == True and number_of_examples == 0:
            return get_french_english_q(word, number_of_examples, grammar_mark)[:2]
        elif number_of_examples != 0 and grammar_mark == False:
            return get_french_english_q(word, number_of_examples, grammar_mark)[1:]
        return get_french_english_q(word, number_of_examples, grammar_mark)
    except:
        print('Try again, something went wrong. It might be spelling')

def get_syn(word, number_of_syn=1):
    try:
        return get_synonym(word, number_of_syn)
    except:
        print('Try again, something went wrong. It might be spelling')

def get_french_english_from_file(file, number_of_examples=0):
    return txt_french_english(file, number_of_examples)

def get_syn_from_file(file, number_of_syn=1):
    return syn_txt(file, number_of_syn)

def get_english_french(word, number_of_examples=0, grammar_mark=False):
    try:
        if grammar_mark == False and number_of_examples == 0:
            return get_eng_fr(word, number_of_examples, grammar_mark)[1:2]
        elif grammar_mark == True and number_of_examples == 0:
            return get_eng_fr(word, number_of_examples, grammar_mark)[:2]
        elif number_of_examples != 0 and grammar_mark == False:
            return get_eng_fr(word, number_of_examples, grammar_mark)[1:]
        return get_eng_fr(word, number_of_examples, grammar_mark)
    except:
        print('Try again, something went wrong. It might be spelling')

def get_definition_from_file(file, number_of_examples=0):
    return definition(file, number_of_examples)
