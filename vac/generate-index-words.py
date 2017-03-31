import mylib.fileapi as fileapi
import vac.models as models
from vac.models import VChar,VWord
import vac.config as config
import mylib.html as html
import mylib.regex as regex
import datetime

import os

def removeMultiSpace(s):
    for c in "?!;.…":
        while c in s:
            s = s.replace(c, "\n")
    while "  " in s:
        s = s.replace("  ", " ")

    for c in ",:`'’\":/\\{}[]@#$%^&*()-_+=~<>|":
        while c in s:
            s = s.replace(c, " ")
    while '”' in s:
        s = s.replace('”', " ")

    while "\n\n" in s:
        s = s.replace("\n\n", "\n")
    while "\t\t" in s:
        s = s.replace("\t\t", "\t")
    while "\t" in s:
        s = s.replace("\t", " ")

    return s

vword = VWord()
#vchar = VChar()
#print(vchar.index('a'))
#print(vchar.list_index('AaOoEeIiUuYy'))


files = os.listdir(config.htmls_folder)

count = 0
for file in files:

    content = fileapi.readFile(config.htmls_folder + "/" + file)
    content = html.strip_tags(content)


    content = regex.searchStringG1DOTALL(r"(Full.*Full)",content)
    content = removeMultiSpace(content)
    lines = content.split('\n')

    sfile = ""
    for line in lines:
        line = vword.lower(line)
        words = line.split(' ')

        for i in range(0, len(words)):
            w = words[i]
            if len(w) > 0:
                arr = vword.correct(w)
                for word in arr:
                    vword.getWordIndex(word)

                if len(arr) == 0:
                    print(w, arr)


fileapi.appendFile(config.words_index_csv, vword.toString())



