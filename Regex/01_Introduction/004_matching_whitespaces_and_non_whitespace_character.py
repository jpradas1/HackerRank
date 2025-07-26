'''
\s
--
`\s` matches any whitespace character `[\r\n\t\f]`.

\S
--
`\S` matches any non-white space character.

Task
----

You have a test string `S`. Your task is to match the pattern `XXxXXxXX`
Here, `x` denotes whitespace characters, and `X~ denotes non-white space
characters.

Note
----

This is a regex only challenge. You are not required to write code.
You have to fill the regex pattern in the blank (_________).
'''

import re

Regex_Pattern = r"\S{2}\s\S{2}\s\S{2}"	# Do not delete 'r'.

texts = [
    '12 11 15', '122 23 56', '12 12	1ee', '123 123 123',
    '12 12  123', '12	23		123'
]
for text in texts:
    print(str(bool(re.search(Regex_Pattern, text))).lower())