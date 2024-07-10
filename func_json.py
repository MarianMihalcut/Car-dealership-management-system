import misc
import os.path
import menu

#option1
def add_car_brand(brand:str)->None:
    dict=misc.extract_dict()
    if brand in dict: #if the brand is already in dictionary
        misc.calc_time_for_error()
        with open("errors.txt","a") as f:
            f.write("Couldn't overwrite an existing field in data.json\n")
        menu.error_msg()
    else:
        dict[brand]=[]
        misc.save_changes_json(dict)
        print("Car brand added successfully.")

def option_1()->None:
    file_exists=os.path.exists("data.json")
    if file_exists==False:
        misc.no_json_file_err()
    else:
        brand=input("Please input a car brand:")
        add_car_brand(brand)
            
#option2
#The fields are: Type(string),Year(number),Price(number),Stock(number)
def add_car_model(brand:str,type:str,year:int,price:int,stock:int)->None:
    dict=misc.extract_dict()
    if brand not in dict:
        misc.calc_time_for_error()
        with open("errors.txt","a") as err:
            err.write("Please add the car brand in database first.\n")
        menu.error_msg()
    else:
        dict1={
            "Type":type,
            "Year":year,
            "Price":price,
            "Stock":stock
        }
        #make more efficient
        if dict1 in dict[brand]:
            misc.calc_time_for_error()
            with open("errors.txt","a") as err:
                err.write("Please do not add duplicates in database\n")
            menu.error_msg()
        else:
            dict[brand].append(dict1)
            misc.save_changes_json(dict)
            print("Car model added successfully.")

def option_2()->None:
    file_exists=os.path.exists("data.json")
    if file_exists==False:
        misc.no_json_file_err()
    else:
        print("Please enter the car type data...")
        type=input('Type:')
        year=int(input('Year:'))
        price=int(input('Price(in dollars):'))
        stock=int(input('Nr of cars in stock:'))
        brand=input('Now please enter the correct car brand:')
        add_car_model(brand,type,year,price,stock)
    
#option3
def search_field(dictionary:dict,brand:str,search:str,info:any):
    list=dictionary[brand]
    for index in range(0,len(list)):
        if list[index][search]==info:
            return True,index
    return False,None

def option_3()->None:
    file_exists=os.path.exists("data.json")
    if file_exists==False:
        misc.no_json_file_err()
    else:
        print('Note:Be careful when changing the brand! May result in wrong results at output.')
        print('Please select which information you want to change:')
        print('1. Car brand')
        print('2. Type')
        print('3. Year')
        print('4. Price')
        print('5. Stock')
        nr=int(input('Please input the coresponding number:'))
        dict=misc.extract_dict()

        #first choice
        if nr==1:
            str1=input('Please input the car brand you want to search:')
            str2=input('Please input the car brand you want to replace with:')
            if str1 not in dict:
                print("The requested word has not been found.")
            else:
                if str2 in dict:
                    misc.calc_time_for_error()
                    with open("errors.txt","a") as err:
                        err.write("Replacing a car brand with an existent car brand is not allowed\n")
                    menu.error_msg()
                else:
                    dict[str2]=dict[str1]
                    del dict[str1]
                    misc.save_changes_json(dict)
                    print("Brand name replacing successfully.")

        #second choice
        if nr==2:
            brand=input('Please input the car brand:')
            current_type=input('Please input the car type to find:')
            new_type=input('Please input the car type to replace:')
            if brand not in dict:
                print('The car brand has not been found.')
            else:
                [found,index]=search_field(dict,brand,"Type",current_type)
                if found==False:
                    print('Car type has not been found.')
                else:
                    dict[brand][index]["Type"]=new_type
                    misc.save_changes_json(dict)
                    print("Replacement was successful.")
        
        #third choice
        if nr==3:
            brand=input('Please input the car brand:')
            type=input('Please input the car type:')
            year=int(input('Please input the year to replace with:'))
            if brand not in dict:
                print('The car brand has not been found.')
            else:
                [found,index]=search_field(dict,brand,"Type",type)
                if found==False:
                    print('Car type has not been found.')
                else:
                    dict[brand][index]["Year"]=year
                    misc.save_changes_json(dict)
                    print('Replacement was successful.')
        
        #fourth choice
        if nr==4:
            brand=input('Please input the car brand:')
            type=input('Please input the car type:')
            price=int(input('Please input the price to replace with:'))
            if brand not in dict:
                print('The car brand has not been found.')
            else:
                [found,index]=search_field(dict,brand,"Type",type)
                if found==False:
                    print('Car type has not been found.')
                else:
                    dict[brand][index]["Price"]=price
                    misc.save_changes_json(dict)
                    print('Replacement was successful.')
        
        #fifth choice
        if nr==5:
            brand=input('Please input the car brand:')
            type=input('Please input the car type:')
            stock=int(input('Please input the stock to replace with:'))
            if brand not in dict:
                print('The car brand has not been found.')
            else:
                [found,index]=search_field(dict,brand,"Type",type)
                if found==False:
                    print('Car type has not been found.')
                else:
                    dict[brand][index]["Stock"]=stock
                    misc.save_changes_json(dict)
                    print('Replacement was successful.')

#option 4
def option_4()->None:
    file_exists=os.path.exists("data.json")
    if file_exists==False:
        misc.no_json_file_err()
    else:
        dict=misc.extract_dict()
        brand=input('Please input the brand:')
        type=input('Please input the car type you want to delete:')
        if brand not in dict:
            print('Car brand has not been found')
        else:
            [found,index]=search_field(dict,brand,"Type",type)
            if found=='False':
                print("Car type has not been found.")
            else:
                del dict[brand][index]
                misc.save_changes_json(dict)
                print("Car type deleted successfully.")

#option5
def option_5()->None:
    file_exists=os.path.exists("data.json")
    if file_exists==False:
        misc.no_json_file_err()
    else:
        dict=misc.extract_dict()
        brand=input('Please input the car brand:')
        if brand not in dict:
            print('Car brand has not been found')
        else:
            del dict[brand]
            misc.save_changes_json(dict)
            print('Car brand deleted successfully.')


            





        


            

    

    
    