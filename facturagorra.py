#creado por marito
#en la fecha x
#clase para atributos de tipo persona
import sqlite3
from pydantic import BaseModel
class Factura_Gorras(BaseModel):
    identificadorFactura:str
    identificadorGorra:str
    def nueva(self, identificadorFactura,identificadorGorra):
        self.identificadorFactura = identificadorFactura
        self.identificadorGorra= identificadorGorra

     
    def guardaenBD(self):
        con = sqlite3.connect('tiendaGorras.db')
        cur = con.cursor()
        sql = f'''INSERT INTO Factura_Gorras(identificadorFactura,identificadorGorra) VALUES (
        '{self.identificadorFactura}', 
        '{self.identificadorGorra}'
        )'''
        cur.execute(sql)
        con.commit()
        con.close()
    def seleccionatodoenBDxFactura(self):
        con = sqlite3.connect('tiendaGorras.db')
        cur = con.cursor()
        listaDevolver=[]
        for fila in cur.execute(f'SELECT * FROM Factura_Gorras where identificadorFactura= {self.identificadorFactura}'):
            objetoInterno =  Factura_Gorras( identificadorFactura = fila[0],identificadorGorra= fila[1])
            listaDevolver.append(objetoInterno)
        return listaDevolver