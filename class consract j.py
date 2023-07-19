class Bike():
    def __init__(self,n,k,m):
        self.name=n
        self.mail=m
        self.kml=k
        
    def speed(self):
        print(f"{self.name}fastest speed....")

p=Bike("pulser",50,110)
s=Bike("dio",40,80)
z=Bike("zest",42,80)

print(p.name,p.kml,p.mail)
p.speed()
print(s.name,s.kml,s.mail)
s.speed()
print(z.name,z.kml,z.mail)
z.speed()

print("--------------------------------------------------------")

class note():
    def __init__(self,n,s,c):
        self.name=n
        self.size=s
        self.color=c

    def notes(self):
        print("writing a note")
j=note(2,"long size","red")
a=note(5,"short size","yellow")
j.notes()
print(j.name,j.size,j.color)
a.notes()
print(a.name,a.size,a.color)
       
        
