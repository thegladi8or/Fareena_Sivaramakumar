class Breed:
    def __init__(self,name,temperament,coat):
        self.name =name
        self.temperament=temperament
        self.coat=coat
        
        
class Pupper:
    def __init__(self,name,sex,weight,height,color,date_of_birth,breed_id):
        self.name =name
        self.sex=sex
        self.weight=weight
        self.height=height
        self.color=color
        self.date_of_birth=date_of_birth
        self.breed_id = breed_id
        
        
breedOne = Breed ("Joker", "Alert","Shiny")
#pupperOne = Pupper("Socks", 'F', 45, 25, "Grey and WHite", "20180908", 3)
        
     
        
        