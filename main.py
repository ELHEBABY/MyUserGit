from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
import mysql.connector

mydb=mysql.connector.connect(
    host="b8fe7neoqvypvqfx1i0y-mysql.services.clever-cloud.com",
    user="u40lrquglsqtnfln",
    passwd="eNb3mamLpTzPN4JZBwYS",
    database="b8fe7neoqvypvqfx1i0y")
mycurser=mydb.cursor()
#mycurser.execute("CREATE TABLE IF NOT EXISTS User(firs_name varchar(255),last_name varchar(255))")
mycurser.execute("SELECT * FROM User")
#row=mycurser.fetchone()
users=[]
for x in mycurser:
    user = []
    user.append(x[0])
    user.append(x[1])
    users.append(user)
mycurser.execute("SELECT * FROM Admin")
admins=[]
for x in mycurser:
    admin = []
    admin.append(x[0])
    admin.append(x[1])
    admins.append(admin)
mycurser.execute("SELECT * FROM Livres")
livres=[]
for x in mycurser:
    livre=[]
    livre.append(x[0])
    livre.append(x[1])
    livre.append(x[2])
    livre.append(x[3])
    livre.append(x[4])
    livres.append(livre)
print(livres)
livre_math=[]
livre_pc=[]
livre_info=[]
livre_bio=[]
livre_aut=[]
for x in livres:
    livre=[]
    livre.append(x[0])
    livre.append(x[1])
    livre.append(x[2])
    livre.append(x[3])
    livre.append(x[4])
    if livre[0]=='Info':
        livre_info.append(livre)
    elif livre[0]=="Math":
        livre_math.append(livre)
    elif livre[0]=="pc":
        for c in range(10):
            livre_pc.append(livre)
            c+=1
    elif livre[0]=="bio":
        livre_bio.append(livre)
    elif livre[0]=="aut":
        livre_aut.append(livre)
print(livres)
print(livre_pc)
print(livre_info)
print(livre_math)
print(livre_aut)
print(livre_bio)
liste_recherch_info=['Informatique','informatique','info']
liste_recherch_math=['Maths','Math','maths','math','Mathématique','mathématique']
liste_recherch_pc=['pc','Pc','physique','Phyqique','Physique, Chimie']
liste_recherch_bio=['Biologie, Géologie','Bio','bio','biologie','Biologie','géologie','Géologie','geologie','Geologie']
class Accueil(Screen):
    def signin(self):
        a = 0
        for x in users:
            if x[0] == self.ids.first.text and x[1] == self.ids.second.text:
                self.ids.first.text=""
                self.ids.second.text=""
                a = 1
                break
        for x in admins:
            if x[0] == self.ids.first.text and x[1] == self.ids.second.text:
                self.ids.first.text=""
                self.ids.second.text=""
                a = 2
                break
        return a
        #if self.password()!="123":
         #   self.ids.erreur.text="erreur"
class User(Screen):
    info=0
    math=0
    phy=0
    bio=0
    autr=0
    def __init__(self,table='', **kwargs):
        super().__init__(**kwargs)

    def table(self):
        aff_tab=self.ids.afftable
        details = BoxLayout(size_hint_y=None, height=30, pos_hint={"top": 1})
        aff_tab.add_widget(details)
        ISBN = Label(text='ISBN', size_hint_x=.1, color=(0, 0, 0, 1))
        Titre = Label(text='Titre', size_hint_x=.1, color=(0, 0, 0, 1))
        Categorie = Label(text='Categorie', size_hint_x=.1, color=(0, 0, 0, 1))
        Disponible = Label(text='Disponible', size_hint_x=.1, color=(0, 0, 0, 1))
        details.add_widget(ISBN)
        details.add_widget(Titre)
        details.add_widget(Categorie)
        details.add_widget(Disponible)

    def table(self,listt,table_floor_layout,table_floor):
        self.columns = 4
        table_data = []
        titrr = ['ISBN', 'Titre', 'Auteur', 'Desponile']
        for y in range(4):
            table_data.append({'text': titrr[y], 'size_hint_y': None, 'height': 30,
                               'bcolor': (.05, .30, .80, 1)})  # append the data
            y = y + 1

        for z in range(len(listt)):
            for y in range(4):
                table_data.append({'text': str(listt[z][y + 1]), 'size_hint_y': None, 'height': 20,
                                   'bcolor': (.06, .25, .50, 1)})  # append the data

        table_floor_layout.cols = self.columns  # define value of cols to the value of self.columns
        table_floor.data = table_data  # add table_data to data value

    def test_titre(self,titre):
        a=0
        if titre in liste_recherch_info :
            self.ids.scr_mng.current = 'scr_info'
            livre_diff = livre_info
            table_floor_layout=self.ids.table_floor_layout_info
            table_floor=self.ids.table_floor_info
            a=1
        elif titre in liste_recherch_math:
            self.ids.scr_mng.current = 'scr_math'
            livre_diff = livre_math
            table_floor_layout = self.ids.table_floor_layout_math
            table_floor = self.ids.table_floor_math
            a=2
        elif titre in liste_recherch_pc:
            self.ids.scr_mng.current = 'scr_phy'
            livre_diff=livre_pc
            table_floor_layout=self.ids.table_floor_layout_pc
            table_floor = self.ids.table_floor_pc
            a=3
        elif titre in liste_recherch_bio:
            self.ids.scr_mng.current = 'scr_bio'
            livre_diff = livre_bio
            table_floor_layout = self.ids.table_floor_layout_bio
            table_floor = self.ids.table_floor_bio
            a=4
        elif titre == "Autre":
            self.ids.scr_mng.current = 'scr_autre'
            livre_diff = livre_aut
            table_floor_layout = self.ids.table_floor_layout_autre
            table_floor = self.ids.table_floor_autre
            a=5
        else:
            self.ids.scr_mng.current = 'scr'
        if self.ids.scr_mng.current != 'scr':
            self.table(livre_diff,table_floor_layout,table_floor)
        return a

    def recherche(self):
        book=self.ids.book_name.text
        a=self.test_titre(book)
        if a==0 and book != '':
            b = 0
            self.ids.mathematique.state="normal"
            self.ids.info.state="normal"
            self.ids.pc.state="normal"
            self.ids.bio.state="normal"
            self.ids.autre.state="normal"
            table_floor_layout= self.ids.table_floor_layout_rech
            table_floor= self.ids.table_floor_rech
            livre_choix = []
            for x in livres:
                if book==str(x[2]):
                    livre_choix.append(x)
                    b=1
            if b==0 :
                for x in livres:
                    if book==str(x[1]):
                        livre_choix.append(x)
                        b=1
            if b==0 :
                for x in livres:
                    if book==str(x[3]):
                        livre_choix.append(x)
                        b=1
            if b==1:
                self.ids.scr_mng.current = 'scr_rech'
                self.table(livre_choix, table_floor_layout, table_floor)
        elif a==1:
            self.ids.mathematique.state="normal"
            self.ids.pc.state="normal"
            self.ids.bio.state="normal"
            self.ids.autre.state="normal"
            self.test_titre(book)
        elif a==2:
            self.ids.mathematique.state="down"
            self.ids.info.state="normal"
            self.ids.pc.state="normal"
            self.ids.bio.state="normal"
            self.ids.autre.state="normal"
            self.test_titre(book)
        elif a==3:
            self.ids.mathematique.state="normal"
            self.ids.info.state="normal"
            self.ids.bio.state="normal"
            self.ids.pc.state="down"
            self.ids.autre.state="normal"
            self.test_titre(book)
        elif a==4:
            self.ids.mathematique.state="normal"
            self.ids.info.state="normal"
            self.ids.pc.state="normal"
            self.ids.bio.state="down"
            self.ids.autre.state="normal"
            self.test_titre(book)
        elif a==5:
            self.ids.mathematique.state="normal"
            self.ids.info.state="normal"
            self.ids.pc.state="normal"
            self.ids.bio.state="normal"
            self.ids.autre.state="down"
            self.test_titre(book)

    def test(self,instance):
        if instance.state == "down":
            self.test_titre(instance.text)
        else:
            self.ids.scr_mng.current = 'scr'

class Profil(Screen):
    pass
class Paswdmodif(Screen):
    pass
class MyGrid(Screen):
    pass
class Secondwindow(Screen):
    pass
class ThirdWindow(Screen):
    pass
class WindowManager(ScreenManager):
    pass
kv = Builder.load_file('My.kv')
class Myapp(App):
    def build(self):
        self.title="Bib"
        return kv
if __name__=='__main__':
    Myapp().run()

mydb.close()
