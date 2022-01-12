#This will be a pokemon battle simulator
class Pokemon:
    def __init__(self,name,type,hp,speed,attack,defense,special_defense, special_attack):
        self.name=name
        self.type=type
        self.hp=hp
        self.speed=speed
        self.attack=attack
        self.defense=defense
        self.special_defense=special_defense
        self.special_attack=special_attack
        self.damage=0
    
    def take_damage(self):
        self.damage=2
        print (f"Damage taken is {self.damage}")

pikachu=Pokemon("Pikachu","Electric",1,1,1,1,1,1)
pikachu.take_damage()