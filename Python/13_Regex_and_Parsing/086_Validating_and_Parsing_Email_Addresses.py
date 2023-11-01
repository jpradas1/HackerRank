'''
A valid email address meets the following criteria:

1. It's composed of a username, domain name, and extension assembled in 
   this format: username@domain.extension
2. The username starts with an English alphabetical character, and any 
   subsequent characters consist of one or more of the following: 
   alphanumeric characters, -,., and _.
3. The domain and extension contain only English alphabetical characters.
4. The extension is 1, 2, or 3 characters in length.

Given `n` pairs of names and email addresses as input, print each name and 
email address pair having a valid email address on a new line.
'''
import re
import email.utils

if __name__=='__main__':
    n = int(input())
    emails = [email.utils.parseaddr(input()) for _ in range(n)]

    L = lambda x: bool(re.findall(r'^([a-zA-Z][\w\.\-]+@[a-zA-Z]+\.[a-zA-Z]{1,3})$', x))

    for ii in emails:
        if L(ii[1]):
            print(email.utils.formataddr(ii))