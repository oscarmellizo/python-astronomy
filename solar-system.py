import numpy as np
import matplotlib.pyplot as plt

# Definición de constantes
G = 6.67430e-11  # Constante de gravitación universal (m^3 kg^-1 s^-2)
m_sun = 1.989e30  # Masa del Sol (kg)

# Definición de las masas de los planetas (en kg)
m_planet1 = 5.972e24  # Masa de la Tierra
m_planet2 = 6.39e23   # Masa de Marte

# Definición de las posiciones iniciales de los planetas (en metros)
r_planet1 = np.array([0, 0])     # La Tierra comienza en el origen
r_planet2 = np.array([1.5e11, 0])  # Marte comienza a 1.5e11 metros del Sol

# Definición de las velocidades iniciales de los planetas (en m/s)
v_planet1 = np.array([0, 29780])   # Velocidad orbital de la Tierra
v_planet2 = np.array([24130, 0])    # Velocidad orbital de Marte

# Definición de la función de aceleración debida a la gravedad
def gravitational_acceleration(r, m):
    r_sun = np.array([0, 0])  # Posición del Sol (que está en el origen)
    r_vector = r_sun - r      # Vector de posición desde el planeta hasta el Sol
    r_norm = np.linalg.norm(r_vector)  # Magnitud del vector de posición
    return (G * m_sun / r_norm**3) * r_vector

# Simulación del movimiento de los planetas durante un año (en segundos)
timestep = 86400  # Un día en segundos
num_steps = 365   # Número de pasos (días)
positions_planet1 = [r_planet1]
positions_planet2 = [r_planet2]

for _ in range(num_steps):
    # Calcula la aceleración debida a la gravedad en las posiciones actuales
    a_planet1 = gravitational_acceleration(r_planet1, m_planet1)
    a_planet2 = gravitational_acceleration(r_planet2, m_planet2)
    
    # Actualiza las velocidades de los planetas usando la aceleración
    v_planet1 += a_planet1 * timestep
    v_planet2 += a_planet2 * timestep
    
    # Actualiza las posiciones de los planetas usando las velocidades
    r_planet1 += v_planet1 * timestep
    r_planet2 += v_planet2 * timestep
    
    # Guarda las nuevas posiciones
    positions_planet1.append(r_planet1.copy())
    positions_planet2.append(r_planet2.copy())

# Convertir la lista de posiciones en un array de NumPy para facilitar el trazado
positions_planet1 = np.array(positions_planet1)
positions_planet2 = np.array(positions_planet2)

# Graficar las órbitas de los planetas
plt.plot(positions_planet1[:, 0], positions_planet1[:, 1], label='Tierra')
plt.plot(positions_planet2[:, 0], positions_planet2[:, 1], label='Marte')
plt.scatter([0], [0], color='yellow', marker='o', label='Sol')
plt.xlabel('Posición en x (m)')
plt.ylabel('Posición en y (m)')
plt.title('Órbitas de la Tierra y Marte durante un año')
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.show()
