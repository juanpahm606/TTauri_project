import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches

#ch1=3.6
#ch2=4.5
#ch3=5.8
#ch4=8.0
cat1=pd.read_csv("SHA-LEVEL_2_Files-part1\\r26897152\\ch1\\pbcd\\Table_NGC2264_4_6_DEFINITIVE.csv")
cat1=cat1.drop(['DATE-OBS_1_mag_0'],axis=1)
cat2=pd.read_csv("SHA-LEVEL_2_Files-part1\\r26897152\\ch2\\pbcd\\Table_NGC2264_4_6_DEFINITIVE.csv")
cat2=cat2.drop(['DATE-OBS_2_mag_0'],axis=1)
cat3=pd.read_csv("SHA-LEVEL_2_Files-part1\\r26897152\\ch3\\pbcd\\Table_NGC2264_4_6_DEFINITIVE.csv")
cat3=cat3.drop(['DATE-OBS_3_mag_0'],axis=1)
cat4=pd.read_csv("SHA-LEVEL_2_Files-part1\\r26897152\\ch4\\pbcd\\Table_NGC2264_4_6_DEFINITIVE.csv")
cat4=cat4.drop(['DATE-OBS_4_mag_0'],axis=1)
catf=pd.merge(cat1, cat2, on=['OBJECT_ID','RA','DEC'], how='inner')
catf=pd.merge(catf, cat3, on=['OBJECT_ID','RA','DEC'], how='inner')
catf=pd.merge(catf, cat4, on=['OBJECT_ID','RA','DEC'], how='inner')
for i in range(1,5):
    filter=(catf[f'{i}_mag_err_0']/catf[f'{i}_mag_0'])<0.2
    #print(filter)
    catf=catf.loc[filter]
    print(catf)
#sin corregir
pass
# plt.grid(True)
# plt.scatter(catf['3_mag_0']-catf['4_mag_0'], catf['1_mag_0']-catf['2_mag_0'], marker='x', color='red', label='Objects')
# plt.xlabel('[5.8]-[8.0]')
# plt.ylabel('[3.6]-[4.5]')
# plt.xlim(0.4, 1.1)
# plt.ylim(0.0,0.8)
# rect_left = 0.4  # Límite izquierdo
# rect_right = 1.1 # Límite derecho
# rect_bottom = 0.0  # Límite inferior
# rect_top = 1.1  # Límite superior
# rect = patches.Rectangle((rect_left, rect_bottom), rect_right - rect_left, rect_top - rect_bottom, linewidth=2, edgecolor='b', facecolor='none')
# plt.gca().add_patch(rect)
#plt.title('color-color IRAC')
#plt.show()
#corregir
E=0.054
A=3.1*E
Ac=[1.125,1.120,1.135,1.221]
R=[0.05228,0.03574,0.02459,0.01433]
# m-R*A-2.5*np.log10(Ac)
pass
C1=catf['1_mag_0']-R[0]*A-2.5*np.log10(Ac[0])
C2=catf['2_mag_0']-R[1]*A-2.5*np.log10(Ac[1])
C3=catf['3_mag_0']-R[2]*A-2.5*np.log10(Ac[2])
C4=catf['4_mag_0']-R[3]*A-2.5*np.log10(Ac[3])
#Plot corregido
pass
catf.to_csv(r"C:\Users\juani\OneDrive\Documentos\TOBS\graph_colcol.csv", index=False)
plt.grid(True)
plt.scatter(C3-C4, C1-C2, marker='x', color='red', label='Objects')
plt.xlabel('[5.8]-[8.0]')
plt.ylabel('[3.6]-[4.5]')
plt.xlim(0.4, 1.1)
plt.ylim(0.0,0.8)
rect_left = 0.4  # Límite izquierdo
rect_right = 1.1 # Límite derecho
rect_bottom = 0.0  # Límite inferior
rect_top = 1.1  # Límite superior
rect = patches.Rectangle((rect_left, rect_bottom), rect_right - rect_left, rect_top - rect_bottom, linewidth=2, edgecolor='b', facecolor='none')
plt.gca().add_patch(rect)
plt.title('color-color IRAC')
plt.show()

lamost=pd.DataFrame()
lamost['#ra']=catf['RA']
lamost['dec']=catf['DEC']
lamost['sep']=2.0
lamost=lamost.reset_index(drop=True)
lamost.to_csv("lamost_ngc2264.csv",sep=",",index=False)