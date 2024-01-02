import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
r_list=[6,8,10,12,14,16,18,20]
path="SHA-LEVEL_2_Files-part1\\r26897152\\ch4\\pbcd\\"
best_r=pd.DataFrame(columns=['Radius','Magnitude'])
i=0
stars=pd.read_csv(path + "merge_all_radius.tsv", sep="\t" )
stars.columns=['OBJECT_ID']
star_random=random.choice(stars['OBJECT_ID'])
for r in r_list:
    cat1=pd.read_csv(path + f"Table_NGC2264_4_{r}.csv")
    cat_ordered=cat1.sort_values(by="OBJECT_ID").reset_index(drop=True)
    #print(cat_ordered)
    #cat_ordered.to_csv(path + f"Table_NGC2264_4_{r}_ordered.csv",index=False )
    try:
        cat3=cat_ordered[cat_ordered['OBJECT_ID']==star_random]
        print(cat3['4_mag_0'].iloc[0])
        best_r.loc[i,'Radius']=r
        best_r.loc[i,'Magnitude']=cat3['4_mag_0'].iloc[0]
    except:
        print('El objeto no se encuentra con esta apertura')   
        pass 
    i=i+1
    #cat_ordered.drop(cat_ordered.index,axis=0)
pass
plt.plot(best_r['Radius'],best_r['Magnitude'],marker='*',linestyle='-')
plt.xlabel('Radio')
plt.ylabel('Magnitud')
plt.title('Mejor radio de apertura')
plt.show()
pass
