import time

x = 100
y = 2
suund = 'down'

def elukas_print():
        elukas = "\033[" + str(y) + ";" + str(x) + "H$"
        elukas = "\033[91m" + elukas + "\033[0m"

        print elukas

def elukas_next():
        # Get pacman position
        pacman = player_xy()
        
        px = pacman[0]
        py = pacman[1]

        # Search pacman from right
        if px >= x and py >= y:
                # Look right
                if kaart_xy(x+1, y) == 1:
                        x = x+1
                        y = y
                        suund = 'right'
                # Look left
                elif kaart_xy(x-1, y) == 1:
                        x = x-1
                        y = y
                        suund = 'left'
                # Look up
                elif kaart_xy(x, y-1) == 1:
                        x = x
                        y = y-1
                        suund = 'up'
                # Look down
                elif kaart_xy(x, y+1) == 1:
                        x = x
                        y = y+1
                        suund = 'down'
                        

        # Search pacman from left
        if px <= x and py == y:
                # Look left
                if kaart_xy(x-1, y) == 1:
                        x = x-1
                        y = y
                        suund = 'left'
                # Look right
                elif kaart_xy(x+1, y) == 1:
                        x = x+1
                        y = y
                        suund = 'right'
                # Look up
                elif kaart_xy(x, y-1) == 1:
                        x = x
                        y = y-1
                        suund = 'up'
                # Look down
                elif kaart_xy(x, y+1) == 1:
                        x = x
                        y = y+1
                        suund = 'down'
                        

        # Search pacman from top
        if px == x and py <= y:
                # Look up
                if kaart_xy(x, y-1) == 1:
                        x = x
                        y = y-1
                        suund = 'up'
                # Look down
                elif kaart_xy(x, y+1) == 1:
                        x = x
                        y = y+1
                        suund = 'down'
                # Look left
                elif kaart_xy(x-1, y) == 1:
                        x = x-1
                        y = y
                        suund = 'left'
                # Look right
                elif kaart_xy(x+1, y) == 1:
                        x = x+1
                        y = y
                        suund = 'right'

        # Search pacman from bottom
        if px == x and py >= y:
                # Look down
                if kaart_xy(x, y+1) == 1:
                        x = x
                        y = y+1
                        suund = 'down'
                # Look up
                elif kaart_xy(x, y-1) == 1:
                        x = x
                        y = y-1
                        suund = 'up'
                # Look left
                elif kaart_xy(x-1, y) == 1:
                        x = x-1
                        y = y
                        suund = 'left'
                # Look right
                elif kaart_xy(x+1, y) == 1:
                        x = x+1
                        y = y
                        suund = 'right'
                                


def elukas_xy():
        return [x, y]
