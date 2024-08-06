from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
import persona
import cliente
import gorras
import factura
import facturagorra
app= FastAPI()
@app.put("/persona")
async def root(item:persona.Persona):
    objetoPersona = persona.Persona(cedula = item.cedula, apellidos = item.apellidos,
                                    correo= item.correo,
                                    nombre= item.nombre,
                                    telefono = item.telefono)
    objetoPersona.guardaenBD()
    return objetoPersona.seleccionatodoenBD()

@app.get("/persona")
async def root():
    objetoPersona = persona.Persona(cedula = '', apellidos = '',
                                    correo= '',
                                    nombre= '',
                                    telefono = '')
    return objetoPersona.seleccionatodoenBD()

@app.delete("/persona")
async def root(item:persona.Persona):
    print(item)
    objetoPersona = persona.Persona(cedula = item.cedula, 
                                    apellidos = '',
                                    correo= '',
                                    nombre= '',
                                    telefono = '')
    objetoPersona.eliminaenBD()
    return objetoPersona.seleccionatodoenBD()

@app.post("/persona")
async def root(item:persona.Persona):
    print(item)
    objetoPersona = persona.Persona(cedula = item.cedula, apellidos = item.apellidos,
                                    correo= item.correo,
                                    nombre= item.nombre,
                                    telefono = item.telefono)
    objetoPersona.actualizaenBD()
    return objetoPersona.seleccionatodoenBD()
@app.put("/cliente")
async def root(item:cliente.Cliente):
    objetoPersona = cliente.Cliente(cedula = item.cedula, 
                                    tipo = item.tipo)
    objetoPersona.guardaenBD()
    return objetoPersona.seleccionatodoenBD()

@app.get("/cliente")
async def root():
    objetoPersona = cliente.Cliente(cedula = '', tipo = '')
    return objetoPersona.seleccionatodoenBD()


@app.get("/clienteHTML")
async def root():
    return FileResponse("cliente.html")


@app.put("/gorra")
async def root(item:gorras.gorra):
    objetoPersona = gorras.gorra(identificacion = item.identificacion, 
                                    marca = item.marca, color=item.color, costo = item.costo)
    objetoPersona.guardaenBD()
    return objetoPersona.seleccionatodoenBD()

@app.get("/gorra")
async def root():
    objetoPersona = gorras.gorra(identificacion='',marca='',color='',costo=0)
    return objetoPersona.seleccionatodoenBD()


@app.get("/gorraHTML")
async def root():
    return FileResponse("gorra.html")


@app.put("/factura")
async def root(item:factura.Factura):
    objetoPersona = factura.Factura(identificador=item.identificador,fecha=item.fecha,montoTotal=item.montoTotal,gorraComprada=item.gorraComprada)
    objetoPersona.guardaenBD()
    return objetoPersona.seleccionatodoenBD()

@app.get("/factura")
async def root():
    objetoPersona = factura.Factura(identificador='',fecha='',montoTotal=0,gorraComprada='')

    return objetoPersona.seleccionatodoenBD()

@app.put("/facturagorra")
async def root(item:facturagorra.Factura_Gorras):
    objetoPersona = facturagorra.Factura_Gorras(identificadorFactura=item.identificadorFactura,identificadorGorra=item.identificadorGorra)
    objetoPersona.guardaenBD()
    return objetoPersona.seleccionatodoenBDxFactura()

@app.get("/facturaGorraxfactura")
async def root(item:facturagorra.Factura_Gorras):
    objetoPersona = facturagorra.Factura_Gorras(identificadorFactura=item.identificadorFactura,identificadorGorra='')
    return objetoPersona.seleccionatodoenBDxFactura()

@app.get("/facturaHTML")
async def root():
    return FileResponse("factura.html")

@app.get("/personaHTML",response_class=HTMLResponse)
async def root():
    objetoPersona = persona.Persona(cedula = '', apellidos = '',
                                    correo= '',
                                    nombre= '',
                                    telefono = '')
    html= objetoPersona.paginaWeb()
    return html 