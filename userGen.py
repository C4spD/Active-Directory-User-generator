#!/usr/bin/python3

import argparse

logo = "\033[91m" + """
█████╗ ██████╗     ██╗   ██╗███████╗███████╗██████╗      ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗    ██║   ██║██╔════╝██╔════╝██╔══██╗    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
███████║██║  ██║    ██║   ██║███████╗█████╗  ██████╔╝    ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██╔══██║██║  ██║    ██║   ██║╚════██║██╔══╝  ██╔══██╗    ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
██║  ██║██████╔╝    ╚██████╔╝███████║███████╗██║  ██║    ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
╚═╝  ╚═╝╚═════╝      ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
""" + "\033[0m"

print(logo)

class CustomHelpFormatter(argparse.RawDescriptionHelpFormatter):
    def _format_action_invocation(self, action):
        if not action.option_strings:
            return action.dest
        else:
            opts = ', '.join(action.option_strings)
            return f"\033[96m{opts}\033[0m"

    def start_section(self, heading):
        heading = f"\033[95m{heading.capitalize()}:\033[0m"
        super().start_section(heading)

    def _format_text(self, text):
        return f"\033[92m{text}\033[0m"

parser = argparse.ArgumentParser(
    epilog='\033[93mUse example:\n  usersAD.py -f "Jhon" -l "Richards" > users.txt\033[0m',
    formatter_class=CustomHelpFormatter
)

parser.add_argument('-f', '--first_name', type=str, required=True)
parser.add_argument('-l', '--last_name', type=str, required=True)

args = parser.parse_args()

nombre = args.first_name.lower()
apellido = args.last_name.lower()

combinaciones = []

# Básicas
combinaciones.append(nombre + apellido)  # nombre + apellido
combinaciones.append(apellido + nombre)  # apellido + nombre
combinaciones.append(f"{nombre}.{apellido}")  # nombre.apellido
combinaciones.append(f"{apellido}.{nombre}")  # apellido.nombre
combinaciones.append(f"{nombre}_{apellido}")  # nombre_apellido
combinaciones.append(f"{apellido}_{nombre}")  # apellido_nombre
combinaciones.append(f"{nombre}-{apellido}")  # nombre-apellido
combinaciones.append(f"{apellido}-{nombre}")  # apellido-nombre

# Iniciales
combinaciones.append(nombre[0] + apellido)  # inicial + apellido
combinaciones.append(apellido[0] + nombre)  # inicial + nombre
combinaciones.append(f"{nombre[0]}.{apellido}")  # inicial.nombre
combinaciones.append(f"{apellido[0]}.{nombre}")  # inicial.nombre
combinaciones.append(f"{nombre}{apellido[0]}")  # nombre + inicial
combinaciones.append(nombre[0] + apellido[0])  # iniciales
combinaciones.append(apellido[0] + nombre[0])  # iniciales

# Solo nombre o apellido
combinaciones.append(nombre)  # solo nombre
combinaciones.append(apellido)  # solo apellido
combinaciones.append(f"{nombre}_{apellido[0]}")  # nombre_apellido inicial
combinaciones.append(f"{apellido}_{nombre[0]}")  # apellido_nombre inicial

# Variadas con fragmentos del nombre y apellido
combinaciones.append(f"{nombre[:3]}_{apellido[:3]}")  # fragmentos con guion bajo
combinaciones.append(f"{apellido[:3]}_{nombre[:3]}")  # fragmentos con guion bajo
combinaciones.append(f"{nombre[:4]}_{apellido[:2]}")  # mezcla con fragmentos
combinaciones.append(f"{apellido[:2]}_{nombre[:4]}")  # mezcla con fragmentos
combinaciones.append(f"{nombre[:2]}{apellido[:3]}")  # fragmentos combinados
combinaciones.append(f"{apellido[:3]}{nombre[:2]}")  # fragmentos combinados
combinaciones.append(f"{nombre[:3]}.{apellido[:3]}")  # fragmentos con punto
combinaciones.append(f"{apellido[:3]}.{nombre[:3]}")  # fragmentos con punto

# Combinaciones con guion bajo
combinaciones.append(f"{nombre[:2]}_{apellido[:4]}")  # guion bajo
combinaciones.append(f"{apellido[:4]}_{nombre[:2]}")  # guion bajo
combinaciones.append(f"{nombre[:3]}_{apellido[:3]}")  # guion bajo
combinaciones.append(f"{apellido[:3]}_{nombre[:3]}")  # guion bajo
combinaciones.append(f"{nombre[0]}_{apellido[:3]}")  # guion bajo
combinaciones.append(f"{apellido[:3]}_{nombre[0]}")  # guion bajo

# Combinaciones más complejas
combinaciones.append(f"{nombre[:2]}_{apellido[1:4]}")  # fragmentos intercalados
combinaciones.append(f"{apellido[1:4]}_{nombre[:2]}")  # fragmentos intercalados
combinaciones.append(f"{nombre[0]}_{apellido[1:3]}")  # fragmentos intercalados
combinaciones.append(f"{apellido[1:3]}_{nombre[0]}")  # fragmentos intercalados
combinaciones.append(f"{nombre[:2]}_{apellido[:3]}")  # fragmentos intercalados
combinaciones.append(f"{apellido[:3]}_{nombre[:2]}")  # fragmentos intercalados

# Más combinaciones con números
combinaciones.append(f"{nombre}{apellido}1234")  # nombre_apellido + número
combinaciones.append(f"{nombre}{apellido}5678")  # nombre_apellido + número
combinaciones.append(f"{nombre}{apellido}0001")  # nombre_apellido + número
combinaciones.append(f"{nombre[:3]}{apellido[:3]}12")  # nombre + apellido + número
combinaciones.append(f"{apellido[:3]}{nombre[:3]}34")  # apellido + nombre + número
combinaciones.append(f"{nombre[0]}{apellido[0]}567")  # iniciales + número
combinaciones.append(f"{apellido[0]}{nombre[0]}789")  # iniciales + número

# Combinaciones con puntuación adicional
combinaciones.append(f"{nombre[0]}_{apellido[:3]}@")  # con arroba
combinaciones.append(f"{apellido[:3]}_{nombre[0]}#")  # con hash
combinaciones.append(f"{nombre[0]}_{apellido[:3]}$")  # con dólar
combinaciones.append(f"{apellido[:3]}_{nombre[0]}!")  # con exclamación
combinaciones.append(f"{nombre[:3]}_{apellido[:3]}%")  # con porcentaje
combinaciones.append(f"{apellido[:3]}_{nombre[:3]}^")  # con caret

# Combinaciones con otros separadores
combinaciones.append(f"{nombre[:2]}-{apellido[2:5]}")  # guion como separador
combinaciones.append(f"{apellido[2:5]}-{nombre[:2]}")  # guion como separador
combinaciones.append(f"{nombre[0]}_{apellido[2:5]}")  # guion bajo
combinaciones.append(f"{apellido[2:5]}_{nombre[0]}")  # guion bajo

# Combinaciones con más fragmentos y números
combinaciones.append(f"{nombre[:3]}_{apellido[:3]}00")  # fragmentos con números
combinaciones.append(f"{apellido[:3]}_{nombre[:3]}01")  # fragmentos con números
combinaciones.append(f"{nombre[:4]}_{apellido[:4]}02")  # fragmentos con números
combinaciones.append(f"{apellido[:4]}_{nombre[:4]}03")  # fragmentos con números
combinaciones.append(f"{nombre[:2]}_{apellido[:5]}04")  # fragmentos con números

# Nuevas combinaciones usando iniciales
combinaciones.append(f"{nombre[0]}.{apellido[0]}01")  # iniciales con número
combinaciones.append(f"{apellido[0]}.{nombre[0]}02")  # iniciales con número
combinaciones.append(f"{nombre[0]}_{apellido[0]}03")  # iniciales con número
combinaciones.append(f"{apellido[0]}_{nombre[0]}04")  # iniciales con número

# Combinaciones con fechas
combinaciones.append(f"{nombre}_{apellido}_2024")  # nombre_apellido_año
combinaciones.append(f"{apellido}_{nombre}_2024")  # apellido_nombre_año
combinaciones.append(f"{nombre[:3]}_{apellido[:3]}_24")  # fragmentos_año
combinaciones.append(f"{apellido[:3]}_{nombre[:3]}_24")  # fragmentos_año

# Agregar números del 0 al 9999 a cada combinación
combinaciones_con_numeros = []
for combinacion in combinaciones:
    for i in range(10000):  # De 0 a 9999
        combinaciones_con_numeros.append(combinacion + str(i))

# Eliminar duplicados
combinaciones_con_numeros = list(set(combinaciones_con_numeros))

print("\n[~] Combinaciónes generadas:\n")
for user in combinaciones:
    print(user)
for user in combinaciones_con_numeros:
    print(user)

