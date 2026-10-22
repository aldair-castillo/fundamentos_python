# Ejemplo minimo
linea = "2026-10-12| ERROR | payment_gateway| Timeout en la respuesta"
linea.strip()
print(linea)
campos = linea. split("|")

print(campos)

print(campos[1]) 
print(len(campos))