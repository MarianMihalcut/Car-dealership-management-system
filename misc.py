import datetime
import json
import menu

def calc_time_for_error(): #also it's printing the time when error occurs aprox.
    with open("errors.txt","a") as f1:
            time_date=datetime.datetime.now()
            date_now=time_date.date()
            time_now=time_date.time()
            f1.write("["+str(date_now)+" "+str(time_now)+"]: ")

def extract_dict()->dict:
    with open("data.json","r") as file:
            d=json.load(file)
    return d

def no_json_file_err()->None:
    calc_time_for_error()
    with open("errors.txt","a") as err:
        err.write("There is no json file in directory. Create one from engineering menu\n")
    menu.error_msg()

def save_changes_json(dictionary:dict)->None:
    with open("data.json","w") as file:
        json.dump(dictionary,file,indent=4)