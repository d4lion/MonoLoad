from src import video_dowload
from colorama import Fore, init

init(autoreset=True)

MonoLoad = """
  __  __                   _                     _ 
 |  \/  |                 | |                   | |
 | \  / | ___  _ __   ___ | |     ___   __ _  __| |
 | |\/| |/ _ \| '_ \ / _ \| |    / _ \ / _` |/ _` |
 | |  | | (_) | | | | (_) | |___| (_) | (_| | (_| |
 |_|  |_|\___/|_| |_|\___/|______\___/ \__,_|\__,_|
"""


def main():
    print(Fore.CYAN + MonoLoad)
    url = input(Fore.YELLOW + "Type the url you want to dowload: " + Fore.WHITE) 
    video_dowload.dowload(url)




if __name__ == "__main__":
    main()