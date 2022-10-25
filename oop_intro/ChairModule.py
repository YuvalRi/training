import time
class Gun:

    # The constructor function
    def __init__(self, ammunition: int, model: str):
        self.ammunition = ammunition
        self.model = model
        
    def reloadMagazine(self):
        self.ammunition = 6

    def getAmmu(self) -> int:
        if self.ammunition < 0 or self.ammunition > 6:
            print ("Error! Please enter a number between [0,6]")
        else:
            return self.ammunition

    def getModel(self) -> str:
        return self.model

    def isEmpty(self):
        if self.ammunition == 0:
            return True
    
    def shoot
