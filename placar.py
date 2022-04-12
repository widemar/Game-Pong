from turtle import Turtle


class Placar(Turtle):
	def __init__(self):
		super().__init__()
		self.hideturtle()
		self.color("white")
		self.penup()
		self.pontuacao_esquerda = 0
		self.pontuacao_direita = 0
		self.atualizar_placar()

	def atualizar_placar(self):
		self.goto(-100, 240)
		self.write(f"{self.pontuacao_esquerda}", align="center", font=("Monospace", 40, "bold"))
		self.goto(100, 240)
		self.write(f"{self.pontuacao_direita}", align="center", font=("Monospace", 40, "bold"))

	def aumentar_placar_esquerdo(self):
		self.pontuacao_esquerda += 1
		self.clear()

	def aumentar_placar_direito(self):
		self.pontuacao_direita += 1
		self.clear()
