global points
points = 0


def scores():
    alll = []
    snoms = []
    global scores
    scores = open('scores.txt', 'r')
    for line in scores:
        y = line
        if '\n' in y:
            y = y.strip('\n')
        alll.append(y)
    for i in snoms:
        i = i.split(',')
        snoms.append(i)
        i[1] = points
        print(points)
        print(alll)
        print('hello')


def login():
    lists = []
    usernames = []
    userAndPass = []
    names = open('names.txt', 'r')
    for line in names:
        x = line
        if '\n' in x:
            x = x.strip('\n')
        lists.append(x)
    for i in lists:
        i = i.split(',')
        userAndPass.append(i)
        username = i[0]
        usernames.append(username)
        #print(username)
    holder = dict(userAndPass)
    #print(holder)
    logged = False
    while logged == False:
        entry = input('Enter username: ')
        if entry in usernames:
            password = (holder[entry])
            password = password.strip(' ')
            trys = 0
            while trys < 3:
                pastry = input('please enter your password: ')
                if pastry == password:
                    print('okay, you are now logged in')
                    logged = True
                    break
                elif trys == 2:
                    print('Password incorrect too many times')
                    break
                else:
                    print('wrong')
                    trys = trys + 1
                    print('you have ' + str(3-trys) + ' attempts left')
        else:
            print("That's wrong try again")


def boot():
    for g in range(0, 2):
        if g == 1:
            print('\nNow login the second user: \n')
        login()
    print('you may now play')


def create():
    ask = input('if you have an account enter 1, if not enter 2: ')
    if ask == '1':
        boot()
    elif ask == '2':
        names = open('names.txt', 'a')
        user = input('Choose user: ')
        pas = input('Choose pas: ')
        writing = (user + ', ' + pas)
        names.write('\n' + writing)
        names.close()
        print('\nAccount has successfully been added\n')
        boot()


create()
