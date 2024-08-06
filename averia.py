#creado por marito
#en la fecha x
#clase para atributos de tipo persona
import sqlite3
from pydantic import BaseModel
class Averia(BaseModel):
    identificador : str
    nombre : str

    def nueva(self, identificador,nombre):
        self.identificador = identificador
        self.nombre= nombre
    def guardaenBD(self):
        con = sqlite3.connect('tallerMecanico.db')
        cur = con.cursor()
        sql = f'''INSERT INTO Averia(identificador,nombre) VALUES (
        '{self.identificador}', 
        '{self.nombre}')'''
        cur.execute(sql)
        con.commit()
        con.close()
    def eliminaenBD(self):
        con = sqlite3.connect('tallerMecanico.db')
        cur = con.cursor()
        sql = f'''DELETE FROM Averia WHERE identificador = {self.identificador}'''
        cur.execute(sql)
        con.commit()
        con.close()
    def actualizaenBD(self):
        con = sqlite3.connect('tallerMecanico.db')
        cur = con.cursor()
        sql = f'''UPDATE Averia SET nombre= 
        {self.nombre}  where identificador = {self.identificador}'''
        cur.execute(sql)
        con.commit()
        con.close()
    def seleccionatodoenBD(self):
        con = sqlite3.connect('tallerMecanico.db')
        cur = con.cursor()
        listaDevolver=[]
        for fila in cur.execute('SELECT * FROM Averia'):
            objetoInterno = Averia(identificador= fila[0], 
                                    nombre = fila[1])
            listaDevolver.append(objetoInterno)
        return listaDevolver
   
        