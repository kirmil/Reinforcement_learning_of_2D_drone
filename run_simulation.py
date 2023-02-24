from tkinter import *
import numpy as np
import nextPos
import time
import random
from nextPos import *
from simple_Dense_Model import *
def run_simulation():
    
    windowSize = 600
    window = Tk()
    canvas = Canvas(window,width=windowSize,height=windowSize)
    canvas.pack()

    class Simulate_Drone:
        
        def __init__(self,x,y,theta):
            import numpy as np
            self.size_body_x = 40
            self.size_body_y= 20
            self.size_rotor_x = 20
            self.size_rotor_y = 10
            self.rotor_yoffset = 10
            self.cordinates = []
            self.exact_cordinates = []
            self.rectangles = []
            self.L = 30
            self.x = x
            self.y = y
            self.theta = theta
            self.drone_cordinates()
            self.rotate()
            self.draw_initial()
        
        def drone_cordinates(self):
            self.vertices_body = [
            [self.x - self.size_body_x/2, self.y - self.size_body_y/2],
            [self.x + self.size_body_x/2, self.y - self.size_body_y/2],
            [self.x + self.size_body_x/2, self.y + self.size_body_y/2],
            [self.x - self.size_body_x/2, self.y + self.size_body_y/2],
            ]
            self.vertices_rotor_left = [
            [self.x-self.L-self.size_rotor_x/2,self.y-self.rotor_yoffset-self.size_rotor_y/2],
            [self.x-self.L+self.size_rotor_x/2,self.y-self.rotor_yoffset-self.size_rotor_y/2],
            [self.x-self.L+self.size_rotor_x/2,self.y-self.rotor_yoffset+self.size_rotor_y/2],
            [self.x-self.L-self.size_rotor_x/2,self.y-self.rotor_yoffset+self.size_rotor_y/2],
            ]
            self.vertices_rotor_right = [
            [self.x+self.L-self.size_rotor_x/2,self.y-self.rotor_yoffset-self.size_rotor_y/2],
            [self.x+self.L+self.size_rotor_x/2,self.y-self.rotor_yoffset-self.size_rotor_y/2],
            [self.x+self.L+self.size_rotor_x/2,self.y-self.rotor_yoffset+self.size_rotor_y/2],
            [self.x+self.L-self.size_rotor_x/2,self.y-self.rotor_yoffset+self.size_rotor_y/2],
            ]
            self.cordinates = [self.vertices_body,self.vertices_rotor_left,self.vertices_rotor_right]

        def rotate(self):
            import numpy as np
            cos_val = np.cos(self.theta)
            sin_val = np.sin(self.theta)
            cx, cy = self.x,self.y
            new_points = []
            for i in self.cordinates:
                for x_old, y_old in i:
                    x_old -= cx
                    y_old -= cy
                    x_new = x_old * cos_val - y_old * sin_val
                    y_new = x_old * sin_val + y_old * cos_val
                    new_points.append([x_new + cx, y_new + cy])
                self.exact_cordinates.append(new_points)
                new_points = []
            
        def draw_initial(self):
            for points in self.exact_cordinates:
                self.rectangles.append(canvas.create_polygon(points, fill="red"))

        def movement(self):
            for points in self.exact_cordinates:
                canvas.coords(self, -1*points)  

    ##INIT VALUES
    x = windowSize/2
    y = 0
    Vx = 0
    Vy = 0
    theta = 0
    alpha = 0
    tao = 0.001
    mass = 10
    testF = mass*9.81*600/(y+1)
    LR = 0.2
    FR = testF/2
    FL = testF/2

    test = dense_model()
    test.add_input_layer(2)
    test.add_dense_layer(128)
    test.add_dense_layer(128)
    test.add_Output(1)
    test.compile_network()

    for i in range(0,100000):
        
        a = np.array([[y],[Vy]])
        Force = test.predict(a)
        x,y,Vx,Vy,theta= uppdate_varaibles(x,y,Vx,Vy,theta,alpha,tao,Force[0][0]*100,Force[0][0]*100,mass,LR,windowSize)
            
        drone = Simulate_Drone(x,windowSize-y,theta)
        str1 = "Current y = "+str(int(y))
        str2 = "Current Vy = "+str(int(Vy))
        str3 = "Current time = "+str(int(tao*i))
        text1 = canvas.create_text(100,100,text=str1)
        text2 = canvas.create_text(100,140,text=str2)
        text3 = canvas.create_text(100,180,text=str3)
        
        window.update()
        #time.sleep(0.00001)
        for i in range(0,len(drone.rectangles)):
            canvas.delete(drone.rectangles[i])
            canvas.delete(text1)
            canvas.delete(text2)
            canvas.delete(text3)

    window.mainloop()

    def run_model(model,x,y,Vx,Vy,theta,alpha,tao,FL,FR,mass,LR,windowSize):
        for i in range(0,1000):
            a = np.array([[y],[Vy]])
            Force = model.predict(a)
            x,y,Vx,Vy,theta= uppdate_varaibles(x,y,Vx,Vy,theta,alpha,tao,Force[0][0],Force[0][0],mass,LR,windowSize)
            
    run_model(test,x,y,Vx,Vy,theta,alpha,tao,FL,FR,mass,LR,windowSize)