from phdictionary.requestor import *
from docx import Document
from random import randint


def txt_french_english(f, number_of_examples=0):
    if number_of_examples == 0:
        document = Document()
        document.add_heading('French-English', 0)
        for word in f:
            re = get_french_english(word, 0)[:2]
            word = word[:len(word) - 1]
            if re[0] == 'feminine noun':
                word += ' (f)'
            elif re[0] == 'masculine noun':
                word += ' (m) '
            document.add_paragraph(word + '  -  ' + re[1], style='List Bullet')
        document.save(f'french-english{randint(0,1000)}.docx')
    else:
        document = Document()
        document.add_heading('French-English', 0)
        for word in f:
            re = get_french_english(word, number_of_examples)
            word = word[:len(word) - 1]
            if re[0] == 'feminine noun':
                word += ' (f)'
            elif re[0] == 'masculine noun':
                word += ' (m) '
            p = document.add_paragraph()
            p.add_run(word + '  -  ' + re[1]).bold = True
            for ex in re[2]:
                document.add_paragraph(ex, style='List Bullet')

        document.save(f'french-english-examples{randint(0, 1000)}.docx')


def syn_txt(f, number_of_syn):
    document = Document()
    document.add_heading('Synonyms', 0)
    for word in f:
        word = word[:len(word) - 1]
        re = get_synonym(str(word), number_of_syn)
        p = document.add_paragraph(style='List Bullet')
        to_add = ''
        for i in range(len(re)):
            if i == len(re) - 1:
                to_add += re[i]
            else:
                to_add += re[i] + ', '
        p.add_run(word + '  -  ' + to_add).bold = True
        document.save(f'synonyms{randint(0,1000)}.docx')


def definition(f, number_of_examples):
    if number_of_examples == 0:
        document = Document()
        document.add_heading('Definition', 0)
        for word in f:
            re = get_definition(word, 0)[:2]
            if '\n' not in word:
                p = document.add_paragraph(style='List Bullet')
                p.add_run(word[0].upper() + word[1:]).bold = True
                p.add_run('  -  ' + re[1])
            else:
                word = word[0].upper() + word[1:len(word) - 1]
                p = document.add_paragraph(style='List Bullet')
                p.add_run(word).bold = True
                p.add_run('  -  ' + re[1])
        document.save(f'definition{randint(0,1000)}.docx')
    else:
        document = Document()
        document.add_heading('Definition', 0)
        for word in f:
            re = get_definition(word, number_of_examples)
            if '\n' not in word:
                p = document.add_paragraph()
                p.add_run(word[0].upper() + word[1:]).bold = True
                p.add_run('  -  ' + re[1])
            else:
                word = word[0].upper() + word[1:len(word) - 1]
                p = document.add_paragraph()
                p.add_run(word).bold = True
                p.add_run('  -  ' + re[1])
            for ex in re[2]:
                document.add_paragraph(ex, style='List Bullet')
        document.save(f'definition_examples{randint(0,1000)}.docx')
