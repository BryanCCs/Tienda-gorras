#creado por marito
#en la fecha x
#clase para atributos de tipo persona
import sqlite3
from pydantic import BaseModel
class gorra(BaseModel):
    identificacion : str
    marca :str
    color :str
    costo : int
    def nueva(self, identificacion,marca,color,costo):
        self.identificacion = identificacion
        self.marca= marca
        self. color =  color
        self.costo= costo
     
    def guardaenBD(self):
        con = sqlite3.connect('tiendaGorras.db')
        cur = con.cursor()
        sql = f'''INSERT INTO gorra(identificacion,marca,color,costo) VALUES (
        '{self.identificacion}', 
        '{self.marca}',
         '{self. color}',
          {self.costo})'''
        cur.execute(sql)
        con.commit()
        con.close()
    def eliminaenBD(self):
        con = sqlite3.connect('tiendaGorras.db')
        cur = con.cursor()
        sql = f'''DELETE FROM gorra WHERE identificacion = {self.identificacion}'''
        cur.execute(sql)
        con.commit()
        con.close()
    def actualizaenBD(self):
        con = sqlite3.connect('tiendaGorras.db')
        cur = con.cursor()
        sql = f'''UPDATE gorra SET marca= 
        {self.marca} ,  color=
        {self. color}, costo=
         {self.costo} where identificacion = {self.identificacion}'''
        cur.execute(sql)
        con.commit()
        con.close()
    def seleccionatodoenBD(self):
        con = sqlite3.connect('tiendaGorras.db')
        cur = con.cursor()
        listaDevolver=[]
        for fila in cur.execute('SELECT * FROM gorra'):
            objetoInterno = gorra(identificacion= fila[0], 
                                    marca = fila[1],
                                     color= fila[2],
                                    costo= fila[3])
            listaDevolver.append(objetoInterno)
        return listaDevolver
   