name = 'Kendrick Kee'
student_num = '7366814'  # UOW Student number
subject_code = 'CSIT110'


def question_1():
    #====insert solution here===#
    # Get imputs
    prompt1 = input("prompt1 ")
    prompt2 = input("prompt2 ")
    prompt3 = int(input("prompt3 "))
    # loop x number or times, x being the int value of (prompt3)
    for i in range(prompt3):
        print(prompt1, end='')  # print prompt1 without newLine
        print(prompt2, end='')  # print prompt2 without newLine
    print()


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
    while(i <= upperB):#loop so long as counter is not above the upper bound
        print(str(i), end="")
        sum = sum + i#get the sum
        i = i+gap#increment counter by gap amount
        if(i <= upperB):#trailing comma when not end of line
            trailing = ", "
        else:
            trailing = '.'#trailing . when end of line
        print(trailing, end='')
    print()
    print("Sum of numbers = " + str(sum))
    i = upperB
    sum = 0
    # go backwards
    print("Go backward: ", end='')
    while(i >= 0):#loop so long as counter is greater than 0
        print(str(i), end='')
        sum = sum + i#get the sum
        i = i-gap#decrement counter by gap amount
        if(i > -1):
            trailing = ", "#trailing with a comma when not end of line
        else:
            trailing = '.'#trailing . when end of line
        print(trailing, end='')
    print()
    print("Sum of numbers = " + str(sum))
    


def question_3():
    # ====insert solution here===#]
    total_int = 0.0
    age = int(input("Enter current age: "))#store age
    oa = float(input("Enter current amount in OA: "))#store OA
    sa = float(input("Enter current amount in SA: "))#store SA
    ma = float(input("Enter current amount in MA: "))#store MA
    #get basic interest for OA,SA,MA
    total_int += oa*0.025
    total_int += sa * 0.04
    total_int += ma * 0.04
    #check if age is above or equal 55
    if(age >= 55):
        ra = float(input("Enter current amount in RA: "))#prompt for RA when user is older than 55
        total_int += ra*0.04#store RA
        if(oa > 20000):#normalize OA to 20000 as extra interest calculations for OA is capped at 20000
            oa = 20000
        total_sum = oa+sa+ma+ra#get the total sum for extra interest computation with normalized OA
        if(total_sum >= 60000):#if total sum is >= 60k offer maximum interest of $900
            total_int += 900
        elif(total_sum >= 30000):#if total sum is >= 30k but not >60k
            total_int += 600#offer the 2% interest on the first 30k and 1% on the remainder amount
            total_int += ((total_sum%30000)*0.01)#get 1% of the remainder of the total sum
        else:
            total_int += (total_sum*0.02)
            
    else:#if age is below 55
        if(oa > 20000):#normalize the OA as its also capped at 20k
            oa = 20000
        total_sum = oa+sa+ma#get total sum
        if(total_sum >= 60000):#if total sum > 60k give maximum interest of $600
            total_int += 600
        else:#else give 1% on whatever is left
            total_int += total_sum*0.01

    print(f'Your interest rate this year will be ${total_int:.2f}')


def question_4():
  #====insert solution here===#
  state = True#status flag for ending the loop

  finalString = ""
  while(state):#loop until a blank line is detected
    x = input("Filename?")
    temp = ""
    skip = 0
    for i in x:
      if i == '[':
        skip += 1
      elif i == ']' and skip > 0:
        skip -= 1
      elif skip == 0:
        temp += i
    skip = 0
    x = removeNestedParentheses(x)
    print(temp)
    finalString += x#append to the cleaned string to the final string output 
    if(x == ""):#when a blankline is detected change state to false ending the loop
        state = False
        finalString = finalString[:-1]#delete the last trailing comma
    else:
        finalString += ","#append a trailing comma if it was a valid input
          
  print(finalString)


def main():  # do not change this line
    print("Assignment 2")  # do not change this line
    # (3) UNCOMMENT THE FOLLOWING LINES TO TEST YOUR SOLUTION FOR EACH QUESTION
    #     YOU DO NOT HAVE TO LEAVE IT UNCOMMENTED DURING SUBMISSION.
    # question_1()
    # question_2()
    # question_3()
    question_4()


if __name__ == '__main__':  # do not change this line
    main()  # do not change this line
