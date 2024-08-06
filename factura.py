#creado por marito
#en la fecha x
#clase para atributos de tipo persona
import sqlite3
import facturagorra
from pydantic import BaseModel
import facturagorra
class Factura(BaseModel):
    identificador:str
    fecha:str
    montoTotal:int
    gorraComprada:str


    def nueva(self, identificador,fecha,montoTotal,gorraComprada,):
        self.identificador = identificador
        self.fecha= fecha
        self.montoTotal = montoTotal
        self.gorraComprada= gorraComprada
    
    def guardaenBD(self):
        con = sqlite3.connect('tiendaGorras.db')
        cur = con.cursor()
        sql = f'''INSERT INTO Factura(identificador,fecha,montoTotal,gorraComprada,,) VALUES (
        '{self.identificador}', 
        '{self.fecha}',
        {self.montoTotal}, 
        {self.gorraComprada},
        )'''
        cur.execute(sql)
        con.commit()
        con.close()
    def eliminaenBD(self):
        con = sqlite3.connect('tiendaGorras.db')
        cur = con.cursor()
        sql = f'''DELETE FROM Factura WHERE identificador = {self.identificador}'''
        cur.execute(sql)
        con.commit()
        con.close()
    def actualizaenBD(self):
        con = sqlite3.connect('tiendaGorras.db')
        cur = con.cursor()
        sql = f'''UPDATE Factura SET fecha= 
        {self.fecha} , montoTotal=
        {self.montoTotal}, gorraComprada=
        {self.gorraComprada}, 
      where identificador = {self.identificador}'''
        cur.execute(sql)
        con.commit()
        con.close()

    def seleccionatodoenBD(self):
        con = sqlite3.connect('tiendaGorras.db')
        cur = con.cursor()
        listaDevolver=[]
        for fila in cur.execute('SELECT * FROM Factura'):
            objetoInterno = Factura( identificador = fila[0],fecha= fila[1],montoTotal = fila[2],
            gorraComprada= fila[3])
            objetoFacturaGorra = facturagorra.Factura_Gorras(identificadorFactura=objetoInterno.identificador,identificadorGorra='')
            #objetoInterno.listadeGorras = objetoFacturaGorra.seleccionatodoenBDxFactura()
            listaDevolver.append(objetoInterno)
        return listaDevolver
   