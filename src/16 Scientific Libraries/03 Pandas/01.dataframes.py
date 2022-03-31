'''
DataFrames
==========

Pandas 2D datasets are called dataframes.  In this example we read data from a file into a dataframe:
            lerwick_data = pd.read_csv("data/lerwick.txt", ...) 

Note that although we are using "read_csv()" the data file doen't have to be a set comma seperated data (although
this was the original idea).  This example shows several methods of the dataframe.

Parameters to "read_csv" include the engine, which can be "python" or "C" dependent on the authoring language;
the C engine is faster but less flexible.  We will use the Python engine in all our examples because unlike the 
C engine, it allows us to use RegExs when specify the field separated.  Normall Pandas will use the first row
to determine column names, but you can provide your own names by setting the "names" parameter.

The field seperator is the RegEx:
            '[*# ]+'
which means at least one of the characters in the [], i.e. * # or space, repeated in any order one or more times.

At the end of the example we show how to iterate through each row of the dataframe.
'''

import pandas as pd
pd.set_option('display.precision', 1)
# pd.set_option('display.width', None)        # None means all data displayed
pd.set_option('display.width', 80)
pd.set_option('display.max_rows', None)



def main(): 
    #set up your own columns
    column_names = ['year', 'month', 'tmax', 'tmin', 'air-frost-days', 'rain(mm)', 'sun(hours)', 'comment']
    lerwick_data = pd.read_csv("data/lerwick.txt", #read csv which is valid for all file types
                               skiprows = 7,       #skip first 7 rows
                               engine = 'python',  #python engine is more flexible(def), C++ is faster
                               names = column_names,#C++ engine can't handle some types of separators
                               skipinitialspace = True, #skip the spaces at the front of each line
                               #separator can be either *, # or space and repeated 1 or more times
                               #+ means 1 or more times. separators stated in []
                               sep = '[*# ]+') #set the separator, allowing for awkward data
    print(lerwick_data)
    
    df = lerwick_data
    pd.set_option('display.width', 80)
    print(df.head())       # show first five rows
    print(df.tail())       # show last five rows
    print(df.sample(5))    # show random sample of rows
    print(df.shape)        # number of rows/columns in a tuple
    print(df.describe())   # calculates measures of central tendency
    df.info()              # memory footprint and datatypes

    tmax = df.sort_values('tmax', axis=0, ascending=False)
    pd.set_option('display.max_rows', 20)
    print(tmax)

    for index, row in df.iterrows():
        print(index, row)
main()

