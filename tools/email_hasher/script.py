import hashlib

# read providers from file
with open('providers.txt', 'r') as file:
    providers = file.read().splitlines()

# extract postfixes from providers
postfixes = set(provider.split('@')[-1].split('.')[-1] for provider in providers)

# Create list of base emails
base_emails = ['keeponrocking7920420bb4@' + provider for provider in providers]

# Create list of emails with dot in different places
emails = []
for base_email in base_emails:
    for i in range(1, len('keeponrocking7920420bb4')):
        email = base_email[:i+1] + '.' + base_email[i+1:]
        emails.append(email)

# Create list of emails with postfix
for provider in providers:
    for postfix in postfixes:
        for i in range(1, len('keeponrocking7920420bb4') + 1):
            email = 'keeponrocking7920420bb4'[:i] + '@' + 'keeponrocking7920420bb4'[i:] + '.' + postfix
            emails.append(email)

# Print number of generated emails
print("Generated emails: " + len(emails))

# Hash emails with MD5
hashes = [hashlib.md5(email.encode()).hexdigest() for email in emails]

# Check if any hash corresponds to 2471b1362bace767fdc0bb9c7e4df686
bool = False
for hash in hashes:
    if hash == '2471b1362bace767fdc0bb9c7e4df686':
        print('Found')
        print(emails[hashes.index(hash)])
        bool = True
        break
if not bool:
    print('Not found')