import requests
from bs4 import BeautifulSoup
from PhDictionary import purifier


def get_definition(query='hello', number_of_examples=0):
    r = requests.get('https://www.collinsdictionary.com/dictionary/english/' + query.replace(' ', '-'),
                     headers={'User-agent': 'Mozilla/5.0'})
    return purifier.purify_definition(r.text, number_of_examples)


def get_french_english(query='bonsoir', number_of_examples=0, grammar_mark=False):
    r = requests.get('https://www.collinsdictionary.com/dictionary/french-english/' + str(query).replace(' ', '-'),
                     headers={'User-agent': 'Mozilla/5.0'})

    return purifier.purify_fr_eng(r.text, number_of_examples)


def get_synonym(query='hello', number_of_synonyms=1):
    r = requests.get('https://www.thesaurus.com/browse/' + query.replace(' ', '-'),
                     headers={'User-agent': 'Mozilla/5.0'})
    return purifier.purify_syn_eng(r.text, number_of_synonyms)


def get_eng_fr(query='bonsoir', number_of_examples=0, grammar_mark=False):
    r = requests.get('https://www.collinsdictionary.com/dictionary/english-french/' + str(query).replace(' ', '-'),
                     headers={'User-agent': 'Mozilla/5.0'})
    return purifier.purify_fr_eng(r.text, number_of_examples)
