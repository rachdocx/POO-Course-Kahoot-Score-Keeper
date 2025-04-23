import pdfplumber
import os
path="pdfs"
dic={}
for fisier in os.listdir(path):
    cale_completa = os.path.join(path, fisier)
    with pdfplumber.open(cale_completa) as pdf:
        for pagina in pdf.pages:
            text = pagina.extract_text()
            lines = text.splitlines()
            if(pagina.page_number == 1):
                for i in range(len(lines)):
                    if lines[i] == "(points) Answers Answers" :
                        lines = lines[i+1:]
                        break
                for i in range(len(lines)):
                    user=lines[i].strip().split()
                    if user[0] != "Page":
                        if user[1].lower() not in dic:
                            dic[user[1].lower()]=int(user[2])
                        else:
                            dic[user[1].lower()]+=int(user[2])
            else:
                for i in range(len(lines)):
                    if lines[i] == 'Final Scores' :
                        lines = lines[i+1:]
                        break
                for i in range(len(lines)):
                    user=lines[i].strip().split()
                    if len(user) >= 3 and user[2].isdigit():
                        if user[1].lower() not in dic:
                            dic[user[1].lower()]=int(user[2])
                        else:
                            dic[user[1].lower()]+=int(user[2])
dic = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
for index, (cheie, valoare) in enumerate(dic.items()):
    print(f"{index+1}: {cheie} → {valoare}")
