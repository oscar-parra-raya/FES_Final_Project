import random
from models import Measurement


def simulate_measurement(number_of_packets=10):
    """
    Genera una sesión ficticia para desarrollar el programa
    sin necesitar una conexión real.
    """
    if number_of_packets <= 0:
        raise ValueError("El número de paquetes debe ser mayor que cero.")

    latencies = []
    packets_received = 0

    for _ in range(number_of_packets):
        # Probabilidad sencilla de perder un paquete.
        if random.random() < 0.05:
            continue

        latency = random.uniform(15, 100)
        latencies.append(round(latency, 2))
        packets_received += 1

    return Measurement(
        latencies=latencies,
        packets_sent=number_of_packets,
        packets_received=packets_received
    )
