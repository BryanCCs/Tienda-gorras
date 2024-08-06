#creado por marito
#en la fecha x
#clase para atributos de tipo persona
import sqlite3
from pydantic import BaseModel
class Persona(BaseModel):
    cedula : str
    nombre : str
    apellidos : str
    correo : str
    telefono : str
    def nueva(self, cedula, nombre, apellidos, correo,telefono):
        self.cedula = cedula
        self.nombre = nombre
        self.apellidos = apellidos
        self.correo= correo
        self.telefono= telefono
    def guardaenBD(self):
        con = sqlite3.connect('tiendaGorras.db')
        cur = con.cursor()
        sql = f'''INSERT INTO Persona(cedula,nombre,apellidos,correo,telefono) VALUES (
        '{self.cedula}', 
        '{self.nombre}', 
        '{self.apellidos}', 
        '{self.correo}' ,
        '{self.telefono}')'''
        cur.execute(sql)
        con.commit()
        con.close()
    def eliminaenBD(self):
        con = sqlite3.connect('tiendaGorras.db')
        cur = con.cursor()
        sql = f'''DELETE FROM Persona WHERE cedula = {self.cedula}'''
        cur.execute(sql)
        con.commit()
        con.close()
    def actualizaenBD(self):
        con = sqlite3.connect('tiendaGorras.db')
        cur = con.cursor()
        sql = f'''UPDATE Persona SET nombre= 
        '{self.nombre}' , apellidos=
        '{self.apellidos}' , correo =
        '{self.correo}' , telefono =
        '{self.telefono}' where cedula = {self.cedula}'''
        cur.execute(sql)
        con.commit()
        con.close()
    def seleccionatodoenBD(self):
        con = sqlite3.connect('tiendaGorras.db')
        cur = con.cursor()
        listaDevolver=[]
        for fila in cur.execute('SELECT * FROM persona'):
            objetoInterno = Persona(cedula= fila[0], apellidos = fila[2],
                                    correo= fila[3],
                                    nombre= fila[1],
                                    telefono = fila[4])
            listaDevolver.append(objetoInterno)
        return listaDevolver
    def paginaWeb(self):
        return '''<html>
     <style>
    body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 20px;
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        background-color: #f4f4f4;
    }
    
    .container {
        max-width: 600px;
        width: 100%;
        background-color: #fff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    
    input[type="text"] {
        display: block;
        margin: 10px 0;
        padding: 10px;
        width: 100%;
        border: 1px solid #ccc;
        border-radius: 4px;
    }
    
    input[type="button"] {
        padding: 8px 16px;
        border: none;
        border-radius: 4px;
        background-color: #007BFF;
        color: white;
        cursor: pointer;
        font-size: 14px;
        margin: 8px 0;
    }
    
    input[type="button"]:hover {
        background-color: #0056b3;
    }
    
    #espacioTabla {
        margin-top: 20px;
        overflow-x: auto;
    }
    
    table {
        width: 100%;
        border-collapse: collapse;
        font-size: 14px;
    }
    
    th, td {
        border: 1px solid #ddd;
        padding: 6px;
        text-align: left;
    }
    
    th {
        background-color: #f4f4f4;
    }
    
    tr:nth-child(even) {
        background-color: #f9f9f9;
    }
    
    tr:hover {
        background-color: #f1f1f1;
    }
</style>

<head>
        </head>
        <body>
         <div class="container">
        <input id="cedula" type="text" placeholder="Escriba su cedula"/>
        <input id="nombre" type="text" placeholder="Escriba su nombre"/>
        <input id="apellidos" type="text" placeholder="Escriba sus apellidos"/>
        <input id="correo" type="text" placeholder="Escriba su correo"/>
        <input id="telefono" type="text" placeholder="Escriba su telefono"/>
        <input id="btnaccion" type="button" value="Ingresar" onclick="guardar()"/>
        <div id="espacioTabla">
            <table>
                <thead>
                    <tr>
                        <td>Cedula</td>
                        <td>Nombre</td>
                        <td>Apellidos</td>
                        <td>Correo</td>
                        <td>Telefono</td>
                        <td>Modificar</td>
                        <td>Eliminar</td>
                    </tr>
                </thead>
                <tbody id="cuerpoTabla">
                </tbody>
            </table>
        </div>
    </div>
        <script>
        listadepersonas=[]
        function cargarDatos()
        {
        var objetoaenviar = new Object();
                    
            try
                {
                    var xhr = new XMLHttpRequest();
                    xhr.open('GET','/persona');
                    xhr.setRequestHeader('Content-Type','application/json');
                    xhr.onload = function()
                    {
                    if(xhr.status == 200)
                        {
                            console.log(JSON.parse(xhr.responseText));
                            rellenaTabla(JSON.parse(xhr.responseText))
                        }
                    else
                        {
                            console.log(xhr);
                        }
                    };
                    xhr.send();
                    }
            catch(err)
                {
                    console.log(err.message);
                }
        }
        function rellenaTabla(vector)
        {
        listadepersonas = vector
        document.getElementById("cuerpoTabla").innerHTML =""
        document.getElementById("cuerpoTabla").innerHTML += "<tr>"
        for (var elemento in vector)
            {
                document.getElementById("cuerpoTabla").innerHTML += "<td>" + vector[elemento].cedula + "</td><td>" + vector[elemento].nombre  + "</td><td>" + vector[elemento].apellidos  + "</td><td>" + vector[elemento].correo  + "</td><td>"+ vector[elemento].telefono  + "</td><td><input type= 'button' value = 'Modificar' onclick= 'modificar("+ vector[elemento].cedula +")' /></td><td><input type= 'button' value = 'Eliminar' onclick= 'eliminar(" + vector[elemento].cedula + ")' /></td><td>"
            }
            document.getElementById("cuerpoTabla").innerHTML += "</tr>"
        }
        function guardar()
        {
            var objetoaenviar = new Object();
            objetoaenviar.cedula = document.getElementById("cedula").value
            objetoaenviar.nombre = document.getElementById("nombre").value
            objetoaenviar.apellidos = document.getElementById("apellidos").value
            objetoaenviar.correo = document.getElementById("correo").value
            objetoaenviar.telefono = document.getElementById("telefono").value        
                    
            try
                {
                    var xhr = new XMLHttpRequest();
                    xhr.open('PUT','/persona');
                    xhr.setRequestHeader('Content-Type','application/json');
                    xhr.onload = function()
                    {
                    if(xhr.status == 200)
                        {
                            console.log(JSON.parse(xhr.responseText));
                            alert('Guardado')
                            rellenaTabla(JSON.parse(xhr.responseText))

                        }
                    else
                        {
                            console.log(xhr);
                        }
                    };
                    xhr.send(JSON.stringify(objetoaenviar));
                    }
            catch(err)
                {
                    console.log(err.message);
                }
        }
        function modificar(cedula)
        {
        if (window.confirm("Desea modificar el dato?")) {
            var objetoEncontrado = listadepersonas.filter(obj => {
                    return obj.cedula === String(cedula)
                    })
            document.getElementById("cedula").value = objetoEncontrado[0].cedula
            document.getElementById("nombre").value = objetoEncontrado[0].nombre
            document.getElementById("apellidos").value = objetoEncontrado[0].apellidos
            document.getElementById("correo").value = objetoEncontrado[0].correo
            document.getElementById("telefono").value = objetoEncontrado[0].telefono    
            document.getElementById('btnaccion').value = 'Modificar'
            document.getElementById('btnaccion').setAttribute( "onClick", "modificaenbd()" );          
        }

      
        }
          function modificaenbd()
        {
         var objetoaenviar = new Object();
            objetoaenviar.cedula = document.getElementById("cedula").value
            objetoaenviar.nombre = document.getElementById("nombre").value
            objetoaenviar.apellidos = document.getElementById("apellidos").value
            objetoaenviar.correo = document.getElementById("correo").value
            objetoaenviar.telefono = document.getElementById("telefono").value        
                               
            try
                {
                    var xhr = new XMLHttpRequest();
                    xhr.open('POST','/persona');
                    xhr.setRequestHeader('Content-Type','application/json');
                    xhr.onload = function()
                    {
                    if(xhr.status == 200)
                        {
                            console.log(JSON.parse(xhr.responseText));
                            alert('Modificado')
                            rellenaTabla(JSON.parse(xhr.responseText))
                            document.getElementById('btnaccion').value = 'Guardar'
                            document.getElementById('btnaccion').setAttribute( "onClick", "guardar()" );          
                            document.getElementById("cedula").value = ""
                            document.getElementById("nombre").value = ""
                            document.getElementById("apellidos").value = ""
                            document.getElementById("correo").value = ""
                            document.getElementById("telefono").value = ""
                        }
                    else
                        {
                            console.log(xhr);
                        }
                    };
                    xhr.send(JSON.stringify(objetoaenviar));
                    }
            catch(err)
                {
                    console.log(err.message);
                }   
                } 
        function eliminar(cedula)
        {
        if (window.confirm("Desea eliminar el dato?")) {
            var objetoaenviar = new Object();
            objetoaenviar.cedula = String(cedula)       
            objetoaenviar.nombre = ""
            objetoaenviar.apellidos = ""
            objetoaenviar.correo = ""
            objetoaenviar.telefono = ""           
            try
                {
                    var xhr = new XMLHttpRequest();
                    xhr.open('DELETE','/persona');
                    xhr.setRequestHeader('Content-Type','application/json');
                    xhr.onload = function()
                    {
                    if(xhr.status == 200)
                        {
                            console.log(JSON.parse(xhr.responseText));
                            alert('Eliminado')
                            rellenaTabla(JSON.parse(xhr.responseText))

                        }
                    else
                        {
                            console.log(xhr);
                        }
                    };
                    xhr.send(JSON.stringify(objetoaenviar));
                    }
            catch(err)
                {
                    console.log(err.message);
                }   
                } 
        }
        cargarDatos()
        </script>
        </body>
        </html>'''
        