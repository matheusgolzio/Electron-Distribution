from time import sleep

def line():
    print('~~'*30)

def recognition(e):
    with open('info/atoms.txt','r') as f:
        lines = f.readlines()
        for i in lines:
            linesplit = i.split()
            if (f'{e};' == linesplit[2]):
                print(f'Name: {linesplit[0]} | Letter: {linesplit[1]} | Atomic Number: {linesplit[2]}')


def distribution(e):
    recognition(e)
    line()
    kv = 0
    lv = 0
    mv = 0
    nv = 0
    ov = 0
    pv = 0
    qv = 0

    if e == 0:
        print('There are no electrons to distribute')
        line()
    
    elif e > 118:
        print('There is no discovered atoms that has more than 118 protons and electrons')
        line()

    elif e == 1:
        kv = 1
    
    elif e > 0:
        k = e - 2
        kv = e - k
        if (k >= 8):
            l = k - 8
            lv = k - l
            if (l >= 18):
                m = l - 18
                mv = l - m
                if (m >= 32):
                    n = m - 32
                    nv = m - n
                    if (n >= 32):
                        o = n - 32
                        ov = n - o
                        if (o >= 18):
                            p = o - 18
                            pv = o - p
                            if (p >= 8):
                                q = p - 8
                                qv = p - q
                            elif (p < 8 and p != 0):
                                qv = p

                        elif (o < 18 and o != 0):
                            pv = o
                    elif (n < 32 and n != 0):
                        ov = n
                elif (m < 32 and m != 0):
                    nv = m
            
            elif (l < 18 and l != 0):
                mv = l
        
        elif (k < 8 and k != 0):
            lv = k
    
    print(f'K layer = {kv}')
    print(f'L layer = {lv}')
    print(f'M layer = {mv}')
    print(f'N layer = {nv}')
    print(f'O layer = {ov}')
    print(f'P layer = {pv}')
    print(f'Q layer = {qv}')



line()
print("""Main menu
[ 1 ] Start
[ 2 ] About
[ 3 ] Quit
""")
option = int(input('Choose an option: '))
line()

while option != 3:
    if option == 1:
        en = int(input('Type a number of electrons to distribute: '))
        line()
        distribution(en)
        line()
        print("""Main menu
[ 1 ] Start
[ 2 ] About
[ 3 ] Quit
        """)
        option = int(input('Choose an option: '))
        line()
    
    elif option == 2:
        print("""This is a program made for education, more specifically made for chemistry or physics.""")
        line()
        break

    elif option == 3:
        break

print('It was good to see you')
sleep(2)
