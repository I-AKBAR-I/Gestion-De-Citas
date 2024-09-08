import csv
import datetime

# Diccionarios para almacenar la información
doctores = {
    "Dr. Martínez": {
        "especialidad": "Pediatría",
        "inicio": "08:00",
        "fin": "14:00",
        "agenda": []
    },
    "Dra. Gómez": {
        "especialidad": "Oftalmología",
        "inicio": "11:00",
        "fin": "17:00",
        "agenda": []
    }
}

clientes = {
    "Carlos Fernández": {
        "telefono": "555-1111",
        "citas": []
    },
    "Ana Pérez": {
        "telefono": "555-2222",
        "citas": []
    }
}

citas = [
    {
        "cliente": "Carlos Fernández",
        "doctor": "Dr. Martínez",
        "fecha": "2024-09-15",
        "hora": "08:30",
        "confirmada": True,
        "cancelada": False
    },
    {
        "cliente": "Ana Pérez",
        "doctor": "Dra. Gómez",
        "fecha": "2024-09-17",
        "hora": "11:45",
        "confirmada": True,
        "cancelada": False
    }
]

# Función para registrar doctores
def registrar_doctor():
    nombre = input("Nombre del doctor: ")
    especialidad = input("Especialidad: ")
    inicio = input("Hora de inicio (HH:MM): ")
    fin = input("Hora de fin (HH:MM): ")
    
    doctores[nombre] = {
        "especialidad": especialidad,
        "inicio": inicio,
        "fin": fin,
        "agenda": []
    }
    print(f"Doctor {nombre} registrado correctamente.\n")

# Función para registrar clientes
def registrar_cliente():
    nombre = input("Nombre del cliente: ")
    telefono = input("Teléfono del cliente: ")
    
    clientes[nombre] = {
        "telefono": telefono,
        "citas": []
    }
    print(f"Cliente {nombre} registrado correctamente.\n")

# Función para verificar disponibilidad
def verificar_disponibilidad(doctor, fecha, hora):
    for cita in doctores[doctor]["agenda"]:
        if cita["fecha"] == fecha and cita["hora"] == hora:
            return False
    return True

# Función para agendar una cita
def agendar_cita():
    cliente = input("Nombre del cliente: ")
    if cliente not in clientes:
        print("Cliente no registrado.\n")
        return
    
    doctor = input("Nombre del doctor: ")
    if doctor not in doctores:
        print("Doctor no registrado.\n")
        return

    fecha = input("Fecha de la cita (YYYY-MM-DD): ")
    hora = input("Hora de la cita (HH:MM): ")

    if verificar_disponibilidad(doctor, fecha, hora):
        cita = {
            "cliente": cliente,
            "doctor": doctor,
            "fecha": fecha,
            "hora": hora,
            "confirmada": False,
            "cancelada": False
        }
        citas.append(cita)
        doctores[doctor]["agenda"].append(cita)
        clientes[cliente]["citas"].append(cita)
        print(f"Cita agendada para {cliente} con {doctor} el {fecha} a las {hora}.\n")
    else:
        print("El doctor no está disponible en esa fecha y hora.\n")

# Función para generar un archivo CSV
def generar_csv():
    with open('citas_medicas.csv', mode='w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        
        # Cabeceras
        escritor_csv.writerow(["Cliente", "Doctor", "Especialidad", "Fecha", "Hora", "Confirmada", "Cancelada"])
        
        # Agregar datos de citas
        for cita in citas:
            cliente = cita["cliente"]
            doctor = cita["doctor"]
            especialidad = doctores[doctor]["especialidad"]
            fecha = cita["fecha"]
            hora = cita["hora"]
            confirmada = "Sí" if cita["confirmada"] else "No"
            cancelada = "Sí" if cita["cancelada"] else "No"
            
            escritor_csv.writerow([cliente, doctor, especialidad, fecha, hora, confirmada, cancelada])
    
    print("Archivo CSV generado: citas_medicas.csv\n")

# Función para cancelar una cita
def cancelar_cita():
    cliente = input("Nombre del cliente: ")
    if cliente not in clientes:
        print("Cliente no registrado.\n")
        return

    fecha = input("Fecha de la cita a cancelar (YYYY-MM-DD): ")
    hora = input("Hora de la cita a cancelar (HH:MM): ")

    for cita in citas:
        if cita["cliente"] == cliente and cita["fecha"] == fecha and cita["hora"] == hora:
            cita["cancelada"] = True
            print(f"Cita cancelada para {cliente} el {fecha} a las {hora}.\n")
            return
    
    print("No se encontró la cita.\n")

# Función para ver doctores registrados
def ver_doctores():
    print("\nDoctores registrados:")
    for nombre, info in doctores.items():
        print(f"Nombre: {nombre}, Especialidad: {info['especialidad']}, Horario: {info['inicio']} - {info['fin']}")
    print()

# Función para ver doctores disponibles
def ver_doctores_disponibles():
    print("\nDoctores disponibles:")
    hoy = datetime.date.today().strftime("%Y-%m-%d")
    for nombre, info in doctores.items():
        disponible = any(cita["fecha"] == hoy and not cita["cancelada"] for cita in info["agenda"])
        if disponible:
            print(f"Nombre: {nombre}, Especialidad: {info['especialidad']}, Horario: {info['inicio']} - {info['fin']}")
    print()

# Función para ver citas agendadas
def ver_citas_agendadas():
    print("\nCitas agendadas:")
    for cita in citas:
        if not cita["cancelada"]:
            print(f"Cliente: {cita['cliente']}, Doctor: {cita['doctor']}, Fecha: {cita['fecha']}, Hora: {cita['hora']}")
    print()

# Función para ver citas canceladas
def ver_citas_canceladas():
    print("\nCitas canceladas:")
    for cita in citas:
        if cita["cancelada"]:
            print(f"Cliente: {cita['cliente']}, Doctor: {cita['doctor']}, Fecha: {cita['fecha']}, Hora: {cita['hora']}")
    print()

# Menú principal
def menu_principal():
    while True:
        print("Sistema de Gestión de Citas Médicas")
        print("1. Registrar doctor")
        print("2. Registrar cliente")
        print("3. Agendar cita")
        print("4. Cancelar cita")
        print("5. Generar archivo CSV")
        print("6. Ver doctores registrados")
        print("7. Ver doctores disponibles")
        print("8. Ver citas agendadas")
        print("9. Ver citas canceladas")
        print("10. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_doctor()
        elif opcion == "2":
            registrar_cliente()
        elif opcion == "3":
            agendar_cita()
        elif opcion == "4":
            cancelar_cita()
        elif opcion == "5":
            generar_csv()
        elif opcion == "6":
            ver_doctores()
        elif opcion == "7":
            ver_doctores_disponibles()
        elif opcion == "8":
            ver_citas_agendadas()
        elif opcion == "9":
            ver_citas_canceladas()
        elif opcion == "10":
            break
        else:
            print("Opción inválida, intente de nuevo.\n")

# Iniciar el programa
menu_principal()