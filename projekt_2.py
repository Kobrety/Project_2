"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Michal Kolar
email: kobracz.mkgmail.com
"""


def vytvor_hraci_pole():
    return [[" " for _ in range(3)] for _ in range(3)]

def zobraz_hraci_pole(pole):
    separator = "+---+---+---+"  # Tento řetězec bude oddělovat řádky
    print(separator)  # Začátek hracího pole
    for i, radek in enumerate(pole):
        print("| " + " | ".join(radek) + " |")
        if i < 2:
            print(separator)  # Oddělovač mezi řádky
    print(separator)  # Konec hracího pole

def je_vyhra(pole, hrac):
    # Kontrola řádků, sloupců a diagonál
    for x in range(3):
        if all(pole[x][y] == hrac for y in range(3)) or all(pole[y][x] == hrac for y in range(3)):
            return True
    if all(pole[x][x] == hrac for x in range(3)) or all(pole[x][2 - x] == hrac for x in range(3)):
        return True
    return False

def je_remiza(pole):
    return all(pole[x][y] != " " for x in range(3) for y in range(3))

def ziskej_tah(hrac, pole):
    # Mapování čísel na pozice
    pozice_mapovani = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
    }
    
    while True:
        print(f"========================================")
        try:
            tah = int(input(f"Hráč {hrac.lower()} | Zadej číslo pole (1-9): "))
            if tah < 1 or tah > 9:
                print("Neplatný vstup! Zadej číslo mezi 1 a 9.")
                continue

            x, y = pozice_mapovani[tah]  # Získání pozice z mapování
            if pole[x][y] != " ":
                print("Toto pole je již obsazené, zkus jiné!")
                continue
            return x, y
        except ValueError:
            print("Neplatný vstup! Zadej číslo mezi 1 a 9.")

def piskvorky():
    # Zobrazení úvodních pravidel
    print("Welcome to Tic Tac Toe")
    print("========================================")
    print("GAME RULES:")
    print("Each player can place one mark (or stone) per turn on the 3x3 grid. The WINNER is")
    print("who succeeds in placing three of their marks in a:")
    print("* horizontal,")
    print("* vertical or")
    print("* diagonal row")
    print("========================================")
    print("Let's start the game\n")
    
    # Zadání jmen hráčů
    jmeno_1 = input("Zadejte jméno hráče X: ")
    jmeno_2 = input("Zadejte jméno hráče O: ")

    score = {jmeno_1: 0, jmeno_2: 0}
    while True:
        pole = vytvor_hraci_pole()
        hrac = jmeno_1  # Začíná hráč X
        while True:
            zobraz_hraci_pole(pole)
            x, y = ziskej_tah(hrac, pole)
            pole[x][y] = "X" if hrac == jmeno_1 else "O"
            if je_vyhra(pole, "X" if hrac == jmeno_1 else "O"):
                zobraz_hraci_pole(pole)
                print(f"============================================")
                print(f"Congratulations, the player {hrac.lower()} WON!")
                print(f"============================================")
                score[hrac] += 1
                break
            if je_remiza(pole):
                zobraz_hraci_pole(pole)
                print("Remíza!")
                break
            hrac = jmeno_2 if hrac == jmeno_1 else jmeno_1
        print(f"Skóre: {jmeno_1} - {score[jmeno_1]}, {jmeno_2} - {score[jmeno_2]}")
        if input("Chcete hrát znovu? (ano/ne): ").lower() != "ano":
            break

if __name__ == "__main__":
    piskvorky()