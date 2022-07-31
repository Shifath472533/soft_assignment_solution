"""
    how to run the script:
        for normal indicators:
            python3 /home/shifath/soft_assignment/soft_assignment_solution.py /home/shifath/soft_assignment/data_cases_1.csv /home/shifath/soft_assignment/disease_list.csv
        for advance indicators:
            python3 /home/shifath/soft_assignment/soft_assignment_solution.py /home/shifath/soft_assignment/data_cases_1.csv /home/shifath/soft_assignment/disease_list.csv advance
"""

import re  # for using regular expression
import sys  # for commandline arguments
import csv  # for using reading csv
import json  # for reading saving json file
import pandas as pd  # for reading csv and doing analysis on it

def get_normal_result(data_df):
    '''
        this function calculates the result for normal indicator
        data_df -- is a dataframe which contains the data_cases csv file in a programmable form
    '''
    result_dict = {} # this stores the result as a dict instead of json
    # below line calculates "total number of reported cases is" by calculating the sum of 'total_number_cases' column
    result_dict["total number of reported cases is"] = str(data_df['total_number_cases'].sum())
    # below line calculates "total number of deaths reported at each location" as a dict (result_)
    # it is calculated by getting sum of 'number_mortality' column grouped by 'location'
    result_ = data_df.groupby(['location']).sum()['number_mortality'].to_dict()
    result_dict["total number of deaths reported at each location"] = result_
    # converting the int/float values to string for converting it to json
    for key in result_dict["total number of deaths reported at each location"]:
        result_dict["total number of deaths reported at each location"][key] = str(result_dict["total number of deaths reported at each location"][key])
    return result_dict

def get_advanced_result(data_df, disease_list_df):
    result_dict = {} # this stores the result as a dict instead of json
    # below line creates a dataframe by merging the main data_cases and disease_list by doing inner join
    # based on the id column
    merged_df = pd.merge(data_df, disease_list_df, how='inner', left_on = 'disease_id', right_on = 'id')
    # changing the 'name' column from disease_list_df to 'disease_name' for more clarity
    merged_df.columns = merged_df.columns.str.replace('name', 'disease_name')
    # creating a dataframe filtering for cats
    cat_df = merged_df.loc[merged_df['species']=='cat']
    # filtering location for villages and the calculating number of sick cats by doing mean
    result_ = round(cat_df.loc[cat_df['location'].str.contains('village', flags=re.I, regex=True)]['number_morbidity'].mean(), 2)
    result_dict["Average number of sick cats reported in reports from villages up to two decimal points"] = str(result_)
    # calculating the sum for each disease from the merged dataframe
    result_dict["total number of deaths from each disease"] = merged_df.groupby(['disease_name']).sum()['number_mortality'].to_dict()
    # converting the int/float values to string for converting it to json
    for key in result_dict["total number of deaths from each disease"]:
        result_dict["total number of deaths from each disease"][key] = str(result_dict["total number of deaths from each disease"][key])
    return result_dict

def read_csv(path):
    try:
        # reading csv file
        data_df = pd.read_csv(path)
        return data_df
    except:
        # reading csv file using csv reader
        reader = csv.reader(open(path, "r"))
        reader = list(reader)
        # setting the header
        header = reader[0]
        target_cols = len(header)
        rows = []
        # iterating through each row
        for row in reader[1:]:
            # if a row contains more than the header colums then extra columns are not concidered
            # mainly concidering the id column
            if len(row) > target_cols:
                modified_row = [" ".join(row[:-7])] + row[-7:]
                rows.append(modified_row)
            else:
                rows.append(row)
        # converting the rows to a dataframe a programmable form of csv file
        data_df = pd.DataFrame(rows, columns = header)
        # converting the type of values to integers for column 3 to 6
        data_df = data_df.astype({field:int for field in header[3:7]})
        return data_df
def read_disease_list(disease_list_path):
    try:
        # reading disease list csv file
        disease_list_df = pd.read_csv(disease_list_path)
        return disease_list_df
    except:
        # providing errors if the file is not okay
        print(f"The format of disease_list_csv file located in {disease_list_path} is not correct!!!")
        exit(1)

def save_json(result_dict):
    # saving the dictionary as a json file
    with open("indicators.json", "w+") as outfile:
        json.dump(result_dict, outfile)

if __name__ == "__main__":
    # in python filename is the 1st argument with id 0 and so on.
    given_args = len(sys.argv)
    # if the arguments are not 3 (excluding executable filename) or 4
    # showing error
    if given_args < 3 or given_args > 4:
        print("Number of arguments provided is not correct.!!!")
        print("Please provide 2 for normal result and 3 for advanced result.")
        print("Example:")
        print("python3 soft_assignment_solution.py data_cases.csv disease_list.csv")
        print("or")
        print("python3 soft_assignment_solution.py data_cases.csv disease_list.csv advance")
        exit(1)
    elif given_args == 3:
        # if argument number is 3 it contains the 2 csv files only
        data_path = sys.argv[1]
        # reading the data cases csv file
        data_df = read_csv(data_path)
        disease_list_path = sys.argv[2]
        # reading the disease list csv file
        disease_list_df = read_disease_list(disease_list_path)
        # generating the result dictionary
        result_dict = get_normal_result(data_df)
        # saving the result dictionary as json
        save_json(result_dict)
    elif given_args == 4:
        if sys.argv[3]=='advance':
            # it contains the 2 csv files with 'advance' argument
            data_path = sys.argv[1]
            # reading the data cases csv file
            data_df = read_csv(data_path)
            disease_list_path = sys.argv[2]
            # reading the disease list csv file
            disease_list_df = read_disease_list(disease_list_path)
            # generating the advance result dictionary
            result_dict = get_advanced_result(data_df, disease_list_df)
            # saving the result dictionary as json
            save_json(result_dict)
        else:
            # the advance argument is not correct
            print("The 3rd is not correct.!!!")
            print("Correct example:")
            print("python3 soft_assignment_solution.py data_cases.csv disease_list.csv advance")
            exit(1)

