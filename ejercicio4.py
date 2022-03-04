from api.library import *

def main ():
    #aplicacion de los diccionarios
    #persona = {
     #   "nombre": "Sandra",
    #  "apellidos": "Daza Mendoza",
     #   "edad": 45

    #}

    persona = {
        "datospersonales":{
            "Nombre": "Sandra",
            "Apellidos": "Daza Mendoza",
            "Edad": 45
        },

        "Salarial": {
            "salario": 2000000,
            "subtransporte": 50000,
            "subalimentacion": 60000
        }
    }

   # print(persona["nombre"]+""+ persona["apellidos"])
   # print(f"{persona['nombre']} {persona['apellidos']}")

    print(f"Nombre: {persona['datospersonales']['Nombre']}  {persona['datospersonales']['Apellidos']}")
if __name__ == "__main__":
    main()