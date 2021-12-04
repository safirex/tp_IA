class Character:
    def __init__(self,arr):
        (self.name,self.firstName,self.age,self.profession,self.morale_value) = arr
        self.morale_value = float(self.morale_value)
        
    def setArmy(self,army):
        self.army=army

    def __repr__(self) -> str:
        val = str(self.firstName)+" "+str(self.name)+ " "+str(self.age)
        val += " "+str(self.profession)+" "+str(self.morale_value)
        val += "\t Army: "+ str(self.army)
        return val