import threading
import time
from setup_game import Baralho, Mesa
from jogador import Jogador
from bot import Bot
from visual import imprime_estado
 
class Jogo:
    def __init__(self):
        self.baralho = Baralho()
        self.mesa = Mesa()
        self.jogadores = [
            Jogador("Você"),
            Bot("Bot 1"),
            Bot("Bot 2"),
            Bot("Bot 3")
        ]

        self.turno = 0
        self.lock = threading.Semaphore(1)
        self.turno_cond = threading.Condition()

    def distribuir_cartas(self):
        self.baralho.embaralhar()
        maos = self.baralho.distribuir(jogadores=4)
        for i, jogador in enumerate(self.jogadores):
            jogador.receber_cartas(maos[i])

    def executar_turno(self, id_jogador):
        while True:
            with self.turno_cond:
                while self.turno != id_jogador:
                    self.turno_cond.wait()

                self.lock.acquire()
                imprime_estado(self.mesa, self.jogadores[0], self.jogadores[1:])

                self.jogadores[id_jogador].jogar(self.mesa)
                self.lock.release()

                self.turno = (self.turno + 1) % 4
                self.turno_cond.notify_all()
                time.sleep(0.1)

    def iniciar(self):
        self.distribuir_cartas()

        threads = []
        for id_jogador in range(4):
            t = threading.Thread(target=self.executar_turno, args=(id_jogador,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

if __name__ == "__main__":
    jogo = Jogo()
    jogo.iniciar()
