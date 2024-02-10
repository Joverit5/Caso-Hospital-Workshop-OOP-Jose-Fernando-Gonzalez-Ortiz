from datetime import date
from datetime import datetime
class Paciente:
    def __init__(self, identificacion, nombre, sexo, fecha_de_nacimiento):
        self.identificacion = identificacion
        self.nombre = nombre
        self.sexo = sexo
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.notas = []
        self.imagen = []
        self.resultados = []
        self.medicamentos= []
        self.ingreso = ""
        self.diagnostico = ""
        self.cronica = 0
        self.servicio = ""
      
    def signos(self,presion_arterial, temperatura, saturacion, frecuencia_respiratoria):
        self.signos_vitales = {
            "presion_arterial": presion_arterial,
            "temperatura": temperatura,
            "saturacion": saturacion,
            "frecuencia_respiratoria": frecuencia_respiratoria
        }
    def actualizar_signos(self,presion_arterial, temperatura, saturacion, frecuencia_respiratoria):
        self.signos_vitales = {
            "presion_arterial": presion_arterial,
            "temperatura": temperatura,
            "saturacion": saturacion,
            "frecuencia_respiratoria": frecuencia_respiratoria
        }
            
    def agregar_imagen(self,imagen):
        self.imagen.append(imagen)    

    def agregar_resultados(self,resultados):
        self.resultados.append(resultados)

    def agregar_medicamentos(self,medicamentos):
        self.medicamentos.append(medicamentos)

    def agregar_notas(self,notas):
        self.notas.append(notas)

    def imprimir_listas(self):
        print("\n\n- Notas de evolución:")
        for item in self.notas:
            print("  -", item)
        print("\n\n- Resultados de Exámenes de Laboratorio:")
        for item in self.resultados:
            print("  -", item)
        print("\n\n- Imágenes Diagnósticas:")
        for item in self.imagen:
            print("  -", item)    
        print("\n\n- Medicamentos Formulados:")
        for item in self.medicamentos:
            print("  -", item)             

    def detalles(self,ingreso,diagnostico,cronica):
        self.ingreso = ingreso
        self.diagnostico = diagnostico
        self.cronica = cronica


class Hospital:
    def __init__(self):
        self.pacientes = []
        self.pacientes_alta = []         
        self.camas = 300
        self.servicio = ["1. General", "2. Cardiología","3. Neumología","4. Gastroenterología","5. Traumatología","6. Pediatría"]
    
    def registro(self):
        if self.camas <= 0:
            "No se pueden ingresar pacientes, no hay camas disponibles."
        else:
            print("Ingrese los siguientes datos del paciente:\n\n")
            identificacion = input("Documento de identidad: ")
            nombre = input("Nombre completo: ")
            while True:
                sexo = input("Sexo (M o F): ")
                if sexo.lower() not in ["m", "f"]:
                    continue
                else:
                    break
            while True:
                fecha_de_nacimiento = input("Fecha de nacimiento (DD-MM-AAAA): ")
                fecha_actual = datetime.now().date()
                fecha_nacimiento = datetime.strptime(fecha_de_nacimiento, "%d-%m-%Y").date()
                if fecha_nacimiento > fecha_actual:
                    print("La fecha de nacimiento no puede ser mayor que la fecha actual.")
                else: 
                    break
            while True:
                ingreso = input("Fecha de ingreso (DD-MM-AAAA): ")
                fecha_ingreso = datetime.strptime(ingreso, "%d-%m-%Y").date()
                if  fecha_ingreso > fecha_actual:
                    print("La fecha de ingreso no puede ser mayor que la fecha actual.")
                else:
                    break
            paciente = Paciente(identificacion, nombre, sexo, fecha_de_nacimiento)        
            while True:
                print("Seleccione el número de servicio necesitado:\n\n")
                print(self.servicio)                
                servicio_ = int(input("\n\n> "))
                if servicio_ <= 0 or servicio_ > 6:
                    print("Opción inválida.\nIntente nuevamente.")
                else:
                    break
            paciente.servicio = self.servicio[servicio_- 1]
            print("\n\nIngrese los signos vitales del paciente:\n\n")
            while True:
                presion_arterial = input("Presion arterial (mmHg): ")
                if presion_arterial < "0":
                    pass
                else:
                    break
            temperatura = int(input("Temperatura (°C): "))
            while True:
                saturacion =  float(input("Saturación de oxígeno en la sangre (%): "))
                if saturacion < 0:
                    pass
                else:
                    break
            while True:   
                frecuencia_respiratoria = float(input("Frecuencia respiratoria (respiraciones por minuto): "))
                if frecuencia_respiratoria < 0:
                    pass
                else:
                    break
            paciente.signos(presion_arterial,temperatura,saturacion,frecuencia_respiratoria)
            diagnostico = input("Diagnóstico: ")
            while True:
                cronica = input("¿La enfermedad es crónica? (Si/No): ")
                if cronica.lower() not in ["s", "n","si","no"]:
                    continue
                else:
                    if cronica.lower == "s" or cronica.lower == "si":
                        contador += 1
                        self.cronicas.append(paciente.diagnostico)
                    break
            print("\n\nEscriba las notas u observaciones sobre el paciente:")
            print("(Escriba 'Fin' para terminar la entrada de notas)\n\n")
            while True:
                notas=input(">")
                if notas.lower()=="fin":
                    break
                else:
                    paciente.agregar_notas(notas)
            print("\n\nIngrese las imágenes diagnósticas:")
            print("(Escriba 'Fin' para terminar la carga)\n\n")
            while True:
                imagen= input(">")
                if imagen.lower() == "fin":
                    break
                else:
                    paciente.agregar_imagen(imagen)
            print("\n\nIngrese los resultados de los exámenes de laboratorio:")
            print("(Escriba 'Fin' para terminar la entrada de resultados)\n\n")
            while True:
                resultados= input(">")
                if resultados.lower() == "fin":
                    break
                else:
                    paciente.agregar_resultados(resultados)
            print("\n\nIngrese los medicamentos formulados:")
            print("(Escriba 'Fin' para terminar la entrada de medicamentos)\n\n")
            medicamentos_servicio = set()
            while True:
                medicamentos = input(">")
                if medicamentos.lower() == "fin":
                    break
                else:
                    if medicamentos not in medicamentos_servicio:
                        paciente.agregar_medicamentos(medicamentos)
                        medicamentos_servicio.add(medicamentos)
            paciente.detalles(ingreso,diagnostico,cronica)
            self.pacientes.append(paciente)
            self.camas -=1
            if paciente.sexo.lower() =="f":
                print("\n\nLa paciente",paciente.nombre,"ha sido registrada exitosamente.")
            elif paciente.sexo.lower()=="m":
                print("\n\nEl paciente",paciente.nombre,"ha sido registrado exitosamente.")
            return paciente
        
    def busqueda(self, id):
        for paciente in self.pacientes:
            if paciente.identificacion == id or paciente.nombre.lower() == id.lower():
                return paciente
        return None
    
    def alta(self, paciente):
        self.pacientes.remove(paciente)
        print("El paciente ",paciente.nombre," ha sido dado de alta exitosamente.")
        self.camas += 1
        self.pacientes_alta.append(paciente)

    def ocupacion_h(self):
        print("\n\n--- Reporte de Porcentaje de Ocupación Hospitalaria ---")
        print("Fecha:", datetime.now().strftime("%d/%m/%Y"))
        porcentaje = ((300 - self.camas) / 300) * 100
        print("Porcentaje de ocupación: ", round(porcentaje,2), "%")
        print("Camas disponibles: ", self.camas)

    def estancia_s(self):
        print("\n\n--- Reporte de Promedio de Estancia por Servicio ---")
        print("Fecha:", datetime.now().strftime("%d/%m/%Y"))
        print("Servicio              |  Promedio de estancia (días)")
        print("----------------------------------------------------")
        for servicio in self.servicio:
            dias_totales = 0
            pacientes_por_servicio = 0
            for paciente in self.pacientes:
                if paciente.servicio == servicio:
                    pacientes_por_servicio += 1
                    fecha_ingreso = datetime.strptime(paciente.ingreso, "%d-%m-%Y")
                    dias_estancia = (datetime.now() - fecha_ingreso).days
                    dias_totales += dias_estancia
                if pacientes_por_servicio > 0:
                    promedio_estancia = dias_totales / pacientes_por_servicio
                else:
                    promedio_estancia = 0
            print(servicio,"|", round(promedio_estancia,2))

    def admisiones_altas(self):
        print("\n\n--- Reporte de Cantidad de Admisiones y Altas por Servicio ---")
        print("Fecha:", datetime.now().strftime("%d/%m/%Y"))
        print("Servicio             | Admisiones | Altas")
        print("----------------------------")
        for servicio in self.servicio:
            pacientes_por_servicio = 0
            altas_por_servicio = 0 
            for paciente in self.pacientes:
                if paciente.servicio == servicio:
                    pacientes_por_servicio += 1
            for paciente in self.pacientes_alta:
                if paciente.servicio == servicio:
                    altas_por_servicio += 1
            print(servicio,"|", pacientes_por_servicio,"|", altas_por_servicio)
            
    def enfermedades_cronicas(self):
        print("\n\n--- Reporte de Pacientes con Enfermedades Crónicas ---")
        print("Fecha:", datetime.now().strftime("%d/%m/%Y"))
        print("Enfermedades crónicas detectadas:")
        
        self.cronicas = {}
        for paciente in self.pacientes:
            if paciente.cronica.lower() == "s" or paciente.cronica.lower() == "si":
                enfermedad = paciente.diagnostico.strip()
                if enfermedad in self.cronicas:
                    self.cronicas[enfermedad] += 1
                else:
                    self.cronicas[enfermedad] = 1
        num = 1
        for enfermedad, cantidad in self.cronicas.items():
            print(num,".",enfermedad, "-",cantidad, "pacientes")
            num += 1
    def medicamentos_servicio(self):
        print("\n\n--- Reporte de Prescripción de Medicamentos por Servicio ---")
        print("Fecha:", datetime.now().strftime("%d-%m-%Y"))
        print("Servicio             | Medicamento               | Cantidad")
        print("-------------------------------------------------------------")
        medicamentos_servicio = {}
        for paciente in self.pacientes:
            servicio = paciente.servicio
            medicamentos = paciente.medicamentos
            for medicamento in medicamentos:
                if (servicio, medicamento) not in medicamentos_servicio:
                    medicamentos_servicio[(servicio, medicamento)] = 1
                else:
                    medicamentos_servicio[(servicio, medicamento)] += 1
        for (servicio, medicamento), cantidad in medicamentos_servicio.items():
            print(servicio,"|",medicamento,"|",cantidad)        