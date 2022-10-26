import time

def show(self):
    print("Shooting in...")
    for i in range(3,0,-1):
        print(i)
        time.sleep(1)
    gunA = """
            _______
            \/\/_____\\\\"""
    gunB = """
                |/
                ||                 
            """
    bullet = "->"
    for i in range(50):
        print(gunA + bullet + gunB)
        bullet = " " + bullet
        time.sleep(0.01)
