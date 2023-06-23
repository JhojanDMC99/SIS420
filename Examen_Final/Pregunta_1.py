import random

# Definir parámetros del algoritmo genético
tamano_poblacion = 100
tamano_horario = 10  # Tamaño del horario (número de horas)
num_generaciones = 50
probabilidad_cruce = 0.8
probabilidad_mutacion = 0.1

# Definir datos del problema
materias = ['Materia 1', 'Materia 2', 'Materia 3', 'Materia 4']
profesores = ['Profesor 1', 'Profesor 2', 'Profesor 3', 'Profesor 4']
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
horas_dia = ['08:00', '09:00', '10:00', '11:00', '12:00', '13:00']

# Función para generar un horario aleatorio
def generar_horario():
    horario = []
    for _ in range(tamano_horario):
        materia = random.choice(materias)
        profesor = random.choice(profesores)
        dia = random.choice(dias_semana)
        hora = random.choice(horas_dia)
        horario.append((materia, profesor, dia, hora))
    return horario

# Función para evaluar la aptitud de un horario
def evaluar_aptitud(horario):
    # Aquí puedes implementar tu función de evaluación de aptitud específica del problema
    # Puedes asignar una puntuación en base a la calidad del horario (ejemplo: evitando solapamientos, preferencias de profesores, etc.)
    return random.uniform(0, 1)

# Función de cruce de dos horarios
def cruzar_horarios(horario1, horario2):
    punto_cruce = random.randint(1, tamano_horario - 1)
    nuevo_horario = horario1[:punto_cruce] + horario2[punto_cruce:]
    return nuevo_horario

# Función de mutación de un horario
def mutar_horario(horario):
    indice_mutacion = random.randint(0, tamano_horario - 1)
    nueva_materia = random.choice(materias)
    nuevo_profesor = random.choice(profesores)
    nuevo_dia = random.choice(dias_semana)
    nueva_hora = random.choice(horas_dia)
    horario[indice_mutacion] = (nueva_materia, nuevo_profesor, nuevo_dia, nueva_hora)
    return horario

# Algoritmo genético para la programación de horarios
def algoritmo_genetico():
    # Generar población inicial
    poblacion = []
    for _ in range(tamano_poblacion):
        horario = generar_horario()
        poblacion.append(horario)

    # Evolución de la población
    for generacion in range(num_generaciones):
        # Evaluación de la aptitud de la población actual
        aptitudes = []
        for horario in poblacion:
            aptitud = evaluar_aptitud(horario)
            aptitudes.append((horario, aptitud))

        # Ordenar la población por aptitud (de mayor a menor)
        aptitudes = sorted(aptitudes, key=lambda x: x[1], reverse=True)

        # Elitismo: mantener los mejores individuos en la siguiente generación
        elite = [aptitudes[i][0] for i in range(tamano_poblacion // 10)]
        nueva_generacion = elite

        # Reproducción y cruce
        while len(nueva_generacion) < tamano_poblacion:
            padre1 = random.choice(aptitudes)[0]
            padre2 = random.choice(aptitudes)[0]

            if random.random() < probabilidad_cruce:
                hijo = cruzar_horarios(padre1, padre2)
            else:
                hijo = random.choice([padre1, padre2])

            # Mutación
            if random.random() < probabilidad_mutacion:
                hijo = mutar_horario(hijo)

            nueva_generacion.append(hijo)

        poblacion = nueva_generacion

    # Obtener el mejor horario de la última generación
    mejor_horario = max(aptitudes, key=lambda x: x[1])[0]
    return mejor_horario

# Ejecutar el algoritmo genético
mejor_horario = algoritmo_genetico()
print("Mejor horario encontrado:")
for i, clase in enumerate(mejor_horario):
    print(f"Clase {i+1}: {clase[0]} - {clase[1]} - {clase[2]} - {clase[3]}")
