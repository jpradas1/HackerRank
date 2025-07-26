'''
\d
--
The expression `\d` matches any digit `[0-9]`.

\D
--
The expression `\D` matches any character that is not a digit.

Task
----

You have a test string `S`. Your task is to match the pattern `xxXxxXxxxx`
Here `x` denotes a digit character, and `X` denotes a non-digit character.

Note
----

This is a regex only challenge. You are not required to write any code.
You only have to fill the regex pattern in the blank (_________).
'''

import re

Regex_Pattern = r"\d{2}\D\d{2}\D\d{4}"	# Do not delete 'r'.

texts = [
    '06-11-2015', '06-11-015', '06-1-2015', '0-10-2015'
]

for text in texts:
    print(str(bool(re.search(Regex_Pattern, text))).lower())