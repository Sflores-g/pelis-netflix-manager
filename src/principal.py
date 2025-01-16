import csv

peliculas = []


def subir_peliculas():
    global peliculas
    ruta_archivo = input ("Ingrese la ruta del archivo: ") 

    try:
        with open(ruta_archivo, mode= "r", encoding="utf-8") as archivo:
            lector=csv.DictReader(archivo)
            peliculas = [fila for fila in lector]
        print ("Peliculas cargada correctamente. ")
    except FileNotFoundError:
        print("El aarchivo no fue encontrado")
    except Exception  as e:
        print(f"Error al cargar el archivo:  {e}")

def buscar_por_titulo():
    if not peliculas:
        print("No hay peliculas cargadas. ")
        return
    
    titulo= input("Introduce el titulo de la pelicula a buscar: ").lower()
    resultados = [pelicula for pelicula in peliculas if titulo in pelicula['title'].lower()]
    if resultados:
        for pelicula in resultados:
            print(f"Título: {pelicula['title']}, Año: {pelicula['year']}, Actores: {pelicula['cast']}")
    else:
        print("No se encontraron películas con ese título.")

def buscar_por_actor():
    if not peliculas:
        print("No hay películas cargadas.")
        return
    
    actor = input("Introduce el nombre del actor a buscar: ").lower()
    resultados = [pelicula for pelicula in peliculas if actor in pelicula['cast'].lower()]
    
    if resultados:
        for pelicula in resultados:
            print(f"Título: {pelicula['title']}, Año: {pelicula['year']}, Actores: {pelicula['cast']}")
    else:
        print("No se encontraron películas con ese actor.")

# Función para mostrar el menú
def mostrar_menu():
    while True:
        print("\n--- Menú ---")
        print("1. Cargar películas")
        print("2. Buscar por título")
        print("3. Buscar por actor")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            subir_peliculas()
        elif opcion == '2':
            buscar_por_titulo()
        elif opcion == '3':
            buscar_por_actor()
        elif opcion == '4':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, selecciona nuevamente.")

# Ejecutar la aplicación
if __name__ == "__main__":
    mostrar_menu()
   
