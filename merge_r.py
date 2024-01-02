import pandas as pd
import numpy as np
path="SHA-LEVEL_2_Files-part1\\r26897152\\ch4\\pbcd\\"
r_list=[6,8,10,12,14,16,18,20]

cat1=pd.read_csv(path + f"Table_NGC2264_4_6.csv")
cat2=pd.read_csv(path + f"Table_NGC2264_4_10.csv")
cat3=pd.read_csv(path + f"Table_NGC2264_4_8.csv")
cat4=pd.read_csv(path + f"Table_NGC2264_4_12.csv")
cat5=pd.read_csv(path + f"Table_NGC2264_4_14.csv")
cat6=pd.read_csv(path + f"Table_NGC2264_4_16.csv")
cat7=pd.read_csv(path + f"Table_NGC2264_4_18.csv")
cat8=pd.read_csv(path + f"Table_NGC2264_4_20.csv")
catf=cat1['OBJECT_ID'].to_frame().merge(cat2['OBJECT_ID'].to_frame(),how='inner')
catf.to_csv(path + "merge_all_radius.tsv", sep="\t",index=False,header=False)





