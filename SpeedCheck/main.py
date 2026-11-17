from analyzer import analyze_measurement
from simulator import simulate_measurement
from storage import save_measurement, load_measurements


def show_result(result):
    print("\n========== SPEEDCHECK ==========")
    print(f"Latencia media:      {result['average_ping']:.2f} ms")
    print(f"Jitter:              {result['jitter']:.2f} ms")
    print(f"Paquetes perdidos:   {result['packet_loss']:.2f} %")
    print(f"Calidad:             {result['quality']}")
    print("================================\n")


def run_speed_test():
    print("\nIniciando medición simulada...")
    measurement = simulate_measurement()
    result = analyze_measurement(measurement)
    show_result(result)
    save_measurement(measurement, result)
    print("Medición guardada en el historial.")


def show_history():
    history = load_measurements()

    if not history:
        print("\nTodavía no hay mediciones guardadas.\n")
        return

    print("\n========== HISTORIAL ==========")
    for index, item in enumerate(history, start=1):
        print(
            f"{index}. {item['timestamp']} | "
            f"Ping: {float(item['average_ping']):.2f} ms | "
            f"Jitter: {float(item['jitter']):.2f} ms | "
            f"Pérdida: {float(item['packet_loss']):.2f}% | "
            f"Calidad: {item['quality']}"
        )
    print("================================\n")


def main():
    while True:
        print("========== SPEEDCHECK ==========")
        print("1. Realizar test de velocidad (simulado)")
        print("2. Consultar historial")
        print("0. Salir")

        option = input("Selecciona una opción: ").strip()

        if option == "1":
            run_speed_test()
        elif option == "2":
            show_history()
        elif option == "0":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción incorrecta. Introduce 1, 2 o 0.\n")


if __name__ == "__main__":
    main()
