import requests
from bs4 import BeautifulSoup
from phdictionary.purifier import Purifier


class Requester:

    def get_definition_1(self, query='hello', number_of_examples=0, grammar_mark=False):
        r = requests.get('https://www.collinsdictionary.com/dictionary/english/' + query.replace(' ', '-'),
                         headers={'User-agent': 'Mozilla/5.0'})
        p = Purifier()
        return p.purify_definition(r.text, number_of_examples)

    def get_french_english_q(self, query='bonsoir', number_of_examples=0, grammar_mark=False):
        r = requests.get('https://www.collinsdictionary.com/dictionary/french-english/' + str(query).replace(' ', '-'),
                         headers={'User-agent': 'Mozilla/5.0'})
        p = Purifier()
        return p.purify_fr_eng(r.text, number_of_examples)

    def get_synonym(self, query='hello', number_of_synonyms=1):
        r = requests.get('https://www.thesaurus.com/browse/' + query.replace(' ', '-'),
                         headers={'User-agent': 'Mozilla/5.0'})
        p = Purifier()
        return p.purify_syn_eng(r.text, number_of_synonyms)

    def get_eng_fr(self, query='bonsoir', number_of_examples=0, grammar_mark=False):
        r = requests.get('https://www.collinsdictionary.com/dictionary/english-french/' + str(query).replace(' ', '-'),
                         headers={'User-agent': 'Mozilla/5.0'})
        p = Purifier()
        return p.purify_fr_eng(r.text, number_of_examples)

    def get_glosbe(self, query='bonsoir', number_of_examples=0, language='fr-ru'):
        if language == 'fr-ru':

            r = requests.get(f'https://glosbe.com/fr/ru/{query}',
                             headers={'User-agent': 'Mozilla/5.0'})
            p = Purifier()
            return p.purify_glosbe(r.text, number_of_examples)
        elif language == 'ru-fr':
            r = requests.get(f'https://glosbe.com/ru/fr/{query}',
                             headers={'User-agent': 'Mozilla/5.0'})
            p = Purifier()
            return p.purify_glosbe(r.text, number_of_examples)
        elif language == 'en-ru':
            r = requests.get(f'https://glosbe.com/en/ru/{query}',
                             headers={'User-agent': 'Mozilla/5.0'})
            p = Purifier()
            return p.purify_glosbe(r.text, number_of_examples)
        elif language == 'ru-en':
            r = requests.get(f'https://glosbe.com/ru/en{query}',
                             headers={'User-agent': 'Mozilla/5.0'})
            p = Purifier()
            return p.purify_glosbe(r.text, number_of_examples)
