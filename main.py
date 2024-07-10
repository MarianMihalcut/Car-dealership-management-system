import func_json
import func_csv
import eng
import menu
import listing
import time

def main():
   menu.welcome()
   while(True):
       print()
       menu.main_menu()
       selection=int(input('Please input the coresponding number with your selection:'))
       if selection==1:
           func_json.option_1()
           time.sleep(5)
       elif selection==2:
           func_json.option_2()
           time.sleep(5)
       elif selection==3:
           func_json.option_3()
           time.sleep(5)
       elif selection==4:
           func_json.option_4()
           time.sleep(5)
       elif selection==5:
           func_json.option_5()
           time.sleep(5)
       elif selection==6:
           listing.option_6()
           time.sleep(5)
       elif selection==7:
           listing.option_7()
           time.sleep(5)
       elif selection==8:
           listing.option_8()
           time.sleep(5)
       elif selection==9:
           func_csv.option_9()
           time.sleep(5)
       elif selection==10:
           while(True):
                menu.eng_menu() #function to ask for selection is already here
                num=int(input())
                if num==1:
                    eng.clear_database()
                    time.sleep(5)
                elif num==2:
                    eng.create_json_file()
                    time.sleep(5)
                elif num==3:
                    eng.list_json_content()
                    time.sleep(5)
                elif num==4:
                    eng.list_csv_content()
                    time.sleep(5)
                elif num==5:
                    eng.list_error_log()
                    time.sleep(10)
                elif num==6:
                    break
                elif num==7:
                    exit(0)
       elif selection==11:
           exit(0)



if __name__=='__main__':
    main()
