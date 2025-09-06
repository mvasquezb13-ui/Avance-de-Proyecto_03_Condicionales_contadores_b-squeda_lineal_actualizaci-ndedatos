#Gestor de Notas 
# Lista para almacenar cursos y sus notas
cursos = {}

# Función para validar si una entrada es numérica
def es_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

# Función para buscar un curso (búsqueda lineal)
def buscar_curso(nombre):
    for curso in cursos:
        if curso.lower() == nombre.lower():
            return curso
    return None

# Menú principal
while True:
    print("\n===== GESTOR DE NOTAS =====")
    print("1. Registrar curso y notas")
    print("2. Mostrar todos los cursos y notas")
    print("3. Calcular promedio por curso")
    print("4. Actualizar notas de un curso")
    print("5. Eliminar un curso")
    print("6. Contar cursos y notas")
    print("7. Salir")

    opcion = input("Seleccione una opción (1-7): ")

    if opcion == "1":
        # 1 Registrar curso y notas
        nombre_curso = input("Ingrese el nombre del curso: ").strip()
        if nombre_curso == "":
            print("El nombre del curso no puede estar vacío.")
            continue

        if buscar_curso(nombre_curso):
            print("Ese curso ya existe.")
            continue

        notas = []
        print("Ingrese las notas para el curso (escriba 'final' para terminar):")
        while True:
            entrada = input("Nota: ")
            if entrada.lower() == "final":
                break
            elif entrada.strip() == "":
                print("La nota no puede estar vacía.")
            elif not es_numero(entrada):
                print("Entrada inválida. Ingrese una nota numérica.")
            else:
                notas.append(float(entrada))
        
        cursos[nombre_curso] = notas
        print(f"Curso '{nombre_curso}' registrado con {len(notas)} nota(s).")

    elif opcion == "2":
        # 2 Mostrar todos los cursos y notas
        if not cursos:
            print("No hay cursos registrados.")
        else:
            print("\nCursos y notas:")
            for curso, notas in cursos.items():
                print(f"- {curso}: {notas}")

    elif opcion == "3":
        # 3 Calcular promedio por curso
        nombre_curso = input("Ingrese el nombre del curso: ").strip()
        curso_encontrado = buscar_curso(nombre_curso)
        if curso_encontrado:
            notas = cursos[curso_encontrado]
            if notas:
                promedio = sum(notas) / len(notas)
                print(f"Promedio de '{curso_encontrado}': {promedio:.2f}")
            else:
                print("Este curso no tiene notas registradas.")
        else:
            print("Curso no encontrado.")

    elif opcion == "4":
        # 4 Actualizar notas de un curso
        nombre_curso = input("Ingrese el nombre del curso a actualizar: ").strip()
        curso_encontrado = buscar_curso(nombre_curso)
        if curso_encontrado:
            print(f"Notas actuales: {cursos[curso_encontrado]}")
            nuevas_notas = []
            print("Ingrese las nuevas notas (escriba 'fin' para terminar):")
            while True:
                entrada = input("Nota: ")
                if entrada.lower() == "fin":
                    break
                elif entrada.strip() == "":
                    print("La nota no puede estar vacía.")
                elif not es_numero(entrada):
                    print("Entrada inválida. Ingrese una nota numérica.")
                else:
                    nuevas_notas.append(float(entrada))
            cursos[curso_encontrado] = nuevas_notas
            print(f"Notas actualizadas para el curso '{curso_encontrado}'.")
        else:
            print("Curso no encontrado.")

    elif opcion == "5":
        # 5 Eliminar un curso
        nombre_curso = input("Ingrese el nombre del curso a eliminar: ").strip()
        curso_encontrado = buscar_curso(nombre_curso)
        if curso_encontrado:
            del cursos[curso_encontrado]
            print(f"Curso '{curso_encontrado}' eliminado.")
        else:
            print("Curso no encontrado.")

    elif opcion == "6":
        # 6 Contar cursos y notas
        total_cursos = len(cursos)
        total_notas = sum(len(notas) for notas in cursos.values())
        print(f"Total de cursos: {total_cursos}")
        print(f"Total de notas registradas: {total_notas}")


    elif opcion == "7":
        # 8 Salir del programa
        print("Gracias por usar el gestor de notas. ¡Hasta pronto!")
        break

    else:
        print("Opción inválida. Intente nuevamente.")
