import turtle

# Configuração da tela
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("skyblue")

# Criando a tartaruga
pen = turtle.Turtle()
pen.speed(5)
pen.width(3)

# Desenhar paredes da casa
pen.penup()
pen.goto(-100, -100)
pen.pendown()
pen.color("yellow")
pen.begin_fill()
for _ in range(4):
    pen.forward(200)
    pen.left(90)
pen.end_fill()

# Desenhar o telhado
pen.penup()
pen.goto(-100, 100)
pen.pendown()
pen.color("red")
pen.begin_fill()
pen.goto(0, 200)
pen.goto(100, 100)
pen.goto(-100, 100)
pen.end_fill()

# Desenhar a porta
pen.penup()
pen.goto(-30, -100)
pen.pendown()
pen.color("brown")
pen.begin_fill()
pen.forward(60)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(60)
pen.end_fill()

# Desenhar a janela
pen.penup()
pen.goto(30, 0)
pen.pendown()
pen.color("blue")
pen.begin_fill()
for _ in range(4):
    pen.forward(40)
    pen.left(90)
pen.end_fill()

# Desenhar o sol
pen.penup()
pen.goto(200, 200)
pen.pendown()
pen.color("yellow")
pen.begin_fill()
pen.circle(40)
pen.end_fill()

# Esconder a tartaruga
pen.hideturtle()

# Manter a janela aberta
screen.mainloop()