import os
import accents

def writeFile(filename, content):
    fw = open(filename, 'w')
    fw.write(content)
    fw.close()

htmls_houses = "../htmls/crawler_houses"
htmls_houses_unaccent = "../htmls/crawler_houses_unaccent"

index = 1
for folder in os.listdir(htmls_houses):
    for filename in os.listdir(htmls_houses + "/" + folder):
        full_path = htmls_houses + "/" + folder + "/" + filename


        f = open(full_path)
        content = f.read()
        content = accents.remove_accents(content)

        save_folder = htmls_houses_unaccent + "/" + folder
        if os.path.isdir(save_folder) == False:
            os.mkdir(save_folder)
        new_path = save_folder + "/" + filename
        writeFile(new_path, content)
        print(index, filename + "\n")
        index = index + 1

    #time.sleep(20)

