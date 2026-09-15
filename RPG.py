import time
import random
import os

sala = ["paredes comuns", "escadarias longas para baixo", "escadarias longas para cima", "espinhos pontudos"]
elementos = ["Fogo", "Água", "Terra", "Ar", "Gelo", "Luz", "Trevas", "Raio", "Natureza", "Veneno"]
inimigo = [False, True]
recompensa = [False, True]
monstros = ["Goblin", "Esqueleto", "Slime", "Orc", "zumbi", "dragão"]

inventario = []
equipado = []

tamanho_recompensa = ["Pequeno", "Médio", "Grande"]
quantidade = None

arma = ["Espada", "Arco", "Cajado", "Adaga", "Machado"]
pocoes = ["Poção de vida", "Poção de mana", "Poção de força", "Poção de defesa"]
armaduras = ["Armadura de Couro", "Armadura de Ferro", "Armadura de Aço", "Armadura de platina"]

def texto_print(mensagem):
    for letra in mensagem:
        print(letra, end="", flush=True)
        time.sleep(0.05)

def texto_input(mensagem):
    for letra in mensagem:
        print(letra, end="", flush=True)
        time.sleep(0.05)

    return input()

def quebrar_texto():
    os.system('cls' if os.name == 'nt' else 'clear')

class Personagem:
       
    def __init__(self, nome, classe, elemento, vida, vida_max, ataque, defesa, mana, mana_max, exp, level, min_exp, pontos, buff_forca, buff_defesa, turnos_buff_forca, turnos_buff_defesa):
        self.nome = nome
        self.classe = classe
        self.elemento = elemento
        self.vida = vida
        self.vida_max = vida_max
        self.ataque = ataque
        self.defesa = defesa
        self.mana = mana
        self.mana_max = mana_max

        self.exp = exp
        self.level = level
        self.min_exp = min_exp
        self.pontos = pontos

        self.buff_forca = buff_forca
        self.buff_defesa = buff_defesa
        self.turnos_buff_forca = turnos_buff_forca
        self.turnos_buff_defesa = turnos_buff_defesa


    def gerar_personagem():
        
        nome = texto_input("Digite o nome do seu personagem: ")
        quebrar_texto()
        
        quebrar_texto()
        texto_print(" lista de classes: \n \n")
        time.sleep(0.5)
        texto_print("1. Guerreiro: 100 de vida, 20 de ataque, 15 de defesa, 50 de mana\n")
        time.sleep(0.5)
        texto_print("2. Mago: 80 de vida, 25 de ataque, 10 de defesa, 100 de mana\n")
        time.sleep(0.5)
        texto_print("3. Arqueiro: 90 de vida, 18 de ataque, 12 de defesa, 75 de mana \n \n")
        time.sleep(0.5)

        while True:
            try:
                classe = int(texto_input("Escolha a classe do seu personagem (1/2/3): "))    
                break
            
            except ValueError:
                texto_print("Valor invalido. Digite apenas números\n")
                continue
            
        quebrar_texto()
        texto_print("\n escolha seu elemento:\n")
        time.sleep(0.5)
        texto_print("1. Fogo\n")
        time.sleep(0.5)
        texto_print("2. Água\n")
        time.sleep(0.5)
        texto_print("3. Terra\n")
        time.sleep(0.5)
        texto_print("4. Ar\n")
        time.sleep(0.5)
        texto_print("5. Gelo\n")
        time.sleep(0.5)
        texto_print("6. Luz\n")
        time.sleep(0.5)
        texto_print("7. Trevas\n")
        time.sleep(0.5)
        texto_print("8. Raio\n")
        time.sleep(0.5)
        texto_print("9. Natureza\n")
        time.sleep(0.5)
        texto_print("10. Veneno\n \n")

        while True:
            try:
                
                elemento = int(texto_input("Escolha o elemento do seu personagem (1/2/3/4/5/6/7/8/9/10): "))

                if elemento == 1:
                    elemento = "Fogo"  

                elif elemento == 2:
                    elemento = "Água"

                elif elemento == 3:
                    elemento = "Terra"

                elif elemento == 4:
                    elemento = "Ar"

                elif elemento == 5:  
                    elemento = "Gelo"

                elif elemento == 6:  
                    elemento = "Luz"

                elif elemento == 7:
                    elemento = "Trevas"

                elif elemento == 8:
                    elemento = "Raio"

                elif elemento == 9:
                    elemento = "Natureza"

                elif elemento == 10:
                    elemento = "Veneno"

                else:
                    texto_print("Escolha inválida. Por favor, escolha um número entre 1 e 10.")
                    continue
                
                break
            
            except ValueError:
                texto_print("Valor invalido. Digite apenas números")
                continue

        if classe == 1:
            return Personagem(nome, "Guerreiro", elemento, 100, 100, 20, 15, 0, 0, 0, 1, 50, 0, 0, 0, 0, 0)
        
        elif classe == 2:
            return Personagem(nome, "Mago", elemento, 80, 80, 25, 10, 100, 100, 0, 1, 50, 0, 0, 0, 0, 0, 0)
        
        elif classe == 3:
            return Personagem(nome, "Arqueiro", elemento, 90, 90, 20, 12, 0, 0, 0, 1, 50, 0, 0, 0, 0, 0)
        
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
        quebrar_texto()
        texto_print(f"\nVocê entrou em uma sala com {sala_nova.estrutura}.")
        time.sleep(1)

        if sala_nova.elementos == "Fogo":
            texto_print("A sala está cheia de chamas ardentes. \n")
            time.sleep(1)

        elif sala_nova.elementos == "Água":
            texto_print("A sala está cheia de água.\n") 
            time.sleep(1)

        elif sala_nova.elementos == "Terra":
            texto_print("A sala está cheia de terra e pedras.")
            time.sleep(1)

        elif sala_nova.elementos == "Ar":
            texto_print("A sala está cheia de ventos fortes.")
            time.sleep(1)

        elif sala_nova.elementos == "Gelo":
            texto_print("A sala está preenchida por um frio congelante")
            time.sleep(1)

        elif sala_nova.elementos == "Trevas":
            texto_print("A sala está envolta em trevas.")
            time.sleep(1)

        elif sala_nova.elementos == "Raio":
            texto_print("A sala está cheia de eletricidade.")
            time.sleep(1)

        elif sala_nova.elementos == "Veneno":
            texto_print("A sala está cheia de gases venenosos.")
            time.sleep(1) 

        elif sala_nova.elementos == "Luz":
            texto_print("luzes intensas invadem a sala.")
            time.sleep(1)

        elif sala_nova.elementos == "Natureza": 
            texto_print("A sala está cheia de plantas e flores.")
            time.sleep(1)


        if sala_nova.inimigo:
            texto_print("Um inimigo aparece!")
            time.sleep(1)

        else:
            texto_print("Não há inimigos nesta sala.")
            time.sleep(1)

        if sala_nova.recompensa:
            texto_print("há recompensas nesta sala.\n")
            time.sleep(1)

        else:
            texto_print("Não há recompensas nesta sala.\n")
            time.sleep(1)


class Monstro:

    def __init__(self, tipo, elemento, ataque, defesa, vida, exp):
        self.tipo = tipo
        self.elemento = elemento
        self.ataque = ataque
        self.defesa = defesa
        self.vida = vida
        self.exp = exp

    def gerar_monstro():
        return Monstro(random.choice(monstros), random.choice(elementos), random.randint(10, 30), random.randint(5, 20), random.randint(50, 150), random.randint(10, 50))


class Recompensas:

    def __init__(self, tamanho):
           self.tamanho = tamanho

    def narrar_recompensa(tamanho):
        tamanho_escolhido = random.choice(tamanho)
        quebrar_texto()
        texto_print(f"Você encontrou uma recompensa de tamanho {tamanho_escolhido}.\n")
        time.sleep(1)

        return tamanho_escolhido


class Item: 
    
    def __init__ (self, tipo_arma, tipo_armadura, tipo_pocao, dano, defesa, efeito):
        self.tipo_arma = tipo_arma
        self.tipo_armadura = tipo_armadura
        self.tipo_pocao = tipo_pocao
        self.dano = dano
        self.defesa = defesa
        self.efeito = efeito

    def __str__(self):
        if self.tipo_arma:
            return f"{self.tipo_arma} (Dano: {self.dano})"
        
        elif self.tipo_armadura:
            return f"{self.tipo_armadura} (Defesa: {self.defesa})"
    
        elif self.tipo_pocao:
            return f"{self.tipo_pocao} (Efeito: {self.efeito})"

    def gerar_arma():
        return Item(random.choice(arma), None, None, random.randint(5, 20), None, None)

    def gerar_armadura():
        return Item(None, random.choice(armaduras), None, None, random.randint(5, 20), None)

    def gerar_pocao():
        return Item(None, None, random.choice(pocoes), None, None, random.randint(5, 20))

    def narrar_item():
        item_gerado = random.choice([Item.gerar_arma(), Item.gerar_armadura(), Item.gerar_pocao()])

        quebrar_texto()
        if item_gerado.tipo_arma:
            texto_print(f"Você encontrou uma arma: {item_gerado.tipo_arma} com {item_gerado.dano} de dano.")

        elif item_gerado.tipo_armadura:
            texto_print(f"Você encontrou uma armadura: {item_gerado.tipo_armadura} com {item_gerado.defesa} de defesa.")

        elif item_gerado.tipo_pocao:
            texto_print(f"Você encontrou uma poção: {item_gerado.tipo_pocao} com efeito de {item_gerado.efeito}.")

        time.sleep(1)
        return item_gerado


class Magias:
   
    def __init__(self, nome, elemento, dano, custo_mana, descricao):
        self.nome = nome
        self.elemento = elemento
        self.dano = dano
        self.custo_mana = custo_mana
        self.descricao = descricao


magias = {
    "magias_fogo": [
        Magias("Bola de Fogo", "Fogo", 20, 10, "Lança uma bola de fogo que causa dano ao inimigo."),
        Magias("Explosão Flamejante", "Fogo", 40, 30, "Cria uma explosão de chamas ao atingir o inimigo."),
        Magias("Rajada em brasa", "Fogo", 30, 20, "Dispara uma rajada de chamas que causa dano ao inimigo."),
    ],
    "magias_agua": [
        Magias("Esguixo de Água", "Água", 20, 10, "Dispara um jato de água que causa dano ao inimigo."),
        Magias("Tsunami", "Água", 40, 30, "Cria uma grande onda que causa dano ao inimigo."),
        Magias("Chuva", "Água", 0, 30, "Cria uma chuva cortante que causa dano ao inimigo."),
    ],
    "magias_terra": [
        Magias("Cascalho Cortante", "Terra", 20, 10, "Dispara pequenas pedras afiadas que causam dano ao inimigo."),
        Magias("Terremoto", "Terra", 40, 30, "Causa um terremoto que causa grande dano ao inimigo na área."),
        Magias("Estalaquitites", "Terra", 30, 20, "Dispara estalactites do chão que causam dano ao inimigo."),
    ],
    "magias_ar": [
        Magias("Rajada de Vento", "Ar", 20, 10, "Dispara uma rajada de vento que causa dano ao inimigo."),
        Magias("Tornado", "Ar", 40, 30, "Cria um tornado que causa grande dano ao inimigo na área."),
        Magias("Furacão", "Ar", 30, 20, "Cria um furacão que causa dano ao inimigo."),
    ],
    "magia_gelo": [
        Magias("Lança de Gelo", "Gelo", 20, 10, "Dispara uma lança de gelo que causa dano ao inimigo."),
        Magias("Tempestade de Neve", "Gelo", 40, 30, "Cria uma tempestade de neve que causa grande dano ao inimigo na área."),
        Magias("Congelamento", "Gelo", 30, 20, "Congela o inimigo, causando danopor frio."),
    ],
    "magias_luz": [
        Magias("Raio de Luz", "Luz", 20, 10, "Dispara um raio de luz que causa dano ao inimigo."),
        Magias("Explosão de Luz", "Luz", 40, 30, "Cria uma explosão de luz que causa grande dano ao inimigo na área."),
        Magias("Prisma brilhante", "Luz", 30, 20, "Cria um prisma de luz que causa dano ao inimigo."),
    ],
    "magias_trevas": [
        Magias("Sombra Cortante", "Trevas", 20, 10, "Dispara uma lâmina de sombra que causa dano ao inimigo."),
        Magias("Explosão Sombria", "Trevas", 40, 30, "Cria uma explosão de trevas que causa grande dano ao inimigo na área."),
        Magias("Manto das Trevas", "Trevas", 30, 20, "Cobre o inimigo com trevas, causando dano."),
    ],
    " magias_raio": [
        Magias("Raio Elétrico", "Raio", 20, 10, "Dispara um raio elétrico que causa dano ao inimigo."),
        Magias("Tempestade Elétrica", "Raio", 40, 30, "Cria uma tempestade elétrica que causa grande dano ao inimigo na área."),
        Magias("Descarrego", "Raio", 30, 20, "Descarrega eletricidade no inimigo, causando dano."),
    ],
    "magias_natureza": [
        Magias("Espinhos Crescentes", "Natureza", 20, 10, "Faz crescer espinhos que causam dano ao inimigo."),
        Magias("Raízes Enredantes", "Natureza", 40, 30, "Faz crescer raízes que prendem e causam dano ao inimigo."),
        Magias("Belas flores", "Natureza", 30, 20, "Cria flores emissoras que de um = pólen que causa dano ao inimigo."),
    ],
    "magias_veneno": [
        Magias("Dardo Venenoso", "Veneno", 20, 10, "Dispara um dardo envenenado que causa dano ao inimigo."),
        Magias("Nuvem Tóxica", "Veneno", 40, 30, "Cria uma nuvem de veneno que causa grande dano ao inimigo na área."),
        Magias("Substância Corrosiva", "Veneno", 30, 20, "Aplica uma substância corrosiva no inimigo, causando dano."),
    ]
}


def aplicar_exp():
    personagem.exp += monstro.exp
   
    while personagem.exp >= personagem.min_exp:
        personagem.level += 1
        personagem.exp -= personagem.min_exp
        personagem.pontos += 5
        personagem.min_exp += 50
 

def aplicar_pontos(pnts):
   
    while pnts > 0:
        quebrar_texto()
        texto_print(f"\nVocê possui {pnts} pontos para distribuir entre seus atributos:")
        texto_print("1 - Vida")
        texto_print("2 - Ataque")
        texto_print("3 - Defesa")
        texto_print("4 - Mana")

        try:
            melhoria = int(texto_input("Qual dos atributos deseja melhorar? "))

        except ValueError:
            texto_print("Opção inválida. Por favor, escolha um número entre 1 e 4.")
            return
       
        if melhoria == 1:
            quebrar_texto()
            texto_print("Você recebeu mais 10 de vida maxima")
            personagem.vida_max += 10
            pnts -= 1

        elif melhoria == 2:
            quebrar_texto()
            texto_print("Você recebeu mais 5 de ataque")
            personagem.ataque += 5
            pnts -= 1

        elif melhoria == 3:
            quebrar_texto()
            texto_print("Você recebeu mais 5 de defesa")
            personagem.defesa += 5
            pnts -= 1
      
        elif melhoria == 4 and personagem.clase == "Mago":
            quebrar_texto()
            texto_print("Você recebeu mais 10 de mana maxima")
            personagem.mana_max += 10
            pnts -= 1
            
        else:
            texto_print("Opção inválida.")
            continue
       
        try:
            continuar = texto_input("Deseja continuar distribuindo pontos? (s/n) ").lower()

        except ValueError:
            texto_print("Opção inválida. Por favor, responda com  's' ou 'n'.")
            continue
        
        if continuar == "s":
            continue
        
        elif continuar == "n":
            break
        
        else:
           texto_print("Opção inválida. Por favor, responda com 's' ou 'n'.")
           continue


def calcular_dano (dano_adicional_personagem, dano_personagem, dano_monstro, defesa_adicional, defesa_personagem, defesa_monstro, elemento_jogador, elemento_monstro, elemento_sala):
   
   multiplicador_monstro = 1
   multiplicador_jogador = 1

   multiplicador_monstro_sala = 1
   multiplicador_jogador_sala = 1

   if elemento_jogador == elemento_monstro:
       multiplicador_monstro = 1
       multiplicador_jogador = 1

   if elemento_sala == elemento_jogador:
       multiplicador_jogador_sala = 1

   if elemento_sala == elemento_monstro:
       multiplicador_monstro_sala = 1

   if elemento_jogador != elemento_monstro:
       
       if elemento_jogador == "Fogo":
           if elemento_monstro in ["Água", "Ar", "Terra"]:
               multiplicador_monstro = 0.5
               multiplicador_jogador = 1.5

           elif elemento_monstro in ["Veneno", "Gelo", "Trevas"]:
               multiplicador_monstro = 1.5
               multiplicador_jogador = 0.5

           else:
               multiplicador_monstro = 1
               multiplicador_jogador = 1

       elif elemento_jogador == "Água":
           if elemento_monstro in ["Ar", "Terra", "Natureza"]:
               multiplicador_monstro = 0.5
               multiplicador_jogador = 1.5

           elif elemento_monstro in ["Fogo", "Luz", "Trevas"]:
               multiplicador_monstro = 1.5
               multiplicador_jogador = 0.5

           else:
               multiplicador_monstro = 1
               multiplicador_jogador = 1

       elif elemento_jogador == "Ar":
           if elemento_monstro in ["Terra", "Veneno", "Natureza"]:
               multiplicador_monstro = 0.5
               multiplicador_jogador = 1.5

           elif elemento_monstro in ["Fogo", "Água", "Luz"]:
               multiplicador_monstro = 1.5
               multiplicador_jogador = 0.5

           else:
               multiplicador_monstro = 1
               multiplicador_jogador = 1

       elif elemento_jogador == "Terra":
           if elemento_monstro in ["Veneno", "Gelo", "Raio"]:
               multiplicador_monstro = 0.5
               multiplicador_jogador = 1.5

           elif elemento_monstro in ["Água", "Fogo", "Ar"]:
               multiplicador_monstro = 1.5
               multiplicador_jogador = 0.5

           else:
               multiplicador_monstro = 1
               multiplicador_jogador = 1

       elif elemento_jogador == "Natureza":
           if elemento_monstro in ["Gelo", "Raio", "Veneno"]:
               multiplicador_monstro = 0.5
               multiplicador_jogador = 1.5

           elif elemento_monstro in ["Água", "Ar", "Terra"]:
               multiplicador_monstro = 1.5
               multiplicador_jogador = 0.5

           else:
               multiplicador_monstro = 1
               multiplicador_jogador = 1

       elif elemento_jogador == "Veneno":
           if elemento_monstro in ["Raio", "Gelo", "Luz"]:
               multiplicador_monstro = 0.5
               multiplicador_jogador = 1.5

           elif elemento_monstro in ["Terra", "Fogo", "Ar"]:
               multiplicador_monstro = 1.5
               multiplicador_jogador = 0.5

           else:
               multiplicador_monstro = 1
               multiplicador_jogador = 1

       elif elemento_jogador == "Gelo":
           if elemento_monstro in ["Luz", "Raio", "Trevas"]:
               multiplicador_monstro = 0.5
               multiplicador_jogador = 1.5

           elif elemento_monstro in ["Fogo", "Veneno", "Natureza"]:
               multiplicador_monstro = 1.5
               multiplicador_jogador = 0.5

           else:
               multiplicador_monstro = 1
               multiplicador_jogador = 1

       elif elemento_jogador == "Raio":
           if elemento_monstro in ["Luz", "Água", "Trevas"]:
               multiplicador_monstro = 0.5
               multiplicador_jogador = 1.5

           elif elemento_monstro in ["Fogo", "Gelo", "Natureza"]:
               multiplicador_monstro = 1.5
               multiplicador_jogador = 0.5

           else:
               multiplicador_monstro = 1
               multiplicador_jogador = 1

       elif elemento_jogador == "Luz":
           if elemento_monstro in ["Trevas", "Fogo", "Ar"]:
               multiplicador_monstro = 0.5
               multiplicador_jogador = 1.5

           elif elemento_monstro in ["Água", "Veneno", "Gelo"]:
               multiplicador_monstro = 1.5
               multiplicador_jogador = 0.5

           else:
               multiplicador_monstro = 1
               multiplicador_jogador = 1

       elif elemento_jogador == "Trevas":
           if elemento_monstro in ["Fogo", "Água", "Natureza"]:
               multiplicador_monstro = 0.5
               multiplicador_jogador = 1.5

           elif elemento_monstro in ["Gelo", "Raio", "Luz"]:
               multiplicador_monstro = 1.5
               multiplicador_jogador = 0.5

           else:
               multiplicador_monstro = 1
               multiplicador_jogador = 1

   if elemento_jogador != elemento_sala:
       
       if elemento_jogador == "Fogo":
           if elemento_sala in ["Água", "Ar", "Terra"]:
               multiplicador_jogador_sala = 1.5

           elif elemento_sala in ["Veneno", "Gelo", "Trevas"]:
               multiplicador_jogador_sala = 0.5

           else:
               multiplicador_jogador_sala = 1

       elif elemento_jogador == "Água":
           if elemento_sala in ["Ar", "Terra", "Natureza"]:
               multiplicador_jogador_sala = 1.5

           elif elemento_sala in ["Fogo", "Luz", "Trevas"]:
               multiplicador_jogador_sala = 0.5
               
           else:
               multiplicador_jogador_sala = 1

       elif elemento_jogador == "Ar":
           if elemento_sala in ["Terra", "Veneno", "Natureza"]:
               multiplicador_jogador_sala = 1.5

           elif elemento_sala in ["Fogo", "Água", "Luz"]:
               multiplicador_jogador_sala = 0.5

           else:
               multiplicador_jogador_sala = 1

       elif elemento_jogador == "Terra":
           if elemento_sala in ["Veneno", "Gelo", "Raio"]:
               multiplicador_jogador_sala = 1.5

           elif elemento_sala in ["Água", "Fogo", "Ar"]:
               multiplicador_jogador_sala = 0.5

           else:
               multiplicador_jogador_sala = 1

       elif elemento_jogador == "Natureza":
           if elemento_sala in ["Gelo", "Raio", "Veneno"]:
               multiplicador_jogador_sala = 1.5

           elif elemento_sala in ["Água", "Ar", "Terra"]:
               multiplicador_jogador_sala = 0.5

           else:
               multiplicador_jogador_sala = 1

       elif elemento_jogador == "Veneno":
           if elemento_sala in ["Raio", "Gelo", "Luz"]:
               multiplicador_jogador_sala = 1.5

           elif elemento_sala  in ["Terra", "Fogo", "Ar"]:
               multiplicador_jogador_sala = 0.5

           else:
               multiplicador_jogador_sala = 1

       elif elemento_jogador == "Gelo":
           if elemento_sala in ["Luz", "Raio", "Trevas"]:
               multiplicador_jogador_sala = 1.5

           elif elemento_sala  in ["Fogo", "Veneno", "Natureza"]:
               multiplicador_jogador_sala = 0.5

           else:
               multiplicador_jogador_sala = 1

       elif elemento_jogador == "Raio":
           if elemento_sala in ["Luz", "Água", "Trevas"]:
               multiplicador_jogador_sala = 1.5

           elif elemento_sala in ["Fogo", "Gelo", "Natureza"]:
               multiplicador_jogador_sala = 0.5

           else:
               multiplicador_jogador_sala = 1

       elif elemento_jogador == "Luz":
           if elemento_sala in ["Trevas", "Fogo", "Ar"]:
               multiplicador_jogador_sala = 1.5

           elif elemento_sala in ["Água", "Veneno", "Gelo"]:
               multiplicador_jogador_sala = 0.5

           else:
               multiplicador_jogador_sala = 1

       elif elemento_jogador == "Trevas":
           if elemento_sala in ["Fogo", "Água", "Natureza"]:
               multiplicador_jogador_sala = 1.5

           elif elemento_sala in ["Gelo", "Raio", "Luz"]:
               multiplicador_jogador_sala = 0.5

           else:
               multiplicador_jogador_sala = 1

   if elemento_monstro != elemento_sala:
       
       if elemento_monstro == "Fogo":
           if elemento_sala in ["Água", "Ar", "Terra"]:
               multiplicador_monstro_sala = 1.5

           elif elemento_sala in ["Veneno", "Gelo", "Trevas"]:
               multiplicador_monstro_sala = 0.5

           else:
               multiplicador_monstro_sala = 1

       elif elemento_monstro == "Água":
           if elemento_sala in ["Ar", "Terra", "Natureza"]:
               multiplicador_monstro_sala = 1.5

           elif elemento_sala in ["Fogo", "Luz", "Trevas"]:
               multiplicador_monstro_sala = 0.5

           else:
               multiplicador_monstro_sala = 1

       elif elemento_monstro == "Ar":
           if elemento_sala in ["Terra", "Veneno", "Natureza"]:
               multiplicador_monstro_sala = 1.5

           elif elemento_sala in ["Fogo", "Água", "Luz"]:
               multiplicador_monstro_sala = 0.5

           else:
               multiplicador_monstro_sala = 1

       elif elemento_monstro == "Terra":
           if elemento_sala in ["Veneno", "Gelo", "Raio"]:
               multiplicador_monstro_sala = 1.5

           elif elemento_sala in ["Água", "Fogo", "Ar"]:
               multiplicador_monstro_sala = 0.5

           else:
               multiplicador_monstro_sala = 1

       elif elemento_monstro == "Natureza":
           if elemento_sala in ["Gelo", "Raio", "Veneno"]:
               multiplicador_monstro_sala = 1.5

           elif elemento_sala in ["Água", "Ar", "Terra"]:
               multiplicador_monstro_sala = 0.5

           else:
               multiplicador_monstro_sala = 1

       elif elemento_monstro == "Veneno":
           if elemento_sala in ["Raio", "Gelo", "Luz"]:
               multiplicador_monstro_sala = 1.5

           elif elemento_sala  in ["Terra", "Fogo", "Ar"]:
               multiplicador_monstro_sala = 0.5

           else:
               multiplicador_monstro_sala = 1

       elif elemento_monstro == "Gelo":
           if elemento_sala in ["Luz", "Raio", "Trevas"]:
               multiplicador_monstro_sala = 1.5

           elif elemento_sala  in ["Fogo", "Veneno", "Natureza"]:
               multiplicador_monstro_sala = 0.5

           else:
               multiplicador_monstro_sala = 1

       elif elemento_monstro == "Raio":
           if elemento_sala in ["Luz", "Água", "Trevas"]:
               multiplicador_monstro_sala = 1.5

           elif elemento_sala in ["Fogo", "Gelo", "Natureza"]:
               multiplicador_monstro_sala = 0.5

           else:
               multiplicador_monstro_sala = 1

       elif elemento_monstro == "Luz":
           if elemento_sala in ["Trevas", "Fogo", "Ar"]:
               multiplicador_monstro_sala = 1.5

           elif elemento_sala in ["Água", "Veneno", "Gelo"]:
               multiplicador_monstro_sala = 0.5

           else:
               multiplicador_monstro_sala = 1

       elif elemento_monstro == "Trevas":
           if elemento_sala in ["Fogo", "Água", "Natureza"]:
               multiplicador_monstro_sala = 1.5

           elif elemento_sala in ["Gelo", "Raio", "Luz"]:
               multiplicador_monstro_sala = 0.5

           else:
               multiplicador_monstro_sala = 1

   dano_total_jogador = ((dano_personagem + dano_adicional_personagem) * multiplicador_jogador * multiplicador_jogador_sala)
   dano_final_jogador = int(dano_total_jogador - (dano_total_jogador * defesa_monstro / 100))

   dano_total_monstro = (dano_monstro * multiplicador_monstro * multiplicador_monstro_sala)
   dano_final_monstro = int(dano_total_monstro - (dano_total_monstro * (defesa_personagem + defesa_adicional) / 100))
   return [dano_final_jogador, dano_final_monstro]


while True:
    quebrar_texto()
    texto_print("RPG elementian \n")
    start = texto_input("Deseja iniciar jogo? (s/n) ").lower()
    
    if start == "n":
        texto_print("\nFechando jogo...")
        time.sleep(1)
        exit()

    elif start == "s":
        quebrar_texto()
        texto_print("Crie seu personagem\n")

        personagem = Personagem.gerar_personagem()
        if personagem.classe == "Guerreiro":
            equipado.append(Item("Espada de Madeira", None, None, 10, None, None))

        elif personagem.classe == "Arqueiro":
            equipado.append(Item("Arco Simples", None, None, 10, None, None))

        elif personagem.classe == "Mago":
            equipado.append(Item("Cajado Rústico", None, None, 10, None, None))

        quebrar_texto()
        texto_print("Em elementian, existem diversos elementos que definem as propriedades magicas dos seres vivos e ambientes.\n")
        time.sleep(1)
        texto_print("Você é um aventureiro que vive em um pequeno vilarejo.\n")
        time.sleep(1)
        texto_print("Um dia, saindo para explorar, encontra uma masmorra misteriosa, nela você sente diferentes energias elementais\n \n")
        time.sleep(1)
        escolha_sala = texto_input("Deseja entrar na masmorra? (s/n) ").lower()
        quebrar_texto()

        while True:
            if escolha_sala == "s":
                sala_nova = Salas.gerar_sala()
                Salas.narrar()

            elif escolha_sala == "n":
                texto_print("Você decide apenas ficar na sala até morrer de causas naturais.\n")
                break
            
            else:
                texto_print("Opção invalida, digite apenas s ou n\n")
                continue
            
            if sala_nova.inimigo:
                monstro = Monstro.gerar_monstro()
                texto_print(f"\n Iniciando batalha...\n")
                time.sleep(2)

                while personagem.vida > 0 and monstro.vida > 0:
                    quebrar_texto()
                    texto_print(f"{personagem.nome} - Vida: {personagem.vida}\n")
                    texto_print(f"{monstro.tipo} - Vida: {monstro.vida}\n")
                    texto_print("\nOpções de combate:\n")
                    texto_print("1 - Atacar\n")
                    texto_print("2 - Ver inventário\n")
                    texto_print("3 - Status\n")
                    texto_print("4 - Fugir\n")
                    time.sleep(1)

                    try:
                        escolha_turno = int(texto_input("Escolha sua ação: "))

                        if escolha_turno == 1:
                            
                            if personagem.classe == "Mago":
                                ataque_mago = texto_input("\nDeseja usar magia? (s/n) ").lower()

                                if ataque_mago == "s":
                                    texto_print("\nMagias disponiveis:")

                                    for i, magia in enumerate(magias[f"magias_{personagem.elemento.lower()}"], start=1):
                                        texto_print(f"{i} - {magia.nome} | Dano: {magia.dano} | Custo de Mana: {magia.custo_mana}")
                                        texto_print(f"Descrição: {magia.descricao}\n")

                                    try:
                                        escolha_magia = int(texto_input("Escolha uma magia para usar: ")) - 1
                                        quebrar_texto()
                                        magia_escolhida = magias[f"magias_{personagem.elemento.lower()}"][escolha_magia]

                                        if personagem.mana >= magia_escolhida.custo_mana:
                                            personagem.mana -= magia_escolhida.custo_mana

                                            for objeto in equipado:
                                                if objeto.tipo_armadura:
                                                    defesa_adicional = objeto.defesa

                                                else:
                                                    defesa_adicional = 0
                                                    break    
                                                
                                            dano_calculado  = calcular_dano(personagem.buff_forca, personagem.ataque + magia_escolhida.dano, monstro.ataque, defesa_adicional, personagem.defesa + personagem.buff_defesa, monstro.defesa, personagem.elemento, monstro.elemento, sala_nova.elementos)                                    
                                            monstro.vida -= dano_calculado[0]

                                        else:
                                            texto_print("Mana insuficiente para usar essa magia. \n")
                                            continue
                                        
                                    except (ValueError, IndexError):
                                        texto_print("Opção inválida. Por favor, escolha uma magia válida. \n")
                                        continue
                                    
                                elif ataque_mago == "n":
                                    for objeto in equipado:
                                        if objeto.tipo_arma:
                                            dano_arma = objeto.dano
                                            break
                                        
                                    dano_calculado  = calcular_dano(personagem.buff_forca, personagem.ataque + dano_arma, monstro.ataque, personagem.defesa + personagem.buff_defesa, monstro.defesa, personagem.elemento, monstro.elemento, sala_nova.elementos)                                    
                                    monstro.vida -= dano_calculado[0]

                                else:
                                    texto_print("Opção invalida, digite apeans s ou n\n")
                                    continue
                                
                            else:
                                for objeto in equipado:
                                    if objeto.tipo_armadura:
                                        defesa_adicional = objeto.defesa
                                        break
                                    
                                dano_calculado  = calcular_dano(objeto.dano, personagem.ataque + personagem.buff_forca, monstro.ataque, defesa_adicional, personagem.defesa + personagem.buff_defesa, monstro.defesa, personagem.elemento, monstro.elemento, sala_nova.elementos)                                    
                                monstro.vida -= dano_calculado[0]

                            texto_print(f"Você atacou o {monstro.tipo} causando {dano_calculado[0]} de dano! \n")
                            time.sleep(1)

                            personagem.vida -= dano_calculado[1]
                            texto_print(f"O {monstro.tipo} atacou causando {dano_calculado[1]} de dano! \n")
                            time.sleep(1)

                            if personagem.turnos_buff_forca > 0:
                                personagem.turnos_buff_forca -= 1

                                if personagem.turnos_buff_forca == 0:
                                    personagem.buff_forca = 0
                                    quebrar_texto()
                                    texto_print("\nO efeito da Poção de Força acabou.\n")
                                    time.sleep(1)

                            if personagem.turnos_buff_defesa > 0:
                                personagem.turnos_buff_defesa -= 1

                                if personagem.turnos_buff_defesa == 0:
                                    personagem.buff_defesa = 0
                                    quebrar_texto()
                                    texto_print("\nO efeito da Poção de Defesa acabou.\n")
                                    time.sleep(1)

                        elif escolha_turno == 2:
                            quebrar_texto()
                            texto_print("\nInventario:")

                            for i in range(len(inventario)):
                                texto_print(f"{i+1} - {inventario[i]}")
                                time.sleep(0.5)

                            print("\n")
                            texto_print("Equipados:")

                            for i in range(len(equipado)):
                                texto_print(f"{i+1} - {equipado[i]}")
                                time.sleep(0.5)

                            quebrar_texto()
                            texto_print("Menu de ações do inventario:\n")
                            texto_print("1 - Equipar item do inventario\n")
                            texto_print("2 - Remover item equipado\n")
                            texto_print("3 - Consumir item do inventario\n")
                            texto_print("4 - Apagar item\n")
                            texto_print("5 - Sair\n")

                            try:
                                escolha_inventario = int(texto_input("Escolha uma das opções: "))
                                
                                if escolha_inventario == 1:
                                    item_equipar = int(texto_input("Escolha um dos itens do seu inventario: "))
                                    item_equipar -= 1
                                    item = inventario[item_equipar]

                                    if item.tipo_arma:
                                        for objeto in equipado:
                                            
                                            if objeto.tipo_arma:
                                                texto_print("Você já possui uma arma.\n")
                                                break
                                            else:
                                                equipado.append(item)
                                                texto_print("Você equipou o item\n")

                                    elif item.tipo_armadura:
                                        for objeto in equipado:
                                            
                                            if objeto.tipo_armadura:
                                                texto_print("Você já possui uma armadura.\n")
                                                break
                                            
                                            else:
                                                equipado.append(item)
                                                texto_print("Você equipou o item\n")

                                    elif item.tipo_pocao:
                                        texto_print("Não é possivel equipar poções\n")

                                elif escolha_inventario == 2:
                                    
                                    item_remover = int(texto_input("Escolha um item equipado para remover: "))
                                    item_remover -= 1
                                    item = equipado[item_remover]

                                    equipado.remove(item)
                                    inventario.append(item)
                                    texto_print("\nItem removido dos equipados")

                                elif escolha_inventario == 3:
                                    item_consumir = int(texto_input("Escolha item para consumir: "))
                                    item_consumir -= 1
                                    item = inventario[item_consumir]

                                    if item.tipo_pocao:
                                        escolha_pocao = texto_input("\nDeseja consumir essa poção? (s/n) ").lower()

                                        if escolha_pocao == "s":
                                            
                                            if item.tipo_pocao == "Poção de vida":
                                                
                                                if personagem.vida == personagem.vida_max:
                                                    texto_print("Você já possui vida máxima, não é possivel consumir essa poção\n")
                                                    continue
                                                
                                                elif personagem.vida > personagem.vida_max:
                                                    personagem.vida += item.efeito

                                                    if personagem.vida > personagem.vida_max:
                                                        personagem.vida = personagem.vida_max
                                                        texto_print("Você possui vida máxima\n")
                                                        continue
                                                    
                                                    else:
                                                        texto_print(f"Você recuperou {item.efeito} de vida\n")
                                                        continue
                                                    
                                            elif item.tipo_pocao == "Poção de mana":
                                                
                                                if personagem.mana == personagem.mana_max:
                                                    texto_print("Você já possui vida máxima, não é possivel consumir essa poção\n")
                                                    continue
                                                
                                                elif personagem.mana > personagem.mana_max:
                                                    personagem.vida += item.efeito

                                                    if personagem.mana > personagem.mana_max:
                                                        personagem.mana = personagem.mana_max
                                                        texto_print("Você possui mana máxima\n")
                                                        continue
                                                    
                                                    else:
                                                        texto_print(f"Você recuperou {item.efeito} de mana\n")
                                                        continue
                                                    
                                            elif item.tipo_pocao == "Poção de força":
                                                personagem.buff_forca = item.efeito
                                                personagem.turnos_buff_forca = 3

                                            elif item.tipo_pocao == "Poção de defesa":
                                                
                                                personagem.buff_defesa = item.efeito
                                                personagem.turnos_buff_defesa = 3

                                            inventario.remove(item)

                                        else:
                                            texto_print("Você não pode consumir itens comuns, apenas poções\n")
                                            continue

                                elif escolha_inventario == 4:
                                    item_apagar = int(texto_input("Escolha um item para apagar: "))
                                    item_apagar -= 1
                                    confirmar_delet = texto_input("Tem certeza que deseja apagar este item? (s/n) ").lower()

                                    if confirmar_delet == "s":
                                        inventario.remove(inventario[item_apagar])

                                    elif confirmar_delet == "n":
                                        continue
                                    
                                    else:
                                        texto_print("Opção invalida\n")
                                        continue
                                    
                                elif escolha_inventario == 5:
                                    continue
                                
                                else:
                                    texto_print("Opção invalida\n")
                                    continue
                                
                            except ValueError:
                                texto_print("opção invalida, use apenas números\n")

                        elif escolha_turno == 3:
                            quebrar_texto()
                            texto_print(f"{personagem.nome}\n")
                            texto_print(f"lvl: {personagem.level} | exp: {personagem.exp}/{personagem.min_exp}\n")
                            texto_print(f"Classe: {personagem.classe}\n")
                            texto_print(f"Vida: {personagem.vida}\n")
                            texto_print(f"Mana: {personagem.mana}\n")
                            texto_print(f"Ataque: {personagem.ataque}\n")
                            texto_print(f"Defesa: {personagem.defesa}\n \n")

                            texto_print(f"{monstro.tipo} \n")
                            texto_print(f"Vida: {monstro.vida}\n")
                            texto_print(f"Ataque: {monstro.ataque}\n")
                            texto_print(f"Defesa: {monstro.defesa}\n")

                        elif escolha_turno == 4:
                            texto_print("Você foge da luta e para de lutar com o monstro\n")
                            break
                        
                    except ValueError:
                        texto_print("opção invalida, use apenas números\n")

                if personagem.vida <= 0:
                    quebrar_texto()
                    texto_print("Você morreu, fim de jogo.\n")
                    recomecar = input("Deseja recomeçar o jogo? (s/n) ").lower()

                    if recomecar == "s":
                        inventario.clear()
                        continue
                    
                    else:
                        exit()
                        break

                if monstro.vida <= 0:
                    quebrar_texto()
                    texto_print(f"Você derrotou o {monstro.tipo} e recebeu {monstro.exp} de experiência\n")
                    aplicar_exp()
                    aplicar_pontos(personagem.pontos)

                    if sala_nova.recompensa:
                        texto_input("\nPressione ENTER para ver a recompensa...")
                        tamanho = Recompensas.narrar_recompensa(tamanho_recompensa)

                        if tamanho == "Pequeno":
                            quantidade = 1

                        elif tamanho == "Médio":
                            quantidade = 2

                        elif tamanho == "Grande":
                            quantidade = 3

                        texto_input("\nPressione ENTER para coletar recompensa...")

                        for i in range(quantidade):
                            item = Item.narrar_item()
                            inventario.append(item)
                    else:
                        pass
                    
            escolha_sala = texto_input("\nDeseja entrar na proxima sala? (s/n)").lower()

    else:
        texto_print("Opção invalida, digite apenas")    