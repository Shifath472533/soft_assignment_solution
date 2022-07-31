# soft_assignment_solution

The solution is built using python. To execute this application python3 (must be greater than python version 3.5) needs to be installed in the machine.
Python3 (any version greater than 3.5) can be  downloded and install from [this link](https://www.python.org/downloads/)

required modules of python:

 - re
 - sys
 - csv  (can be installed using command `pip install csv`)
 - json  
 - pandas  (can be installed using command `pip install pandas`)

The program mainly takes 2 arguments. (mandatory) 
1. data_cases.csv (it's and example name. the name can be anything with csv extention)
2. disease_list.csv (it's and example name. the name can be anything with csv extention)


The no. 1 file is expected to have following fields
uuid,datetime,species,number_morbidity,disease_id,number_mortality,total_number_cases,location

The no. 2 file is expected to have following fields
id, name

to run the command either you need to move to the directory of this files (in this case the 2 files must be in the same folder)
or need to provide the absolute path of the files.
example:

```
  cd /home/shifath/soft_assignment/
  python3 soft_assignment_solution.py data_cases_1.csv disease_list.csv
```

in this case the .py file and .csv files are in same folder.
or


```
  python3 /home/shifath/soft_assignment/soft_assignment_solution.py /home/shifath/soft_assignment/data_cases_1.csv /home/shifath/soft_assignment/disease_list.csv
```

N.B: In these cases the files are in linux environment. In Windows it will be different. In Mac it will be kind of similar.

for Windows:


```
  python3 C:\Users\shifath\soft_assignment\soft_assignment_solution.py C:\Users\shifath\soft_assignment\data_cases_1.csv C:\Users\shifath\soft_assignment\disease_list.csv
```


and another option 3rd argument "advance" can be passed to get advanced indicators.

```
  python3 /home/shifath/soft_assignment/soft_assignment_solution.py /home/shifath/soft_assignment/data_cases_1.csv /home/shifath/soft_assignment/disease_list.csv advance
```


The output will be always a json file in the folder the program exist if no error occurs.
in this case,
`/home/shifath/soft_assignment/indicators.json`
