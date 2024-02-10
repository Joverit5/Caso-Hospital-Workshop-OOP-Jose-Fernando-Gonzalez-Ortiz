from paciente import Hospital
print("Nombre del estudiante: José Fernando González Ortiz")
print("Código: T00068395")
print("\n\n-- Sistema de Información Hospitalaria --")
def menu():
        print("\n\n-- Menú Principal--\n\n")
        print("1.Buscar paciente")
        print("2.Registrar nuevo paciente")
        print("3.Generar reportes")
        print("4.Salir")
def actualizar():
        print("--- Actualizar información del Paciente ---")
        print("\nSeleccione qué información desea actualizar:")
        print("1. Signos vitales")
        print("2. Notas de evolucion")
        print("3. Resultados de exámenes de laboratorio")
        print("4. Medicamentos formulados")
        print("5. Dar de alta")
        print("6. Regresar al menú principal")
def reportes():
        print("\n\n--- Generar Reportes ---\n\n")
        print("Seleccione el tipo de reporte:")
        print("1. Porcentaje de ocupación hospitalaria")
        print("2. Promedio de estancia por servicio")
        print("3. Cantidad de admisiones y altas por servicio")
        print("4. Pacientes con enfermedades crónicas")
        print("5. Preescripción de medicamentos por servicio")
        print("6. Regresar al menú principal")
def main():
    hospital = Hospital()
    while True:
        opcion = input("\n\n1.Ingresar al sistema\n2.Salir\n\n> ")
        if opcion == "1":
            while True:
                menu()
                opcion_2 = input("\n\n> ")
                if  opcion_2 == "1":
                    print("\n\n--- Búsqueda de Paciente ---")
                    print("Ingrese el número de identificación del paciente o su nombre completo:")
                    id = input("\n\n>")
                    encontrado = hospital.busqueda(id)
                    if encontrado:
                        print("--- Perfil del paciente ---\n\n")
                        print("Documento de identidad: ", encontrado.identificacion)
                        print("Nombre completo: ", encontrado.nombre)
                        print("Sexo: ", encontrado.sexo)
                        print("Fecha de nacimiento (DD-MM-YYYY): ", encontrado.fecha_de_nacimiento)
                        print("\n\nHistoria Clínica:")
                        print("- Fecha de ingreso: ", encontrado.ingreso)
                        print("- Diagnóstico: ", encontrado.diagnostico)
                        print("- ¿La enfermedad es crónica?: ", encontrado.cronica)
                        print("- Tratamiento: ")
                        for item in encontrado.medicamentos:
                            print("  -", item) 
                        print("- Servicio: ", encontrado.servicio)
                        print("\n\n¿Qué acción desea realizar?")
                        print("1. Ver información completa")
                        print("2. Actualizar información")
                        print("3. Regresar al menú principal")
                        opcion_3 = input("\n\n> ")
                        if opcion_3 == "1":
                            print("--- Detalles completos de la Historia Clínica ---")
                            print("\n\n- Signos Vitales:") 
                            print(" - Presión arterial: ",end="") 
                            print(encontrado.signos_vitales.get("presion_arterial"),"mmHg")
                            print(" - Temperatura: ",end="")
                            print(encontrado.signos_vitales.get("temperatura"),"°C")
                            print(" - Saturación de oxígeno: ", end="")
                            print(encontrado.signos_vitales.get("saturacion"),"%")
                            print(" - Frecuencia respiratoria: ", end ="")
                            print(encontrado.signos_vitales.get("frecuencia_respiratoria"), end ="")
                            print(" respiraciones por minuto")
                            encontrado.imprimir_listas()
                            input("Presione cualquier tecla para volver al menú principal.\n\n > ")
                        if opcion_3 == "2":
                            actualizar()
                            opcion_4 = input("\n\n> ")
                            if opcion_4 == "1":
                                print("\n\n--- Actualizar Signos Vitales ---")
                                nueva_presion_arterial = input("Nueva presión arterial (mmHg): ")
                                nueva_temperatura = int(input("Nueva temperatura (°C): "))
                                nueva_saturacion = float(input("Nueva saturación de oxígeno en la sangre (%): "))
                                nueva_frecuencia_respiratoria = float(input("Nueva frecuencia respiratoria (respiraciones por minuto): "))        
                                encontrado.actualizar_signos(nueva_presion_arterial,nueva_temperatura,nueva_saturacion,nueva_frecuencia_respiratoria)
                            if opcion_4 == "2":
                                print("\n\n--- Actualizar Notas de Evolución ---")
                                print("\n\nLas notas de evolución actuales son:")
                                for item in encontrado.notas:
                                    print("  -", item) 
                                print("\n\nIngrese las nuevas notas de evolución del paciente:")
                                print("(Escriba 'Fin' para terminar la entrada de notas)\n\n")
                                while True:
                                    notas=input(">")
                                    if notas.lower()=="fin":
                                        break
                                    else:
                                        encontrado.agregar_notas(notas)
                            if opcion_4 == "3":
                                print("--- Actualizar Exámenes de Laboratorio ---")
                                print("\n\nLos resultados actuales son:")
                                for item in encontrado.resultados:
                                    print("  -", item) 
                                print("\n\nIngrese los nuevos resultados de laboratorio:")
                                print("(Escriba 'Fin' para terminar la entrada de resultados)\n\n")
                                while True:
                                    resultados=input(">")
                                    if resultados.lower()=="fin":
                                        break
                                    else:
                                        encontrado.agregar_resultados(resultados)
                            if opcion_4 == "4":
                                print("\n\n--- Actualizar Medicamentos Formulados ---")
                                print("\n\nLos Medicamentos actuales son:")
                                for item in encontrado.resultados:
                                    print("  -", item) 
                                print("\n\nIngrese los nuevos medicamentos formulados:")
                                print("(Escriba 'Fin' para terminar la entrada de resultados)\n\n")
                                medicamentos_servicio = set()
                                while True:
                                    medicamentos = input(">")
                                    if medicamentos.lower() == "fin":
                                        break
                                    else:
                                        if medicamentos not in medicamentos_servicio:
                                            encontrado.agregar_medicamentos(medicamentos)
                                            medicamentos_servicio.add(medicamentos)
                            if opcion_4 == "5":
                                hospital.alta(encontrado)
                            if opcion_4 == "6":
                                pass
                        if opcion_3 == "3":
                            pass
                    else:
                        print("La id u nombre no existen o no se han colocado correctamente.")
                elif opcion_2 == "2":
                    print("-- Registro de un nuevo paciente--")
                    hospital.registro()
                    input("Presione cualquier tecla para volver al menú principal.\n\n > ")
                elif opcion_2 == "3":
                    while True:
                        reportes()
                        opcion_5 = input("\n\n> ")
                        if opcion_5 == "1":
                            hospital.ocupacion_h()
                            input("Presione cualquier tecla para volver al menú de reportes.\n\n > ")
                        if opcion_5 == "2":
                            hospital.estancia_s()
                            input("Presione cualquier tecla para volver al menú de reportes.\n\n > ")
                        if opcion_5 == "3":
                            hospital.admisiones_altas()
                            input("Presione cualquier tecla para volver al menú de reportes.\n\n > ")
                        if opcion_5 == "4":
                            hospital.enfermedades_cronicas()
                            input("Presione cualquier tecla para volver al menú de reportes.\n\n > ")
                        if opcion_5 == "5":
                            hospital.medicamentos_servicio()
                            input("Presione cualquier tecla para volver al menú de reportes.\n\n > ")
                        if opcion_5 == "6":
                            break
                elif opcion_2 == "4":
                    print("\nGracias por utilizar nuestro sistema de información hospitalaria.",end ="") 
                    print("¡Hasta luego!")
                    exit()
        elif opcion == "2":
            print("\nGracias por utilizar nuestro sistema de información hospitalaria.",end ="") 
            print("¡Hasta luego!")
            break
        else:
            continue
main()
