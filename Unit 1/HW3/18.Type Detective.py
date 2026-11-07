# Ejercicio 18: Type Detective

# Tabla de Predicción vs Resultado Real
# -----------------------------------------------------------
# Expresión    | Predicción   | Resultado Real (type)
# -----------------------------------------------------------
# 5 / 2        | float        | <class 'float'>
# 5 // 2       | int          | <class 'int'>
# "5"          | str          | <class 'str'>
# 3 > 2        | bool         | <class 'bool'>
# -----------------------------------------------------------

# Código funcional para verificar los resultados:
print("Verificacion en la Shell:")
print("5 / 2   es:", type(5 / 2))
print("5 // 2  es:", type(5 // 2))
print('"5"     es:', type("5"))
print("3 > 2   es:", type(3 > 2))
