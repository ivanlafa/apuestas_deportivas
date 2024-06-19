import random
import time


class AviatorGame:
    def __init__(self):
        self.coefficient = 1.0
        self.is_flying = True

    def start_flight(self):
        self.coefficient = 1.0
        self.is_flying = True
        print("El avión ha despegado!")

    def update_coefficient(self):
        if self.is_flying:
            increment = random.uniform(0.01, 0.1)
            self.coefficient += increment
            print(f"El coeficiente actual es: {self.coefficient:.2f}")

    def stop_flight(self):
        self.is_flying = False
        print("El avión ha dejado de volar!")


def main():
    game = AviatorGame()
    balance = 100.0  # Balance inicial del jugador

    while True:
        print(f"\nBalance actual: {balance:.2f}")
        bet = float(input("Ingrese su apuesta (0 para salir): "))
        if bet == 0:
            break
        if bet > balance:
            print("Apuesta inválida. No tienes suficiente balance.")
            continue

        balance -= bet
        game.start_flight()

        try:
            while game.is_flying:
                game.update_coefficient()
                time.sleep(1)  # Simula el paso del tiempo

                action = input(
                    "Escriba 'retirar' para retirar su apuesta o presione Enter para continuar: ").strip().lower()
                if action == 'retirar':
                    winnings = bet * game.coefficient
                    balance += winnings
                    print(f"¡Has retirado tu apuesta! Ganaste {winnings:.2f}")
                    break

            if game.is_flying:
                game.stop_flight()
                print("El avión ha dejado de volar antes de que pudieras retirar tu apuesta.")

        except KeyboardInterrupt:
            print("\nJuego interrumpido. Saliendo del juego.")
            break

    print(f"Te retiras con un balance de: {balance:.2f}")


if __name__ == "__main__":
    main()
