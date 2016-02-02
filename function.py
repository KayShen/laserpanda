import pandas as pd
import numpy as np
import os

os.chdir("/Users/Kay/Desktop/HD")

def read_data(dic):
	df = pd.read_csv(dic)
	train = pd.read_csv("data/train.csv")
	test = pd.read_csv("data/test.csv")
	attr = pd.read_csv("data/attributes.csv")
	prod_desc = pd.read_csv("data/prod_desc")


temp2 = temp %>%
	group_by(X1) %>%
	summarize(X2_mean = mean(X2), X3_median = median(X3), Count = n())
