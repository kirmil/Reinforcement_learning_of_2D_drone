def uppdate_varaibles(x,y,Vx,Vy,theta,alpha,tao,FR,FL,mass,LR,windowsize):
    import numpy
    dragCoeff = 0
    g = 9.81
    I = 3/2*mass

    nextX = x+Vx*tao
    if y <0:
        nextY = 0
        nextVy = 0
    else:
        nextY = y+Vy*tao
        nextVy = Vy+((FL+FR)*numpy.cos(theta)-Vy*dragCoeff-mass*g)*tao/mass

    nextTheta = theta + (-FL+FR)*LR*tao/I
    nextVx = Vx+((-FL-FR)*numpy.sin(theta)-Vx*dragCoeff)*tao/mass

    return nextX,nextY,nextVx,nextVy,nextTheta




