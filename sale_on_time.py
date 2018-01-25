import pandas as pd
from matplotlib import pyplot

datapath = 'data/'

train_df = pd.read_csv(datapath + '[new] yancheng_train_20171226.csv')
train_df = train_df.sort_values('sale_date')
#train_df['sale_date'] = train_df['sale_date'].map(str)

test_df = pd.read_csv(datapath + 'yancheng_testA_20171225.csv')

class_ids = train_df['class_id'].unique()

for cid in class_ids:
    one_sales = train_df[train_df['class_id']==cid].groupby('sale_date').sale_quantity.sum().round()
    #pyplot.plot(one_sales)
    saleof10 = train_df[(train_df['class_id']==cid) & (train_df['sale_date']%100==10)].groupby('sale_date').sale_quantity.sum().round()
    saleof11 = train_df[(train_df['class_id']==cid) & (train_df['sale_date']%100==11)].groupby('sale_date').sale_quantity.sum().round()
    sale = saleof11.join(saleof10)
pyplot.show()
print(one_sales)