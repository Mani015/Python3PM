print('Welcome to templa run')


level1 = int(input('Enter your level :'))
if 1 == level1:
    print('Level one complete successfully ')
    level2 = int(input('Enter your level :'))
    if 2 == level2:
        print('Level two complete successfully ')
        level3 = int(input('Enter your level :'))
        if 3 == level3:
            print('Level three complete successfully ')
            level4 = int(input('Enter your level :'))
            if 4 == level4:
                print('Level four complete successfully ')
            else:
                print('sorry! you are failed in level4')
        else:
            print('sorry! you are failed level3')
    else:
        print('sorry! you are fauled level2')
else:
    print('sorry! you are fauled')