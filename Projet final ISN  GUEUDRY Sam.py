from tkinter import*
from random import*
from tkinter.font import Font


######################################################
                                #FONCTIONS
def Lancement0():
    try :
        Score = open("Score.txt","r")
        Caneva1.delete("debut")
        Caneva1.pack_forget()
        Lancement1()
    except FileNotFoundError:
        Score = open("Score.txt","w")
        Score.write("Sam \n0")
        Score.close()
        Caneva1.delete("debut")
        Caneva1.destroy()
        Lancement1()

def Lancement1():
    global t
    t=2
    global Pts
    Pts=1
    global SC
    SC=0
    global Croix
    Croix=0
    Lancement()

def Lancement():
    global X, cptrou,Trou
    X = False
    Trou=True
    cptrou =0
    global x1,y1,x2,y2
    x1 = 385
    y1 = 265
    x2 = 185
    y2 = 735
    global Croix
    global DEF
    DEF=True
    global decompte
    decompte=5
    global continu
    continu=True
    global Cpt
    Cpt = 200
    global T
    T=300
    for i in range (1000):
        x= randrange(0,1200)
        y= randrange(0,1000)
        #Etoiles
        Caneva.create_oval(x, y, x+5, y+5,fill= 'white',tag="Stars")
    #Trou Noir
    Caneva.create_oval(-x1, y1, x2, y2,fill= '#460063',tag="Trou")
    Caneva.create_oval(-x1+10, y1+10, x2-10, y2-10,fill= '#7500a6',tag="Trou")
    Caneva.create_oval(-x1+30, y1+35, x2-35, y2-35,fill= '#bcb6fc',tag="Trou")
    Caneva.create_oval(-x1+65, y1+60, x2-60, y2-60,fill= '#0c4070',tag="Trou")
    Caneva.create_oval(-x1+90, y1+90, x2-90, y2-90,fill= 'black',tag="Trou")
    #Zone Progression
    Caneva.create_rectangle(0,0,1200,50,fill="grey")
    Caneva.create_rectangle(100,17,1100,27,fill="black",tag="Prog")
    #Zone Croix
    Caneva.create_rectangle(1100,150,1200,750,fill="grey",tag="Err")
    #Croix
    Caneva.create_line(1125,200,1175,300,width=10,tag="Err")
    Caneva.create_line(1125,201,1175,299,width=7,fill="grey",tag="Croix")
    Caneva.create_line(1175,200,1125,300,width=10,tag="Err")
    Caneva.create_line(1175,201,1125,299,width=7,fill="grey",tag="Croix")
    #2 croix
    Caneva.create_line(1125,400,1175,500,width=10,tag="Err")
    Caneva.create_line(1125,401,1175,499,width=7,fill="grey",tag="Croix")
    Caneva.create_line(1175,400,1125,500,width=10,tag="Err")
    Caneva.create_line(1175,401,1125,499,width=7,fill="grey",tag="Croix")
    #3 croix
    Caneva.create_line(1125,600,1175,700,width=10,tag="Err")
    Caneva.create_line(1125,601,1175,699,width=7,fill="grey",tag="Croix")
    Caneva.create_line(1175,600,1125,700,width=10,tag="Err")
    Caneva.create_line(1175,601,1125,699,width=7,fill="grey",tag="Croix")
    Caneva.pack()
    if Croix==2 :
        Caneva.create_line(1125,401,1175,499,width=7,fill="red",tag="Croix")
        Caneva.create_line(1175,401,1125,499,width=7,fill="red",tag="Croix")
        Caneva.create_line(1125,201,1175,299,width=7,fill="red",tag="Croix")
        Caneva.create_line(1175,201,1125,299,width=7,fill="red",tag="Croix")
    
    if Croix==1 :    
        Caneva.create_line(1125,201,1175,299,width=7,fill="red",tag="Croix")
        Caneva.create_line(1175,201,1125,299,width=7,fill="red",tag="Croix")
    
    Decompte()
    ChangementTrou(x1,y1,x2,y2)
    
        
    menubar.destroy()
#Début = bouton Start debut
def Début():
    global DEB
    DEB=False
    Début2()
    
def Début2():
    global DEB
    global x,y
    if DEB==False:
        Starter= Button(text="START ?" ,activebackground="white", command=Lancement0)
        Start=Caneva1.create_window(x,y,window=Starter,tag="Button")
        TimDebut()
        
def TimDebut():
    global x,y,DEF
    if DEB==False:
        x = randrange(100,850)
        y = randrange(100,850)
        fenetre.after(1000,Début2)
        
######################
    #Début du jeu
        #Décompte
        
def Decompte():
    global DEF
    DEF=False
    global Croix
    Caneva.delete("Decompte")
    global decompte
    font = Font(family='Arial',size=T)
    Txt =Caneva.create_text(600,500,text=decompte,font=font,tag="Decompte",fill="white")
    decompte-=1
    TimeStart()

def TimeStart():
    global DEF
    global Croix
    global decompte
    if decompte > -1 :
        fenetre.after(1000,Decompte)
    else:
        DEF=True
        Caneva.delete("Decompte")
        RandomLettre()
        
########################
        
        #Trou Noir

def ChangementTrou(x1,y1,x2,y2):
    global Trou
    if Trou ==True :
        Caneva.delete("Trou")
        Caneva.create_oval(-x1, y1, x2, y2,fill= '#460063',tag="Trou")
        Caneva.create_oval(-x1+10, y1+10, x2-10, y2-10,fill= '#7500a6',tag="Trou")
        Caneva.create_oval(-x1+30, y1+35, x2-35, y2-35,fill= '#bcb6fc',tag="Trou")
        Caneva.create_oval(-x1+65, y1+60, x2-60, y2-60,fill= '#0c4070',tag="Trou")
        Caneva.create_oval(-x1+90, y1+90, x2-90, y2-90,fill= 'black',tag="Trou")
        Agrandir(x1,y1,x2,y2)
    else :
        Caneva.delete("Trou")

def Agrandir(x1,y1,x2,y2):
    global cptrou, X
    if X==False:
        if cptrou<20:
            x1-=1
            y1-=1
            x2+=1
            y2+=1
            cptrou+=1
            fenetre.after(50,ChangementTrou,x1,y1,x2,y2)
        else :
            Retrecir(x1,y1,x2,y2)
            X=True
    if X==True:
        Retrecir(x1,y1,x2,y2)

def Retrecir(x1,y1,x2,y2):
    global X, cptrou
    if X == True :
        if cptrou>0:        
            x1+=1
            y1+=1
            x2-=1
            y2-=1
            cptrou -=1
            fenetre.after(150,ChangementTrou,x1,y1,x2,y2)
        else:
            X=False
            ChangementTrou(x1,y1,x2,y2)
            
###########################
    #LES LETTRES
        #Déf des lettres
            
def RandomLettre():
    global continu
    continu=True
    global texte
    texte=chr(randrange(65,90))
    global T
    x = randrange(100,850)
    y = randrange(100,850)
    font = Font(family='Arial',size=T)
    Txt =Caneva.create_text(x,y,text=texte,font=font,tag="Text",fill="white")
    Timer(texte,x,y)

    #Changement des dimentions
    
def ChangementLettre(T,texte,x,y):
    global continu
    if(continu==True)and (T>10):
        font = Font(family='Arial',size=T)
        Caneva.delete("Text")
        Caneva.create_text(x,y,text=texte,font=font,tag="Text",fill="white")
        Timer(texte,x,y)
    else :
        Caneva.delete("Text")
        
def Timer(texte,x,y):
    global T
    global t
    global continu
    if(continu==True)and (T>10):
        T-=t
        fenetre.after(100,ChangementLettre,T,texte,x,y)
    if T<15:
        font = Font(family='Arial',size=100)
        Caneva.delete("Text")
        Caneva.create_text(600,500,text="DEFAITE",font=font,fill="white",tag="fin")
        continu=False
        Défaite()
        
##################################
    #CLAVIER
        #Interaction lettre clavier
def LettreConfirmé(event):
    global DEF
    global continu
    global Croix
    global texte
    global SC
    code = event.keycode
    if DEF==True:
        if (code==ord(texte)):
            Caneva.delete("Text")
            continu=False
            SC +=1
            Progression()
        else :
            if Croix==2 :
                Caneva.delete("Text")
                Caneva.create_line(1125,601,1175,699,width=7,fill="red",tag="Croix")
                Caneva.create_line(1175,601,1125,699,width=7,fill="red",tag="Croix")
                font = Font(family='Arial',size=100)
                Caneva.create_text(600,500,text="DEFAITE",font=font,fill="white",tag="fin")
                continu=False
                Défaite()
            if Croix==1 :    
                Caneva.create_line(1125,401,1175,499,width=7,fill="red",tag="Croix")
                Caneva.create_line(1175,401,1125,499,width=7,fill="red",tag="Croix")
                Croix+=1
            if Croix==0 :    
                Caneva.create_line(1125,201,1175,299,width=7,fill="red",tag="Croix")
                Caneva.create_line(1175,201,1125,299,width=7,fill="red",tag="Croix")
                Croix+=1

#######################################
            
def Progression():
    global Cpt
    global continu
    global DEF
    if Cpt<1100:  
        fenetre.after(100,RandomLettre)
        Caneva.create_rectangle(100,17,Cpt,27,fill="red",tag="Prog")
        Cpt += 150
    else:
        DEF=False
        continu=False
        Caneva.create_rectangle(100,17,Cpt,27,fill="red",tag="Prog")
        font = Font(family='Arial',size=100)
        Caneva.create_text(600,500,text="VICTOIRE",font=font,fill="white",tag="Vic")
        Starter= Button(text="Niveau Supérieur?" ,activebackground="white", command=Reset)
        Start=Caneva.create_window(600,400,window=Starter,tag="Vic")
        
########################################
        


    
def LvlSup():
    global t
    Caneva.delete("Lvl","Stars")
    t+=1
    Lancement()
    

def Reset():
    global Trou
    Trou=False
    global Pts
    Pts+=1
    Texte=["Lvl Sup :",Pts]
    Caneva.delete("Trou","Croix","Prog","Err","Vic")
    font = Font(family='Arial',size=100)
    Caneva.create_text(600,500,text=Texte,font=font,fill="white",tag="Lvl")
    fenetre.after(3000,LvlSup)
############################
    #Fin
    
def Défaite():
    global DEF
    DEF=False
    global Pts
    global SC
    Caneva.delete("Croix","Prog","Err","Vic")
    font = Font(family='Arial',size=25)
    Caneva.create_text(600,750,text="Entrer votre Nom ici:",fill="white",font=font,tag="fin")
    Name=Entry(fenetre)
    EntrerNom=Caneva.create_window(600,800,window=Name,tag="fin")
    Enter=Button(text="ENTER" ,activebackground="white", command=lambda: END(Name.get(),Pts,SC))
    Caneva.create_window(700,800,window=Enter,tag="fin")


def END(Prenom,Pts,SC):
    Caneva.delete("fin")
    font = Font(family='Arial',size=50)
    Caneva.create_text(600,500,text=Prenom,fill="white",font=font,tag="END")
    Caneva.create_text(600,600,text="Niveau :",fill="white",font=font,tag='END')
    Caneva.create_text(750,600,text=Pts,fill="white",font=font,tag='END')
    Caneva.create_text(600,700,text="Score :",fill="white",font=font,tag='END')
    Caneva.create_text(750,700,text=SC,fill="white",font=font,tag='END')
    ScoBut=Button(text="HighScore" ,activebackground="white", command=lambda :AffScore(Prenom))
    Caneva.create_window(800,800,window=ScoBut,tag='END')

def AffScore(Prenom):
    global Pts
    global SC
    Score = open("Score.txt","r")
    Nom=Score.readline()
    sc=Score.readline()
    Score.close()
    Caneva.delete("END")
    PointHi = float(sc)
    if (SC > PointHi):
        Score = open("Score.txt",'w')
        Score.write(Prenom)
        Score.write('\n')
        Score.write(str(SC))
        Score.close()
        Caneva.delete('END')
        font = Font(family='Arial',size=50)
        Caneva.create_text(600,400,text="HIGHSCORE:",fill="white",font=font,tag="end")
        Caneva.create_text(600,500,text=Prenom,fill="white",font=font,tag="end")
        Caneva.create_text(600,600,text="Niveau :",fill="white",font=font,tag="end")
        Caneva.create_text(750,600,text=Pts,fill="white",font=font,tag="end")
        Caneva.create_text(600,700,text="Score :",fill="white",font=font,tag='end')
        Caneva.create_text(750,700,text=SC,fill="white",font=font,tag='end')
        ScoBut=Button(text="Retry" ,activebackground="white", command=lambda :RESTART())
        Caneva.create_window(800,800,window=ScoBut,tag='end')

    else :
        font = Font(family='Arial',size=50)
        Caneva.create_text(600,400,text="HIGHSCORE:",fill="white",font=font,tag="end")
        Caneva.create_text(600,550,text= Nom ,fill="white",font=font,tag="end")
        Caneva.create_text(600,600,text="Score :",fill="white",font=font,tag="end")
        Caneva.create_text(750,600,text=sc,fill="white",font=font,tag="end")
        ScoBut=Button(text="Retry" ,activebackground="white", command=lambda :RESTART())
        Caneva.create_window(800,800,window=ScoBut,tag='end')
        
        
def RESTART():
    Caneva.delete("Trou","Croix","Prog","Err","Vic","end","Stars")
    Lancement1()
     
    
###################################################################################################
#La fenetre
    #Fenetre
    
fenetre = Tk()
fenetre.title('Isn GUEUDRY Mini-projet')
    #Le Canevas
Caneva=Canvas(fenetre,width=1200,height=1000,bg='black')

Caneva1=Canvas(fenetre,width=1200,height=1000,bg='black')
for i in range (1000):
    x= randrange(0,1200)
    y= randrange(0,1000)
        #Etoiles
    Caneva1.create_oval(x, y, x+5, y+5,fill= 'white',tag="debut")
    
Caneva1.create_oval(-285, 265, 285, 735,fill= '#460063',tag="debut")
Caneva1.create_oval(-275, 275, 275, 725,fill= '#7500a6',tag="debut")
Caneva1.create_oval(-250, 300, 250, 700,fill= '#bcb6fc',tag="debut")
Caneva1.create_oval(-225, 325, 225, 675,fill= '#0c4070',tag="debut")
Caneva1.create_oval(-175, 375, 175, 625,fill= 'black',tag="debut")
font = Font(family='Arial',size=50)
Caneva1.create_text(600,500,text="The Game :\nBlack Hall B !",fill="white",font=font)
Caneva1.pack()


#MENU
    #Menu
menubar = Menu(fenetre)
menu1 = Menu(menubar,tearoff=0)
menu1.add_command(label='commencer',command=Lancement1)
menubar.add_cascade(label='menu',menu=menu1)

    #Affichage sympa

Début()


#Fenetre Aff
fenetre.bind('<KeyRelease>',LettreConfirmé)
fenetre.config(menu=menubar)

fenetre.mainloop()









