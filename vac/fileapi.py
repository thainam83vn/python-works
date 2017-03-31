def readFile(filename):
   f = open(filename, 'r', encoding="utf8")
   content = f.read()
   f.close()
   return content

def writeFile(filename, content):
   f = open(filename, 'w', encoding="utf8")
   f.write(content)
   f.close()

