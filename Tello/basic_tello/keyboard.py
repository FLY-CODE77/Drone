import pygame

def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))

def getKey(keyName):
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, "K_{}".format(keyName))

    if keyInpit[myKey]:
        ans = True
    pygame.display.updata()

    return ans

def main()
    if getKey("LEFT"):
        print("Left key pressed")
    
    if getKey("RIGHT"):
        print("Right key pressed")

if __name__ == "__main_":
    init()
    while True:
        main()
