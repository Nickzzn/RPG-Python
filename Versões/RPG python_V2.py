while True: #Cadeia principal que só acaba quando o jogador não querer recomeçar
    #variaveis
    itens = False
    inventario = []
 
    turnos = 0
    vida_jogador = 100
    dano_espada = 20
 
    vida_monstro = 150
    dano_monstro = 15
 
    #historia/contexto do programa. Usa apenas if e else simples para inicialização do jogo
    print("\nRPG de texto em python!")
 
    start = input("\ndeseja começar o jogo? (S/N) ").upper()
 
    if start == "S":
        print("Carregando jogo...")
 
    else:
        print("fechando jogo")
        exit()
    
    nome = input("Qual seu nome? \n")

    input("\nVocê é um aventureiro iniciante de uma vila pequena, a alguns dias houve relatos sobre desaparecimentos próximos a uma floresta, sua bravura impede de deixar isto para lá... (pressione ENTER para avançar)")
    input("Camninhando pela floresta você acha uma trilha, que levava a uma escura caverna. (pressione ENTER para avançar)")
    #Variável de decisao para a escolha de entrar ou não na caverna.
    decisao_caverna = input("\nEntrar na caverna? (S/N) ").upper()
 
    if decisao_caverna == "S":
        input("\nA caverna era úmida e fria, um som de gotas ecoa por todo local... (pressione ENTER para avançar)")
    else:
        input("\nVocê se vira e volta pra vila, e volta a viver... (pressione ENTER para avançar)")
        print("Fim")

        jogar_de_novo = input("\nDeseja jogar de novo? (S/N) ").upper() #Verifica se o jogador que jogar de novo
        if jogar_de_novo == "S":
            continue  # Volta para o início do loop principal
        else:
            print("Obrigado por jogar!")
            break
 
    input("Após andar por um tempo pela caverna, você encontra um baú brilhante, que ilumina a escuridão (pressione ENTER para avançar)")
    abrir_bau =input("\nVocê abre o baú? (S/N) ").upper()
    #Escolha mais importante de todo o código para que o resto dos comandos funcionem
    if abrir_bau == "S":
        input("\nVocê abre o baú, encontrando um amuleto em formato de raio brilhante, uma espada de aço reluzente e um frasco com um líquido vermelho (pressione ENTER para avançar)")
        input("Você pega os dois objetos e os guarda no seu inventário (pressione ENTER para avançar)")
        inventario.append("Emblema de raio")
        inventario.append("Poção de cura")
        itens = True # afirma que ele pegou os itens no baú
    else:
        print("Você apenas passa reto\n")
    
    input("\nDe repente, um barulho amendrontador ressoa atrás de você. \nAo se virar, você avista um monstro horrendo e gigante diante de ti. (pressione ENTER para avançar)")
    #Primeira decisão que pode resultar em morte e no fim do programa sem a opção de luta
    decisao_luta =input("\nVocê decide fugir? (S/N) ").upper()
    if decisao_luta == "S":
        input("\nVocê se vira e corre o máximo que pode, chegando em uma parte sem saída da caverna. O monstro gigante aparece e vai caminhando em sua direção. Ele prepara um soco e te acerta com toda a força. (pressione ENTER para avançar)\n")
        print("Você morreu...")
        print("Fim")

        jogar_de_novo = input("\nDeseja jogar de novo? (S/N) ").upper()
        if jogar_de_novo == "S":
            continue  
        else:
            print("Obrigado por jogar!")
            exit()
    else:
        input("\nEm um movimento instintivo, você entra em posição de combate, mesmo que não tenha chance de sobreviver. (pressione ENTER para avançar)")
        input("\nO monstro olha para você e dá uma risada, aceitando o desafio. (pressione ENTER para avançar)\n")
        input("Pressione ENTER para iniciar a batalha")
    #Interface do menu de escolhas, parte principal do combate. O combate é baseado em turnos contados onde o jogador escolhe a sua ação e no próximo o monstro ataca.
    if itens == True: #verifica se ele tem ou não os itens do baú
        while vida_monstro > 0 and vida_jogador > 0:
            print(f"Turno: {turnos}")
            print(f"\nVida do monstro: {vida_monstro}")
            print(f"Vida do jogador: {vida_jogador}\n")
            print("1 - Olhar inventario")
            print("2 - Atacar")
            print("3 - fugir")
            try:
                escolha_turno = int(input("Escolha uma opção para o turno: "))

            except ValueError:
                print("Opção invalida, use apenas os números do menu")
                continue

    #Comandos para decidir o que o jogador irá realizar no turno
            if escolha_turno == 1:
                #Listar todos os itens do invertário
                for i in range(len(inventario)):
                    print(f"{i+1}° item: {inventario[i]}")
                print("\nEscreva 3 para sair")
                
                try:
                    #Escolha do item do invertário que será utilizado
                    escolha_item = int(input("Escolha um dos itens: "))
                except ValueError:
                    print("Opção invalida, use apenas numeos presentes na lista de itens")

                if escolha_item == 1:
                    print("Um amuleto em formato de raio que da pequenos choques ao tocar.")
    
                elif escolha_item == 2:
                    print("\nUma poção de cura que recupera 50 de vida.")
                    pocao = input("Deseja consumir a poção? (S/N)").upper()
                    #Verificar se a vida não passará do limite de 100 ao usar a poção
                    if pocao == "S":
                        vida_nova_jogador = vida_jogador + 50
    
                        if vida_nova_jogador > 100:
                            vida_jogador = 100

                        else:
                            vida_jogador = vida_nova_jogador
                        inventario.pop()
    
                    else:
                        print("Opção invalida, use apenas numeos presentes na lista de itens")
                        continue
                   
                else:
                    continue
            
            elif escolha_turno == 2:
                vida_jogador = vida_jogador - dano_monstro
                vida_monstro = vida_monstro - dano_espada
                print("Você golpeia ele com um corte em seu corpo, porém logo depois ele se recompõe e te acerta com um soco")

            else:
                print("Você corre pela sua vida e consegue fugir dele como um covarde.")
                print("Fim.")
                exit() #Termina o programa dependendo da escolha do jogador

            turnos += 1 #Aumenta um na variável turno independentemente da escolha do jogador
    else:
        input(" escolhe lutar sem nenhum tipo de arma ou artefato. O monstro te mata e você nunca mais foi visto. (pressione ENTER para avançar)")
        print("Fim.")

        jogar_de_novo = input("\nDeseja jogar de novo? (S/N) ").upper()
        if jogar_de_novo == "S":
            continue 
        else:
            print("Obrigado por jogar!")
            exit()
 
    if vida_jogador > 0:
        print(f"Luta finalizada em {turnos} turnos") # mostra em qual turno a luta acabou
        input("\nVocê enfim derrota o monstro. Ao adentrar mais a caverna, percebe que as pessoas desaparecidas estavam sido mantidas em cativeiro pelo monstro. (pressione ENTER para avançar)")
        input("\nVocê liberta os prisoneiros e os leva de volta à vila, se tornando o héroi deles. (pressione ENTER para avançar)")
        print("Fim.")
    
        jogar_de_novo = input("\nDeseja jogar de novo? (S/N) ").upper()
        if jogar_de_novo == "S":
            continue
        else:
            print("Obrigado por jogar!")
            break
 
    elif vida_monstro > 0:
        print(f"Luta finalizada em {turnos} turnos")
        input("\n O monstro consegue te derrotar e o vilarejo continua sendo assombrado com sua presença. (pressione ENTER para avançar)")
        print("Fim.")

        jogar_de_novo = input("\nDeseja jogar de novo? (S/N) ").upper()
        if jogar_de_novo == "S":
            continue
        else:
            print("Obrigado por jogar!")
            break