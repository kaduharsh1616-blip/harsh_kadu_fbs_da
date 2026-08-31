### a program to check if person is eligible to marry or not (male age >=21 and
##female age>=18)

ma= int(input('enter the ma'))
ga = int(input('enter the ga'))

if ( ma > 21):
    print(' ma eligible for marriage:')

    if (ga > 18):
        print('ga eligible for marriage:')

    else:
        print('ga not eligible for marriage:')

else:
    print('ma not eligible for marriage:')

