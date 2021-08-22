from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
import mysql.connector
from kivymd.app import MDApp

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
        livre_pc.append(livre)
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
    data_info = [{"isbn": "1", "name": "info1", "categorie": "info","Disponible":"oui"},
                 {"isbn": "2", "name": "info2", "categorie": "info","Disponible":"oui"},
                 {"isbn": "3", "name": "info3", "categorie": "info","Disponible":"oui"}]
    name_info = ["info","Info","informatique","Informatique"]
    def pc_button(self):
        #self.ids.loll.cols=5
        for i in range(len(livre_pc)):
            aff_tab=self.ids.scr_phy
            details = BoxLayout(size_hint_y=None, height=30, pos_hint={"top": 1})
            aff_tab.add_widget(details)
            ISBN = Label(text=str(livre_pc[i][1]), size_hint_x=.1, color=(0, 0, 0, 1))
            Titre = Label(text=str(livre_pc[i][2]), size_hint_x=.1, color=(0, 0, 0, 1))
            Categorie = Label(text=str(livre_pc[i][0]), size_hint_x=.1, color=(0, 0, 0, 1))
            Disponible = Label(text=str(livre_pc[i][4]), size_hint_x=.1, color=(0, 0, 0, 1))
            details.add_widget(ISBN)
            details.add_widget(Titre)
            details.add_widget(Categorie)
            details.add_widget(Disponible)
    def informatique(self,widjet):
            self.info=1
           # self.table()
            aff_lol=self.ids.aff
            for i in range(len(self.data_info)):
                details = BoxLayout(size_hint_y=None, height=30, pos_hint={"top": 1})
                aff_lol.add_widget(details)
                isbn = Label(text=self.data_info[i]["isbn"], size_hint_x=.15, color=(0, 0, 0, 1))
                titre = Label(text=self.data_info[i]["name"], size_hint_x=.4, color=(0, 0, 0, 1))
                Categorie = Label(text=self.data_info[i]["categorie"], size_hint_x=.2, color=(0, 0, 0, 1))
                Disponible = Label(text=self.data_info[i]["Disponible"], size_hint_x=.25, color=(0, 0, 0, 1))
                details.add_widget(isbn)
                details.add_widget(titre)
                details.add_widget(Categorie)
                details.add_widget(Disponible)
    def change_screen(self,instance):
        if instance.text=='Informatique':
            self.ids.scr_mng.current = 'scr_info'
        elif instance.text=='Mathématique':
            self.ids.scr_mng.current = 'scr_math'
        elif instance.text=="Physique, Chimie":
            self.ids.scr_mng.current = 'scr_phy'
        elif instance.text=="Biologie, Géologie":
            self.ids.scr_mng.current = 'scr_bio'
        elif instance.text=="Autre":
            self.ids.scr_mng.current = 'scr_autre'


    def chercher(self,widjet):
        book=self.ids.book_name.text
        if  book in self.name_info:
            if self.info==0:
                self.info=1
                self.informatique(widjet)
class Profil(Screen):
    pass
class Paswdmodif(Screen):
    pass
class MyGrid(Screen):
    pass
class WindowManager(ScreenManager):
    pass
kv = Builder.load_file('My.kv')
class Myapp(MDApp):
    def build(self):
        self.title="Bib"
        return kv
if __name__=='__main__':
    Myapp().run()