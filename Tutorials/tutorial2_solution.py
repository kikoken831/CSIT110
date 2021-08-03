# question 1
for i in range(1,11):
    print(f"{i} + {i} = {i+i}")

# question 2
for i in range(1,11):
    print(f"{i:>2} x {i:>2} = {i*i:>3}")


# question 3
for i in range(1, 11):
    if i<10:
        trailing = " - "
    else:
        trailing = "\n"
    
    print(f"{i}", end= trailing)

for i in range(1, 11):
    if i<10:
        trailing = " : "
    else:
        trailing = "\n"

    print(f"{i}",end= trailing)


# question 4
# part1
for i in range(1, 6):  # 1,2,3,4,5
    if i<5:
        trailing = ", "
    else:
        trailing = ".\n"
    
    print(f"{10+2*i} ",end= trailing)

for i in range(12, 21, 2):  # 12,14,16,18,20
    if i<20:
        trailing = ", "
    else:
        trailing = ".\n"
    
    print(f"{i} ",end= trailing)

# part2
for i in range(1, 6):  # 1,2,3,4,5
    if i<5:
        trailing = " * "
    else:
        trailing = ".\n"
    
    print(f"{1+0.2*i}",end= trailing)

for i in range(12, 21, 2):  # 12,14,16,18,20
    if i<20:
        trailing = "* " #note: spacing difference
    else:
        trailing = ".\n"
    
    print(f"{i*0.1} ",end= trailing)

# part3
for i in range(1, 10, 2):  # 1,3,5,7,9
    if i<9:
        trailing = "; "
    else:
        trailing = ".\n"
    
    print(f"{i}",end= trailing)

for i in range(1, 6):  # 1,2,3,4,5
    if i<9:
        trailing = "; "
    else:
        trailing = ".\n"
    
    print(f"{i*2-1}",end= trailing)

# question 5  four solutions
for i in range(0, 21, 2):
    for m in range(0,i+1,2):
        print(m,end= "")
    print()

for i in range(0,12):
    # print(0, end= "")
    for m in range(0,i):
        print(m*2, end="")
    print()

for ith_row in range(0,11):
    #print(f"0{ith_row*2}")
    for ith_col in range(0, ith_row+1):
        print(ith_col*2, end="")
    print()

txt = ""
for i in range(0,11):
    txt += str(i*2)
    print(txt)

# question 6
num = input("Enter a number (1-9): ")
print("Go forward: ")
for i in range(1, num+1):
    print(str(i)+"?"*i)

for i in range(1, num+1):
    print(i, end="")
    for i_q in range(0,i):
        print("?", end="")
    print()

print("Go backward: ")
for i in range(1, num+1):
    print("-"*i+str(i))

for i in range(1, num+1):
    for i_q in range(0,i):
        print("-", end="")
    print(i)

# question 7
num_min = int(input("Enter the minimum integer: "))
num_max = int(input("Enter the maximum integer: "))
print()
print(f"\t{'Number':<9}{'Sign'<15}{'Parity':<6}")
for i in range(num_min, num_max):
    sign = "Zero"
    if i < 0:
        sign = "Negative"
    elif i > 0:
        sign = "Positive"
    parity = "Even"
    if i%2 != 0:
        parity = "Odd"
    print(f"\t{i:<9}{sign<15}{parity:<6}")

# question 8
i = 1
while i < 11:
    print(i, end= "")
    if i <10:
        print(" : ", end="")
    else:
        print()
    i += 1

i = 1
while i < 6:
    print(i*2, end= "")
    if i <5:
        print(" * ", end="")
    else:
        print(".")
    i += 1

i = 1
while i < 10:
    print(i, end= "")
    if i <9:
        print("; ", end="")
    else:
        print(".")
    i += 2
# question 9
i = 2
while i < 11:
    print(f"{i:>2} + {i:>2} = {i+i:>2}")
    i += 2

# question 10
total = 0
count_odd = 0
count_even = 0
count_pos = 0
count_neg = 0
while True:
    user_input = input("Enter an integer or q to quit: ")
    if user_input.lower() == "q":
        break
    num = int(user_input)
    if num%2==0:
        count_even += 1
    else:
        count_odd += 1
    if num >0:
        count_pos +=1
    else:
        count_neg +=1
    total += num
print()
print("Summary information:")
print(f"You have entered {count_odd + count_even} integers. "
+ f"The sum of these numbers is {total}.")
print(f"There are {count_even} even numbers.")
print(f"There are {count_odd} odd numbers.")
print(f"There are {count_pos} positive numbers.")
print(f"There are {count_neg} negative numbers.")