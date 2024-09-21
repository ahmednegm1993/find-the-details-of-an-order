library(dplyr)

df1 <- read.csv('E:\\Data_analysis_projects\\find the details of an order\\dataset\\orders.csv')
df2 <- read.csv('E:\\Data_analysis_projects\\find the details of an order\\dataset\\customer.csv')
df3 <- read.csv('E:\\Data_analysis_projects\\find the details of an order\\dataset\\salesman.csv')

df_merge <- inner_join(df1, df2, by='customer_id')
final_merge <- inner_join(df_merge, df3, by = c("salesman_id.x" = "salesman_id"))
print(final_merge)
