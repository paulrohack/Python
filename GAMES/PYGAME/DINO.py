import pygame, random
pygame.init()
w, h = 900, 350
screen = pygame.display.set_mode((w, h))

class Player():
    def __init__(self, window, size, color, width, height):
        self.size = size
        self.color = color
        self.window = window
        self.posx = 10/100 * width
        self.posy = height - size
        self.player_box = pygame.Rect(self.posx, self.posy, self.size, self.size)
    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.posx, self.posy, self.size, self.size))
    def Jump(self, UpVelocity):
        self.posy -= UpVelocity

class Enemy():
    def __init__(self, window, color, width, height, sizey):
        self.window = window
        self.color = color
        self.width = width
        self.height = height
        self.posx = width
        self.sizey = sizey
        self.posy = height - sizey
        self.Enemy_box = pygame.Rect(self.posx, self.posy, 20, self.sizey)
 
    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.posx, self.posy, 20, self.sizey))
    def Move(self, SideSpeed):
        self.posx -= SideSpeed

    
Cacti = []
cactus_wave = 20
Dino = Player(screen, 50, pygame.Color("Green"), w, h)
Jump = False
cactus_speed = 6
UpVelocity = 25
Gravity = 8
def collide_check(Player, Enemy):
    pygame.Rect.colliderect(Player, Enemy)
while True:
    pygame.time.Clock().tick(60)
    screen.fill(pygame.Color("Black"))
    Dino.draw()

    if len(Cacti) == 0:
        cactus = Enemy(screen , pygame.Color("Red"), w, h, random.randint(10, 100))
        Cacti.append(cactus)
    if cactus.posx < w/3:
        cactus_speed += 0.2
        if cactus_speed >= 15:
            cactus_speed = 6
        #print(cactus_speed)
        cactus_wave += 10
        for _ in range(cactus_wave):
            cactus = Enemy(screen , pygame.Color("Red"), w, h, random.randint(10, 100))
            Cacti.append(cactus)
    for cactus in Cacti:
        cactus.draw()
    for cactus in Cacti[:]:
        cactus.Move(cactus_speed)
        if cactus.posx <= 0:
            Cacti.remove(cactus)
    if Dino.posy <= h - Dino.size:
        Dino.posy += Gravity

    keys = pygame.key.get_pressed()
    if Dino.posy >= h - Dino.size:
        Jump = True
        v = UpVelocity
    if Dino.posy <= h - Dino.size - 250:
        Jump = False
        v = 0


    if keys[pygame.K_SPACE] and Jump:                
        Dino.Jump(v)
    print(Dino.player_box.colliderect(cactus.Enemy_box))
    pygame.display.update()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()

