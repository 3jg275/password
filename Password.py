password = 'a123456'
x = 3
while x > 0:
    pwd = input('plz input password ')
    if pwd == password:
        print('Success!')
        break #stop asking
    else:
        x = x - 1
        if x > 0:
            print('wrong pass word! You still got ', x, "chances")
        else:
            print('Unavailable, Account suspended.')


