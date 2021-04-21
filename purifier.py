from bs4 import BeautifulSoup


def purify(a):
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


def purify_syn_english(a):
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


def purify_fr_eng(text, number_of_examples):
    soap = BeautifulSoup(text, 'html.parser')
    grammar = str(soap.find(class_='pos'))
    translation = str(soap.find(class_='cit type-translation quote'))
    examples = soap.find_all(class_='quote')
    p_examples = list()
    for i in range(len(examples) - 1, len(examples) - number_of_examples - 1, -1):
        p_examples.append(purify(str(examples[i])))
    return purify(grammar), purify(translation), p_examples


def purify_definition(text, number_of_examples):
    soap = BeautifulSoup(text, 'html.parser')
    grammar = str(soap.find(class_='gramGrp pos'))
    definition = str(soap.find(class_='def'))
    examples = soap.find_all(class_='quote')
    p_examples = list()
    for i in range(len(examples) - 1, len(examples) - number_of_examples - 1, -1):
        p_examples.append(purify(str(examples[i])))
    return purify(grammar), purify(definition), p_examples


def purify_syn_eng(text, number_of_synonyms):
    soap = BeautifulSoup(text, 'html.parser')
    syn = soap.find_all(class_='css-1kg1yv8 eh475bn0')
    syn_res = list()
    if len(syn) < number_of_synonyms:
        additional = syn + soap.find_all(class_='css-1gyuw4i eh475bn0')
        for i in range(number_of_synonyms):
            syn_res.append(purify_syn_english(str(additional[i])))
        return syn_res
    else:
        for i in range(number_of_synonyms):
            syn_res.append(purify_syn_english(str(syn[i])))
        return syn_res
