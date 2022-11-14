#importar libreria
import pandas as pd
import matplotlib.pyplot as plt

#archivo excel a leer 
libro = "libro.xlsx"
#leemos el pdf
df = pd.read_excel(libro)

print(df.head())

valores = df [["bancos","saldos"]]
print(valores)
#organizamos los datos
ax= valores.plot.bar(x= "bancos", y="saldos", rot =0)

plt.show()
