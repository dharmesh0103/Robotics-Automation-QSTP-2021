import numpy as np
import matplotlib.pyplot as plt

class Unicycle:
    def __init__(self, x: float, y: float, theta: float, dt: float):
        self.x = x
        self.y = y
        self.theta = theta
        self.dt = dt
        # Store the points of the trajectory to plot
        self.x_points = [self.x]
        self.y_points = [self.y]

    def step(self, v: float, w: float, n: int  ):
        v=5
        w=4
        n=0      
        self.x = 0
        self.y = 0
        self.theta = 0.77
        self.x_points=[0]
        self.y_points=[0]  
        while n<=50:           
            x= self.x +v *np.cos(self.theta)*self.dt*n
            y =self.y +v *np.sin(self.theta)*self.dt*n
            theta = self.theta+w*self.dt*n
            self.x_points.append(x)
            self.y_points.append(y)
            n=n+1
            self.theta = theta
            self.x = x
            self.y = y
        
        plt.title(f"Unicycle Model: {v}, {w}")
        plt.xlabel("X-Coordinates")
        plt.ylabel("Y-Coordinates")
        plt.plot(self.x_points, self.y_points, color="red", alpha=0.75)
        plt.grid()
        plt.show()
        return x ,y ,theta
final=Unicycle(0,0,0.77,0.05)
print(final.step(5,4,50))        
if __name__ == "__main__":
    print("Unicycle Model Assignment")
    
    
