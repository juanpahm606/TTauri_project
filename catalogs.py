import pandas as pd
cat1=pd.read_csv("SHA-LEVEL_2_Files-part1\\r26897152\\ch1\\pbcd\\catalog.tsv",sep="\t")
cat2=cat1[['RA_ICRS','DE_ICRS','Source']]
cat2.to_csv('SHA-LEVEL_2_Files-part1\\r26897152\\ch1\\pbcd\\catalog_gaia.tsv',sep="\t",index=False,header=False)


