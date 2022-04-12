from turtle import Turtle


class Raquete(Turtle):
	def __init__(self, posicoes):
		super().__init__()
		self.shape("square")
		self.color("white")
		self.shapesize(stretch_len=1, stretch_wid=5)
		self.penup()
		self.goto(posicoes)

	def mover_raquete_para_cima(self):
		novo_y = self.ycor() + 20
		x = self.xcor()
		self.goto(x, novo_y)

	def mover_raquete_para_baixo(self):
		novo_y = self.ycor() - 20
		x = self.xcor()
		self.goto(x, novo_y)
