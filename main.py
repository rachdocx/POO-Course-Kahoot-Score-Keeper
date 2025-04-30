import pdfplumber
import os
import unicodedata

def remove_accents(text):
    return ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )

path="pdfs"
dic={}
for fisier in os.listdir(path):
    psf_path = os.path.join(path, fisier)
    with pdfplumber.open(psf_path) as pdf:
        print(f"{psf_path} is loaded")
        for pagina in pdf.pages:
            tabel = pagina.extract_table()
            if pagina.page_number == 1:
                tabel = tabel[3:]
            for rand in tabel:
                if '\n' in rand[1]:
                    rand[1] = rand[1].replace('\n', '')
                if ' ' in rand[1]:
                    rand[1] = rand[1].replace(' ', '')
                if '_' in rand[1]:
                    rand[1] = rand[1].replace('_', '')
                if '-' in rand[1]:
                    rand[1] = rand[1].replace('-', '')
                text = remove_accents(rand[1])
                rand[1] = text
            if tabel:
                for rand in tabel:
                    if rand[1].lower() not in dic:
                        dic[rand[1].lower()] = int(rand[2])
                    else:
                        dic[rand[1].lower()] += int(rand[2])
dic = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
for index, (cheie, valoare) in enumerate(dic.items()):
    print(f"{index+1}: {cheie} → {valoare}")
opt = 9;
while opt != 0:
    print("1. To search by name")
    print("0. To exit")
    opt = int(input())
    if opt == 1:
        name = input()
        for index, (cheie, valoare) in enumerate(dic.items()):
            if name.lower() == cheie:
                print(f"{index + 1}: {cheie} → {valoare}")
                break