import time
import random

sala = ["paredes comuns", "escadarias longas para baixo", "escadarias longas para cima", "espinhos pontudos"]
elementos = ["Fogo", "Água", "Terra", "Ar", "Gelo", "Luz", "Trevas", "Raio", "Veneno"]
inimigo = [False, True]
recompensa = [False, True]

monstros = ["Goblin", "Esqueleto", "Slime", "Orc", "zumbi", "dragão"]

inventario = []
tamanho_recompensa = ["Pequeno", "Médio", "Grande"]
quantidade = None

arma = ["Espada", "Arco", "Cajado", "Adaga", "Machado"]
pocoes = ["Poção de Vida", "Poção de Mana", "Poção de Força", "Poção de Defesa"]
efeito_pocoes = ["Cura", "Mana", "Força", "Defesa"]
armaduras = ["Armadura de Couro", "Armadura de Ferro", "Armadura de Aço", "Armadura de platina"]


while True:

    class Personagem:
        def __init__(self, nome, classe, elemento, vida, ataque, defesa, mana):
            self.nome = nome
            self.classe = classe
            self.elemento = elemento
            self.vida = vida
            self.ataque = ataque
            self.defesa = defesa
            self.mana = mana

        def gerar_personagem():
            nome = input("Digite o nome do seu personagem: ")
            print("\n lista de classes:")
            print("1. Guerreiro: 100 de vida, 20 de ataque, 15 de defesa, 50 de mana")
            print("2. Mago: 80 de vida, 25 de ataque, 10 de defesa, 100 de mana")
            print("3. Arqueiro: 90 de vida, 18 de ataque, 12 de defesa, 75 de mana \n")

            classe = input("Escolha a classe do seu personagem (1/2/3): ")

            print("\n escolha seu elemento:")
            print("1. Fogo")
            print("2. Água")
            print("3. Terra")
            print("4. Ar")
            print("5. Gelo")
            print("6. Luz")
            print("7. Trevas")
            print("8. Raio")

            elemento = input("Escolha o elemento do seu personagem (1/2/3/4/5/6/7/8): ")

            if classe == "1":
                return Personagem(nome, "Guerreiro", elemento, 100, 20, 15, 50)
            
            elif classe == "2":
                return Personagem(nome, "Mago", elemento, 80, 25, 10, 100)
            
            elif classe == "3":
                return Personagem(nome, "Arqueiro", elemento, 90, 18, 12, 75)
            
            else:
                print("Classe inválida.")
                return None
            

    class Salas:
        def __init__(self, estrutura, elementos, inimigo, recompensa):
            self.estrutura = estrutura
            self.elementos = elementos
            self.inimigo = inimigo
            self.recompensa = recompensa

        def gerar_sala():
            return Salas(random.choice(sala), random.choice(elementos), random.choice(inimigo), random.choice(recompensa))

        def narrar():
            print(f"Você entrou em uma sala com {sala_nova.estrutura}.")
            time.sleep(1)
            if sala_nova.elementos == "Fogo":
                print("A sala está cheia de chamas ardentes")
                time.sleep(1)
            
            elif sala_nova.elementos == "Água":
                print("A sala está cheia de água.")
                time.sleep(1)
            
            elif sala_nova.elementos == "Terra":
                print("A sala está cheia de terra e pedras.")
                time.sleep(1)
            
            elif sala_nova.elementos == "Ar":
                print("A sala está cheia de ventos fortes.")
                time.sleep(1)

            elif sala_nova.elementos == "Gelo":
                print("A sala está preenchida por um frio congelante")
                time.sleep(1)

            elif sala_nova.elementos == "Trevas":
                print("A sala está envolta em trevas.")
                time.sleep(1)
            
            elif sala_nova.elementos == "Raio":
                print("A sala está cheia de eletricidade.")
                time.sleep(1)
            
            elif sala_nova.elementos == "Veneno":
                print("A sala está cheia de gases venenosos.")
                time.sleep(1)
            
            elif sala_nova.elementos == "Luz":
                print("luzes intensas invadem a sala.")
                time.sleep(1)


            if sala_nova.inimigo:
                print("Um inimigo aparece!")
                time.sleep(1)
            else:
                print("Não há inimigos nesta sala.")
                time.sleep(1)


            if sala_nova.recompensa:
                print("Você encontrou uma recompensa!\n")
                time.sleep(1)

            else:
                print("Não há recompensas nesta sala.\n")
                time.sleep(1)
 

    class Monstro:
        def __init__(self, tipo, elemento, ataque, defesa, vida, loot):
            self.tipo = tipo
            self.elemento = elemento
            self.ataque = ataque
            self.defesa = defesa
            self.vida = vida
            self.loot = loot

        def gerar_monstro():
            return Monstro(random.choice(monstros), random.choice(elementos), random.randint(10, 30), random.randint(5, 20), random.randint(50, 150), random.choice(loot))


    class Recompensas:
        def __init__(self, tamanho):
                self.tamanho = tamanho

        def narrar_recompensa():

            tamanho_escolhido = random.choice(tamanho_recompensa)

            print(f"Você encontrou uma recompensa de tamanho {tamanho_escolhido}.\n")
            return tamanho_escolhido
            time.sleep(1)


    class Item:
        def __init__ (self, tipo_arma, tipo_armadura, tipo_pocao, dano, defesa, efeito):
            self.tipo_arma = tipo_arma
            self.tipo_armadura = tipo_armadura
            self.tipo_pocao = tipo_pocao
            self.dano = dano
            self.defesa = defesa
            self.efeito = efeito

        def gerar_arma():
            return Item(random.choice(arma), None, None, random.randint(5, 20), None, None)
        
        def gerar_armadura():
            return Item(None, random.choice(armaduras), None, None, random.randint(5, 20), None)
        
        def gerar_pocao():
            return Item(None, None, random.choice(pocoes), None, None, random.choice(efeito_pocoes))
        
        def narrar_item():
            item_gerado = random.choice([Item.gerar_arma(), Item.gerar_armadura(), Item.gerar_pocao()])

            if item_gerado.tipo_arma:
                print(f"Você encontrou uma arma: {item_gerado.tipo_arma} com {item_gerado.dano} de dano.")

            elif item_gerado.tipo_armadura:
                print(f"Você encontrou uma armadura: {item_gerado.tipo_armadura} com {item_gerado.defesa} de defesa.")
            
            elif item_gerado.tipo_pocao:
                print(f"Você encontrou uma poção: {item_gerado.tipo_pocao} com efeito de {item_gerado.efeito}.")
            
            return item_gerado
            time.sleep(1)
        
    

    print("RPG elementiano\n")
    print("Crie seu personagem\n")
    personagem = Personagem.gerar_personagem()

    print("Em elementian, existem diversos elementos que definem as propriedades magicas dos seres vivos e ambientes")
    print("Você é um aventureiro que vive em um pequeno vilarejo")
    print("Um dia, saindo para explorar, encontra uma masmorra misteriosa, nela você sente diferentes energias elementais")
    escolha_sala = input("Deseja entrar na masmorra? (S/N) ").upper()

    while True:

        if escolha_sala == "S":
            sala_nova = Salas.gerar_sala()
            Salas.narrar()

        elif escolha_sala == "N":
            print("Você decide apenas ficar na sala até morrer de causas naturais.")
            break
        
        else: 
            print("Opção invalida, digite apenas S ou N")
            continue

        if sala_nova.inimigo:
            monstro = Monstro.gerar_monstro()
            print(f"\n Iniciando batalha...")

            while personagem.vida > 0 and monstro.vida > 0:
                print("Opções de combate:")
                print("1 - Atacar")
                print("2 - Ver inventário")
                print("3 - Fugir")
        
                escolha_turno = int(input("Escolha sua ação: "))
        if sala_nova.recompensa:
                input("Pressione ENTER para ver a recompensa...")
                tamanho = Recompensas.narrar_recompensa()

                if tamanho == "Pequeno":
                    quantidade = 1

                elif tamanho == "Médio":
                    quantidade = 2

                elif tamanho == "Grande":
                    quantidade = 3

                input("Pressione ENTER para coletar recompensa...")
                for i in range(quantidade):
                    item = Item.narrar_item()
                    inventario.append(item)

        else:
            pass
        escolha_sala = input("Deseja entrar na proxima sala? (S/N)").upper()