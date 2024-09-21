import pandas as pd

df1 = pd.read_csv(r'E:\\Data_analysis_projects\\find the details of an order\dataset\\orders.csv')
df2 = pd.read_csv(r'E:\Data_analysis_projects\find the details of an order\dataset\customer.csv')
df3 = pd.read_csv(r'E:\Data_analysis_projects\find the details of an order\dataset\salesman.csv')

df1 = df1.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
df2 = df2.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
df3 = df3.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

df1_merge = pd.merge(df1, df2, how='inner', on='customer_id')

final_merge = pd.merge(df1_merge, df3, how='inner', left_on='salesman_id_x',right_on='salesman_id')
final_merge_filterd=final_merge[['ord_no','ord_date','purch_amt','cust_name','grade','name','commission']]
print(final_merge_filterd)