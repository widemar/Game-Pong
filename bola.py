from turtle import Turtle
import random

lista_de_cores = ["red", "blue", "green", "yellow"]


class Bola(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.color("white")
		self.penup()
		self.move_x = 10
		self.move_y = 10
		self.velocidade_de_movimento = 0.1

	def mover_bola(self):
		novo_x = self.xcor() + self.move_x
		novo_y = self.ycor() + self.move_y
		self.goto(novo_x, novo_y)

	def detectar_colisao_y(self):
		self.move_y *= -1

	def detectar_colisao_x(self):
		self.color(random.choice(lista_de_cores))
		self.move_x *= -1
		if self.velocidade_de_movimento > 0.05:
			self.velocidade_de_movimento -= 0.01

	def resetar_bola(self):
		self.home()
		self.detectar_colisao_x()
		self.velocidade_de_movimento = 0.1
