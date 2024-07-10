import csv
import os.path
import misc

def option_9()->None:
    file_exists=os.path.exists("data.json")
    if file_exists=='False':
        misc.no_json_file_err()
    else:
        dict=misc.extract_dict()
        with open("data.csv","w") as file:
            header=["Brand","Type","Year","Price","Stock"]
            csv_reader=csv.writer(file,dialect="excel",delimiter=',',skipinitialspace=True,lineterminator='\n')
            csv_reader.writerow(header)
            for brand in dict:
                for index in range(0,len(dict[brand])):
                    list=[
                        brand,
                        dict[brand][index]["Type"],
                        dict[brand][index]["Year"],
                        dict[brand][index]["Price"],
                        dict[brand][index]["Stock"]
                    ]
                    csv_reader.writerow(list)
                    