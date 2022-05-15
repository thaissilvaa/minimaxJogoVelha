playerTurn = True

def TicTacToe():
    board = [1,2,3,4,5,6,7,8,9]
    MagicSquare = [4,9,2,3,5,7,8,1,6]

    # VERIFICA SE TEM ALGUM QUADRADO DO TABULEIRO PREENCHIDO
    def getE(i, type):
        # TABULEIRO 0, O QUE FICA VAZIO
        if(type == 0):
            if(board[i] == 'X' or board[i] == 'O'):
                return (board[i])
            else:
                return (" ")
    
        # TABULEIRO 1, O QUE FICA COM OS NÚMEROS
        if(type == 1):
            if(board[i] == 'X' or board == 'O'):
                return ('-')
            else:
                return(board[i])

    # IMPRIME OS DOIS TABULEIROS
    # OS getE(N, 0) É O TABULEIRO VAZIO
    # OS getE(N, 1) É O TABULEIRO PREECNHIDO COM OS NÚMEROS
    def PrintBoard():
        print('')
        print('', getE(0,0), '|', getE(1,0), '|', getE(2,0),'         ', getE(0,1), '|', getE(1,1), '|', getE(2,1))
        print('---|---|---','       ','---|---|---')
        print('', getE(3,0), '|', getE(4,0), '|', getE(5,0),'         ',getE(3,1), '|', getE(4,1), '|', getE(5,1))
        print('---|---|---','       ','---|---|---')
        print('', getE(6,0), '|', getE(7,0), '|', getE(8,0),'         ',getE(6,1), '|', getE(7,1), '|', getE(8,1))
        print('')

    #PEGA O NÚMERO DIGITADO PELO PLAYER
    def GetNumber(player):
        while True:
            number = input("Escolha uma posição " + player + ": ")
            try:
                # CONVERTE NÚMERO DIGITADO PELO PLAYER PARA O TIPO INTEIRO
                number = int(number)

                # SE FOR UM NÚMERO DE 1 AO 9 RETORNA O NÚMERO
                if number in range(1,10):
                    return number
                
                # SE NÃO FOR UM NÚMERO VÁLIDO, TEM QUE DIGITAR NOVAMENTE
                else:
                    print('Digite um número válido!')
            
            # SE DIGITAR UM CARACTER ESPECIAL OU UMA LETRA, TEM QUE DIGITAR NOVAMENTE
            except ValueError:
                print('Eu preciso de um número!')
                continue

    #CHECA SE ALGUÉM JÁ GANHOU
    def CheckWin(thisBoard):
        count = 0

        for x in range(9):
            for y in range(9):
                for z in range(9):
                    if x != y and y != z and x != z:
                        if thisBoard[x] == 'X' and thisBoard[y] == 'X' and thisBoard[z] == 'X':
                            if MagicSquare[x] + MagicSquare[y] + MagicSquare[z] == 15:
                                return 1
                        
                        if thisBoard[x] == 'O' and thisBoard[y] == 'O' and thisBoard[z] == 'O':
                            if MagicSquare[x] + MagicSquare[y] + MagicSquare[z] == 15:
                                return -1

        for v in range(9):
            if(thisBoard[v] == 'X' or thisBoard[v] == 'O'):
                count += 1

        if(count == 9):
            return 0
        return 5

    # JOGADAS DO PLAYER
    def Turn(player):
        # PEGA O NÚMERO QUE O PLAYER DIGITOU
        n = GetNumber(player)
        # VÁLIDA SE A POSIÇÃO JÁ NÃO ESTÁ OCUPADA
        if(board[n-1] == 'X' or board[n-1] == 'O'):
            print('Esse espaço está ocupado. Tente outro!')
            # SE TIVER DIGITA OUTRO NÚMERO
            Turn(player)
        else:
            # SE NÃO PREENCHE A POSIÇÃO
            board[n-1] = player

    # MINIMAX DA AI/PC
    def miniMax(current, depth, isMaximizing):
        rVal = 0
        newB = current[:]

        score = CheckWin(newB)

        if(depth == 0):
            if(score == 5):
                return 0

            return score
        
        if(score != 5):
            return score

        if(isMaximizing):
            minVal = -10
            for i in range(9):
                if(newB[i] != 'X' and newB[i] != 'O'):
                    newB[i] = 'X'
                    rVal = miniMax(newB, depth - 1, not isMaximizing)
                    if(rVal > minVal):
                        minVal = rVal
                    newB[i] = i + 1
            return minVal

        if(not isMaximizing):
            maxVal = 10
            for i in range(9):
                if(newB[i] != 'X' and newB[i] != 'O'):
                    newB[i] = 'O'
                    rVal = miniMax(newB, depth - 1, not isMaximizing)
                    if(rVal < maxVal):
                        maxVal = rVal
                    newB[i] = i + 1
            return maxVal


    # AI/PC Jogando
    def AITurn():
        newB = board[:]     #NOVO TABULEIRO

        winBox = 0          #INDEX DO TABULEIRO
        minVal = -10    

        print('Boa jogada, pensando...')
        for i in range(9):
            if(newB[i] != 'X' and newB[i] != 'O'):
                newB[i] = 'X'
                receivedVal = miniMax(newB, 6, False)

                if(receivedVal > minVal):
                    minVal = receivedVal
                    winBox = i
                newB[i] = i + 1

        board[winBox] = 'X'

    end = 5
    playerX = not playerTurn

    # ENQUANTO O JOGO NÃO ACABA, CHECA SE ALGUÉM GANHOU
    while end == 5:
        end = CheckWin(board)

        # IMPRIME O TABULEIRO
        PrintBoard()

        # QUANDO O JOGO ACABA, CHECA QUEM FOI QUEM GANHOU OU SE TERMINOU EMPATADO
        # SE O PLAYER GANAHR (MIN)
        if(end == -1):
            print("Parabéns! Jogador \'O\' ganhou")
        # SE A IA/PC GANHAR (MAX)
        elif(end == 1):
            print("Parabéns! Jogador \'X\' ganhou")
        # SE EMPATAR
        elif(end == 0):
            print("O jogo acabou em empate!")

        # VERIFICA DE QUEM É A VEZ DE JOGAR
        if(end == 5):
            if(playerX):
                AITurn()
            else:
                Turn('O')

            # MUDA O PLAYER
            playerX = not playerX

while True:
    TicTacToe()
    # PERGUNTA SE O JOGADOR QUER OUTRA RODADA
    inp = input("Jogar novamente? Y/N: ")
    # SE SIM JOGA NOVAMENTE
    if(inp.lower() == "y"):
        print("Vamos jogar novamente!\n")
    # SE NÃO, PARA O JOGO
    else:
        break