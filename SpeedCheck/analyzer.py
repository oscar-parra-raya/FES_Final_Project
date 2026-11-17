
def calculate_average_ping(latencies):
    """Devuelve la latencia media en milisegundos."""
    if not latencies:
        return 0.0
    return sum(latencies) / len(latencies)


def calculate_jitter(latencies):
    """
    Calcula el jitter como la media de las diferencias absolutas
    entre latencias consecutivas.
    """
    if len(latencies) < 2:
        return 0.0

    differences = []
    for index in range(1, len(latencies)):
        differences.append(abs(latencies[index] - latencies[index - 1]))

    return sum(differences) / len(differences)


def calculate_packet_loss(packets_sent, packets_received):
    """Calcula el porcentaje de paquetes perdidos."""
    if packets_sent == 0:
        return 0.0

    lost_packets = packets_sent - packets_received
    return (lost_packets / packets_sent) * 100


def classify_quality(average_ping, jitter, packet_loss):
    """
    Clasificación inicial del proyecto.
    Los umbrales son criterios orientativos definidos para este MVP.
    """
    if average_ping < 50 and jitter < 10 and packet_loss < 1:
        return "Excelente"
    elif average_ping < 100 and jitter < 20 and packet_loss < 2:
        return "Buena"
    elif average_ping < 150 and jitter < 30 and packet_loss < 5:
        return "Regular"
    return "Mala"


def analyze_measurement(measurement):
    """Calcula todos los indicadores de una sesión."""
    average_ping = calculate_average_ping(measurement.latencies)
    jitter = calculate_jitter(measurement.latencies)
    packet_loss = calculate_packet_loss(
        measurement.packets_sent,
        measurement.packets_received
    )
    quality = classify_quality(average_ping, jitter, packet_loss)

    return {
        "average_ping": average_ping,
        "jitter": jitter,
        "packet_loss": packet_loss,
        "quality": quality
    }
