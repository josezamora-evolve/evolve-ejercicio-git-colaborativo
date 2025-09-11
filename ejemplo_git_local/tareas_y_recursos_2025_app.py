
def mostrar_menu():
    print("\n=== MENÚ ===")
    print("1. Ver todas las listas")
    print("2. Modificar estado de tareas")
    print("3. Modificar estado de objetivos")
    print("4. Salir")
    return input("Seleccione una opción (1-4): ")

def mostrar_lista(items, titulo):
    print(f"\n{titulo}")
    for i, (item, completado) in enumerate(items.items(), 1):
        print(f"{i}. [{'✓' if completado else ' '}] {item}")

def modificar_estado(items, titulo):
    while True:
        mostrar_lista(items, titulo)
        print("\nEscriba el número del elemento para cambiar su estado (o 0 para volver):")
        try:
            opcion = int(input())
            if opcion == 0:
                break
            if 1 <= opcion <= len(items):
                item = list(items.keys())[opcion - 1]
                items[item] = not items[item]
                print(f"Estado actualizado para: {item}")
            else:
                print("Número no válido. Intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def main(): 
    print("Hola, Equipo!")
    
    tareas = {
        "Hacer la compra": False,
        "Desarrollar app de correo": False,
        "Hacer un colacao": False,
        "Tirar la basura": False,
        "Hacer monográfico de pokémon": False,
        "Diseño de interfaz": False
    }

    recursos = ["2 Coches", "1 Oficina", "4 Mesas", "2 Portátiles"]
    
    objetivos = {
        "Buscar capital": False,
        "Preparar clases antes del lunes": False,
        "Sacar matrícula de honor": False
    }

    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            mostrar_lista(tareas, "Lista de cosas que hacer en 2025:")
            print("\nLista de recursos:")
            for i, recurso in enumerate(recursos, 1):
                print(f"{i}. {recurso}")
            mostrar_lista(objetivos, "Lista de objetivos:")
            
        elif opcion == "2":
            modificar_estado(tareas, "Lista de cosas que hacer en 2025:")
            
        elif opcion == "3":
            modificar_estado(objetivos, "Lista de objetivos:")
            
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
    