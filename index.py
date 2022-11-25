import random # Libreria necesaria para crear numeros randoms

# Definimos el rango de los numeros aleatorios que se van a generar
MIN_NUMBER = 0
MAX_NUMBER = 1000

random.seed(20)  # Fijamos la semilla a 0

# Obtenemos los tres números aleatorios que
# se encuentren entre MIN_NUMBER y MAX_NUMBER
x = random.randint(MIN_NUMBER, MAX_NUMBER)
y = random.randint(MIN_NUMBER, MAX_NUMBER)
z = random.randint(MIN_NUMBER, MAX_NUMBER)

suma = x + (y + z)

# Mostramos el resultado de la suma por pantalla
print(suma)

# Al tener fijado una semilla veremos que el resultado siempre sera el mismo.
# Para modificar este comportamiento tendriamos que eliminar la semilla