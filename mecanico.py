#creado por marito
#en la fecha x
#clase para atributos de tipo persona
import sqlite3
from pydantic import BaseModel
class Mecanico(BaseModel):
    cedula : str
    especialidad : str
    salarioxHora : int
    def nueva(self, cedula,especialidad,salarioxHora):
        self.cedula = cedula
        self.especialidad= especialidad
        self.salarioxHora= salarioxHora
    def guardaenBD(self):
        con = sqlite3.connect('tallerMecanico.db')
        cur = con.cursor()
        sql = f'''INSERT INTO Mecanico(cedula,especialidad,salarioxHora) VALUES (
        '{self.cedula}', 
        '{self.especialidad}',
        {self.salarioxHora})'''
        cur.execute(sql)
        con.commit()
        con.close()
    def eliminaenBD(self):
        con = sqlite3.connect('tallerMecanico.db')
        cur = con.cursor()
        sql = f'''DELETE FROM Mecanico WHERE cedula = {self.cedula}'''
        cur.execute(sql)
        con.commit()
        con.close()
    def actualizaenBD(self):
        con = sqlite3.connect('tallerMecanico.db')
        cur = con.cursor()
        sql = f'''UPDATE Mecanico SET especialidad= 
        {self.especialidad} , salarioxHora=
        {self.salarioxHora} where cedula = {self.cedula}'''
        cur.execute(sql)
        con.commit()
        con.close()
    def seleccionatodoenBD(self):
        con = sqlite3.connect('tallerMecanico.db')
        cur = con.cursor()
        listaDevolver=[]
        for fila in cur.execute('SELECT * FROM Mecanico'):
            objetoInterno = Mecanico(cedula= fila[0], 
                                    especialidad = fila[1],
                                    salarioxHora= fila[2])
            listaDevolver.append(objetoInterno)
        return listaDevolver
  