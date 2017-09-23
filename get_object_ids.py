import pandas as pd

url = 'https://s3.amazonaws.com/irs-form-990/index_2017.csv'
fy = 2016
form_type = '990'

df = pd.read_csv(url) #Quick and dirty using Pandas
df.head(100).to_csv('head.csv', index = False)
#df.to_csv('index_' + str(fy) + '_.csv')

fye_list = [] #FYE is derived

for t in list(df['TAX_PERIOD']):
    fye_list.append(str(t)[:4])
    
df['FYE'] = fye_list
df['FYE'] = pd.to_numeric(df['FYE'])

df2 = df[(df['FYE'] == fy) & (df['RETURN_TYPE']==form_type)]
df2['OBJECT_ID'].to_csv('object_ids_' + str(fy) +'_.csv', index = False)

