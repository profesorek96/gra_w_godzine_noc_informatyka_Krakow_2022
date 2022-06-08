import pgzrun
WIDTH = 800
HEIGHT = 480

class Samolot(Actor):
    def __init__(self,x,y):
        super(Samolot, self).__init__("planered1", (x, y))
        self.klatak=0
    def update(self):
        if self.klatak<5:
            self.image="planered1"
        elif self.klatak<10:
            self.image = "planered2"
        else:
            self.image = "planered3"
        self.klatak+=1
        self.klatak%=15

gracz = Samolot(200,200)
przeszkody=[Actor("rockgrass",midbottom=(400,480)),
            Actor("rockgrassdown",midtop=(700,0)),
            Actor("rockgrass", midbottom=(1100, 480)),
            Actor("rockgrassdown", midtop=(1400, 0))]
stan_gry=1
szybkosc_gry=4
def draw():
    screen.clear()
    screen.blit("background",(0,0))
    gracz.draw()
    for i in przeszkody:
        i.draw()
    if stan_gry==0:
        screen.draw.text("KONIEC GRY", center=(400, 240), color="orange",fontsize=60)


def update():
    global stan_gry,gracz,przeszkody,szybkosc_gry
    if stan_gry==1:
        gracz.update()
        if keyboard.UP:
            gracz.y-=szybkosc_gry
            gracz.angle=20
        elif keyboard.DOWN:
            gracz.y += szybkosc_gry
            gracz.angle = -20
        for i in przeszkody:
            i.x-=szybkosc_gry
            if i.x<-54:
                i.x=1200
            if i.collidepoint(gracz.pos):
                stan_gry=0
    else:
        if keyboard.R:
            gracz = Samolot(200, 200)
            przeszkody = [Actor("rockgrass", midbottom=(400, 480)),
                          Actor("rockgrassdown", midtop=(700, 0)),
                          Actor("rockgrass", midbottom=(1100, 480)),
                          Actor("rockgrassdown", midtop=(1400, 0))]
            stan_gry = 1
            szybkosc_gry=4

def zmian_szybkosc():
    global szybkosc_gry
    if szybkosc_gry<8:
        szybkosc_gry+=1

clock.schedule_interval(zmian_szybkosc,2)
pgzrun.go()