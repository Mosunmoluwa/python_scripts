while True:
    print('who are you?')
    name = input()
    if name != 'joe':
        continue
    print('hello joe please input your password')
    password = input()
    if password == 'swordfish':
        print('welcome joe')
        break
    else :
        print('access denied')
