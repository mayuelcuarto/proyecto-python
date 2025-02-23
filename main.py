"""
Proyecto Python y Mysql:
- Abrir asistente
- Login o registro
- Si elegimos registro, nos creará un usuario en la bd
- Si elegimos login, identifica al usuario y nos preguntará
- Crear nota, mostrar notas, borrarlas.

Prueba de cambios
"""

print("""
Acciones disponibles:
    - registro
    - login
""")

accion = input("¿Qué quieres hacer?: ")

if accion == "registro":
    print("Ok!! Vamos a registrarte en el sistema...")
elif accion == "login":
    print("Vale!! Identifícate en el sistema...")