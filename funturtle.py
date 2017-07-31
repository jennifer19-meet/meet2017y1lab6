import turtle
turtle.shape('turtle')
square = turtle.clone ()
square.shape ('turtle')
square.goto(0,100)
square.goto(100,100)
square.goto(100, 0)
square.goto(0, 0)

triangle = turtle.clone()
triangle.shape("triangle")
triangle.penup ()
triangle.goto(-200,0)
triangle.pendown()
triangle.goto(-100, 0)
triangle.goto(-100,+100)
triangle.goto(-200, +100-100)
turtle.mainloop()

