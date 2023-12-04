'''
Task

You are given an HTML code snippet of `N` lines.
Your task is to print start tags, end tags and empty tags separately.

Format your results in the following way:

Start : Tag1
End   : Tag1
Start : Tag2
-> Attribute2[0] > Attribute_value2[0]
-> Attribute2[1] > Attribute_value2[1]
-> Attribute2[2] > Attribute_value2[2]
Start : Tag3
-> Attribute3[0] > None
Empty : Tag4
-> Attribute4[0] > Attribute_value4[0]
End   : Tag3
End   : Tag2
'''

import re

class DaoHTMLParser(object):
    empty_tag = ['br', 'img']

    def __init__(self, html: str):
        cleansing = lambda x: re.findall('.*\>', x.strip())[0].replace('>','').split(' ')
        parsing = [cleansing(x) for x in re.split('\<', html) if x.strip()]
        
        for pars in parsing:
            self._handle_starttag(pars)
            self._handle_endtag(pars)
            # self._handle_startendtag(pars)

    def _handle_attributes(self, attr):
        for x in attr:
            at = re.findall('''([\w\-]*)(?:=?)([\w\d'"\/\.\-]*)''', x)[0]
            at = [None if not x else x.strip('''"' ''') for x in at]
            print('-> {} > {}'.format(at[0],at[1]))

    def _handle_starttag(self, tag):
        if tag[0] in self.empty_tag:
            print("Empty :", tag[0])
        elif not re.findall('^\/\w*', tag[0]):
            print("Start :", tag[0])
            if all(x for x in tag[1:]):
                self._handle_attributes(tag[1:])

    def _handle_endtag(self, tag):
        if re.findall('^\/\w*', tag[0]):
            print("End   :", tag[0].strip('/'))

if __name__=='__main__':
    html = ''
    for _ in range(int(input())):
        html += input()

    DaoHTMLParser(html)