class Gun():
    name="awm"
    scope="8x"
    bullet_size=5.5
    def shoot(self):
        print("firing.....")
user=Gun()
print(f"name={Gun.name}")
print(f"scope={Gun.scope}")
print(f"bullet={Gun.bullet_size}")
user.shoot()
print("-----------------------")
class Clock():
    model="walk clock"
    Type="battery"
    def runing(self):
        print("working")
j=Clock()
print(Clock.model)
print(Clock.Type)
j.runing()
print("---------------------")
class Headphone():
    model="bluetooh"
    Type="wireless"
    company="apple"
    def music(self):
        print("songs playing...")
user2=Headphone()
print(Headphone.model)
print(Headphone.Type)
print(Headphone.company)
user2.music()

