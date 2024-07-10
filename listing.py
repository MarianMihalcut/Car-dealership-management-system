import os.path
import misc
import func_json

def option_6()->None:
    file_exists=os.path.exists("data.json")
    if file_exists=='False':
        misc.no_json_file_err()
    else:
        dict=misc.extract_dict()
        brand=input('Please input the car brand:')
        type=input('Please input the car type:')
        if brand not in dict:
            print("Car brand has not been found.")
        else:
            [found,index]=func_json.search_field(dict,brand,"Type",type)
            if found=='False':
                print('Car type has not been found.')
            else:
                print("Year:",end=' ')
                print(dict[brand][index]["Year"])
                print("Price:",end=' ')
                print(dict[brand][index]["Price"])
                print("Stock:",end=' ')
                print(dict[brand][index]["Stock"])

def option_7()->None:
    file_exists=os.path.exists("data.json")
    if file_exists=='False':
        misc.no_json_file_err()
    else:
        dict=misc.extract_dict()
        brand=input('Please input the car brand:')
        if brand not in dict:
            print("Car brand has not been found.")
        else:
            for index in range(0,len(dict[brand])):
                print("Type:",end=' ')
                print(dict[brand][index]["Type"])
                print("Year:",end=' ')
                print(dict[brand][index]["Year"])
                print("Price:",end=' ')
                print(dict[brand][index]["Price"])
                print("Stock:",end=' ')
                print(dict[brand][index]["Stock"])
                print()

def option_8()->None:
    file_exists=os.path.exists("data.json")
    if file_exists=='False':
        misc.no_json_file_err()
    else:
        dict=misc.extract_dict()
        print("%10s %10s %10s %10s %10s"%("Brand","Type","Year","Price","Stock"))
        print()
        for brand in dict:
            for index in range(0,len(dict[brand])):
                print("%10s %10s %10d %10d %10d"%(brand,dict[brand][index]["Type"],dict[brand][index]["Year"],dict[brand][index]["Price"],dict[brand][index]["Stock"]))
            print()

            