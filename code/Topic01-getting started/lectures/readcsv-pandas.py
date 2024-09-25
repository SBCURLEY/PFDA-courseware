 # reading in the CSV as a pandas table
# Author: Andrew Beatty

FILENAME= "data.csv"
DATADIR = "../datafiles/"

import pandas
df = pandas.read_csv(DATADIR + FILENAME)
print (df)
