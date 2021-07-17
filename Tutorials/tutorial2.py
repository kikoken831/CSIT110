def qn1():
    for x in range(10):
        print(f'{x+1} + {x+1} = {(x+1)*2}')


def qn2():
    for x in range(10):
        print(f'{x+1:^3}x{x+1:>3} ={(x+1)*(x+1):>4}')
def qn3():
    for x in range(10):
        print(x,end='')
        if(x < 9):
            trail = ' - '
        else:
            trail = '\n'
        print(trail,end='')

    for y in range(10):
        print(y,end='')
        if(y<9):
            trail = ' : '
        else:
            trail = '\n'
        print(trail,end='')
def qn4():
    for x in range(12,21,2):
        print(x,end='')
        if(x<20):
            trail = ", "
        else:
            trail = ".\n"
        print(trail,end='')
    z = 1.2
    for y in range(5):
        
        print(f'{z:.1f}',end="")
        if(y<4):
            trail = " * "
        else:
            trail = '.\n'
        print(trail,end='')
        z = z + 0.2

    for i in range(10):
        if(i%2 != 0):
            print(i,end='')
            if(i<9):
                trail = "; "
            else:
                trail = '.\n'
            print(trail,end='')

def qn5():
    s = ''
    for x in range(0,21,2):
        s += str(x)
        print(s)

def qn6():
    x = int(input("Enter a number (1-9): "))
    print("Go forward:")
    for i in range(1,x+1):
        print(f'{i}{"?"*i}')
    print("Go backward")
    for i in range(x,0,-1):
        print(f'{"-"*i}{i}')
    print()

def qn7():
    min = int(input("Enter the minimum integer: "))
    max = int(input("Enter the maximum integer: "))
    print(f'{"Number":<10}{"Sign":<20}{"Parity":<6}')
    for x in range(min,max+1):
        if(x < 0):
            text = "Negative"
        if(x == 0):
            text = "Zero"
        if(x > 0):
            text = "Positive"
        if(x%2 == 0):
            par = "Even"
        else:
            par = "Odd"
        print(f'{x:<10}{text:<20}{par:<6}')

def qn8():
    counter = 1
    while(counter<=10):
        print(counter,end="")
        if(counter<10):
                trail = " : "
        else:
            trail = '\n'
        print(trail,end='')
        counter = counter + 1
    print()
    counter = 2
    while(counter <= 10):
        print(counter,end="")
        if(counter<10):
                trail = " * "
        else:
            trail = '.\n'
        print(trail,end='')
        counter = counter + 2
    print()
    counter = 1
    while(counter<=10):
        print(counter,end="")
        if(counter<10):
                trail = "; "
        else:
            trail = '.\n'
        print(trail,end='')
        counter = counter + 2
    print()
def qn9():
    for x in range(2,11,2):
        print(f'{x:>2} + {x:>2} = {(x)*2:>2}')

def qn10():
    flag = True
    sum = 0
    count = 0
    ecount = 0
    pcount = 0
    ncount = 0
    while(flag):
        c = input("Enter an integer or q to quit: ")
        if(c == 'q'):
            flag = False
            break
        i = int(c)
        sum = sum + i
        count += 1
        if(i%2 == 0):
            ecount += 1
        if(i>0):
            pcount += 1
        if(i<0):
            ncount += 1
    print()
    print("Summary information: ")
    print(f'You have entered {count} integers. The sum of these numbers is {sum}.')
    print(f'There are {ecount} even numbers.')
    print(f'There are {count-ecount} odd numbers. There are {pcount} positive numbers.')
    print(f'There are {ncount} negative numbers.')


"""   
qn1()
print()
qn2()
print()
qn3()
print()
qn4()
print()
qn5()
print()
qn6()
print()
qn7() 
print()
qn8()
print()
qn9()
print()
qn10()
"""