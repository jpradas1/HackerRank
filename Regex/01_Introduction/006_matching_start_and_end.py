'''
^
-
The `^` symbol matches the position at the start of a string.

$
-
The `$` symbol matches the position at the end of a string.

Task
----

You have a test string `S`. Your task is to match the pattern `Xxxxx.`
Here, `x` denotes a word character, and `X` denotes a digit.
`S` must start with a digit `X` and end with . symbol.
`S` should be `6` characters long only.

Note
----

This is a regex only challenge. You are not required to write code.
You have to fill the regex pattern in the blank (_________).
'''

import re

Regex_Pattern = r"^\d\w{4}\.$"	# Do not delete 'r'.

texts = [
    '0qwer.', '00000.', '10aaaa.', '1qazq.2w', '1a2a2.',
    '.1.2.2..'
]

for text in texts:
    print(str(bool(re.search(Regex_Pattern, text))).lower())