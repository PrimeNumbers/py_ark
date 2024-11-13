import os.path #confirm file exists
import csv #read from csv files
from pprint import pprint #pretty print lists

#load file and return a list of key value pairs
def load_vars(filename,version):
    myvars = []
    warns = []

    #returns true or false if the string can be represented as an integer
    def check_int(s):
        if len(s) >= 1:
            if s[0] in ('-', '+'):
                return s[1:].isdigit()
            return s.isdigit()
        else:
            return False

    #if the file exists
    if not os.path.isfile(filename):
        print('Cannot find file named: {}'.format(filename))
    else:
        #store the key value pairs in a list
        with open(filename, newline='') as f:
            r = csv.reader(f)
            for row in r:
                #skip empty and commented rows
                if len(row) > 0 and row[0] != None and row[0][0] != '#': #skip empty rows
                    #to view the data that has made it this far
                    #print("Type: {}  Length: {}  Value: {}".format(type(row), len(row), row))
                    if len(row) == 1: #warn about keys without values
                        warns.append(row)
                    else:
                        if row[0] == 'file_version' and row[1] != version:
                            raise ValueError("variables file version: '{}', but expected: '{}'".format(row[1],version))
                        #check if the value is an integer
                        if check_int(row[1]):
                            #convert before adding it
                            myvars.append([row[0],int(row[1])])
                        else:
                            #otherwise add it as a string
                            myvars.append(row)

    #split the keys and values into separate lists
    keys = [key_val[0] for key_val in myvars]
    vals = [key_val[1] for key_val in myvars]
    if len(warns)>0:
        print("Warning no values set for: \n{}".format(pprint(warns)))
    return keys,vals

#helper function to extract values
def val(key,keys,vals):
    return vals[keys.index(key)]

if __name__ == "__main__":
    #extract the keys and values
    keys,vals = load_vars("vars.txt",'1') #passing the version number that you expect it to be


    #example value extraction:
    ver = val('file_version',keys,vals)
    print(ver)

    #print contents
    view_pairs = True
    if view_pairs:
        i = 0
        k = len(keys)
        j = []
        while i < k:
            j.append([keys[i],vals[i]])
            i+=1
        pprint(j)
