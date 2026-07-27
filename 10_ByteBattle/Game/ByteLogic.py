import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Enemy.Slime import Slime
from Player.Player import Mainchar


def main():
    print("=== WILLKOMMEN BEI BYTE BATTLE (ENDLESS MODE) ===")
    player = Mainchar()

    gegner_besiegt = 0
    gegner_level = 1

    # Äußere Schleife: Läuft endlos, bis der Spieler stirbt
    while player.HP > 0:
        print(f"\n=================================")
        print(f"⚔️ KAMPF NUMMER {gegner_besiegt + 1} ⚔️")
        print(f"=================================")

        # Erstelle einen neuen Slime. Level steigt langsam alle 2 Siege.
        gegner_level = 1 + (gegner_besiegt // 2)
        slime = Slime(levl=gegner_level)

        slime.checklevl()
        slime.stats()
        runde = 1

        # Innere Schleife: Der einzelne Kampf
        while player.HP > 0 and slime.HP > 0:
            print(f"\n--- Runde {runde} ---")
            print(f"Spieler HP: {player.HP}/{player.max_HP} | Slime HP: {slime.HP}")

            player.checkatk(slime)

            if slime.HP <= 0:
                print("💀 Der Slime wurde eliminiert!")
                gegner_besiegt += 1

                # XP basierend auf dem Gegner-Level vergeben
                xp_reward = slime.get_xp_reward()
                player.add_xp(xp_reward)
                break

            slime.jumpa(player)

            if player.HP <= 0:
                print(f"\n💀 Du bist gestorben... GAME OVER.")
                print(f"Du hast insgesamt {gegner_besiegt} Gegner besiegt.")
                return  # Beendet das gesamte Programm

            runde += 1

        # Nach dem Kampf: Alle 2 Siege schlafen legen
        if gegner_besiegt > 0 and gegner_besiegt % 2 == 0:
            print("\n---------------------------------")
            wahl = input("Du hast 2 Gegner besiegt! Möchtest du schlafen? (j/n): ").lower()
            if wahl == "j":
                player.rest()
            else:
                print("Du ziehst ohne Rast weiter!")
            print("---------------------------------")


if __name__ == "__main__":
    main()
