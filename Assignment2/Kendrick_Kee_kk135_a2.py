name = 'Kendrick Kee'
student_num = '7366814'  # UOW Student number
subject_code = 'CSIT110'


def question_1():
    #====insert solution here===#
    # Get imputs
    prompt1 = input("prompt1")
    prompt2 = input("prompt2")
    prompt3 = int(input("prompt3"))
    # loop x number or times, x being the int value of (prompt3)
    for i in range(prompt3):
        print(prompt1, end='')  # print prompt1 without newLine
        print(prompt2, end='')  # print prompt2 without newLine


def question_2():
    #====insert solution here===#
    # get upper bound
    upperB = int(input("Enter upper bound: "))
    # get gap
    gap = int(input("Enter gap: "))
    i = 0
    sum = 0
    # go forwards
    print("Go forward: ", end='')
    while(i <= upperB):
        print(str(i), end="")
        sum = sum + i
        i = i+gap
        if(i <= upperB):
            trailing = ", "
        else:
            trailing = '.'
        print(trailing, end='')
    print()
    print("Sum of numbers = " + str(sum))
    i = upperB
    sum = 0
    # go backwards
    print("Go backward: ", end='')
    while(i > 0):
        print(str(i), end='')
        sum = sum + i
        i = i-gap
        if(i > 0):
            trailing = ", "
        else:
            trailing = '.'
        print(trailing, end='')
    print()
    print("Sum of numbers = " + str(sum))
    # REMEMBER TO ADD THE COMMAS AND FULLSTOP


def question_3():
    # ====insert solution here===#]
    total_int = 0.0
    age = int(input("Enter current age: "))
    oa = float(input("Enter current amount in OA: "))
    sa = float(input("Enter current amount in SA: "))
    ma = float(input("Enter current amount in MA: "))
    total_int += oa*0.025
    total_int += sa * 0.04
    total_int += ma * 0.04
    if(age >= 55):
        ra = float(input("Enter current amount in RA: "))
        total_int += ra*0.04
        if(oa > 20000):
            oa = 20000
        total_sum = oa+sa+ma+ra
        if(total_sum >= 30000):
            total_int += 600
            total_sum -= 30000
            if(total_sum >= 30000):
                total_int += 300
                total_sum -= 30000
        total_int += total_sum*0.01
    else:
        if(oa > 20000):
            oa = 20000
        total_sum = oa+sa+ma
        if(total_sum >= 60000):
            total_int += 600
        else:
            total_int += total_sum*0.01

    print(f'Your interest rate this year will be ${total_int:.2f}')


def question_4():
    #====insert solution here===#
    state = True

    finalString = ""
    while(state):
        x = input("Filename?")
        finalString += x
        if(x == ""):
            state = False
            finalString = finalString[:-1]
        else:
            finalString += ","
            
    print(finalString)


def main():  # do not change this line
    print("Assignment 2")  # do not change this line
    # (3) UNCOMMENT THE FOLLOWING LINES TO TEST YOUR SOLUTION FOR EACH QUESTION
    #     YOU DO NOT HAVE TO LEAVE IT UNCOMMENTED DURING SUBMISSION.
    # question_1()
    # question_2()
    question_3()
    # question_4()


if __name__ == '__main__':  # do not change this line
    main()  # do not change this line
