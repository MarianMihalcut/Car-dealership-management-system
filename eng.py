import json
import misc
import os.path
import menu
import csv

def create_json_file()->None:
    path=os.path.exists("data.json")
    if path==True: 
        misc.calc_time_for_error()
        with open("errors.txt","a") as err:
            err.write("Attempt to override the data.json file in eng. menu\n")
        menu.error_msg()
    else:
        with open("data.json","w") as file:
            json.dump({},file)
            print("File created. Returning to main menu...\n")
            

def clear_database()->None:
    dict={}
    path=os.path.exists("data.json")
    if path==True: 
        misc.calc_time_for_error()
        with open("errors.txt","a") as err:
            err.write("Trying to use a non-existent json file\n")
        menu.error_msg()
    else:
        with open("data.json","w") as file:
            json.dump(dict,file)
            print("Database cleared successfully. Returning to main menu...")


def list_json_content()->None:
    path=os.path.exists("data.json")
    if path==False:
        misc.calc_time_for_error()
        with open("errors.txt","a") as err:
            err.write("Trying to use non-existent json file\n")
        menu.error_msg()
    if path==True:
        with open("data.json","r") as file:
            dict=json.load(file)
            dict1=json.dumps(dict,indent=4) 
            print(dict1)

def list_csv_content()->None:
    path=os.path.exists("data.csv")
    if path==False:
        misc.calc_time_for_error()
        with open("errors.txt","a") as err:
            err.write("Trying to use a non-existent csv file\n")
        menu.error_msg()
    if path==True:
        with open("data.csv","r") as file:
            csvFile=csv.reader(file,dialect="excel")
            for lines in csvFile:
                print(lines)

def list_error_log()->None:
    path=os.path.exists("errors.txt")
    if path==False:
        print("There are no errors reported within the program.\n")
    else:
        with open("errors.txt","r") as file:
            string=file.read()
            print(string)
