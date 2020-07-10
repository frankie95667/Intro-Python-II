from playsound import playsound
import random


class Monster:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.health = 100

    def __str__(self):
        return (f"""{self.name} - {self.description}
Health: {self.health}
""")

    def on_attack(self):
        is_hit = ["strong", "weak", "miss"]
        hit_is = is_hit[random.randint(0, 2)]
        if(hit_is == "strong"):
            playsound('sword_collide.mp3')
            playsound('slashkut.wav')
            self.health -= 30
        elif(hit_is == "weak"):
            playsound('sword_collide.mp3')
            playsound('slashkut.wav')
            self.health -= 20
        else:
            playsound('sword_swing.mp3')
        if(self.health <= 0):
            playsound('dying.wav')
        return self.health
