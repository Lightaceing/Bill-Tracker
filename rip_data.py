#read all files from a dir and write the info to a csv file
import os
import csv
import pandas as pd
import json

# TODO : Add compatibility with other file types
# TODO : #savelist[0] coz saving data to that, mayube needs to be changed???? Fn save_df_to_csv
# TODO : Files need to be saved in 1 format only

def extract_bill_type(file_name):
    #Extracting amount
    temp = file_name.rsplit('.pdf')[0].rsplit('-')[0:1]
    #converting to string
    bill_type = ''
    for i in temp:
        bill_type +=i
    return bill_type

def extract_date(file_name):
    #Extracting date
    full_date = ''
    bill_date = file_name.rsplit('.pdf')[0].rsplit('-')[1:4]

    #Adding the dates up together to form a proper format DD-MM-YYYY
    for each in bill_date:
        full_date = full_date + each + "-" 
    full_date = full_date.rstrip('-')
    return full_date

def extract_amount(file_name):
    #Extracting amount
    temp = file_name.rsplit('.pdf')[0].rsplit('-')[4:5]
    #converting to string
    bill_amount = ''
    for i in temp:
        bill_amount +=i
    return bill_amount

def extract_extra_info(file_name):
    try:
        extra_info = file_name.rsplit('.pdf')[0].rsplit('-')[5:6]
        #converting to string
        temp = ''
        for i in extra_info:
            temp +=i
        return temp
    
    except:
        pass

def extract_info_from_json(json_file):
    f = open(json_file)
    data = json.load(f)

    #Only Extracting from files under "dir_to_search"
    list_of_dir_to_search = []
    for i in data['dir_to_search']:
        list_of_dir_to_search.append(i)
    
    #Only Extracting from files under "dir_to_save"
    list_of_dir_to_save = []
    for i in data['dir_to_save']:
        list_of_dir_to_save.append(i)

    return list_of_dir_to_search, list_of_dir_to_save

def create_df_from_dir(dir):

    df = pd.DataFrame(columns=['Date', 'Amount', 'Extra Information'])
    file_names = os.listdir(dir)

    for name in file_names:

        bill_type = extract_bill_type(name)
        full_date = extract_date(name)
        bill_amount = extract_amount(name)
        extra_info = extract_extra_info(name)
        
        #print(f"Full date : {full_date}, Bill Amount : {bill_amount}, Extra Info : {extra_info} ")
        df.loc[len(df.index)] = [full_date, bill_amount, extra_info]
    return bill_type, df

def gather_info_from_dirs(list_of_dir_to_search):
    for each_dir in list_of_dir_to_search:
        bill_type, df = create_df_from_dir(each_dir)
        
        #Saved to CSV File
        save_df_to_csv(df, save_list, bill_type)
        
        #Terminal o/p for testing
        print(df.head(10))

def save_df_to_csv(df, save_list, bill_type):
    #savelist[0] coz saving data to that, mayube needs to be changed????
    new_csv = save_list[0] + str(bill_type) + "_compiled_data.csv"
    df.to_csv(index=True, path_or_buf=new_csv)  

#Constants KINDA 
json_file_name = 'info.json'

#Function calls
search_list, save_list = extract_info_from_json(json_file_name)
gather_info_from_dirs(search_list)  
