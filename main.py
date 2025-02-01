                                                               # Imports

import os                                                      # Mostly just here for screen clearing

                                                               # Filesystem

root = ['usr']
usr = []
wrt = []

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
print('PyX version 1.0.0')
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

    elif a == 'ls':
        print(' '.join(ls))
    
    elif a == 'cd /' or a == 'cd ..' and ls == usr:
        ls = root
        pwd = '/'
    
    elif a == 'cd /usr' or a == 'cd usr' and ls == root:
        ls = usr
        pwd = '~'
    
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
    if ls == usr:

        if len(b) != 0:                                        # If the response has no keyword it would IndexError
            if b[0] == 'cat':
                if len(b) >= 2:
                    if b[1] in ls:
                        print('\n'.join(wrt[usr.index(b[1])])) # Each file is stored as an array and it prints it line by line
                    else:
                        print('Error: File not found')
                else:
                    print('Error: Filename not given')

            elif b[0] == 'touch':
                if len(b) >= 2:
                    if not b[1] in usr:
                        usr.append(b[1])
                        wrt.append([])
                    else:
                        print('Error: File already exists')
                else:
                    print('Error: No filename given')
            elif b[0] == 'rm':
                if len(b) >= 2:
                    if b[1] in usr:
                        wrt.pop(usr.index(b[1]))
                        usr.pop(usr.index(b[1]))
                    else:
                        print('Error: File does not exist')
                else:
                    print('Error: No filename given')
            elif b[0] == 'te':
                if len(b) >= 2:
                    if not b[1] in usr:
                        usr.append(b[1])
                        wrt.append([])
                    tem = wrt[usr.index(b[1])]
                    while True:                                # Main loop for the text editor
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
