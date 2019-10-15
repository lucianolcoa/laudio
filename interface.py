from tkinter import*
import os
class programa():
    def __init__(self,master=None):
        self.janela=Tk()
        self.janela1=Frame(master)
        self.janela1.pack()
        self.janela2=Frame(master)
        self.janela2.pack()
        self.janela3=Frame(master)
        self.janela3.pack()
        self.janela4=Frame(master)
        self.janela4.pack()
        self.janela5=Frame(master)
        self.janela5.pack()
        self.janela6=Frame(master)
        self.janela6.pack()
        self.label= Label(self.janela1,background="white",
                          foreground="black",text="Distorcedor e limpador de voz",font="Arial 24")
        self.label.pack() 
        self.label1= Label(self.janela2,background="white",
                          foreground="black",text="Coloque embaixo os campos de distorção ,duração e suavização da voz",font="Arial 14")
        self.label1.pack() 
        self.label2= Label(self.janela2,background="white",
                          foreground="black",text="duração",font="Arial 14")
        self.label2.pack(side=LEFT)
        self.duracao= Entry(self.janela2,background="white",
                          foreground="black",font="Arial 14")
        self.duracao.pack(side=LEFT)
        self.label3= Label(self.janela3,background="white",
                          foreground="black",text="corte baixa frequência",font="Arial 14")
        self.label3.pack(side=LEFT)
        self.baixaf= Entry(self.janela3,background="white",foreground="black",font="Arial 14")
        self.baixaf.pack(side=LEFT)
        self.label4= Label(self.janela4,background="white",
                          foreground="black",text="corte alta frequência",font="Arial 14")
        self.label4.pack(side=LEFT)
        self.altaf= Entry(self.janela4,background="white",
                          foreground="black",text="duração",font="Arial 14")
        self.altaf.pack(side=LEFT)
        self.label5= Label(self.janela5,background="white",
                          foreground="black",font="Arial 14",text="distorção")
        self.label5.pack(side=LEFT)
        self.distorcao= Entry(self.janela5,background="white",
                          foreground="black",font="Arial 14")
        self.distorcao.pack(side=LEFT)
        self.botao= Button(self.janela6,background="blue",foreground="white",text="ENTER",font="Arial 16",
                           command=self.iniciar)
        self.botao.pack(side=LEFT)
        self.botao1= Button(self.janela6,background="blue",foreground="white",text="ultimo valor",font="Arial 16",
                           command=self.iniciar1)
        self.botao1.pack(side=LEFT)
        
        self.janela.mainloop()
    def iniciar1(self):
        os.system("python3 audio.py")
        
    def iniciar(self):
        #self.label5.configure(text="foi")
        dados1=[]
        dados1.append(self.duracao.get())
        dados1.append(",")
        dados1.append(self.baixaf.get())
        dados1.append(",")
        dados1.append(self.altaf.get())
        dados1.append(",")
        dados1.append(self.distorcao.get())
        dados=open("dados.txt","w+")
        dados1=str(dados1)
        dados1=dados1.replace("'","")
        dados1=dados1.replace("[","")
        dados1=dados1.replace("]","")
        dados1=dados1.replace(",,","")
        dados.write(dados1)
        
        dados.close()
        os.system("python3 audio.py")
app= programa()
