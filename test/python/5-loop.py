# start
num_of_try = 0
while num_of_try != 3:
    user = input('Pleaser insert your id : ')
    Youpass = input('Please insert your password : ')
    if user == 'sinan' and Youpass == '123456':
        print('welcome To :')
        num_of_try = 0
        exit()
    else:
        print('Please Try again :')
        num_of_try += 1
        print('you have ' + str(3 - num_of_try) + ' try left')
