# Take an email address and print username, domain, and reversed domain.
email = input()
at_position = email.find("@")

username = email[:at_position]
domain = email[at_position +1:]
reversed_domain = domain[::-1]

print(username)
print(domain)
print(reversed_domain)