# -*- coding: utf-8 -*-
import re
import sys


s1 = u'ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'
s0 = u'AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOoUuAaAaAaAaAaAaAaAaAaAaAaAaEeEeEeEeEeEeEeEeIiIiOoOoOoOoOoOoOoOoOoOoOoOoUuUuUuUuUuUuUuYyYyYyYy'

targets = {
    'A':'AÀÁÂÃĂẠẤẦẨẪẬẮẰẲẴẶ',
    'a':'aàáâãăạấầẩẫậắằẳẵặ',
    'E':'EÈÉÊẸẺẼẾỀỂỄỆ',
    'e':'eèéêẹẻẽếềểễệ',
    'I':'IÌÍĨỈỊ',
    'i':'iìíĩỉị',
    'O':'OÒÓÔÕƠỌỎỐỒỔỖỘỚỜỞỠỢ',
    'o':'oòóôõơọỏốồổỗộớờởỡợ',
    'U':'UÙÚŨƯỤỦỨỪỬỮỰ',
    'u':'uùúũưụủứừửữự',
    'Y':'YÝỴỶỸ',
    'y':'yýỵỷỹ',
    'D':'DĐ',
    'd':'dđ'
}

char_empty = '\n'
all_space = '\t '
all_others = '~!@#$%^&*()-_+={}|\\/[]:;\'"<>,.?'
all_numeric = '1234567890'
all_normal_chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvXxYy'
all_accent_chars = 'ÀÁÂÃĂẠẤẦẨẪẬẮẰẲẴẶàáâãăạấầẩẫậắằẳẵặÈÉÊẸẺẼẾỀỂỄỆèéêẹẻẽếềểễệÌÍĨỈỊiìíĩỉịÒÓÔÕƠỌỎỐỒỔỖỘỚỜỞỠỢòóôõơọỏốồổỗộớờởỡợÙÚŨƯỤỦỨỪỬỮỰùúũưụủứừửữựÝỴỶỸyýỵỷỹĐđ'
all_chars = char_empty + all_space + all_others + all_numeric + all_normal_chars + all_accent_chars

class VChar:
    def unaccent(self, c):
        for i in range(0, len(s1)):
            try:
                if s1[i] == c:
                    return s0[i]
            except:
                pass
                return c
        return c

    def index(self, c):
        return self.index_ls(c, all_chars)

    def index_ls(self, c, ls):
        for i in range(0, len(ls)):
            if ls[i] == c:
                return i
        return -1

    def list_index(self, s):
        r = []
        for c in s:
            index = self.index(c)
            r = r + [index]
        return r

    def target_index(self, c):
        return self.list_index(self.target(c))

    def target(self, c):
        if targets.get(c):
            return targets.get(c)
        return None

    def index_in_target(self, c):
        a = self.unaccent(c)
        if targets.get(a):
            ls = targets.get(a)
            ind = self.index_ls(c, ls)
            return ind
        return 0

    def has_accent(self, c):
        a = self.unaccent(c)
        if targets.get(a):
            return True
        return False

