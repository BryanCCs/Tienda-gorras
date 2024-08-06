#creado por marito
#en la fecha x
#clase para atributos de tipo persona
import sqlite3
from pydantic import BaseModel
class Vehiculo(BaseModel):
    placa: str
    color: str
    marca: str
    motor: str
    duenno: str

    def nueva(self, placa,color,marca,motor,duenno):
        self.placa = placa
        self.color= color
        self.marca = marca
        self.motor= motor
        self.duenno = duenno
    def guardaenBD(self):
        con = sqlite3.connect('tallerMecanico.db')
        cur = con.cursor()
        sql = f'''INSERT INTO Vehiculo(placa,color,marca,motor,duenno) VALUES (
        '{self.placa}', 
        '{self.color}','{self.marca}', 
        '{self.motor}','{self.duenno}')'''
        cur.execute(sql)
        con.commit()
        con.close()
    def eliminaenBD(self):
        con = sqlite3.connect('tallerMecanico.db')
        cur = con.cursor()
        sql = f'''DELETE FROM Vehiculo WHERE placa = {self.placa}'''
        cur.execute(sql)
        con.commit()
        con.close()
    def actualizaenBD(self):
        con = sqlite3.connect('tallerMecanico.db')
        cur = con.cursor()
        sql = f'''UPDATE Vehiculo SET color= 
        {self.color} , marca=
        {self.marca}, motor=
        {self.motor}, duenno=
        {self.duenno} where placa = {self.placa}'''
        cur.execute(sql)
        con.commit()
        con.close()
    def seleccionatodoenBD(self):
        con = sqlite3.connect('tallerMecanico.db')
        cur = con.cursor()
        listaDevolver=[]
        for fila in cur.execute('SELECT * FROM Vehiculo'):
            objetoInterno = Vehiculo(placa= fila[0], 
                                    color = fila[1], 
                                    marca = fila[2], 
                                    motor = fila[3], 
                                    duenno = fila[4])
            listaDevolver.append(objetoInterno)
        return listaDevolver
   