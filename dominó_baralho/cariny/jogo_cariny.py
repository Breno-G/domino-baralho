import threading
import random
import time
import queue

ORDEM = ['K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2', 'A']
NAIPES = ['♠', '♥', '♦', '♣']
NAIPE_INPUT = {'E': '♠', 'C': '♥', 'O': '♦', 'P': '♣'}

lock = threading.Lock()
turno = 0
tempo_turno = 30
jogo_ativo = True

def criar_baralho():
    return [f"{valor}{naipe}" for valor in ORDEM for naipe in NAIPES]

def cartas_validas(mao, mesa):
    jogaveis = []
    for carta in mao:
        valor, naipe = carta[:-1], carta[-1]
        if not mesa[naipe]:
            if valor == 'K':
                jogaveis.append(carta)
        else:
            ultima = mesa[naipe][-1][:-1]
            if ORDEM.index(valor) == ORDEM.index(ultima) + 1:
                jogaveis.append(carta)
    return jogaveis

def imprimir_mesa(mesa):
    print("\n=== MESA ===")
    for naipe in NAIPES:
        print(f"{naipe}: {' '.join(mesa[naipe])}")
    print()

def jogador_humano(id_jogador, mao, mesa, jogadores):
    global turno, jogo_ativo
    while jogo_ativo:
        if turno != id_jogador:
            time.sleep(1)
            continue

        lock.acquire()
        imprimir_mesa(mesa)
        print(f"\nSua vez, Jogador {id_jogador+1}")
        print("Sua mão:", " ".join(mao))
        validas = cartas_validas(mao, mesa)

        def jogada_bot_substituto():
            nonlocal mao
            validas_sub = cartas_validas(mao, mesa)
            if validas_sub:
                carta = random.choice(validas_sub)
                print(f"\n[Bot] jogando no lugar do jogador {id_jogador+1}: {carta}")
                mao.remove(carta)
                mesa[carta[-1]].append(carta)
            else:
                print(f"\n[Bot] passou a vez do jogador {id_jogador+1}")

        print(f"\nVocê tem {tempo_turno} segundos para jogar.")
        print("Digite a carta para jogar (ex: ♠ = E   ♥= C   ♦ = O   ♣ = P ) ou 'passar' (só se não tiver carta válida)")

        input_queue = queue.Queue()

        def get_input():
            entrada = input("Sua jogada: ").strip().upper()
            input_queue.put(entrada)

        thread_input = threading.Thread(target=get_input)
        thread_input.daemon = True
        thread_input.start()

        jogou = False
        start = time.time()

        while time.time() - start < tempo_turno:
            if not input_queue.empty():
                entrada = input_queue.get()

                if entrada == 'PASSAR':
                    if validas:
                        print("Você tem cartas válidas para jogar. Não pode passar!")
                        # inicia outro input para tentar novamente
                        thread_input = threading.Thread(target=get_input)
                        thread_input.daemon = True
                        thread_input.start()
                        continue
                    else:
                        print("Você passou a vez.")
                        break

                # converte letra do naipe para símbolo
                if len(entrada) >= 2 and entrada[-1] in NAIPE_INPUT:
                    carta = entrada[:-1] + NAIPE_INPUT[entrada[-1]]
                else:
                    carta = entrada

                if carta in validas:
                    mao.remove(carta)
                    mesa[carta[-1]].append(carta)
                    jogou = True
                    break
                else:
                    print("Carta inválida. Tente novamente.")
                    thread_input = threading.Thread(target=get_input)
                    thread_input.daemon = True
                    thread_input.start()
            else:
                time.sleep(0.1)

        if not jogou:
            print("\nTempo esgotado! Bot substituto jogará para você.")
            jogada_bot_substituto()

        if not mao:
            print(f"\n🎉 Jogador {id_jogador+1} venceu!")
            jogo_ativo = False
            lock.release()
            return

        turno = (turno + 1) % len(jogadores)
        lock.release()
        time.sleep(1)

def bot(id_jogador, mao, mesa, jogadores):
    global turno, jogo_ativo
    while jogo_ativo:
        if turno != id_jogador:
            time.sleep(1)
            continue

        lock.acquire()
        print(f"\nTurno do Bot {id_jogador+1}")
        validas = cartas_validas(mao, mesa)
        time.sleep(2)
        if validas:
            carta = random.choice(validas)
            print(f"Bot {id_jogador+1} jogou {carta}")
            mao.remove(carta)
            mesa[carta[-1]].append(carta)
        else:
            print(f"Bot {id_jogador+1} passou")

        if not mao:
            print(f"\n🤖 Bot {id_jogador+1} venceu!")
            jogo_ativo = False
            lock.release()
            return

        turno = (turno + 1) % len(jogadores)
        lock.release()
        time.sleep(1)

def main():
    global jogo_ativo
    mesa = {naipe: [] for naipe in NAIPES}
    num_reais = int(input("Quantos jogadores reais? (1 a 4): "))
    num_bots = 4 - num_reais

    baralho = criar_baralho()
    random.shuffle(baralho)
    maos = [baralho[i*13:(i+1)*13] for i in range(4)]
    jogadores = []

    for i in range(num_reais):
        t = threading.Thread(target=jogador_humano, args=(i, maos[i], mesa, list(range(4))))
        jogadores.append(t)

    for i in range(num_bots):
        idx = i + num_reais
        t = threading.Thread(target=bot, args=(idx, maos[idx], mesa, list(range(4))))
        jogadores.append(t)

    print("\nJogo iniciado com", num_reais, "jogador(es) e", num_bots, "bot(s).\n")

    for t in jogadores:
        t.start()

    for t in jogadores:
        t.join()

    print("\n🏁 Fim de jogo!")

if __name__ == "__main__":
    main()