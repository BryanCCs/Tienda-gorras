
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from pydantic import BaseModel
from Cliente import *
from venta import *
app= FastAPI()
class Item(BaseModel):
    cedula : str
    nombre : str
    primerapellido: str
    segundoapellido : str
    direccion: str
    correolectronico: str
    tipo:str
    clave :str
class ItemProducto(BaseModel):
    id:str
    nombre:str
    descripcion:str
    precioxunidad:str
    unidaddemedida:str
    tienda:str
class ItemVenta(BaseModel):
    id:str
    fecha:str
    cliente:str
    productos:str
    montototal:str
    impuesto:str
    montototalconimpuesto :str
class ItemTienda(BaseModel):
    id:str
    nombre : str
    descripcion : str
    direccion : str
    telefonos : str
@app.get("/")
async def root():
    return FileResponse('Login.html')
@app.get("/ventas")
async def root():
    return FileResponse('venta.html')
@app.get("/archivopaginaweb")
async def root():
    return FileResponse('Cliente.html')
@app.get("/archivopaginawebproducto")
async def root():
    return FileResponse('Producto.html')

@app.get("/clientejs")
async def root():
    return FileResponse('fastapi-env/clientefrontend.js') 


@app.get("/productojs")
async def root():
    return FileResponse('fastapi-env/productofrontend.js') 

@app.get("/tiendajs")
async def root():
    return FileResponse('fastapi-env/tiendafrontend.js') 
@app.get("/ventajs")
async def root():
    return FileResponse('fastapi-env/ventafrontend.js') 
@app.get("/clientes")
async def root():
    clientecito = Cliente()
   
    listadeclientesenarchivo = clientecito.listar()
    for elemento in listadeclientesenarchivo:
        elemento.modificar = '<input type="button" value="modificar" onclick="modificaclienteprimerpaso(\''+ elemento.cedula +'\')"></input>'
        elemento.eliminar = '<input type="button" value="eliminar" onclick="eliminacliente(\''+ elemento.cedula +'\')"></input>'
    return listadeclientesenarchivo 



@app.get("/tiendas")
async def root():
    tiendita = Tienda()
   
    listadeclientesenarchivo = tiendita.listar()
    for elemento in listadeclientesenarchivo:
        elemento.modificar = '<input type="button" value="modificar" onclick="modificaclienteprimerpaso(\''+ elemento.id +'\')"></input>'
        elemento.eliminar = '<input type="button" value="eliminar" onclick="eliminacliente(\''+ elemento.id +'\')"></input>'
    return listadeclientesenarchivo 

@app.get("/productos")
async def root():
    tiendita = producto()
   
    listadeclientesenarchivo = tiendita.listar()
    for elemento in listadeclientesenarchivo:
        elemento.tienda = elemento.tienda.id
        elemento.modificar = '<input type="button" value="modificar" onclick="modificaclienteprimerpaso(\''+ elemento.id +'\')"></input>'
        elemento.eliminar = '<input type="button" value="eliminar" onclick="eliminacliente(\''+ elemento.id +'\')"></input>'
    return listadeclientesenarchivo 
@app.get("/productosparaventa")
async def root():
    tiendita = producto()
   
    listadeclientesenarchivo = tiendita.listar()
    for elemento in listadeclientesenarchivo:
        elemento.tienda = elemento.tienda.id
        elemento.agregar = '<input type="button" value="Agregar" onclick="Agrega(\''+ elemento.id +'\')"></input>'
    return listadeclientesenarchivo 

@app.put("/clientes")
async def root(item:Item):
    clientecito = Cliente()
    clientecito.cedula = item.cedula
    clientecito.clave = item.clave
    clientecito.correolectronico = item.correolectronico
    clientecito.direccion= item.direccion
    clientecito.nombre = item.nombre
    clientecito.primerapellido = item.primerapellido
    clientecito.segundoapellido = item.segundoapellido
    clientecito.tipo = item.tipo
  
    clientecito.guardar()
    listadeclientesenarchivo = clientecito.listar()
    for elemento in listadeclientesenarchivo:
        elemento.modificar = '<input type="button" value="modificar" onclick="modificaclienteprimerpaso(\''+ elemento.cedula +'\')"></input>'
        elemento.eliminar = '<input type="button" value="eliminar" onclick="eliminacliente(\''+ elemento.cedula +'\')"></input>'
    return listadeclientesenarchivo

@app.put("/productos")
async def root(item:ItemProducto):
    clientecito = producto()
    clientecito.id=item.id
    clientecito.nombre=item.nombre
    clientecito.descripcion = item.descripcion
    clientecito.precioxunidad= float(item.precioxunidad)
    clientecito.unidaddemedida= item.unidaddemedida
    tiendecita = Tienda()
    tiendecita.id = item.tienda
    clientecito.tienda = tiendecita
    clientecito.guardar()
    listadeclientesenarchivo = clientecito.listar()
    for elemento in listadeclientesenarchivo:
        elemento.tienda = elemento.tienda.id
        elemento.modificar = '<input type="button" value="modificar" onclick="modificaclienteprimerpaso(\''+ elemento.id +'\')"></input>'
        elemento.eliminar = '<input type="button" value="eliminar" onclick="eliminacliente(\''+ elemento.id +'\')"></input>'
    return listadeclientesenarchivo 

@app.put("/ventas")
async def root(item:ItemVenta):
    #id=""
    #fecha=""
    #cliente = Cliente()
    #productos= []
    #montototal= 0.0
    #impuesto = 0.0
    #montototalconimpuesto = 0.0
    clientecito = venta()
    clientecito.id=item.id
    clientecito.fecha=item.fecha
    clienteinterno = Cliente()
    clienteinterno.cedula = item.cliente
    clienteinterno.cliente = clienteinterno
    listadeproductosagregados = item.productos.split(',')
    for iteminterno in listadeproductosagregados:
        productointerno = producto()
        productointerno.id = iteminterno
        clientecito.productos.append(productointerno)
    
    clientecito.montototal  = float(item.montototal)
    clientecito.impuesto= float(item.impuesto)
    clientecito.montototalconimpuesto= float(item.montototalconimpuesto)
    return "Venta realizada" 
@app.post("/clientes")
async def root(item:Item):
    clientecito = Cliente()
    clientecito.cedula = item.cedula
    clientecito.clave = item.clave
    clientecito.correolectronico = item.correolectronico
    clientecito.direccion= item.direccion
    clientecito.nombre = item.nombre
    clientecito.primerapellido = item.primerapellido
    clientecito.segundoapellido = item.segundoapellido
    clientecito.tipo = item.tipo
  
    clientecito.modificar()
    listadeclientesenarchivo = clientecito.listar()
    for elemento in listadeclientesenarchivo:
        elemento.modificar = '<input type="button" value="modificar" onclick="modificaclienteprimerpaso(\''+ elemento.cedula +'\')"></input>'
        elemento.eliminar = '<input type="button" value="eliminar" onclick="eliminacliente(\''+ elemento.cedula +'\')"></input>'
    return listadeclientesenarchivo
@app.post("/loginclientes")
async def root(item:Item):
    clientecito = Cliente()
    clientecito.cedula = item.cedula
    clientecito.clave = item.clave
    clientecito.correolectronico = item.correolectronico
    clientecito.direccion= item.direccion
    clientecito.nombre = item.nombre
    clientecito.primerapellido = item.primerapellido
    clientecito.segundoapellido = item.segundoapellido
    clientecito.tipo = item.tipo
    return clientecito.login()
@app.delete("/clientes")
async def root(item:Item):
    clientecito = Cliente()
    clientecito.cedula = item.cedula
    clientecito.clave = item.clave
    clientecito.correolectronico = item.correolectronico
    clientecito.direccion= item.direccion
    clientecito.nombre = item.nombre
    clientecito.primerapellido = item.primerapellido
    clientecito.segundoapellido = item.segundoapellido
    clientecito.tipo = item.tipo
    clientecito.eliminar()
    listadeclientesenarchivo = clientecito.listar()
    for elemento in listadeclientesenarchivo:
       elemento.modificar = '<input type="button" value="modificar" onclick="modificaclienteprimerpaso(\''+ elemento.cedula +'\')"></input>'
       elemento.eliminar = '<input type="button" value="eliminar" onclick="eliminacliente(\''+ elemento.cedula +'\')"></input>'
    return listadeclientesenarchivo