'''
You are given an integer `N` followed by `N` email addresses. Your task is 
to print a list containing only valid email addresses in lexicographical 
order.


Valid email addresses must follow these rules:

1. It must have the username@websitename.extension format type.
2. The username can only contain letters, digits, dashes and underscores 
    [a-z],[A-Z],[0-9],[_-].
3. The website name can only have letters and digits [a-z],[A-Z],[0-9].
4. The extension can only contain letters [a-z],[A-Z].
5. The maximum length of the extension is 3.
'''

def fun(s):
    parts = s.split('@')
    if all(True if x in s else False for x in ['@', '.']) and len(parts)==2:
        parts = s.split('@')
        username = parts[0].replace('-','').replace('_','').isalnum()
        website = parts[1].split('.')[0].isalnum()
        extension = [parts[1].split('.')[1].isalpha(), len(parts[1].split('.')[1])<=3]

        flag = [username, website] + extension
        print(parts, flag)

        if all(flag):
            return s

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)