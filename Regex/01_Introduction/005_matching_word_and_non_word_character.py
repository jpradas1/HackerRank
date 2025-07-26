'''
\w
--
The expression `\w` will match any word character.
Word characters include alphanumeric characters (a-z, A-Z and 0-9) and 
underscores (_).

\W
--
`\W` matches any non-word character.
Non-word characters include characters other than alphanumeric characters
(a-z, A-Z and 0-9) and underscore (_).

Task
----

You have a test string `S`. Your task is to match the pattern xxxXxxxxxxxxxxXxxx
Here `x` denotes any word character and `X` denotes any non-word character.

Note
----

This is a regex only challenge. You are not required to write any code.
You only have to fill the regex pattern in the blank (_________).
'''

import re

Regex_Pattern = r"\w{3}\W\w{10}\W\w{3}"	# Do not delete 'r'.

texts = [
    'www.hackerrank.com', 'www.hackerrrank.co', '132.__________.co_',
    '132.___________co_', 'www.hackerrank.co', 'http://www.wikipedia.com.http://www.hackerrank.com'
]

for text in texts:
    print(str(bool(re.search(Regex_Pattern, text))).lower())