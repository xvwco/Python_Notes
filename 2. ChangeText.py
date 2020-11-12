#If you have a column naimed ['NameColumn'] in a dataframe with pandas, 
#you can replace a part of the text with another:
#In my case for SQL INSERT INTO "Name of a table".

import pandas as pd
#1. Load the texts 

df = pd.read_csv(*.csv)

#2. Add Columns Name ['NameColumn']
df.columns = ['NameColumn']

#3. Replace

text = (df
           .apply(lambda row: row['NameColumn'], axis=1)
           .apply(lambda body: body.replace('`some_text`','`Another_text`' ))
            )
text
