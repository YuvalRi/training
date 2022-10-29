import time
from ShowFunc import show

# A


class Gun:

    # The constructor function
    def __init__(self, ammunition: int, model: str):
        if ammunition < 0 or ammunition > 6:
            raise ValueError("Error! Please enter a number between [0,6]")
        else:
            self.ammunition = ammunition
        if model != "Sniper" and model != "Assault" and model != "Automatic":
            raise ValueError("Error! Please enter a valid type of gun")
        else:
            self.model = model

    def reload_magazine(self):
        '''
        Reload ammunition to its max capacity
        '''
        self.ammunition = 6
        return self.ammunition

    def get_ammu(self) -> int:
        '''
        Returns the current ammunition count
        '''
        return self.ammunition

    def get_model(self) -> str:
        '''
        Returns the gun model
        '''
        return self.model

    def is_empty(self):
        '''
        Returns True if ammunition is empty and false otherwise
        '''
        if self.ammunition == 0:
            return True
        return False

    def shoot(self):
        '''
        A function which cause the gun to shoot
        '''
        if self.ammunition != 0:
            show(self)
            self.ammunition -= 1
        else:
            print("Error! Please enter a number between [1,6]")

# B


if __name__ == "__main__":
    g = Gun(ammunition=0, model="Sniper")  # Creating g class
    g.shoot()  # Trying shooting it
    print(g.is_empty())  # Checking it is has any ammunition left
    g.reload_magazine()  # Reloading it
    print(g.is_empty())  # Checking if it has ammunition again
    g.shoot()  # Shooting it
    # Creating a gun with invalid inputs
    g1 = Gun(ammunition=8, model="Tesla")
    g1.shoot()
