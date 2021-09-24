#area of a circle
import math

def area(r):
    return math.pi*r**2 

if __name__ == "__main__":
 r = float(input("please enter a value: "))
 print(f"The answer is:{area(r)}")
