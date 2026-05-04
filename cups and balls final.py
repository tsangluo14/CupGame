import turtle
import time
import random

c1=turtle.Turtle()
c1.hideturtle()
c2=turtle.Turtle()
c2.hideturtle()
c3=turtle.Turtle()
c3.hideturtle()
ball=turtle.Turtle()
ball.hideturtle()
text=turtle.Turtle()
text.hideturtle()
bkg=turtle.Turtle()
bkg.hideturtle()
fw=turtle.Turtle()
fw.hideturtle()
sc=turtle.Screen()
sc.tracer(0)
sc.bgcolor('linen')

cup_scale = 1.1
cup_order=[0,1,2] #order of c1, c2, and c3
cup_positions=[0,1,2] #c1 position, c2 position, c3 position

#cup_order[0] gives the cup at first position
#cup_order[1] gives the cup at second position
#cup_order[2] gives the cup at third position

#cup_positions[0] gives the position of c1
#cup_positions[1] gives the position of c2
#cup_positions[2] gives the position of c3

def stampoval(radius1,radius2,myturtle):
    myturtle.right(15)
    for _ in range(2):
        myturtle.circle(radius1, 30)
        myturtle.circle(radius2, 150)
    myturtle.left(15)

def drawcup(myturtle, scale):
    myturtle.penup()
    myturtle.backward(39.0124*scale)
    myturtle.pendown()
    
    #bottom oval
    myturtle.fillcolor('red')
    myturtle.begin_fill()
    myturtle.pencolor('black')
    stampoval(150*scale,5*scale,myturtle)
    myturtle.end_fill()
    
    myturtle.penup()
    myturtle.backward(3.6*scale)
    myturtle.pendown()
    
    #trapezoid
    myturtle.fillcolor('red')
    myturtle.begin_fill()
    myturtle.pencolor('red')
    myturtle.forward(85.2248*scale)
    myturtle.pencolor('black')
    myturtle.left(96)
    myturtle.forward(120.66*scale)
    myturtle.left(84)
    myturtle.forward(60*scale)
    myturtle.left(84)
    myturtle.forward(120.66*scale)
    myturtle.end_fill()
    
    myturtle.penup()
    myturtle.backward(120.66*scale)
    myturtle.right(84)
    myturtle.backward(59*scale)
    
    myturtle.rt(180);myturtle.rt(174)
    myturtle.fillcolor('crimson')
    myturtle.begin_fill()
    myturtle.pencolor('crimson')
    myturtle.fd(24*scale);myturtle.lt(86)
    myturtle.fd(120.9546*scale);myturtle.lt(94)
    myturtle.fd(32.4374*scale);myturtle.lt(90)
    myturtle.fd(120.66*scale);myturtle.lt(90)
    myturtle.end_fill()
    myturtle.fillcolor('firebrick')
    myturtle.begin_fill()
    myturtle.pencolor('firebrick')
    for i in range(2):
        myturtle.fd(7*scale);myturtle.lt(90)
        myturtle.fd(120.66*scale);myturtle.lt(90)
    myturtle.end_fill()
    myturtle.lt(174);
    myturtle.lt(180);
        
    #top oval
    myturtle.pendown()
    myturtle.pencolor('black')
    myturtle.fillcolor('white')
    myturtle.begin_fill()
    stampoval(110*scale,4*scale,myturtle)
    myturtle.end_fill()
    
    myturtle.penup()
    myturtle.forward(59*scale)
    myturtle.left(84)
    myturtle.forward(120.66*scale)
    myturtle.left(96)
    
    myturtle.forward(42.6124*scale)
    myturtle.pendown()
    
def drawcupshadow(myturtle, scale):
    cupy = myturtle.ycor()
    myturtle.penup()
    myturtle.backward(39.0124*scale)
    myturtle.goto(myturtle.xcor(), posy)
    myturtle.pendown()
    myturtle.fillcolor('gray')
    myturtle.begin_fill()
    myturtle.pencolor('gray')
    stampoval(200*scale,5*scale,myturtle)
    myturtle.end_fill()
    
    myturtle.penup()
    myturtle.forward(39.0124*scale) #39

    myturtle.goto(myturtle.xcor(), cupy)
    myturtle.pendown()
    
def drawball(x, y, radius):
    ball.penup()
    ball.goto(x, y)
    ball.pendown()
    ball.fillcolor('yellow')
    ball.begin_fill()
    ball.circle(radius)
    ball.end_fill()
    
def selectMode():
    answer=input('Which difficulty mode would you like to play?\nPress E for easy, M for medium, H for hard, and S for super hard.\n')
    if answer=='e' or answer=='E':
        return 1
    elif answer=='m' or answer=='M':
        return 2
    elif answer=='h' or answer=='H':
        return 3
    elif answer=='s' or answer=='S':
        return 5
    else:
        print('Defaulting to easy.')
        return 1

def startingcups():
    c1.penup()
    c1.goto(-225,posy)
    drawcupshadow(c1,cup_scale)
    drawcup(c1, cup_scale)

    c2.penup()
    c2.goto(0,posy)
    drawcupshadow(c2,cup_scale)
    drawcup(c2, cup_scale)

    c3.penup()
    c3.goto(225,posy)
    drawcupshadow(c3,cup_scale)
    drawcup(c3, cup_scale)

    sc.update()
    
def getCupFromIndex(index):
    match index:
        case 0:
            return c1
        case 1:
            return c2
        case 2:
            return c3
        
def swap(left_index,right_index,steps):
    a = cup_order[left_index]
    b = cup_order[right_index]
    
    left = getCupFromIndex(a)
    right = getCupFromIndex(b)
    
    #cup animation
    delta = (right.xcor() - left.xcor())/steps
    while steps > 0:
        lx = left.xcor()
        rx = right.xcor()
        lx = lx + delta
        rx = rx - delta
        
        left.setx(lx)
        right.setx(rx)
        left.clear()
        drawcupshadow(left,cup_scale)
        drawcup(left, cup_scale)
        right.clear()
        drawcupshadow(right,cup_scale)
        drawcup(right, cup_scale)
        
        steps-=1
        time.sleep(0.001)
        sc.update()
    time.sleep(0.2/speed)
    
    #swap positions
    cup_order[left_index] = b
    cup_order[right_index] = a
    
    cup_positions[b] = left_index
    cup_positions[a] = right_index
    
def cup_animation(aturtle, correct, movement):
    cupy=aturtle.ycor()
    for i in range(100):
        aturtle.clear()
        drawcupshadow(aturtle,cup_scale)
        if correct == True:
            drawball(ballx, bally, 15)
        #draw cup
        if movement == 'up':
            cupy+=0.5
        else:
            cupy-=0.5
        aturtle.sety(cupy)
        drawcup(aturtle, cup_scale)
        time.sleep(0.001)
        sc.update()

def starting_animation():
    time.sleep(1)
    cup_animation(c2, True, 'up')
    time.sleep(0.7)
    cup_animation(c2, True, 'down')
    time.sleep(1)
    ball.clear()
    #3,2,1!
    text.penup()
    text.goto(0,-125)
    text.pencolor('black')
    text.pendown()
    for i in range(3):
        text.write(3-i,font=('timesnewroman',250,'bold'),align='center')
        sc.update()
        time.sleep(0.5)
        text.clear()

def label():
    for i in range(3):
        text.penup()
        text.goto(-222+i*225, posy)
        text.pendown()
        text.pencolor('white')
        text.write(i+1,font=('timesnewroman',50,'bold'),align='center')
    sc.update()
    
def playgame(speed):
    for i in range(20):
        choices = [0,1,2]
        selected1, selected2 = random.sample(choices, 2)
        swap(selected1, selected2, 60/speed)
    
def userinput():
    correct_cup = cup_positions[1]
    label()
    
    while True:
        try:            
            useranswer=int(input('Which cup has the yellow ball: 1, 2, or 3?\n'))
            if useranswer>=1 and useranswer<=3:
                text.clear()
                break
            print('Please enter a number between 1 and 3.')
        except ValueError:
            print('Please enter a number between 1 and 3.')
        
    pick_cup = cup_order[useranswer-1]
    
    if useranswer-1==correct_cup:
        print('Congradulations! You were correct!')
        time.sleep(1)
        cup_animation(c2, True, 'up')
        firework()
    else:
        print('Wrong! The ball was in cup number',str(correct_cup+1)+'.')
        time.sleep(1)
        if pick_cup==0:
            cup_animation(c1, False, 'up')
            time.sleep(0.7)
            cup_animation(c1, False, 'down')
        elif pick_cup==2:
            cup_animation(c3, False, 'up')
            time.sleep(0.7)
            cup_animation(c3, False, 'down')
        time.sleep(1)
        cup_animation(c2, True, 'up')
          
def slanted_tree(x,y,length,direction,i):
    branch_color = ('saddle brown', 'sienna')
    leaf_color = ('lime', 'medium spring green')
    if i > 10:
        bkg.pencolor(leaf_color[i%2])
    else:
        bkg.pencolor(branch_color[i%2])
    
    if i > 12:
        return
    bkg.penup()
    bkg.goto(x,y)
    bkg.pendown()
    bkg.seth(direction)
    bkg.pensize(length/10)
    bkg.forward(length)
    px = bkg.xcor()
    py = bkg.ycor()
    slanted_tree(px, py, length*0.75, direction+45,i+1)
    slanted_tree(px, py, length*0.75, direction-15,i+1)
    
def frame(x,y,w,h):
    bkg.penup()
    bkg.goto(x,y)
    bkg.pendown()
    bkg.seth(90)
    bkg.pencolor('peru')
    bkg.fillcolor('white')
    bkg.pensize(20)
    bkg.begin_fill()
    for i in range(2):
        bkg.forward(h);bkg.left(90)
        bkg.forward(w);bkg.left(90)
    bkg.end_fill()

def drawBkg():
    frame(250,-60,500,470)
    slanted_tree(40,0,100,90,0)
    
    bkg.penup()
    bkg.goto(-800,posy+70)
    bkg.pendown()
    bkg.pencolor('black')
    bkg.fillcolor('tan')
    bkg.pensize(2)
    bkg.seth(-90)
    bkg.begin_fill()
    for i in range(2):
        bkg.forward(1600);bkg.left(90)
        bkg.forward(1600);bkg.left(90)
    bkg.end_fill()
    bkg.penup()
    sc.update()
    
def firework():
    for i in range(15):
        scale=random.uniform(0.1,1.5)
        nlines=random.randint(6,15)
        color=random.choice(['cyan','purple','pink','teal','green','red','orange','gold'])
        fw.pencolor(color)
        fw.pensize(3)
        total=100*scale
        gap=10*scale
        while total-gap>0:
            for i in range(nlines):
                fw.pu();fw.fd(gap);fw.pd()
                fw.fd(total-gap)
                fw.pu();fw.bk(total);fw.pd()
                fw.rt(360/nlines)
            fw.rt(180/nlines)
            for i in range(nlines):
                fw.pu();fw.fd(gap/2);fw.pd()
                fw.fd(total/2-gap/2)
                fw.pu();fw.bk(total/2);fw.pd()
                fw.rt(360/nlines)
            fw.lt(180/nlines)
            sc.update()
            fw.clear()
            total*=1.05
            gap*=1.2
            time.sleep(0.01)
        fw.clear()
        time.sleep(0.05)
    sc.update()

#main
posy = -230

drawBkg()
startingcups()

while True:
    speed = selectMode()
    time.sleep(1)
    
    startingcups()

    ballx = c2.xcor()
    bally = posy

    starting_animation()

    playgame(speed)

    ballx = c2.xcor()
    bally = posy
    
    userinput()
    
    time.sleep(1)
    answer=input('Would you like to play again?\nPress Y for yes and N for no.\n')
    if answer=='y' or answer=='Y':
        print('Here it comes again!')
    elif answer=='n' or answer=='N':
        print('Thank you for playing our game.')
        break
    else:
        print('Defaulting to no. Goodbye!')
        break
    time.sleep(2)
    
    #reset
    c1.clear()
    c2.clear()
    c3.clear()
    ball.clear()
    
    cup_order=[0,1,2] #order of c1, c2, and c3
    cup_positions=[0,1,2] #c1 position, c2 position, c3 position
