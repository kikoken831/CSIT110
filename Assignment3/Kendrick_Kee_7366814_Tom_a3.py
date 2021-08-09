name = 'Kendrick Kee'
student_num = '7366814'
subject_code = 'CSIT110'


#=========insert solution to question 1 here=============#
def process_subscription():
    # declare dict
    dic = {"Standard Food Delivery Plan": 13.40, "Premium Food Delivery Plan": 25.40,
           "Basic Commute Plan": 39.80, "Premium Commute Plan": 69.80,
           "All Access Plan(Lite)": 79.60, "All Access Plan(Premium)": 108.60}
    print("Packages available for subscription(price/mth)")
    # print key and values from dict using print f
    for k, v in dic.items():
        print(f'{k:<39}{"{:.2f}".format(v):>7}')
    selection = []  # create list to store active subs
    sum = 0  # create a sum for total cost output
    print()
    for k in dic.keys():  # iterate through all possible subs
        x = input(f'Subscribe to {k}? (Y/N): ')
        if x == 'Y' or x == 'y':  # if user keys in Y add key to selection li
            selection.append(k)
        # no check for "N" as it is assumed only Y and N is possible inputs
    print()
    print('Your selection:')
    if len(selection) == 0:  # if list is empty means no selection was made, hence print NONE
        print(' - None\n')
        print(f'Total cost ${"{:.2f}".format(sum)}')
    else:
        for i in selection:  # print "receipt" by getting the values with the keys stored in selection list
            print(f' - {i}(${"{:.2f}".format(dic[i])})')
            sum += dic[i]  # sum the values from the dict
        print()
        # print the sum as the total cost
        print(f'Total cost ${"{:.2f}".format(sum)}')

#============end of solution to question 1===============#
#=========insert solution to question 2 here=============#


def generate_qns_from_list(data: list) -> list:
    answer = []
    for x in data:
        sum = 0  # new answer at every iteration
        tempdic = {}  # new temp dict every iteration
        tempstr = ""  # new qns at every iteration
        if(len(x) >= 2):
            # get the answer of the equation and equation string
            for i in x:
                sum += i  # get the answer
                tempstr += str(i) + " + "  # equation string

            tempstr = tempstr[:-3]  # remove trailing + sign
            tempdic["qns"] = tempstr  # add qns key with string
            tempdic["ans"] = sum  # add ans key with answer int
            answer.append(tempdic)  # append to output list
        else:
            continue
    return answer


#============end of solution to question 2===============#
#=========insert solution to question 3 here=============#
class ShoppingCart:
    server_url: str = "128.123.123.0"

    def __init__(self, account_id: str):  # create intialiser that accepts the account ID as param
        # create a new dict with str and int as key and value types
        self.cart: dict[str, int] = {}
        self.account_id = account_id

    def __str__(self) -> str:  # used for testing
        return f"Server Url: {self.server_url}, AccountID: {self.account_id}, Cart: {self.cart}"

    def add_item_to_cart(self, product_name: str, quantity: int):
        if product_name in self.cart:  # if key is present
            # add the current qty with parameter's qty
            self.cart[product_name] += quantity
        else:
            # else key is not present, new key and qty is assigned
            self.cart[product_name] = quantity

    def remove_item_from_cart(self, product_name: str, quantity: int):
        self.cart[product_name] = self.cart[product_name] - \
            quantity  # reduce the cart qty with the parameter's qty
        if self.cart[product_name] == 0:  # if quantity for key is 0 delete the entire element
            del self.cart[product_name]

    def empty_cart(self):
        self.cart.clear()  # clears the cart dict

    def count_items(self) -> int:
        if bool(self.cart) == False:  # if dict is empty return 0
            return 0
        else:
            sum = 0
            for k in self.cart.keys():  # iterate keys
                sum += self.cart[k]  # sum the cart qty
            return sum

#============end of solution to question 3===============#
#=========insert solution to question 4 here=============#


def get_magic_num_checksum(ic_no: str) -> str:
    sum = 0
    magic_dict = {10: "A", 9: "B", 8: "C", 7: "D", 6: "E",
                  5: "F", 4: "G", 3: "H", 2: "I", 1: "Z", 0: "J"}  # dict for corresponding checksums
    weights = [2, 7, 6, 5, 4, 3, 2]  # list of weights
    for i in range(7):
        # sum the int with the corresponding weight
        sum += int(ic_no[i]) * weights[i]
    checksum = sum % 11  # mod 11 to get checksum int
    return magic_dict[checksum]  # return the Char coressponding to the chcksum


def get_car_plate_checksum(car_no: str) -> str:
    weights = [9, 4, 5, 4, 3, 2]  # list of weights
    checklist: list[int] = []  # empty int list for checksum computation
    splitted = car_no.split()  # split the str via whitespace
    # interate through the str and append to prefix if char or num_ser if int
    prefix = ""
    num_ser = ""
    for i in car_no:#Check if char is str type or int type
        try:
            int(i)
            num_ser += i #append to num series if int type
        except ValueError: #append to prefix as it is a str type
            prefix += i

    checksum = 0
    output = ['A', 'Z', 'Y', 'X', 'U', 'T', 'S', 'R', 'P',
              'M', 'L', 'K', 'J', 'H', 'G', 'E', 'D', 'C', 'B']  # list for possible output with 'A'' = 0 via index
    if len(prefix) == 3:  # if prefix has 3 chars
        # get int value of the second char ord(x) - 64 gets the alphabetical value where a = 1
        checklist.append(ord(prefix[1])-64)
        checklist.append(ord(prefix[2])-64)  # get int value of the third char
    elif len(prefix) == 2:  # if prefix has 2 chars
        # get int value of the first and second char
        checklist.append(ord(prefix[0])-64)
        checklist.append(ord(prefix[1])-64)
    elif len(prefix) == 1:  # if prefix has 1 char
        checklist.append(0)  # append 0 at the front of the checklist
        checklist.append(ord(prefix[0])-64)  # get the int value of the char

    if len(num_ser) == 4:  # if series has 4 ints
        for i in num_ser:
            checklist.append(int(i))  # append each int to the checklist
    elif len(num_ser) == 3:  # if series only has 3 or lesser ints append 0 per missing int before appending the ints
        checklist.append(0)
        for i in num_ser:
            checklist.append(int(i))
    elif len(num_ser) == 2:
        checklist.extend([0, 0])
        for i in num_ser:
            checklist.append(int(i))
    elif len(num_ser) == 1:
        checklist.extend([0, 0, 0])
        for i in num_ser:
            checklist.append(int(i))

    sum = 0
    for i in range(6):
        sum += int(checklist[i]) * weights[i]  # get the checksum total

    checksum = sum % 19  # mod 19 to get corresponding checksum value

    return output[checksum]  # output the char based on the list
#============end of solution to question 4===============#


def main():  # do not change this line
    print("Assignment 3")  # do not change this line
    # process_subscription()
    # input_list=[[1,3,3],[2,5,-1],[3,2],[4,5,3],[0,23],[1,2,3,4]]
    # print(generate_qns_from_list(input_list))
    """
    newCart = ShoppingCart("1234567")
    newCart.add_item_to_cart("fruit juice", 2)
    newCart.add_item_to_cart("tissue box", 4)
    newCart.add_item_to_cart("ice cream", 3)
    print(newCart)
    newCart.remove_item_from_cart("tissue box",1)
    newCart.remove_item_from_cart("fruit juice",2)
    print(newCart)
    print(newCart.count_items())
    newCart.empty_cart()
    print(newCart)
    print(newCart.count_items())
    
    while True:
        ip = input("Enter IC no: ")
        print(get_magic_num_checksum(ip))
    
    while True:
        ip = input("Enter carplate no: ")
        print(get_car_plate_checksum(ip))
    """

if __name__ == '__main__':  # do not change this line
    main()  # do not change this line
