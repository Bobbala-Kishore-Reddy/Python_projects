email = input("Enter Your Email: ").strip()

a = email.split('@')

username=a[0]
domain=a[1]

print(f'Username is {username}    &  Domain is {domain}')
