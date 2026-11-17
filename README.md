# SpeedCheck

Proyecto final de Fonaments d'Enginyeria de Software (FES).

SpeedCheck analiza la calidad de una conexión mediante:
- Latencia media (ping).
- Jitter.
- Porcentaje de pérdida de paquetes.

## Estado actual

Primera versión base: utiliza mediciones simuladas. Todavía no realiza pruebas reales de Internet.

## Requisitos

- Python 3.10 o superior.
- No necesita instalar librerías externas.

## Cómo ejecutar

Desde la carpeta `SpeedCheck`, ejecutar:

```bash
python3 main.py
```

## Cómo ejecutar las pruebas

```bash
python3 -m unittest discover -s tests
```

## Estructura

- `main.py`: menú e interacción con el usuario.
- `models.py`: clase Measurement.
- `analyzer.py`: cálculos y clasificación.
- `simulator.py`: generación de mediciones ficticias.
- `storage.py`: guardado y lectura del historial CSV.
- `data/`: datos guardados.
- `tests/`: pruebas automáticas.

## Criterios iniciales de calidad

Los valores de clasificación son orientativos y se podrán ajustar y justificar en la memoria:
- Excelente: ping < 50 ms, jitter < 10 ms y pérdida < 1%.
- Buena: ping < 100 ms, jitter < 20 ms y pérdida < 2%.
- Regular: ping < 150 ms, jitter < 30 ms y pérdida < 5%.
- Mala: cualquier resultado que no cumpla los criterios anteriores.

## Próximas mejoras

1. Añadir mediciones reales mediante ping a un servidor.
2. Permitir elegir el número de paquetes y el destino.
3. Añadir estadísticas y comparación de sesiones.
4. Incorporar gráficos e interfaz gráfica, si procede.
5. Ampliar las pruebas y documentar las limitaciones.
