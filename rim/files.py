import os

def count_files(path):
    folders = os.listdir(path)
    i = 0
    for folder in folders:
        files = os.listdir(path + "/" + folder)

        for filename in files:
            i=i+1
    return i

print(count_files("/home/thai/Realtate/htmls/houses"))
print(count_files("/home/thai/Realtate/htmls/houses_processed"))
