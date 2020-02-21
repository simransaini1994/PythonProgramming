# @author Simranjit Singh
import pandas as pd
df = pd.read_csv('personarrested.csv')
print(df.head())

df.set_index('Year', inplace = True)
print(df.head())

df['Offenders_Conviction_in_the_past_Twice'].to_csv('newConvicted.csv')
df= pd.read_csv('newConvicted.csv')
df.set_index('Year', inplace=True)
print(df.head())

df.to_pickle('new_pickle')
new_df= pd.read_pickle('new_pickle')
print(new_df.head())
