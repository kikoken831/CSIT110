from typing import Union


name = 'Kendrick Kee'
student_num = '7366814'
subject_code = 'CSIT110'
#=========insert solution to question 1 here=============#


class Employee:

    def __init__(self, dic: dict):#takes dict obj 
        self.name: str = dic["name"]#name == key.name
        self.sales: dict[str, int] = dic["sales"]#sales dict = sales.key

    @classmethod#class method for dict2class
    def dict_to_class_obj(cls, li: list[dict]) -> list:
        emp_li: list[Employee] = []#create output list
        for x in li:
            emp_li.append(cls(x))#initiate and append employee obj to output list
        return emp_li #return list

    def get_weighted_sales(self, weights: dict[str, float]) -> float:#take in dict of str and float
        sales: float = 0
        for k, v in weights.items():#iterate dict
            try:
                if k in self.sales.keys():#if key match sum the weighted sale value
                    sales += v * float(self.sales[k])
                else:#raise exception as it does not exist
                    raise ProductNotFoundError(self.name, k)
            except ProductNotFoundError as e:
                return e#print error msg of __str__
                #pass#proceed with the next product (PLEASE CHECK IF PROGRAM SHOULD PROCEED OR BREAK)
        return sales#return total sales

#============end of solution to question 1===============#
#=========insert solution to question 2 here=============#


class ProductNotFoundError(Exception):

    def __init__(self, name: str, product: str):#product not found exception
        self.name = name
        self.product = product

    def __str__(self) -> str:#return this error msg when found
        return (f'{self.product} sales quantity cannot be found in {self.name}’s sales results')

#============end of solution to question 2===============#
#=========insert solution to question 3 here=============#


class InvalidDepthError(Exception):
    def __str__(self) -> str:#returns this error msg when found
        return 'Invalid Depth'


class WaterBody:
    RHO = 997#class atrrbs
    G = 9.81

    def __init__(self, volume: Union[int, float]):#init with Union as vol can either only be int or float
        self.volume = volume

    def get_water_mass(self) -> float:
        return self.RHO * self.volume#return water mass

    @classmethod
    def get_hydrostatic_pressure(cls, depth: float) -> float:#class mthd that takes depth
        try:
            if cls.RHO * cls.G * depth < 0:#if pressure is less than 0 raise error
                raise InvalidDepthError
            else:
                return cls.RHO * cls.G * depth#else return volume
        except InvalidDepthError as e:
            return e#print error when found


#============end of solution to question 3===============#
#=========insert solution to question 4 here=============#
def myClass_get_int_unit_test(inputClass)->Union[str,int]:#Union for returning either str or int as error msg are str and get_integer by nature should return int
    try:
        obj = inputClass()
        return obj.get_integer()#try get_integer method and see if errors are raised, will cause exception error otherwise
    except AttributeError:#error msgs based on assignment doc
        return 'A'
    except ValueError:
        return 'V'
    except:
        return 'O'


#============end of solution to question 4===============#
def myClass_demo_unit_test(inputClass):
    """ This example takes in a class definition as input,
        then instantiates a class object and test its method
        in a try except system.
    """
    try:
        obj = inputClass()
        obj.demo()
    except ValueError as e:
        print('A ValueError was raised because ' + str(e))

def example():
    # A class with one method
    class MyClass():
        def __init__(self):
            pass

        def demo(self):
            raise ValueError('Wrong input given!')
    # test the demo method
    myClass_demo_unit_test(MyClass)

def main():
    print("Assignment4")
    #example()
    """
    weights ={"product_1":1.0,"product_51":3.0}
    e2 = Employee.dict_to_class_obj([{ "name": "Rajah Din","sales": {"product_0": 3,"product_2": 5,"product_4": 4,},},{"name": "JafarMin","sales": {"product_1": 1,"product_2": 3,"product_5": 5,},}])
    print(e2[1].get_weighted_sales(weights))
    
    w = WaterBody(2)
    print(w.get_hydrostatic_pressure(-100))
    """
if __name__ == '__main__':  # DO NOT EDIT THESE TWO LINES.Y
    main()
