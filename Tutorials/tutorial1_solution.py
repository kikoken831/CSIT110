radius = 3
pi = 3.142
length = 4
breadth = 2.5

# 1
circumference = 2*pi*radius

# 2
area_of_circle = 2*pi*(radius**2)

# 3
perimeter_of_rect = (length+breadth)*2

# 4
area_of_rect = length*breadth

# 5
sol = (512-2**5)/(231+10)
print(sol)

# 6
x = int(input('Enter an integer: '))
# using end
print(x,end="---")
print(2*x,end="---")
print(3*x,end="---")
print(4*x)
# using sep
print(x, 2*x, 3*x, 4*x, sep='---')

# 7

x = 3+2
print(x)
print(type(x))  # int
x = 1 + 1.0 
print(x)
print(type(x))  # float
x = 17/3
print(x)
print(type(x))  # float
x = 8-5
print(x)
print(type(x))  # int
x = 5*6
print(x)
print(type(x))  # int
x = 16**2
print(x)
print(type(x))  # int
x = 2**3
print(x)
print(type(x))  # int
x = 16**0.5
print(x)
print(type(x))  # float
x = 34 % 6
print(x)
print(type(x))  # int
x = 18/5
print(x)
print(type(x))  # float
x = 18//5
print(x)
print(type(x))  # int

product_code = "377B"
product_name = "Beef Liquid Stock"
product_size = "250mL"
product_price = 2.15
# 14
print(product_code + ": " + product_name + ", " + product_size)

# 15
print("\"" + product_name + "\"," + product_size)

# 16
print(product_name + ", "
      + product_size + " $"
      + str(product_price))

# 17
print(f"{product_code}: {product_name}, {product_size}")

# 18
print(f'"{product_name}",{product_size}')
# 19
print(f"{product_name}, {product_size}, ${product_price:.2f}")

#20
print(f'{"President":<14}{"Secret Service Code Name":^30}In Office')
name = "Joe Biden"
code_name = '"Celtic"'
term = "2021-"
print(f"{name:<14}{code_name:^30}{term}")
name = "Donald Trump"
code_name = '"Mogul"'
term = "2017-2020"
print(f"{name:<14}{code_name:^30}{term}")
name = "Barack Obama"
code_name = '"Renegade"'
term = "2009-2017"
print(f"{name:<14}{code_name:^30}{term}")
name = "George W. Bush"
code_name = '"Tumbler"'
term = "2001-2009"
print(f"{name:<14}{code_name:^30}{term}")
name = "Bill Clinton"
code_name = '"Eagle"'
term = "1993-2001"
print(f"{name:<14}{code_name:^30}{term}")

#21
print("Alkali metals\n")
print("Alkali metals")
print()
print("Alkali metals", end="\n\n")
print(f"{'Element':<14}{'Symbol':<8}{'Atomic number':^16}{'Atomic weight':>14}")
element = "Lithium"
symbol = "Li"
AN = 3
Aw = 6.94
print(f"{element:<14}{symbol:<8}{AN:^16}{Aw:>14.3f}")
element = "Sodium"
symbol = "Na"
AN = 11
Aw = 22.9
print(f"{element:<14}{symbol:<8}{AN:^16}{Aw:>14.3f}")
element = "Potassium"
symbol = "K"
AN = 19
Aw = 39.098
print(f"{element:<14}{symbol:<8}{AN:^16}{Aw:>14.3f}")
element = "Rubidium"
symbol = "K"
AN = 19
Aw = 85.468
print(f"{element:<14}{symbol:<8}{AN:^16}{Aw:>14.3f}")
element = "Caesium"
symbol = "Cs"
AN = 55
Aw = 132.905
print(f"{element:<14}{symbol:<8}{AN:^16}{Aw:>14.3f}")
element = "Francium"
symbol = "Fr"
AN = 87
Aw = 230
print(f"{element:<14}{symbol:<8}{AN:^16}{Aw:>14.3f}")

#13
# False
# True
# False
# True
# False
# True
# True
# True
# False
# True
# True
# True
# True

#14
num_items = int(input("Enter the number of items: "))
# get items and postage cost
item_cost = 3
postage = 10
total_cost = 0
if num_items >50:
  item_cost = 2
  postage = 0
# calculate total cost
total_cost = num_items*item_cost + postage
print("Receipt:")
print(f"{num_items} items x ${item_cost} = {num_items*item_cost}")
print(f"Postage: ${postage:.2f}")
print(f"Total: ${total_cost:.2f}")
#15
num_items = int(input("Enter the number of items: "))
shipping = input("Enter shipping method (s/r/e): ")
# get items and postage cost
cost_item = 3
postage = 10
cost_total = 0
if shipping =="r":
  postage = 15
elif shipping == "e":
  postage = 20
if num_items >50:
  cost_item = 2
  postage = 0
  if shipping =="r":
    postage = 10
  elif shipping == "e":
    postage = 17
# calculate total cost
cost_total = num_items*cost_item + postage
print("Receipt:")
print(f"{num_items} items x ${cost_item} = {num_items*cost_item}")
if shipping == "r":
    post_name = "Registered"
elif shipping == "e":
    post_name = "Expressed"
else:
    post_name = "Standard"
print(f"{post_name} post: ${postage}")
print(f"Total: ${cost_total}")

# 16
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))
num4 = int(input("Enter the fourth integer: "))
num_max = num1
num_min = num1
if num2>num_max:
  num_max = num2
if num3>num_max:
  num_max = num3
if num4>num_max:
  num_max = num4
if num2<num_min:
  num_min = num2
if num3<num_min:
  num_min = num3
if num4<num_min:
  num_min = num4