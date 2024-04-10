# Función para leer el archivo y mostrar los detalles
def read_file_and_print_details(file_path):
    # Abre el archivo en modo lectura y lee todas las líneas
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Bucle infinito para permitir al usuario elegir entre ver un registro específico, ver toda la información o salir
    while True:
        print("Escoga una opción:")
        print("1. Ver un registro en especifico")
        print("2. Ver toda la información")
        print("3. salir")
        
        # Solicita la opción del usuario
        choice = input("Ingrese su opción: ")
        
        # Si la opción es 1, solicita el número de registro y muestra los detalles si está dentro del rango válido
        if choice == '1':
            line_number = int(input("Ingrese el número de registro que quiere ver: "))
            if 1 <= line_number <= len(lines):
                # Divide la línea seleccionada en campos y verifica que haya suficientes campos
                fields = [field.strip() for field in lines[line_number - 1].strip().split(';')]
                if len(fields) >= 4:
                    # Extrae los campos necesarios y muestra los detalles
                    name = fields[0]
                    last_name = fields[1]
                    address_fields = fields[2].split(',')
                    address = ', '.join([address_field.strip() for address_field in address_fields])
                    email = fields[3]
                    print(f"Name: {name}")
                    print(f"Last Name: {last_name}")
                    print(f"Address: {address}")
                    print(f"Email: {email}\n")
                else:
                    print("No hay suficientes campos en la línea seleccionada.")
            else:
                print("Número de línea no válido. Inténtalo de nuevo.")
        
        # Si la opción es 2, muestra los detalles de cada registro
        elif choice == '2':
            # Itera sobre cada línea y muestra los detalles si hay suficientes campos
            for line in lines:
                # Divide la línea en campos separados por ';', elimina espacios en blanco y guarda en una lista
                fields = [field.strip() for field in line.strip().split(';')]
                if len(fields) >= 4:
                    name = fields[0]
                    last_name = fields[1]
                    address_fields = fields[2].split(',')
                    address = ', '.join([address_field.strip() for address_field in address_fields])
                    email = fields[3]
                    print(f"Name: {name}")
                    print(f"Last Name: {last_name}")
                    print(f"Address: {address}")
                    print(f"Email: {email}\n")
                else:
                    print("No hay suficientes campos en una línea")
        
        # Si la opción es 3, sale del bucle y del programa
        elif choice == '3':
            print("Saliendo del programa")
            break
        
        # Si la opción no es válida, muestra un mensaje de error
        else:
            print("Elección no válida. Por favor ingresa una opción válida.")

# Ruta del archivo
file_path = 'informacion.txt'

# Llama a la función para leer el archivo y mostrar los detalles
read_file_and_print_details(file_path)