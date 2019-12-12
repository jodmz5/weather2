import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.setup(240,320)
s.bgcolor('black')
s.colormode(255)
def turtlefun(tempx, feelsx, pricex):
    #Change color based on temperature
    t.up()
    t.setx(-85)
    t.sety(120)
    t.down()
    if tempx<32:
        t.color('white')
    elif tempx>32&tempx<=40:
        t.color('cyan')
    elif tempx>40&tempx<=60:
        t.color('yellow')
    elif tempx>60&tempx<=75:
        t.color('orange')
    else:
        t.color('red')
        
    t.write('Temperature:', font=("Times", 18, "normal"))
    t.up()
    t.forward(130)
    t.down()
    t.write(tempx, font=("Times", 18, "normal"))
    t.up()
    t.setx(-85)
    t.sety(120)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.down()
    if feelsx<32:
        t.color('white')
    elif feelsx>32&feelsx<=40:
        t.color('cyan')
    elif feelsx>40&feelsx<=60:
        t.color('yellow')
    elif feelsx>60&feelsx<=75:
        t.color('orange')
    else:
        t.color('red')
        
    t.write('Feels Like:', font=("Times", 18, "normal"))
    t.up()
    t.forward(130)
    t.down()
    t.write(feelsx, font=("Times", 18, "normal"))
    t.up()
    t.setx(-85)
    t.sety(120)
    t.right(90)
    t.forward(80)
    t.left(90)
    t.down()
    t.color(188,19,254)
    t.write('Price of U:', font=("Times", 18, "normal"))
    t.up()
    t.forward(120)
    t.down()
    t.write('$', font=("Times", 18, "normal"))
    t.up()
    t.forward(12)
    t.down()
    t.write(pricex, font=("Times", 18, "normal"))
    
