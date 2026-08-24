import pandas as pd

# Cargar un CSV en un DataFrame
df = pd.read_csv('clientes.csv')

# Primer vistazo
print(df.shape)
print(df.head())
print(df.info())
print(df.describe())

# ¿Cuántos valores faltan por columna?
print(df.isna().sum())

# Filtrar y agrupar
activos = df[df['estado' ] == 'activo']
print(activos.groupby('ciudad') ['edad'].mean())