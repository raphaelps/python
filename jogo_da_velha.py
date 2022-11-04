class JogoDaVelha:
    tabuleiro = {'7': ' ', '8': ' ', '9': ' ',
                 '4': ' ', '5': ' ', '6': ' ',
                 '1': ' ', '2': ' ', '3': ' '}

    turno = None

    def __init__(self, Jogador_inicial="X"):
        self.turno = Jogador_inicial

    # método para exibir o tabuleiro
    def exibirTabuleiro(self):
        print("┌───┬───┬───┐")
        print(
            f"│ {self.tabuleiro['7']} │ {self.tabuleiro['8']} │ {self.tabuleiro['9']} │")
        print("├───┼───┼───┤")
        print(
            f"│ {self.tabuleiro['4']} │ {self.tabuleiro['5']} │ {self.tabuleiro['6']} │")
        print("├───┼───┼───┤")
        print(
            f"│ {self.tabuleiro['1']} │ {self.tabuleiro['2']} │ {self.tabuleiro['3']} │")
        print("└───┴───┴───┘")

    # método para verificar se a jogada é válida
    def verificarJogada(self, jogada):
        if jogada in self.tabuleiro.keys():
            if self.tabuleiro[jogada] == " ":
                return True
        return False

    # Método que irá verificar o estado do tabuleiro,
    # se já temos um vencedor ou se podemos declarar um empate
    def verificarTabuleiro(self):
        # Verificações das 3 verticais
        if self.tabuleiro['7'] == self.tabuleiro['4'] == self.tabuleiro['1'] != ' ':
            return self.tabuleiro['7']
        elif self.tabuleiro['8'] == self.tabuleiro['5'] == self.tabuleiro['2'] != ' ':
            return self.tabuleiro['8']
        elif self.tabuleiro['9'] == self.tabuleiro['6'] == self.tabuleiro['3'] != ' ':
            return self.tabuleiro['9']

        # Verificações das 3 horizontais
        elif self.tabuleiro['7'] == self.tabuleiro['8'] == self.tabuleiro['9'] != ' ':
            return self.tabuleiro['7']
        elif self.tabuleiro['4'] == self.tabuleiro['5'] == self.tabuleiro['6'] != ' ':
            return self.tabuleiro['8']
        elif self.tabuleiro['1'] == self.tabuleiro['2'] == self.tabuleiro['3'] != ' ':
            return self.tabuleiro['1']

        # Verificações das 2 diagonais
        elif self.tabuleiro['7'] == self.tabuleiro['5'] == self.tabuleiro['3'] != ' ':
            return self.tabuleiro['7']
        elif self.tabuleiro['1'] == self.tabuleiro['5'] == self.tabuleiro['9'] != ' ':
            return self.tabuleiro['1']

        # Verificando empate
        if [*self.tabuleiro.values()].count(' ') == 0:
            return "empate"
        else:
            return [*self.tabuleiro.values()].count(' ')

    def jogar(self):

        while True:
            self.exibirTabuleiro()

            print(f"Turno do {self.turno}, qual sua jogada?")

            # Enquanto o jogador não fizer uma jogada valida
            while True:
                jogada = input("Jogada: ")

                if self.verificarJogada(jogada):
                    break
                else:
                    print(f"Jogada do {self.turno} invalida, jogue novamente.")

            self.tabuleiro[jogada] = self.turno

            estado = self.verificarTabuleiro()

            if estado == "X":
                print("X é o Vencedor!!!")
                break
            elif estado == "O":
                print("O é o Vencedor!!!")
                break

            if estado == "empate":
                print("Empatou!!!")
                break

            # troca o jogador do proximo turno
            self.turno = "X" if self.turno == "O" else "O"

        self.exibirTabuleiro()


jogo = JogoDaVelha()

jogo.jogar()
