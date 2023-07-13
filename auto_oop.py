class Region:

    def __init__(self,name):
        self.name=name

    def __repr__(self):
        return self.name
class Marka:
    def __init__(self,title):
        self.title=title
        self.chevrolet={}
        self.kia=[]

    def get_chevrolet(self):
        return self.chevrolet

    def __repr__(self):
        return self.title
class Model:
    def __init__(self,marka:Marka):

        self.marka=marka


    def add_model(self,modelcar):
        self.marka.chevrolet.update(modelcar)






    def __repr__(self):


        return self.title

class Car:
    def __init__(self,name_1):
        self.name=name_1
        self.position=[]
        self.b = marka1

    def get_marka(self,firstletter,car):
        for i,(key,value) in enumerate(self.b.chevrolet)
            if key == firstletter:
            if firstletter in self.b.chevrolet:





    def add_position(self,posion):
        return self.position.extend(posion)




region1=Region("Andijan")
marka1=Marka("Chevrolet")
model=Model(marka1)
model.add_model({"A":["Astra" ,"Aveo"]})
model.add_model({"B":["Blazer","Bolt"]})
model.add_model({"C":["Camaro","Caprice","Captiva","Cobalt","Colorado","Corsica","Cruze"]})
model.add_model({"D":["Damas"]})
model.add_model({"E":["Epica","Equinox","Evanda"]})
model.add_model({"G":["G-series","Gentra"]})
model.add_model({"L":["Labo","Lacetti","Lanos","Lumina"]})
model.add_model({"M":["Malibu","Malibu 2","Matiz","Matiz Best","Menlo","Monza"]})
model.add_model({"N":["Nexia 2","Nexia 3 ","Niva","Nubira"]})
model.add_model({"O":["Onix","Optra","Orlando"]})
model.add_model({"R":["Rezzo"]})
model.add_model({"S":["Spark","Suburban"]})
model.add_model({"T":["Tacuma","Tahoe","Tracker","Tracker 2","Tracker Premier","TrailBlazer","Traverse"]})
model.add_model({"V":["Volt"]})
# print(model.marka.chevrolet)
car1=Car(marka1.chevrolet["G"][1])
car1.add_position(["3 позиция","2 позиция ","1 Позиция газ бензин"])
car2=Car(marka1.chevrolet["M"][1])


print(car1.__dict__)
