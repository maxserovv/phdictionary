from bs4 import BeautifulSoup


class Purifier:
    def purify(self, a):
        try:
            purified = ''
            add = False
            for i in range(len(a)):
                if a[i] == '>':
                    add = True
                elif a[i] == '<':
                    add = False
                elif a[i] == '\n':
                    pass
                elif add:
                    purified += a[i]
            if purified[0] == ' ':
                purified = purified[1:]
            return purified
        except:
            return ''

    def purify_syn_english(self, a):
        try:
            purified = ''
            add = False
            for i in range(len(a)):
                if a[i] == '/':
                    add = True
                elif a[i] == '"':
                    add = False
                elif a[i] == '\n':
                    pass
                elif add:
                    purified += a[i]
            if purified[0] == ' ':
                purified = purified[1:]
            purified = purified[6:len(purified) - 2]
            return purified
        except:
            print('Only this amount of appropriate synonyms has found')
            return ''

    def purify_fr_eng(self, text, number_of_examples):
        p = Purifier()
        soap = BeautifulSoup(text, 'html.parser')
        grammar = str(soap.find(class_='pos'))
        translation = str(soap.find(class_='cit type-translation quote'))
        examples = soap.find_all(class_='quote')
        p_examples = list()
        for i in range(len(examples) - 1, len(examples) - number_of_examples - 1, -1):
            p_examples.append(p.purify(str(examples[i])))
        return p.purify(grammar), p.purify(translation), p_examples

    def purify_definition(self, text, number_of_examples):
        p = Purifier()
        soap = BeautifulSoup(text, 'html.parser')
        grammar = str(soap.find(class_='gramGrp pos'))
        definition = str(soap.find(class_='def'))
        examples = soap.find_all(class_='quote')
        p_examples = list()
        for i in range(len(examples) - 1, len(examples) - number_of_examples - 1, -1):
            p_examples.append(p.purify(str(examples[i])))
        return p.purify(grammar), p.purify(definition), p_examples

    def purify_syn_eng(self, text, number_of_synonyms):
        p = Purifier()
        soap = BeautifulSoup(text, 'html.parser')
        syn = soap.find_all(class_='css-1kg1yv8 eh475bn0')
        syn_res = list()
        if len(syn) < number_of_synonyms:
            additional = syn + soap.find_all(class_='css-1gyuw4i eh475bn0')
            for i in range(number_of_synonyms):
                try:
                    syn_res.append(p.purify_syn_english(str(additional[i])))
                except:
                    syn_res.append('')
                    print('Currently it is not possible to find so many synonyms')
            return syn_res
        else:
            for i in range(number_of_synonyms):
                syn_res.append(p.purify_syn_english(str(syn[i])))
            return syn_res

    def purify_glosbe(self, text, number_of_examples):
        p = Purifier()
        soap = BeautifulSoup(text, 'html.parser')
        s = soap.find_all(class_='translation')
        translation = []
        examples = []

        for el in s:
            translation.append(p.purify(str(el)))

        s = soap.find_all(class_='translation__example')

        for j in range(number_of_examples):
            res = p.purify(str(s[j]))
            r = ''
            split = True
            for i in range(len(res)):
                if ord(res[i]) > 1000 and split:
                    split = False
                    r += ' || '
                    r += res[i]
                else:
                    r += res[i]
            examples.append(r)

        return translation, examples
        # s = soap.find_all(class_='phrase__summary__field')
        # for el in s:
        #     purify_french_russian(str(el))
