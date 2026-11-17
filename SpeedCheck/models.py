from dataclasses import dataclass
from datetime import datetime


@dataclass
class Measurement:
    """Representa una sesión de medición de conexión."""

    latencies: list[float]
    packets_sent: int
    packets_received: int
    timestamp: str = ""

    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if self.packets_sent < 0 or self.packets_received < 0:
            raise ValueError("El número de paquetes no puede ser negativo.")

        if self.packets_received > self.packets_sent:
            raise ValueError("Los paquetes recibidos no pueden superar los enviados.")

        if any(value < 0 for value in self.latencies):
            raise ValueError("La latencia no puede ser negativa.")

        if len(self.latencies) != self.packets_received:
            raise ValueError(
                "Debe existir una latencia por cada paquete recibido."
            )
