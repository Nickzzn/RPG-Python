import time
import random

sala = ["paredes comuns", "escadarias longas para baixo", "escadarias longas para cima", "espinhos pontudos"]
elementos = ["Fogo", "Água", "Terra", "Ar", "Gelo", "Luz", "Trevas", "Raio", "Veneno"]
inimigo = [False, True]
recompensa = [False, True]

monstros = ["Goblin", "Esqueleto", "Slime", "Orc", "zumbi", "dragão"]

inventario = []
equipado = []
tamanho_recompensa = ["Pequeno", "Médio", "Grande"]
quantidade = None

min_exp = 50

arma = ["Espada", "Arco", "Cajado", "Adaga", "Machado"]
pocoes = ["Poção de vida", "Poção de mana", "Poção de força", "Poção de defesa"]
armaduras = ["Armadura de Couro", "Armadura de Ferro", "Armadura de Aço", "Armadura de platina"]

class Personagem:
        def __init__(self, nome, classe, elemento, vida, ataque, defesa, mana, exp, level, pontos, buff_forca, buff_defesa, turnos_buff_forca, turnos_buff_defesa):
            self.nome = nome
            self.classe = classe
            self.elemento = elemento
            self.vida = vida
            self.ataque = ataque
            self.defesa = defesa
            self.mana = mana
            self.exp = exp
            self.level = level
            self.pontos = pontos

            self.buff_forca = buff_forca
            self.buff_defesa = buff_defesa
            self.turnos_buff_forca = turnos_buff_forca
            self.turnos_buff_defesa = turnos_buff_defesa

        def gerar_personagem():

            nome = input("Digite o nome do seu personagem: ")

            print("\n lista de classes:")
            time.sleep(0.5)
            print("1. Guerreiro: 100 de vida, 20 de ataque, 15 de defesa, 50 de mana")
            time.sleep(0.5)
            print("2. Mago: 80 de vida, 25 de ataque, 10 de defesa, 100 de mana")
            time.sleep(0.5)
            print("3. Arqueiro: 90 de vida, 18 de ataque, 12 de defesa, 75 de mana \n")
            time.sleep(0.5)

            try:
                classe = input("Escolha a classe do seu personagem (1/2/3): ")

            except ValueError:
                print("Valor invalido. Digite apenas números")

            print("\n escolha seu elemento:")
            time.sleep(0.5)
            print("1. Fogo")
            time.sleep(0.5)
            print("2. Água")
            time.sleep(0.5)
            print("3. Terra")
            time.sleep(0.5)
            print("4. Ar")
            time.sleep(0.5)
            print("5. Gelo")
            time.sleep(0.5)
            print("6. Luz")
            time.sleep(0.5)
            print("7. Trevas")
            time.sleep(0.5)
            print("8. Raio")
            time.sleep(0.5)

            try:
                elemento = input("Escolha o elemento do seu personagem (1/2/3/4/5/6/7/8): ")

                if elemento == "1":
                    elemento = "Fogo"  

                elif elemento == "2":
                    elemento = "Água"

                elif elemento == "3":
                    elemento = "Terra"

                elif elemento == "4":
                    elemento = "Ar"

                elif elemento == "5":   
                    elemento = "Gelo"

                elif elemento == "6":   
                    elemento = "Luz"

                elif elemento == "7":
                    elemento = "Trevas"

                elif elemento == "8":
                    elemento = "Raio"

            except ValueError:
                print("Valor invalido. Digite apenas números")


            if classe == "1":
                return Personagem(nome, "Guerreiro", elemento, 100, 20, 15, 50, 0, 1, 0, 0, 0, 0, 0)
            
            elif classe == "2":
                return Personagem(nome, "Mago", elemento, 80, 25, 10, 100, 0, 1, 0, 0, 0, 0, 0)
            
            elif classe == "3":
                return Personagem(nome, "Arqueiro", elemento, 90, 18, 12, 75, 0, 1, 0, 0, 0, 0, 0)
            
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
        print(f"\nVocê entrou em uma sala com {sala_nova.estrutura}.")
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

        if item_gerado.tipo_arma:
            print(f"Você encontrou uma arma: {item_gerado.tipo_arma} com {item_gerado.dano} de dano.")

        elif item_gerado.tipo_armadura:
            print(f"Você encontrou uma armadura: {item_gerado.tipo_armadura} com {item_gerado.defesa} de defesa.")
        
        elif item_gerado.tipo_pocao:
            print(f"Você encontrou uma poção: {item_gerado.tipo_pocao} com efeito de {item_gerado.efeito}.")
        
        return item_gerado
        time.sleep(1)

def aplicar_exp():
    Personagem.exp += Monstro.exp

    if Personagem.exp == min_exp:
        Personagem.level += 1
        Personagem.exp = 0
        Personagem.pontos += 5
        min_exp += 50

    elif Personagem.exp > min_exp:
        Personagem.level += 1
        Personagem.exp -= min_exp
        Personagem.pontos += 5
        min_exp += 500
    
def aplicar_pontos(pnts):
    while pnts > 0:
        print(f"\nVocê possui {pnts} pontos para distribuir entre seus atributos:")
        print("1 - Vida")
        print("2 - Ataque")
        print("3 - Defesa")
        print("4 - Mana")

        try:
            melhoria = int(input("Qual dos atributos deseja melhorar? "))

        except ValueError:
            print("Opção inválida. Por favor, escolha um número entre 1 e 4.")
            return

        if melhoria == 1:
            Personagem.vida += 10

        elif melhoria == 2:
            Personagem.ataque += 5

        elif melhoria == 3:
            Personagem.defesa += 5

        elif melhoria == 4:
            Personagem.mana += 10

        else:
            print("Opção inválida.")
            continue
        
        pnts -= 1
        continuar = input("Deseja continuar distribuindo pontos? (s/n) ").lower()

        if continuar == "s":
            continue

        elif continuar == "n":
            break

        else:
            print("Opção inválida. Por favor, responda com 's' ou 'n'.")
            continue


while True:

    print("RPG elementian\n")
    print("Crie seu personagem\n")
    personagem = Personagem.gerar_personagem()

    if personagem.classe == "Guerreiro":
        equipado.append(Item("Espada de Madeira", None, None, 10, None, None))

    elif personagem.classe == "Arqueiro":
        equipado.append(Item("Arco Simples", None, None, 10, None, None))

    elif personagem.classe == "Mago":
        equipado.append(Item("Cajado Rústico", None, None, 10, None, None))

    print("\nEm elementian, existem diversos elementos que definem as propriedades magicas dos seres vivos e ambientes")
    time.sleep(1)
    print("Você é um aventureiro que vive em um pequeno vilarejo")
    time.sleep(1)
    print("Um dia, saindo para explorar, encontra uma masmorra misteriosa, nela você sente diferentes energias elementais")
    time.sleep(1)
    escolha_sala = input("Deseja entrar na masmorra? (s/n) ").lower()

    while True:

        if escolha_sala == "s":
            sala_nova = Salas.gerar_sala()
            Salas.narrar()

        elif escolha_sala == "n":
            print("Você decide apenas ficar na sala até morrer de causas naturais.")
            break
        
        else: 
            print("Opção invalida, digite apenas S ou N")
            continue

        if sala_nova.inimigo:
            monstro = Monstro.gerar_monstro()
            print(f"\n Iniciando batalha...")
            time.sleep(2)

            while personagem.vida > 0 and monstro.vida > 0:
                print(f"\n{personagem.nome} - Vida: {personagem.vida}")
                print(f"{monstro.tipo} - Vida: {monstro.vida}\n")

                print("\nOpções de combate:")
                print("1 - Atacar")
                print("2 - Ver inventário")
                print("3 - Status")
                print("4 - Fugir")
                time.sleep(1)

                try:
                    escolha_turno = int(input("Escolha sua ação: "))

                    if escolha_turno == 1:
                        dano_jogador = personagem.ataque + personagem.buff_forca

                        for objeto in equipado:
                            if objeto.tipo_arma:
                                dano_jogador += objeto.dano
                                break

                        dano_final = int(dano_jogador - (dano_jogador * monstro.defesa / 100))

                        monstro.vida -= dano_final

                        print(f"Você atacou o {monstro.tipo} causando {dano_final} de dano!")
                        time.sleep(1)
                        defesa_jogador = personagem.defesa + personagem.buff_defesa

                        for objeto in equipado:
                            if objeto.tipo_armadura:
                                defesa_jogador += objeto.defesa
                                break

                        dano_monstro = monstro.ataque
                        dano_final = int(dano_monstro - (dano_monstro * defesa_jogador / 100))

                        personagem.vida -= dano_final

                        print(f"O {monstro.tipo} atacou causando {dano_final} de dano!")
                        time.sleep(1)

                        if personagem.turnos_buff_forca > 0:
                            personagem.turnos_buff_forca -= 1

                            if personagem.turnos_buff_forca == 0:
                                personagem.buff_forca = 0
                                print("\nO efeito da Poção de Força acabou.\n")
                                time.sleep(1)

                        if personagem.turnos_buff_defesa > 0:
                            personagem.turnos_buff_defesa -= 1

                            if personagem.turnos_buff_defesa == 0:
                                personagem.buff_defesa = 0
                                print("\nO efeito da Poção de Defesa acabou.\n")
                                time.sleep(1)

                    elif escolha_turno == 2: 
                        print("\nInventario:")

                        for i in range(len(inventario)):
                            print(f"{i+1} - {inventario[i]}")
                            time.sleep(0.5)

                        print("\n")

                        print("Equipados:")
                        for i in range(len(equipado)):
                            print(f"{i+1} - {equipado[i]}")
                            time.sleep(0.5)

                        print("\n")
                        print("Menu de ações do inventario:")
                        print("1 - Equipar item do inventario")
                        print("2 - Remover item equipado")
                        print("3 - Consumir item do inventario")
                        print("4 - Apagar item")
                        print("5 - Sair\n")

                        try:
                            escolha_inventario = int(input("Escolha uma das opções: "))

                            if escolha_inventario == 1:
                                item_equipar = int(input("Escolha um dos itens do seu inventario: "))
                                item_equipar -= 1

                                item = inventario[item_equipar]

                                if item.tipo_arma:
                                    for objeto in equipado:
                                        if objeto.tipo_arma:
                                            print("Você já possui uma arma.")
                                            break

                                        else:
                                            equipado.append(item)
                                            print("Você equipou o item")

                                elif item.tipo_armadura:
                                    for objeto in equipado:
                                        if objeto.tipo_armadura:
                                            print("Você já possui uma armadura.")
                                            break

                                        else:
                                            equipado.append(item)
                                            print("Você equipou o item")

                                elif item.tipo_pocao:
                                    print("Não é possivel equipar poções")

                            elif escolha_inventario == 2:
                                item_remover = int(input("Escolha um item equipado para remover: "))
                                item_remover -= 1

                                item = equipado[item_remover]

                                equipado.remove(item)
                                inventario.append(item)

                                print("Item removido dos equipados")

                            elif escolha_inventario == 3:
                                item_consumir = int(input("Escolha item para consumir: "))
                                item_consumir -= 1

                                item = inventario[item_consumir]

                                if item.tipo_pocao:
                                    escolha_pocao = input("\nDeseja consumir essa poção? (s/n) ").lower()

                                    if escolha_pocao == "s":
                                        if item.tipo_pocao == "Poção de vida":
                                            personagem.vida += item.efeito

                                        elif item.tipo_pocao == "Poção de mana":
                                            personagem.mana += item.efeito

                                        elif item.tipo_pocao == "Poção de força":
                                            personagem.buff_forca = item.efeito
                                            personagem.turnos_buff_forca = 3

                                        elif item.tipo_pocao == "Poção de defesa":
                                            personagem.buff_defesa = item.efeito
                                            personagem.turnos_buff_defesa = 3

                                    else:
                                        print("Você não pode consumir itens comuns, apenas poções")
                                        continue

                            
                            elif escolha_inventario == 4:
                                item_apagar = int(input("Escolha um item para apagar: "))
                                item_apagar -= 1

                                confirmar_delet = input("Tem certeza que deseja apagar este item? (s/n) ").lower()
                                if confirmar_delet == "s":
                                    inventario.remove(inventario[item_apagar])

                                elif confirmar_delet == "n":
                                    continue

                                else:
                                    print("Opção invalida")
                                    continue

                            elif escolha_inventario == 5:
                                continue

                            else: 
                                print("Opção invalida")
                                continue
                
                        except ValueError:
                            print("opção invalida, use apenas números")

                    elif escolha_turno == 3:
                        print(personagem.nome)
                        print(f"lvl: {personagem.level} | exp: {personagem.exp}/{min_exp}")
                        print(f"Classe: {personagem.classe}")
                        print(f"Vida: {personagem.vida}")
                        print(f"Mana: {personagem.mana}")
                        print(f"Ataque: {personagem.ataque}")
                        print(f"Defesa: {personagem.defesa}\n")
                        print(monstro.tipo)
                        print(f"Vida: {monstro.vida}")
                        print(f"Ataque: {monstro.ataque}")
                        print(f"Defesa: {monstro.defesa}")

                    elif escolha_turno == 4:
                        print("Você foge da luta e para de lutar com o monstro")
                        break
                    
                except ValueError:
                    print("opção invalida, use apenas números")

        if personagem.vida <= 0:
            print("Você morreu! Fim de jogo.")

            recomecar = input("Deseja recomeçar o jogo? (s/n) ").lower()

            if recomecar == "s":
                continue
            else:
                break
    

        if monstro.vida <= 0:
            print(f"Você derrotou o {monstro.tipo} e recebeu {monstro.exp} de experiência")
            aplicar_exp()
            aplicar_pontos(personagem.pontos)

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
            
            escolha_sala = input("Deseja entrar na proxima sala? (s/n)").lower()