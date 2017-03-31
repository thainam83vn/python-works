import mylib.fileapi as fileapi
import vac.models as models
from vac.models import VChar
import vac.config as config
import mylib.html as html
import mylib.regex as regex
import datetime

import os

def removeMultiSpace(s):
    while "  " in s:
        s = s.replace("  ", " ")
    while "\n\n" in s:
        s = s.replace("\n\n", "\n")
    while "\t\t" in s:
        s = s.replace("\t\t", "\t")

    return s



vchar = VChar()

files = os.listdir(config.htmls_folder)


for file in files:

    content = fileapi.readFile(config.htmls_folder + "/" + file)
    content = html.strip_tags(content)


    content = regex.searchStringG1DOTALL(r"(Full.*Full)",content)
    content = removeMultiSpace(content)



    sfile = ""
    for i in range(0, len(content)):
        c = content[i]
        if vchar.has_accent(c):
            j = i - 20

            s = ""
            while j <= i + 20:
                if j == i:
                    s = s + vchar.unaccent(content[j])
                elif j >= 0 and j < len(content):
                    s = s + content[j]
                else:
                    s = s + models.char_empty
                j = j + 1
            #print(c, s.replace("\n", ""))
            yind = vchar.index_in_target(c)
            sfile = sfile + (str(vchar.list_index(s)).replace("[","").replace("]", "") + ", " + str(yind)).replace(" ", "") + "\n"
    fileapi.appendFile(config.data_csv, sfile)
    print(datetime.datetime.now, "update by " + file)

