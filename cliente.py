#creado por marito
#en la fecha x
#clase para atributos de tipo persona
import sqlite3
from pydantic import BaseModel
class Cliente(BaseModel):
    cedula : str
    tipo : str

    def nueva(self, cedula,tipo):
        self.cedula = cedula
        self.tipo= tipo
    def guardaenBD(self):
        con = sqlite3.connect('tallerMecanico.db')
        cur = con.cursor()
        sql = f'''INSERT INTO Cliente(cedula,tipo) VALUES (
        '{self.cedula}', 
        '{self.tipo}')'''
        cur.execute(sql)
        con.commit()
        con.close()
    def eliminaenBD(self):
        con = sqlite3.connect('tallerMecanico.db')
        cur = con.cursor()
        sql = f'''DELETE FROM Cliente WHERE cedula = {self.cedula}'''
        cur.execute(sql)
        con.commit()
        con.close()
    def actualizaenBD(self):
        con = sqlite3.connect('tallerMecanico.db')
        cur = con.cursor()
        sql = f'''UPDATE Cliente SET tipo= 
        {self.tipo} , apellidos=
        {self.telefono} where cedula = {self.cedula}'''
        cur.execute(sql)
        con.commit()
        con.close()
    def seleccionatodoenBD(self):
        con = sqlite3.connect('tallerMecanico.db')
        cur = con.cursor()
        listaDevolver=[]
        for fila in cur.execute('SELECT * FROM Cliente'):
            objetoInterno = Cliente(cedula= fila[0], 
                                    tipo = fila[1])
            listaDevolver.append(objetoInterno)
        return listaDevolver
   