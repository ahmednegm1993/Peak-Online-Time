import pandas as pd
df=pd.read_excel(r'E:\\Data_analysis_projects\\Peak Online Time\\\dataset\\full_amazon_user_activity_data.xlsx')
df['time_period']=df['start_timestamp'].astype(str)+' '+'to'+' '+df['end_timestamp'].astype(str)
df1 = df.groupby(['device_type', 'time_period']).agg({'user_count': 'sum'}).reset_index()
df1=df1.sort_values(by=['device_type','user_count'],ascending=[True,False])
df_top3 = df1.groupby('device_type').head(1)
print(df_top3)