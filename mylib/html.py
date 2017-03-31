import re
import mylib.regex as regex

'''
class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()
'''

def strip_tags(value):
    """Returns the given HTML with all tags stripped."""
    s = re.sub(r'<[^>]*?>', '', value)
    s = re.sub(r'{[^}]*?}', '', s)
    s = re.sub(r'([^)]*?)', '', s)
    s = s.replace("(function() )();", "")
    return s