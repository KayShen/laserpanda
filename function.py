import pandas as pd
import numpy as np
import os

os.chdir("/Users/Kay/Desktop/HD")

def read_data(dic):
	df = pd.read_csv(dic)
	train = pd.read_csv("data/train.csv",encoding = "ISO-8859-1")
	test = pd.read_csv("data/test.csv", encoding = "ISO-8859-1")
	attr = pd.read_csv("data/attributes.csv", encoding = "ISO-8859-1")
	prod_desc = pd.read_csv("data/product_descriptions.csv")



attr['value'] = attr[['product_uid','value']].groupby('product_uid').transform(lambda x: ",".join(x))
temp2 = temp %>%
	group_by(X1) %>%
	summarize(X2_mean = mean(X2), X3_median = median(X3), Count = n())


temp[['product_uid','value']].groupby('product_uid')['value'].apply(lambda x: ",".join(x)).reset_index()
attr2 = attr[['product_uid','value']].groupby('product_uid')['value'].apply(lambda x: ",".join(x)).reset_index()
type(temp['value'])

value = np.array(attr['value'])
