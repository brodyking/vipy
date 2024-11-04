import os

class Clear:
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear');