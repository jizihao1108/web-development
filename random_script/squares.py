import turtle

def draw_sqaures():
    
    win = turtle.Screen()
    win.bgcolor('white')
    
    tt = turtle.Turtle()
    tt.color('green')
    tt.shape('turtle')
    tt.speed(3)
    for i in range(36):
        
        tt.right(10)
        for i in range(4):
        
            tt.forward(100)
            print(tt.position())
            tt.right(90)
            print(tt.position())
    
    #window.exitonlick()
    
    win.exitonclick()

draw_sqaures()