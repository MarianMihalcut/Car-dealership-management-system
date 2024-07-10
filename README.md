# Car Dealership Management Database

<strong>Note</strong>: This project is not meant to be used in commercial purposes without owner's approval.

<h2>Description</h2>
This is a Python based database which is used to manage the sell of cars for a dealership. Initially, the back part of the project will be done, which is mainly formed of Python script, but also uses <strong>.json</strong> and <strong>.csv</strong> files. The dealership will use it to add, delete and monitor the products available at their dealership.<br>

<h2>How to use the application</h2>
Download the repository, extract and place the content in a folder. Ensure that you have Python 3.11 installed or the VS Code Python extention, in case you want to use inside VS. Use the following command line:<br>
<strong>python3 main.py</strong>
<br>When running the command, ensure that you use powershell in the right directory.<br>
Use:
<strong> cd (copied directory path)</strong><br>
You don't need to create the json and csv files directly. They'll be created trough the program.
However, you'll need to create the json file by using engineering menu. Use one of the 10 codes from <strong>key.txt</strong> to access it and generate the json file necessary for database.
Keys are not meant to be released for the usual user; they are just for developers in order to access exclusive functions helping them manipulate the files or visualize the errors.
<br>
If you enconter any bugs, please report them at this link:
https://forms.gle/X31GQXhUCZdfEN3S9
<br>

<h2>Short documentation for some functions</h2>
In menu.py:<br>
<strong> Pass_check </strong> -- takes a string, which is password prompted by user, and returns a bool. Functions verifies that the password is one of the 10 keys provided by project builder.
<br><br>
In misc.py:<br>
<strong> calc_time_for_error </strong> -- Calculates the time when a program error occurs and writes the time in file errors.txt . It is complementary with any kind of error which is writen in the errors file.<br>
<strong> extract_dict </strong> -- Extracts the file content from data.json and returns it as a dictionary.<br>
<strong> no_json_file_err </strong> -- Prints a short information about absence of data.json file in errors.txt<br>
<strong> save_changes_json </strong> -- Saves the changes done to the current dictionary into the json file.
<br><br>
In func_json.py:<br>
<strong> add_car_brand </strong> -- adds a car brand with an empty list in database<br>
<strong> add_car_model </strong> -- adds a new car model at a specific brand. Also ensures that no duplicates are created.<br>
<strong> search_field </strong> -- searches the car type of a brand and returns the index if it's found. A note is "search" variable takes only "Type" field from dictionaries.