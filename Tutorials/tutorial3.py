
"""
l1 = [1,2,3,4,1,2,3,4]
l2 = [1,2,3,4,1,2,3,4,2000]
l3 = [2,3,4,1,2,3,4,2000]
l4 = [2,3,4,1,2,3,4,0]
l5 = [1,2,3,4,1,2,3,4,0]
for x in range(len(l5)):
    l5[x] = l5[x] + 10
print(l5)
for x in range(len(l5)):
    l5[x] = 10
print(l5)
for x in range(len(l5)):
    l5[x] += x
print(l5)
l5.clear()
print(l5)
"""


def qn2():
    x = int(input("How many square numbers to genreate? "))
    li = []
    for i in range(x):
        li.append(i*i)
    print("Here is a list of generated squares: ", li)
# qn2()


def qn3():
    x = int(input("How many Fibonacci numbers to generate? "))
    li = [0, 1]

    for i in range(2, x):

        li.append(li[i-1]+li[i-2])

    print("Here is a list of generated Fibonacci numbers: ", li)
# qn3()


def qn4():
    li = []
    while True:
        x = input("Enter an integer (enter QUIT to quit) : ")
        if x == "QUIT":
            break
        li.append(int(x))
    print(li)
# qn4()


def qn5():
    state_abb = {"NSW": "New South Wales", "ACT": "Australian Capital Territory", "NT": "Northern Territory",
                 "QLD": "Queensland", "SA": "South Australia", "TAS": "Tasmania", "VIC": "Victoria", "WA": "Western Australia"}
    print(state_abb.get("QLD"))
    print(state_abb.get("VIC"))

# qn5()


def qn6():
    user_info = {"first_name": "Amanda", "last_name": "Smith", "age": 20}
    print(user_info.get("first_name"))
    user_info["last_name"] = "Harrison"
    user_info["email"] = "a.harrison@gmail.com"
    print(user_info)
    del user_info["age"]
    print(user_info)

# qn6()


def qn7():
    x = input("Enter state NSW/ACT/NT/QLD/SA/TAS/VIC/WA: ")
    state_abb = {"NSW": "New South Wales", "ACT": "Australian Capital Territory", "NT": "Northern Territory",
                 "QLD": "Queensland", "SA": "South Australia", "TAS": "Tasmania", "VIC": "Victoria", "WA": "Western Australia"}
    if(state_abb.get(x) is None):
        print("Sorry please enter a valid code.")
    else:
        print("You have entered", state_abb.get(x))

# qn7()


def qn8():
    x = input("Enter a key (string) ")
    y = input("Enter a value: ")
    d = {x: y}
    x = input("Enter a key (string) ")
    y = input("Enter a value: ")
    d[x] = y
    print(d)

# qn8()


def qn9():
    dic1 = {12: 144, 13: 169}
    dic2 = {3: 33, 4: 44}
    dic3 = {5: 510, 6: 632}
    Sample_dictionary = {}
    Sample_dictionary.update(dic1)
    Sample_dictionary.update(dic2)
    Sample_dictionary.update(dic3)
    print(Sample_dictionary)

# qn9()


def qn10():
    school = {"classA": {
        "student": {
            "name": "Merlion Tan",
            "subjects": {
                "phython": 70, "communications": 80}}}}
    print(school["classA"]["student"]["subjects"]["communications"])

# qn10()


def qn11():
    sampleDict = {
        "name": "Kelly",
        "interest": "badminton",
        "age": 32,
        "town": "Ang Mo Kio"}

    sampleDict["district"] = sampleDict.pop("town")
    print(sampleDict)

# qn11()


def qn12():
    inventory = {'coins': 500,
                 'pouch': ['flint', 'twine', 'gemstone'],
                 'haversack': ['wooden spear', 'dagger', 'fish', 'drumstick']}
    inventory["equipped"] = ['ruby', 'red', 'potion', 'apple']
    inventory["haversack"].sort()
    inventory["haversack"].remove('dagger')
    inventory['coins'] += 50
    print(inventory)
# qn12()


def qn13():
    stock = {"sunblock": 25, "swimming cap": 2, "ear plugs": 4, "goggles": 15}
    unit_price = {"sunblock": 16, "swimming cap": 10,
                  "ear plugs": 1.5, "goggles": 9.9}
    li = []
    for key in stock:
        li.append(key)
    print(li)
    sum = 0.0
    for x in li:
        sum += stock[x] * unit_price[x]
    sum += 0.07
    print(f'The total checkout price is {sum:.2f}')
# qn13()


def triple(x: str):
    result = ''
    for i in x:
        result += i*3
    return result

#print(triple("little fish"))


def next_number(x: int):
    if(x % 2 == 0):
        return 3*x + 1
    else:
        return 2*x + 2


# print(next_number(2))

def qn17():
    x = int(input("Enter the initial number: "))
    count = 0
    print("Sequence: ")
    while(x <= 1000000):
        print(f"Step{count:>3}: {x}")
        x = next_number(x)
        count += 1

# qn17()


# qn3()

def filter_digit(data):
    itmp = ""
    sum = 0
    for x in data:
        if type(x) == int:
            itmp += str(x)

    for x in itmp:
        sum += int(x)

    return itmp, sum


li = [0, "egg", 1, "egg", 5, "cat", 77]
# print(filter_digit(li))


def compute_hypothenuse(p1: float, p2: float) -> float:
    return ((p1*p1) + (p2*p2))**0.5


def get_area_of_circle(p1: float = 1.0):
    from math import pi
    return (p1*p1)*pi

# print(get_area_of_circle())


def get_volume_of_cylinder(p1: float, p2: float = 10.0) -> float:
    return get_area_of_circle(p1)*p2


def is_prime_number(p1: int) -> bool:
    if p1 > 1:
        for x in range(2, int(p1/2)+1):
            if p1 % x == 0:
                return False

        return True
    else:
        return False
# print(is_prime_number(15))


def get_next_prime_number(i: int) -> int:
    t = i+1
    while(True):
        if is_prime_number(t):
            return t
        else:
            t += 1

# print(get_next_prime_number(97))


def bin_to_dec(s: str) -> int:
    sum = 0
    count = 0
    for x in range(len(s)-1, -1, -1):
        sum += int(s[x])*(2**count)
        count += 1

    return sum

# print(bin_to_dec("01011"))


class Employee:
    fn = ""
    ln = ""
    en = ""
    pos = ""
    phone = ""
    def __init__(self, fn, ln, en, pos, phone):
        self.fn = fn
        self.ln = ln
        self.en = en
        self.pos = pos
        self.phone = phone
    def display(self):
        print(self.fn, self.ln, self.en, self.pos, self.phone)
    def __str__(self):
        return f"Employee ({self.en}, {self.fn}, {self.ln}, {self.pos}, {self.phone})"
    def __repr__(self):
        return f"Employee ({self.en}, {self.fn}, {self.ln}, {self.pos}, {self.phone})"
    


#e2 = Employee("John", "Smith", "12345678", "Software Engineer", "ext 4567")
#print(e2)


class Pizza:
    ingredients = []
    def __init__(self,ingredients: list):
        self.ingredients = ingredients.copy()
    def __repr__(self) -> str:
        output = "Pizza Ingredients: "
        for x in self.ingredients:
            output += x + ", "
        output = output[:-2]
        return output
li = ["dough","cheese","sauce","meat","oil"]
p1 = Pizza(li)
print(str(p1))
print(li)