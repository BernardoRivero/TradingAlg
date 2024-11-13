import pandas as pd

# Cargar el archivo CSV original
df = pd.read_csv('MSFT_data.csv')

# Ver las primeras filas para comprobar cómo se ve el archivo
print("Primeras filas antes de procesar:")
print(df.head())

# Convertir la fecha a formato 'YYYY-MM-DD' sin la zona horaria
df['Date'] = pd.to_datetime(df['Date']).dt.date

# Eliminar filas donde la fecha no es válida (si existe alguna)
df = df.dropna(subset=['Date'])

# Ahora verificamos que las fechas estén bien alineadas y ordenar las filas por 'Date'
df = df.sort_values(by='Date', ascending=True)

# Reordenar las columnas en el orden correcto
df = df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]

# Ver las primeras filas después de procesar para comprobar que los valores coinciden
print("Primeras filas después de procesar:")
print(df.head())

# Guardar el archivo limpio en un nuevo CSV
df.to_csv('ORCL_data_clean.csv', index=False)

print("Archivo limpio y ordenado guardado como 'ORCL_data_clean.csv'")
