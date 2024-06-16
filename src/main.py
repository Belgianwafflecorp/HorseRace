from race import Race
import os

# winget install --id Microsoft.WindowsTerminal -e
# Windows Terminal is not required to run the game, but it is recommended for a better experience.
os.system("winget install --id Microsoft.WindowsTerminal -e")

def main():
    while True:
        race = Race() 
        race.new_race()

if __name__ == "__main__":
    main()
