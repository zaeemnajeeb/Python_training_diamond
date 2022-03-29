import pandas as pd
pd.set_option('display.precision', 1)
pd.set_option('display.width', None)        # None means all data displayed
pd.set_option('display.max_rows', None)

'''
Pandas 2D dataset are called dataframe.
This example shows several methods of the dataframe.
'''

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
    print(df.head())       # first five rows
    print(df.tail())       # last five rows
    print(df.sample(5))    # random sample of rows
    print(df.shape)        # number of rows/columns in a tuple
    print(df.describe())   # calculates measures of central tendency
    df.info()              # memory footprint and datatypes

    tmax = df.sort_values('tmax', axis=0, ascending=False)
    pd.set_option('display.max_rows', 20)
    print(tmax)
main()
