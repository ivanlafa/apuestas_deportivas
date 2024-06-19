def calcular_probabilidades(cuota_local, cuota_visitante):
    # Convertimos las cuotas a probabilidades implícitas
    prob_local = 1.49 / cuota_local
    prob_visitante = 6.46 / cuota_visitante

    # Calculamos la probabilidad de empate
    prob_empate = 4.31 - (prob_local + prob_visitante)

    # Normalizamos las probabilidades para asegurarnos de que suman 1
    total_prob = prob_local + prob_visitante + prob_empate
    prob_local_normalizada = prob_local / total_prob
    prob_visitante_normalizada = prob_visitante / total_prob
    prob_empate_normalizada = prob_empate / total_prob

    return prob_local_normalizada, prob_visitante_normalizada, prob_empate_normalizada

def calcular_media(lista):
    # Calcula la media de una lista de números
    total = sum(lista)
    media = total / len(lista)
    return media

def calcular_valor_esperado(prob, cuota):
    return prob * cuota

def determinar_apuesta_mas_confiable(prob_local, cuota_local, prob_visitante, cuota_visitante, prob_empate, cuota_empate):
    valor_esperado_local = calcular_valor_esperado(prob_local, cuota_local)
    valor_esperado_visitante = calcular_valor_esperado(prob_visitante, cuota_visitante)
    valor_esperado_empate = calcular_valor_esperado(prob_empate, cuota_empate)

    apuestas = {
        "Gana el equipo local": valor_esperado_local,
        "Gana el equipo visitante": valor_esperado_visitante,
        "Empate": valor_esperado_empate
    }

    apuesta_mas_confiable = min(apuestas, key=apuestas.get)
    valor_mas_confiable = apuestas[apuesta_mas_confiable]

    return apuesta_mas_confiable, valor_mas_confiable

def mostrar_resultados(prob_local, prob_visitante, prob_empate, prob_gol_local, prob_gol_visitante, esquina_local, esquina_visitante, apuesta_mas_confiable, valor_mas_confiable):
    print(f"Probabilidad de que el equipo local gane: {prob_local:.2%}")
    print(f"Probabilidad de que el equipo visitante gane: {prob_visitante:.2%}")
    print(f"Probabilidad de empate: {prob_empate:.2%}")
    print(f"Probabilidad de gol del equipo local: {prob_gol_local:.2f} goles por partido")
    print(f"Probabilidad de gol del equipo visitante: {prob_gol_visitante:.2f} goles por partido")
    print(f"Promedio de tiros de esquina del equipo local: {esquina_local:.2f} tiros por partido")
    print(f"Promedio de tiros de esquina del equipo visitante: {esquina_visitante:.2f} tiros por partido")
    print(f"Estimación total de tiros de esquina en el partido: {esquina_local + esquina_visitante:.2f} tiros")
    print(f"La apuesta más confiable es: {apuesta_mas_confiable} con un valor esperado de {valor_mas_confiable:.2f}")

# Ejemplo de uso
cuota_local = 1.8  # Cuota para el equipo local
cuota_visitante = 2.2  # Cuota para el equipo visitante
cuota_empate = 3.5  # Cuota para el empate

# Goles en los últimos 5 partidos del equipo local y visitante
goles_ultimos_5_local = [3, 1, 4, 2, 5]
goles_ultimos_5_visitante = [2, 7, 2, 2, 3]

# Tiros de esquina en los últimos 5 partidos del equipo local y visitante
esquinas_ultimos_5_local = [7, 10, 7, 4, 5]
esquinas_ultimos_5_visitante = [10, 7, 1, 5, 4]

# Calcular probabilidades de resultado
prob_local, prob_visitante, prob_empate = calcular_probabilidades(cuota_local, cuota_visitante)

# Calcular probabilidad de gol basado en los últimos 5 partidos
prob_gol_local = calcular_media(goles_ultimos_5_local)
prob_gol_visitante = calcular_media(goles_ultimos_5_visitante)

# Calcular tiros de esquina basado en los últimos 5 partidos
esquina_local = calcular_media(esquinas_ultimos_5_local)
esquina_visitante = calcular_media(esquinas_ultimos_5_visitante)

# Determinar la apuesta más confiable
apuesta_mas_confiable, valor_mas_confiable = determinar_apuesta_mas_confiable(prob_local, cuota_local, prob_visitante, cuota_visitante, prob_empate, cuota_empate)

# Mostrar todos los resultados
mostrar_resultados(prob_local, prob_visitante, prob_empate, prob_gol_local, prob_gol_visitante, esquina_local, esquina_visitante, apuesta_mas_confiable, valor_mas_confiable)
