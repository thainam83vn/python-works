import web
import regex
import json

server = "http://localhost:7474"
create_url = "/db/data/transaction/60"

def correctString(s):
    return s.replace(","," ").replace(":", " ").replace("\"", " ").replace("{", " ").replace("}", " ")

def correctJson(s):
    s1 = s.replace("\"", "").replace(", ", ",").replace(": ", ":")
    s2 = s1.replace(":", ":\"").replace(",", "\",").replace("}", "\"}")
    s3 = s2.replace("\"[","[\"").replace("]\"","\"]").replace("\"{","{").replace("}\"","}")
    return s3

def jsonDump(o):
    s = json.dumps(o)
    s2 = correctJson(s)
    return s2

def jsonLoad(s):
    s2 = regex.searchStringG1(".*properties=({.*})", s).replace("'","\"")
    h = json.loads(s2)
    return h