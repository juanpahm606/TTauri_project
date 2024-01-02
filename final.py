import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
pass
# table1=pd.read_csv(r"C:\Users\juani\OneDrive\Documentos\TOBS\lamost_ngc2264.csv").sort_values(by="#ra")
table2=pd.read_csv(r"C:\Users\juani\OneDrive\Documentos\TOBS\spectra\ngc2264_spectra.csv").sort_values(by="#ra")
# table3=pd.read_csv(r"C:\Users\juani\OneDrive\Documentos\TOBS\mgc2264_2mass.tsv",sep="\t")
# table4=pd.read_csv(r"C:\Users\juani\OneDrive\Documentos\TOBS\gaia_NGC2264.tsv",sep="\t")
# table5=pd.read_csv(r"C:\Users\juani\OneDrive\Documentos\TOBS\two_tables.csv")
table6=pd.read_csv(r"C:\Users\juani\OneDrive\Documentos\TOBS\graph_colcol.csv")
table7=pd.read_csv(r"C:\Users\juani\OneDrive\Documentos\TOBS\graph_final.csv")
table9=pd.read_csv(r"C:\Users\juani\OneDrive\Documentos\TOBS\spectra_for_graph.csv")
table8=pd.read_csv(r"C:\Users\juani\OneDrive\Documentos\TOBS\graph_colcol_final.csv")
plt.grid(True)
E=0.054
A=3.1*E
Ac=[1.125,1.120,1.135,1.221]
R=[0.05228,0.03574,0.02459,0.01433]
# m-R*A-2.5*np.log10(Ac)
pass
C1=table7['1_mag_0']-R[0]*A-2.5*np.log10(Ac[0])
#C2=table7['2_mag_0']-R[1]*A-2.5*np.log10(Ac[1])
#C3=table7['3_mag_0']-R[2]*A-2.5*np.log10(Ac[2])
C4=table7['4_mag_0']-R[3]*A-2.5*np.log10(Ac[3])
plt.scatter(table7['Kmag']-C4,C1, marker='x', color='red', label='Objects')
plt.xlabel('K-[8.0]')
plt.ylabel('[3.6]')
plt.title('Extintion')
plt.show()
pass

table8['width'] = table8['width'].replace(',', '.', regex=True)
table8['width'] = table8['width'].str.replace('Angstrom', '')
D1=table8['1_mag_0']-R[0]*A-2.5*np.log10(Ac[0])
D2=table8['2_mag_0']-R[1]*A-2.5*np.log10(Ac[1])
D3=table8['3_mag_0']-R[2]*A-2.5*np.log10(Ac[2])
D4=table8['4_mag_0']-R[3]*A-2.5*np.log10(Ac[3])
plt.grid(True)
plt.xlabel('[5.8]-[8.0]')
plt.ylabel('[3.6]-[4.5]')
#plt.xlim(0.4, 1.1)
#plt.ylim(0.0,0.8)
rect_left = 0.4  # Límite izquierdo
rect_right = 1.1 # Límite derecho
rect_bottom = 0.0  # Límite inferior
rect_top = 1.1  # Límite superior
rect = patches.Rectangle((rect_left, rect_bottom), rect_right - rect_left, rect_top - rect_bottom, linewidth=2, edgecolor='b', facecolor='none')
plt.gca().add_patch(rect)
plt.title('TTauri stars in NGC 2264')
ttauri=plt.scatter(D3-D4, D1-D2,c=table8['width'],cmap='magma', marker='o')
plt.colorbar(ttauri, label='Width')
plt.show()