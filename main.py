from turtle import Screen
from raquete import Raquete
from bola import Bola
from placar import Placar
import time

tela = Screen()
tela.title("Pong")
tela.setup(width=800, height=600)
tela.bgcolor("black")
tela.tracer(0)

raquete_usuario = Raquete((-350, 0))
raquete_computador = Raquete((350, 0))
bola = Bola()
placar = Placar()

tela.listen()
tela.onkeypress(raquete_usuario.mover_raquete_para_cima, "w")
tela.onkeypress(raquete_usuario.mover_raquete_para_baixo, "s")
tela.onkeypress(raquete_computador.mover_raquete_para_cima, "Up")
tela.onkeypress(raquete_computador.mover_raquete_para_baixo, "Down")

jogo_em_andamento = True

while jogo_em_andamento:
	time.sleep(bola.velocidade_de_movimento)
	tela.update()
	bola.mover_bola()

	# Verifica se a bola atingiu o topo ou rodape
	if bola.ycor() > 280 or bola.ycor() < -280:
		bola.detectar_colisao_y()

	# Detecta a colisão da bola com as raquetes
	if bola.distance(raquete_usuario) < 50 and bola.xcor() < -320 or \
			bola.distance(raquete_computador) < 30 and bola.xcor() < 380:
		bola.detectar_colisao_x()

	# Verifica se a bola ultrassou o lado direito
	if bola.xcor() > 420:
		placar.aumentar_placar_esquerdo()
		placar.atualizar_placar()
		bola.resetar_bola()

	# Verifica se a bola ultrassou o lado esquerdo
	if bola.xcor() < -420:
		placar.aumentar_placar_direito()
		placar.atualizar_placar()
		bola.resetar_bola()

tela.exitonclick()
