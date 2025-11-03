user = input()
while len(user) > 1:
    b = 0
    for i in user:
        a = int(i)
        b += a
    user = f"{b}"
print(user)
