from PhDictionary import requestor
from PhDictionary import file_manager


class PhDictionary:
    def get_definition(self, word, number_of_examples=0, grammar_mark=False):
        if grammar_mark == False and number_of_examples == 0:
            return requestor.get_definition(word, number_of_examples, grammar_mark)[1:2]
        elif grammar_mark == True and number_of_examples == 0:
            return requestor.get_definition(word, number_of_examples, grammar_mark)[:2]
        elif number_of_examples != 0 and grammar_mark == False:
            return requestor.get_definition(word, number_of_examples, grammar_mark)[1:]
        return requestor.get_definition(word, number_of_examples, grammar_mark)

    def get_french_english(self, word, number_of_examples=0, grammar_mark=False):
        if grammar_mark == False and number_of_examples == 0:
            return requestor.get_french_english(word, number_of_examples, grammar_mark)[1:2]
        elif grammar_mark == True and number_of_examples == 0:
            return requestor.get_french_english(word, number_of_examples, grammar_mark)[:2]
        elif number_of_examples != 0 and grammar_mark == False:
            return requestor.get_french_english(word, number_of_examples, grammar_mark)[1:]
        return requestor.get_french_english(word, number_of_examples, grammar_mark)

    def get_syn(self, word, number_of_syn=1):
        return requestor.get_synonym(word, number_of_syn)

    def get_french_english_from_file(self, file, number_of_examples=0):
        return file_manager.txt_french_english(file, number_of_examples)

    def get_syn_from_file(self, file, number_of_syn=1):
        return file_manager.syn_txt(file, number_of_syn)

    def get_english_french(self, word, number_of_examples=0, grammar_mark=False):
        if grammar_mark == False and number_of_examples == 0:
            return requestor.get_eng_fr(word, number_of_examples, grammar_mark)[1:2]
        elif grammar_mark == True and number_of_examples == 0:
            return requestor.get_eng_fr(word, number_of_examples, grammar_mark)[:2]
        elif number_of_examples != 0 and grammar_mark == False:
            return requestor.get_eng_fr(word, number_of_examples, grammar_mark)[1:]
        return requestor.get_eng_fr(word, number_of_examples, grammar_mark)

    def get_definition_from_file(self, file, number_of_examples=0):
        return file_manager.definition(file, number_of_examples)
