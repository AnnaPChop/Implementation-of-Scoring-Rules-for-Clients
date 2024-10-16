
''' The analysis model created will be tested by generating the code with 100 different clients, with random results for each parameter, 
and finally by creating a graph of the scores of the 100 clients to visualize the health of the portfolio for that month. 
If the percentage of clients with a score above 90 percent exceeds 85% of the portfolio, we can hypothesize that the client portfolio is easy to recover. 
Otherwise, new negotiation tools would need to be implemented for account recovery.'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generar datos aleatorios para 100 clientes
np.random.seed(42)  # Para reproducibilidad
n_clientes = 100
clientes_data = {
    'Cliente': [f'Cliente_{i}' for i in range(1, n_clientes+1)],
    'Refinanciamientos': np.random.randint(0, 4, n_clientes),  # De 0 a 3 refinanciamientos
    'Mora_Meses': np.random.randint(0, 8, n_clientes),  # De 0 a 7 meses en mora
    'Cancelaciones': np.random.randint(0, 3, n_clientes),  # 0 a 2 solicitudes de cancelación
    'Aportaciones_Capital': np.random.randint(0, 2, n_clientes)  # 0 o 1 para aportaciones a capital
}

clientes = pd.DataFrame(clientes_data)
clientes['Score'] = 100  # Inicializar score en 100

# Función para calcular score basado en las reglas
def calcular_score(row):
    score = 100
    
    # Refinanciamientos (si hay refinanciamientos y no hay aportaciones a capital, se descuentan puntos)
    if row['Refinanciamientos'] > 0 and row['Aportaciones_Capital'] == 0:
        score -= row['Refinanciamientos']
    
    # Adeudos y Mora
    if 1 <= row['Mora_Meses'] <= 3:
        score -= 2
    elif 4 <= row['Mora_Meses'] <= 6:
        score -= 4
    elif row['Mora_Meses'] >= 7:
        score -= 6
    
    # Cancelaciones
    score -= row['Cancelaciones'] * 5
    
    return score

clientes['Score_Final'] = clientes.apply(calcular_score, axis=1)

# Gráfico de los puntajes de los clientes
plt.figure(figsize=(10, 6))
plt.hist(clientes['Score_Final'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribución del Score de los Clientes')
plt.xlabel('Score Final')
plt.ylabel('Número de Clientes')
plt.grid(True)
plt.show()

# Calcular porcentaje de clientes con score mayor al 90
clientes_recuperables = len(clientes[clientes['Score_Final'] > 90])
porcentaje_recuperables = (clientes_recuperables / n_clientes) * 100

# Mostrar si la cartera es fácil de recuperar o no
hipotesis = "fácil de recuperar" if porcentaje_recuperables > 85 else "necesita nuevas herramientas de negociación"
porcentaje_recuperables, hipotesis
