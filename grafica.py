import random
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from typing import List, Tuple

def generate_random_glucose_data(
    start_datetime: datetime.datetime,
    end_datetime: datetime.datetime,
    min_glucose: int,
    max_glucose: int,
    mode: str = "day"
) -> Tuple[List[datetime.datetime], List[int]]:
    """
    Genera datos de glucosa aleatorios en intervalos de día, hora o minuto.
    
    Parámetros:
        start_datetime (datetime.datetime): Fecha y hora de inicio.
        end_datetime (datetime.datetime): Fecha y hora de fin.
        min_glucose (int): Nivel mínimo de glucosa.
        max_glucose (int): Nivel máximo de glucosa.
        mode (str): "minute", "hour", o "day".
        
    Retorna:
        timestamps (list): Lista de fechas/horas.
        glucose_levels (list): Lista de valores de glucosa generados.
    """
    if start_datetime >= end_datetime:
        raise ValueError("start_datetime debe ser anterior a end_datetime.")
    
    if mode not in ["minute", "hour", "day"]:
        raise ValueError("El modo debe ser 'minute', 'hour' o 'day'.")

    timestamps = []
    glucose_levels = []

    delta = {
        "minute": datetime.timedelta(minutes=1),
        "hour": datetime.timedelta(hours=1),
        "day": datetime.timedelta(days=1)
    }[mode]  # Selecciona el incremento basado en el modo

    current_datetime = start_datetime
    while current_datetime <= end_datetime:
        timestamps.append(current_datetime)
        glucose_levels.append(random.randint(min_glucose, max_glucose))
        current_datetime += delta

    return timestamps, glucose_levels

def plot_glucose_data(
    timestamps: List[datetime.datetime],
    glucose_levels: List[int],
    mode: str = "day",
    line_color: str = 'r',
    marker_size: int = 4,
    line_width: float = 1.2,
    alpha: float = 0.7
):
    """
    Grafica los niveles de glucosa en el tiempo.

    Parámetros:
        timestamps (list): Lista de fechas/horas.
        glucose_levels (list): Lista de valores de glucosa.
        mode (str): "minute", "hour", o "day".
        line_color (str): Color de la línea.
        marker_size (int): Tamaño de los marcadores.
        line_width (float): Ancho de la línea.
        alpha (float): Transparencia de la línea.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(timestamps, glucose_levels, marker='o', linestyle='-', color=line_color, markersize=marker_size, linewidth=line_width, alpha=alpha)
    plt.title(f'Glucose Levels Over Time ({mode.capitalize()})')
    plt.xlabel('Time')
    plt.ylabel('Glucose Level (mg/dL)')
    plt.grid(True, linestyle='--', alpha=0.5)

    if mode == "minute":
        plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=1))  # Mostrar 1 hora a la vez
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))  # Formato HH:MM
        plt.xticks(rotation=45)
        plt.xlim(timestamps[0], timestamps[min(len(timestamps) - 1, 60)])  # Zoom en la primera hora
    elif mode == "hour":
        plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=1))
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        plt.xticks(rotation=45)
    elif mode == "day":
        plt.gca().xaxis.set_major_locator(mdates.DayLocator())
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()

# Ejemplo de uso
if __name__ == "__main__":
    start_datetime = datetime.datetime(2025, 1, 30, 0, 0)  # Inicio: 00::00 AM
    end_datetime = datetime.datetime(2025, 1, 30, 23, 59)  # Fin: 11:59 PM
    min_glucose = 70
    max_glucose = 180

    mode = "minute"  # Cambia entre "minute", "hour" y "day"

    timestamps, glucose_levels = generate_random_glucose_data(start_datetime, end_datetime, min_glucose, max_glucose, mode)
    plot_glucose_data(timestamps, glucose_levels, mode, line_color='b', marker_size=5, line_width=1.5, alpha=0.8)