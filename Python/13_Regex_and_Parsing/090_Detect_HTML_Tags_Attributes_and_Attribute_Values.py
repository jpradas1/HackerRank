'''
You are given an HTML code snippet of `N` lines.
Your task is to detect and print all the HTML tags, attributes and 
attribute values.

Print the detected items in the following format:

Tag1
Tag2
-> Attribute2[0] > Attribute_value2[0]
-> Attribute2[1] > Attribute_value2[1]
-> Attribute2[2] > Attribute_value2[2]
Tag3
-> Attribute3[0] > Attribute_value3[0]


The -> symbol indicates that the tag contains an attribute. It is 
immediately followed by the name of the attribute and the attribute value.
The > symbol acts as a separator of attributes and attribute values.

If an HTML tag has no attribute then simply print the name of the tag.
'''

import re

class DaoHTML_Parsing(object):
    def __init__(self, html: str) -> None:
        self.html = html
        self._drop_comment_lines()
        self.tags = re.findall(r'''(?<=\<)([^\/].*?)(?=\>)''', self.html, re.DOTALL)
        self._tags()
    
    def _tags(self) -> None:
        for x in self.tags:
            attr = re.split(r'\s+', x.strip(), re.DOTALL)
            print(attr[0])
            attr = re.findall(r'([\w\-]*)(?:=)(".*?")', x, re.DOTALL)
            if attr:
                self._attributes(attr)
        
    def _attributes(self, attr: list) -> None:
        for x in attr:
            tag, val = x
            print(f'''-> {tag} > {val.strip('"')}''')

    def _drop_comment_lines(self):
        comments = re.findall('(<!--.*?-->)', self.html, re.DOTALL)
        if comments:
            for x in comments:
                self.html = self.html.replace(x, '')


if __name__=='__main__':
    html = '\n'.join([input() for _ in range(int(input()))])
    print('\n')
    DaoHTML_Parsing(html)