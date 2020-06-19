"""

Nome: Vitor Santos Pereira
Matrícula: 201510170911
24/12/2018

"""

from tkinter import*
from tkinter import messagebox
tela = Tk()

tela["bg"] = ("#6A5ACD")

def muda_cor_blue():
    tela["bg"] = "#191970"
    titulo["bg"] = "#191970"
    dicas["bg"] = "#191970"
    dicas2["bg"] = "#191970"
    botao["fg"] = "#191970"
    slider1["fg"] = "#191970"
    text1["bg"] = "#191970"
def muda_cor_purple():
    tela["bg"] = "purple"
    titulo["bg"] = "purple"
    dicas["bg"] = "purple"
    dicas2["bg"] = "purple"
    botao["fg"] = "purple"
    slider1["fg"] = "purple"
    text1["bg"] = "purple"
def muda_cor_green():
    tela["bg"] = "#66CDAA"
    titulo["bg"] = "#66CDAA"
    dicas["bg"] = "#66CDAA"
    dicas2["bg"] = "#66CDAA"
    botao["fg"] = "#66CDAA"
    slider1["fg"] = "#66CDAA"
    text1["bg"] = "#66CDAA"
def muda_cor_pink():
    tela["bg"] = "#BC8F8F"
    titulo["bg"] = "#BC8F8F"
    dicas["bg"] = "#BC8F8F"
    dicas2["bg"] = "#BC8F8F"
    botao["fg"] = "#BC8F8F"
    slider1["fg"] = "#BC8F8F"
    text1["bg"] = "#BC8F8F"
def muda_cor_black():
    tela["bg"] = "#D2B48C"
    titulo["bg"] = "#D2B48C"
    dicas["bg"] = "#D2B48C"
    dicas2["bg"] = "#D2B48C"
    botao["fg"] = "#D2B48C"
    slider1["fg"] = "#D2B48C"
    text1["bg"] = "#D2B48C"
def muda_cor_choc():
    tela["bg"] = "#D2691E"
    titulo["bg"] = "#D2691E"
    dicas["bg"] = "#D2691E"
    dicas2["bg"] = "#D2691E"
    botao["fg"] = "#D2691E"
    slider1["fg"] = "#D2691E"
    text1["bg"] = "#D2691E"
def muda_cor_sky():
    tela["bg"] = "#87CEFA"
    titulo["bg"] = "#87CEFA"
    dicas["bg"] = "#87CEFA"
    dicas2["bg"] = "#87CEFA"
    botao["fg"] = "#87CEFA"
    slider1["fg"] = "#87CEFA"
    text1["bg"] = "#87CEFA"
def muda_cor_skyfall():
    tela["bg"] = "#6A5ACD"
    titulo["bg"] = "#6A5ACD"
    dicas["bg"] = "#6A5ACD"
    dicas2["bg"] = "#6A5ACD"
    botao["fg"] = "#6A5ACD"
    slider1["fg"] = "#6A5ACD"
    text1["bg"] = "#6A5ACD"


titulo = Label(tela , text = "GUESS GAME!!!", font = ("Showcard Gothic", 25, "bold"), bg = "#6A5ACD", fg = "white")
titulo.place(x = 300, y = 80)


cor1 = Button (tela, text= "", command = muda_cor_blue, bg = "#191970", padx = 30)
cor1.grid(row = 0, column = 0)

cor2 = Button (tela, text= "", command = muda_cor_purple, bg = "purple", padx = 30)
cor2.grid(row = 0, column = 1)

cor3 = Button (tela, text= "", command = muda_cor_green, bg = "#66CDAA", padx = 30)
cor3.grid(row = 0, column = 2)

cor4 = Button (tela, text= "", command = muda_cor_pink, bg = "#BC8F8F", padx = 30)
cor4.grid(row = 0, column = 3)

cor5 = Button (tela, text= "", command = muda_cor_black, bg = "#D2B48C", padx = 30)
cor5.grid(row = 0, column = 4)

cor6 = Button (tela, text= "", command = muda_cor_choc, bg = "#D2691E", padx = 30)
cor6.grid(row = 0, column = 5)

cor7 = Button (tela, text= "", command = muda_cor_sky, bg = "#87CEFA", padx = 30)
cor7.grid(row = 0, column = 6)

cor8 = Button (tela, text= "", command = muda_cor_skyfall, bg = "#6A5ACD", padx = 30)
cor8.grid(row = 0, column = 7)

slider1 = Entry(tela,   fg = "#6A5ACD", bg = "white",font = ("Showcard Gothic", 15, "bold"))
slider1.place(x = 295, y = 180)

dicas = Label(tela, text = "DICA:", fg = "white", bg = "#6A5ACD", font = ("Showcard Gothic", 15, "bold"))
dicas.place(x = 100, y = 250)

dicas2 = Label(tela,text = "",font = ("Showcard Gothic", 15, "bold italic"), fg = "white", bg = "#6A5ACD")
dicas2.place(x= 180, y =250)

text1 = Label(tela, text = "JOGO:   Escolha um número entre 1 e 100 para \ntentar acertar o número \nque foi escolhido aleatoriamente pelo jogo.\nParece ser difícil, mas relaxe que as dicas vão te ajudar\n com isso.",font = ("Showcard Gothic", 15, "bold"), bg = "#6A5ACD", fg = 'white')
text1.place(x = 80, y = 400)

import random

i = 0
y = random.randint(1, 100)
array = []
k = 0

FV, MQ, QT, MO, FR, MF, CG = 0, 0, 0, 0, 0, 0, 0

def cond():
    global i, y, x
    global FV, MQ, QT, MO, FR, MF, CG

    if x != y:
        i += 1

        if i != 11:

            if i == 9:
                print("Última chance!")

            if i == 10:
                print("A resposta era", y)
                messagebox.showwarning("Perdeu", "Acabaram as chances, você perdeu ¯\_(ツ)_/¯, a resposta era " + str(y) + "!")
                tela.quit()

            if abs(x - y) < 2:  # Condição Fervendo(FV)
                FV += 1

                if FV == 1:
                    if CG != 0:
                        dicas2["text"] = ("Quase acertou na mosca! Está vervendo!")
                    elif MF != 0:
                        dicas2["text"] =("Esquentou muito e está fervendo!!!")
                    elif FR != 0:
                        dicas2["text"] =("Esquentou  demais e está fervendo!!!!")
                    elif MO != 0:
                        dicas2["text"] =("Esquentou muuuito e está fervendo!!")
                    elif QT != 0:
                        dicas2["text"] =("Nossa quase acertou!! Está fervendo")
                    elif MQ != 0:
                        dicas2["text"] =("Deu uma esquentada boa, está fervendo!")

                    else:
                        dicas2["text"] =("FERVENDOO!!")
                    MQ, QT, MO, FR, MF, CG = 0, 0, 0, 0, 0, 0
                else:
                    dicas2["text"] =("CONTINUA FERVENDO, TA QUASE!!")

            if 2 <= abs(x - y) < 7:  # Condição Muito Quente (MQ)
                MQ += 1

                if MQ == 1:
                    if CG != 0:
                        dicas2["text"] =("Agora deu uma esquentada boa e está muito quente!!!")
                    elif MF != 0:
                        dicas2["text"] =("Deu uma boa esquentada, e está muito quente!!! ")
                    elif FR != 0:
                        dicas2["text"] =("Esquentou bem agora!! Está muito quente!")
                    elif MO != 0:
                        dicas2["text"] =("Esquentou e agora está muito quente!!")
                    elif QT != 0:
                        dicas2["text"] =("Agora ficou muuito quente!!")
                    elif FV != 0:
                        dicas2["text"] =("Deu uma pequena esfriada, mas está muito quente!!!")

                    else:
                        dicas2["text"] =("TA MUITO QUENTE!")
                    FV, QT, MO, FR, MF, CG = 0, 0, 0, 0, 0, 0

                else:
                    dicas2["text"] =("CONTINUA MUITO QUENTE!!")

            if 7 <= abs(x - y) < 12:  # Condição Quente (QT)
                QT += 1

                if QT == 1:
                    if CG != 0:
                        dicas2["text"] =("Esquentou!!!")
                    elif MF != 0:
                        dicas2["text"] =("Deu uma boa esquentada!!")
                    elif FR != 0:
                        dicas2["text"] =("Esquentou bem!")
                    elif MO != 0:
                        dicas2["text"] =("Ficou mais quente!!")
                    elif MQ != 0:
                        dicas2["text"] =("Deu uma esfriada, mas está quente!")
                    elif FV != 0:
                        dicas2["text"] =("Esfriou!!")

                    else:
                        dicas2["text"] =("TA QUENTE!!")
                    FV, MQ, MO, FR, MF, CG = 0, 0, 0, 0, 0, 0
                else:
                    dicas2["text"] =("CONTINUA QUENTE!!")

            if 12 <= abs(x - y) < 18:  # Condição Morno (MO)
                MO += 1

                if MO == 1:
                    if CG != 0:
                        dicas2["text"] =("Esquentou e ficou morno...")
                    elif MF != 0:
                        dicas2["text"] =("Esquentou um pouco, está morno!")
                    elif FR != 0:
                        dicas2["text"] =("Esquentou, mas está morno...")
                    elif QT != 0:
                        dicas2["text"] =("Deu uma esfriada, mas está morno.")
                    elif MQ != 0:
                        dicas2["text"] =("Esfriou...")
                    elif FV != 0:
                        dicas2["text"] =("Esfriou!!")

                    else:
                        dicas2["text"] =("TA MORNO!!")
                    FV, MQ, QT, FR, MF, CG = 0, 0, 0, 0, 0, 0
                else:
                    dicas2["text"] =("CONTINUA MORNO!!")

            if 18 <= abs(x - y) < 25:  # Condição Frio (FR)
                FR += 1

                if FR == 1:
                    if CG != 0:
                        dicas2["text"] =("Deu uma pequena esquentada, mas ainda está frio...")
                    elif MF != 0:
                        dicas2["text"] =("Esquentou um pouco, mas ainda está frio...")
                    elif MO != 0:
                        dicas2["text"] =("Esfriou...")
                    elif MQ != 0:
                        dicas2["text"] =("Esfriou o palpite!")
                    elif QT != 0:
                        dicas2["text"] =("Esfriou!!")
                    elif FV != 0:
                        dicas2["text"] =("Ta frio demais!")

                    else:
                        dicas2["text"] =("TA FRIO!!")
                    FV, MQ, QT, MO, MF, CG = 0, 0, 0, 0, 0, 0
                else:
                    dicas2["text"] =("CONTINUA FRIO!!")

            if 25 <= abs(x - y) < 50:  # Condição Muito Frio (MF)
                MF += 1

                if MF == 1:
                    if CG != 0:
                        dicas2["text"] =("Esquentou só um pouco, está muito frio...")
                    elif FR != 0:
                        dicas2["text"] =("Deu uma esquentada, mas está muito frio!")
                    elif MO != 0:
                        dicas2["text"] =("Esfriou...")
                    elif MQ != 0:
                        dicas2["text"] =("Esfriou muuito!")
                    elif QT != 0:
                        dicas2["text"] =("Esfriou muito o palpite!")
                    elif FV != 0:
                        dicas2["text"] =("Agora ficou muito frio!")

                    else:
                        dicas2["text"] =("Ta muito frio!!")
                    FV, MQ, QT, MO, FR, CG = 0, 0, 0, 0, 0, 0
                else:
                    dicas2["text"] =("Continua muito frio!!")

            if abs(x - y) >= 50:  # Condição Congelando(CG)
                CG += 1

                if CG == 1:
                    if MF != 0:
                        dicas2["text"] =("Esfriou mais e está congelando!")
                    elif FR != 0:
                        dicas2["text"] =("Congelando..")
                    elif MO != 0:
                        dicas2["text"] =("Congelou muito!")
                    elif MQ != 0:
                        dicas2["text"] =("Esfriou muito e está congelando...")
                    elif QT != 0:
                        dicas2["text"] =("Congelando de tão longe...")
                    elif FV != 0:
                        dicas2["text"] =("Estava quase acertando, agora está longe!")

                    else:
                        dicas2["text"] =("TA CONGELANDO DE TÃO LONGE")
                    FV, MQ, QT, MO, FR, MF = 0, 0, 0, 0, 0, 0
                else:
                    dicas2["text"] =("CONTINUA CONGELANDO, CHUTA PRO OUTRO LADO")

    else:
        messagebox.showinfo("Mensagem", "Acertou!!!")
        tela.quit()

def game():
    global x, array

    x = int(slider1.get())

    if x != y:

        if i < 10:

            if x in list(range(1, 101)):
                if x in array:

                    messagebox.showinfo("Mensagem", "Não digite o mesmo número!")

                else:
                    array.append(x)
                    # print(array)
                    cond()

            else:
                messagebox.showwarning("Warning!", "Digite um número entre 1 e 100!!")

        else:
            messagebox.showwarning("Perdeu", "Acabaram as chances, você perdeu ¯\_(ツ)_/¯, a reposta era " + str(y) + "!")
            tela.quit()
    else:
        messagebox.showinfo("Mensagem", "Acertou!!!")
        tela.quit()

botao = Button (tela, text = "C H U T E", padx = 35, pady = 5, font = ("Showcard Gothic", 10, "bold"), fg = "#6A5ACD", command = game)
botao.place(x = 350, y= 300)

tela.title("GUESS GAME")

tela.geometry("850x600")

tela.resizable(width = False, height = False)

tela.mainloop()



