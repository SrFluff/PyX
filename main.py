                                                               # Imports
from random import randint                                     # Just here for Fortune
import os                                                      # Mostly just here for screen clearing

                                                               # Filesystem

root = ['pac','usr']
usr = []
wrt = []
pac = []

                                                               # Other variables

name = 'user'
pwd = '~'
ls = usr
main = True

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

                                                               # Initial message

print('Type "help" for help')
print('PyX version 1.1.0')
print()

                                                               # Main loop

while main:

    a = input(f'{name}@pylinux:{pwd}$ ')                       # The main prompt
    b = a.split()                                              # Turning each word into an item in an array

    if a == 'exit':
        main = False
    
    elif a == 'help':
        print('help - prints this help message')
        print('exit - exits PyLinux')
        print('touch - makes a new empty file, only works in /usr')
        print('rm - removes a text file, only works in /usr')
        print('cd - changes directory')
        print('ls - lists files')
        print('pwd - prints the working directory')
        print('te - text editor, type "a" while in it to append a line, "r" to remove a line, and "q" to save and exit')
        print('cat - prints the contents of a file')
        print('ppm - PyX package manager, run "ppm help" for help')

    elif a == 'fortune':                                       # Fortune, but it's 10 fortunes
        if 'fortune' in pac:
            if randint(1,10) == 1:
                print('You are destined to become the commandant of the fighting men of the department of transportation.')
            elif randint(1,10) == 2:
                print('Do not overtax your powers.')
            elif randint(1,10) == 3:
                print('Many pages make a thick book.')
            elif randint(1,10) == 4:
                print('The whole world is a tuxedo and you are a pair of brown shoes.\n-- George Gobel')
            elif randint(1,10) == 5:
                print('You are capable of planning your future.')
            elif randint(1,10) == 6:
                print('Write yourself a threatening letter and pen a defiant reply.')
            elif randint(1,10) == 7:
                print("Don't get to bragging.")
            elif randint(1,10) == 8:
                print('Water, taken in moderation cannot hurt anybody.\n-- Mark Twain')
            elif randint(1,10) == 9:
                print('You will forget that you ever knew me.')
            else:
                print('You will never know hunger.')
        else:
            print('Error: Fortune not installed')
    elif a == 'ls':
        print(' '.join(ls))
    
    elif a == 'cd /' or a == 'cd ..' and ls == usr:
        ls = root
        pwd = '/'
    
    elif a == 'cd /usr' or a == 'cd usr' and ls == root:
        ls = usr
        pwd = '~'

    elif a == 'cd /pac' or a == 'cd pac' and ls == root:
        ls = pac
        pwd = '/pac'
    
    elif a == 'pwd':
        if ls == root:
            print('/')
        elif ls == usr:
            print('/usr')

    elif a == 'clear':
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    if len(b) != 0:                                            # If the response has no keyword it would IndexError
        if b[0] == 'cat':
            if ls == usr:
                if len(b) >= 2:
                    if b[1] in ls:
                        print('\n'.join(wrt[usr.index(b[1])])) # Each file is stored as an array and it prints it line by line
                    else:
                        print('Error: File not found')
                else:
                    print('Error: Filename not given')

        elif b[0] == 'touch':
            if ls == usr:
                if len(b) >= 2:
                    if not b[1] in usr:
                        usr.append(b[1])
                        wrt.append([])
                    else:
                        print('Error: File already exists')
                else:
                    print('Error: No filename given')
        elif b[0] == 'rm':
            if ls == usr:
                if len(b) >= 2:
                    if b[1] in usr:
                        wrt.pop(usr.index(b[1]))
                        usr.pop(usr.index(b[1]))
                    else:
                        print('Error: File does not exist')
                else:
                    print('Error: No filename given')
        elif b[0] == 'te':
            if ls == usr:
                if len(b) >= 2:
                    if not b[1] in usr:
                        usr.append(b[1])
                        wrt.append([])
                    tem = wrt[usr.index(b[1])]
                    while True:                                    # Main loop for the text editor
                        if os.name == 'nt':
                            os.system('cls')
                        else:
                            os.system('clear')
                        print('\n'.join(tem))
                        a = input(': ')
                        if a == 'q':
                            break
                        elif a == 'a':
                            if os.name == 'nt':
                                os.system('cls')
                            else:
                                os.system('clear')
                            print('\n'.join(tem))
                            a = input('> ')
                            tem.append(a)
                        elif a == 'r':
                            try:
                                if os.name == 'nt':
                                    os.system('cls')
                                else:
                                    os.system('clear')
                                print('\n'.join(tem))
                                a = input('> ')
                                tem.pop(int(a))
                            except IndexError:
                                if os.name == 'nt':
                                    os.system('cls')
                                else:
                                    os.system('clear')
                                print('Error: Line does not exist')
                                input()
        elif b[0] == 'ppm':
            if len(b) >= 2:
                if b[1] == 'install':
                    if len(b) >= 3:
                        if b[2] == 'fortune':
                            if 'fortune' in pac:
                                print('Error: Package already installed')
                            else:
                                pac.append('fortune')
                        else:
                            print('Error: Package not found, use "ppm list" to list all available packages')
                    else:
                        print('Error: No package name given')
                elif b[1] == 'list':
                    print('1. Fortune')
                elif b[1] == 'help':
                    print('ppm list - lists all available packages')
                    print('ppm install <package> - installs a specified package')
                    print('ppm remove <package> - removes a specified package')
                    print('ppm help - prints this help message')
                elif b[1] == 'remove':
                    if len(b) >= 3:
                        if b[2] in pac:
                            pac.pop(pac.index(b[2]))
                        else:
                            print('Error: Package not installed')
                    else:
                        print('Error, No package name given')
                else:
                    print('ppm list - lists all available packages')
                    print('ppm install <package> - installs a specified package')
                    print('ppm remove <package> - removes a specified package')
                    print('ppm help - prints this help message')
            else:
                print('ppm list - lists all available packages')
                print('ppm install <package> - installs a specified package')
                print('ppm remove <package> - removes a specified package')
                print('ppm help - prints this help message')
