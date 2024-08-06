# Creado por Marito
# Fecha: x

import sqlite3
from pydantic import BaseModel

class Tienda(BaseModel):
    identificacion: str
    nombre: str
    ganancia: float
    direccion: str
    correo: str

    def guardaenBD(self):
        con = sqlite3.connect('tiendaGorras.db')
        cur = con.cursor()
        sql = '''INSERT INTO Tienda (identificacion, nombre, ganancia, direccion, correo) VALUES (?, ?, ?, ?, ?)'''
        cur.execute(sql, (self.identificacion, self.nombre, self.ganancia, self.direccion, self.correo))
        con.commit()
        con.close()

    def eliminaenBD(self):
        con = sqlite3.connect('tiendaGorras.db')
        cur = con.cursor()
        sql = '''DELETE FROM Tienda WHERE identificacion = ?'''
        cur.execute(sql, (self.identificacion,))
        con.commit()
        con.close()

    def actualizaenBD(self):
        con = sqlite3.connect('tiendaGorras.db')
        cur = con.cursor()
        sql = '''UPDATE Tienda SET nombre = ?, ganancia = ?, direccion = ?, correo = ? WHERE identificacion = ?'''
        cur.execute(sql, (self.nombre, self.ganancia, self.direccion, self.correo, self.identificacion))
        con.commit()
        con.close()

    def seleccionatodoenBD(self):
        con = sqlite3.connect('tiendaGorras.db')
        cur = con.cursor()
        listaDevolver = []
        for fila in cur.execute('SELECT * FROM Tienda'):
            objetoInterno = Tienda(
                identificacion=fila[0],
                nombre=fila[1],
                ganancia=fila[2],
                direccion=fila[3],
                correo=fila[4]
            )
            listaDevolver.append(objetoInterno)
        con.close()
        return listaDevolver

    def paginaWeb(self):
        return '''<html><head>
</head>
<body>
<input id="identificacion" type="text" placeholder="Escriba la identificación"/>
<input id="nombre" type="text" placeholder="Escriba el nombre"/>
<input id="ganancia" type="text" placeholder="Escriba la ganancia"/>
<input id="direccion" type="text" placeholder="Escriba la dirección"/>
<input id="correo" type="text" placeholder="Escriba el correo"/>
<input id="btnaccion" type="button" value="Ingresar" onclick="guardar()"/>
<div id="espacioTabla">
<table>
<thead>
<tr>
<td>Identificación</td>
<td>Nombre</td>
<td>Ganancia</td>
<td>Dirección</td>
<td>Correo</td>
<td>Modificar</td>
<td>Eliminar</td>
</tr>
</thead>
<tbody id="cuerpoTabla">
</tbody>
</table>
</div>
<script>
listadeTiendas = []
function cargarDatos() {
{
var objetoaenviar = new Object();
    try {
        var xhr = new XMLHttpRequest();
        xhr.open('GET', '/Tienda');
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onload = function() {
            if (xhr.status == 200) {
                console.log(JSON.parse(xhr.responseText));
                rellenaTabla(JSON.parse(xhr.responseText));
            } else {
                console.log(xhr);
            }
        };
        xhr.send();
    } catch (err) {
        console.log(err.message);
    }
}

function rellenaTabla(vector) {
listadeTienda = vector;
document.getElementById("cuerpoTabla").innerHTML = "";
document.getElementById("cuerpoTabla").innerHTML += "<tr>"
for (var elemento in vector)
  { 
    document.getElementById("cuerpoTabla").innerHTML += "<td>" + vector[elemento].indentificacion + "</td><td>" + vector[elemento].nombre  + "</td><td>" + vector[elemento].ganancia  + "</td><td>" + vector[elemento].correo  + "</td><td>"+ vector[elemento].direccion  + "</td><td><input type= 'button' value = 'Modificar' onclick= 'modificar("+ vector[elemento].identificacion +")' /></td><td><input type= 'button' value = 'Eliminar' onclick= 'eliminar(" + vector[elemento].identificacion + ")' /></td><td>"
}
 document.getElementById("cuerpoTabla").innerHTML += "</tr>"
}


function guardar() {
 function guardar()
{
    var objetoaenviar = new Object();
    objetoaenviar.identificacion = document.getElementById("identificacion").value
    objetoaenviar.nombre = document.getElementById("nombre").value
    objetoaenviar.ganancia = document.getElementById("ganancia").value
    objetoaenviar.correo = document.getElementById("correo").value
    objetoaenviar.direccion = document.getElementById("direccion").value        

    try {
        var xhr = new XMLHttpRequest();
        xhr.open('PUT', '/tienda');
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onload = function() 
        {
            if (xhr.status == 200) 
            {
                console.log(JSON.parse(xhr.responseText));
                alert('Guardado');
                rellenaTabla(JSON.parse(xhr.responseText));
            } else {
                console.log(xhr);
            }
        };
        xhr.send(JSON.stringify(objetoaenviar));
    } catch (err) {
        console.log(err.message);
    }
}

function modificar(identificacion) {
    if (window.confirm("Desea modificar el dato?")) {
        var objetoEncontrado = listadeTiendas.filter(obj => {
         return obj.identificacion === String(identificacion)
        })
        document.getElementById("identificacion").value = objetoEncontrado.identificacion;
        document.getElementById("nombre").value = objetoEncontrado.nombre;
        document.getElementById("ganancia").value = objetoEncontrado.ganancia;
        document.getElementById("direccion").value = objetoEncontrado.direccion;
        document.getElementById("correo").value = objetoEncontrado.correo;
        document.getElementById('btnaccion').value = 'Modificar';
        document.getElementById('btnaccion').setAttribute("onClick", "modificaenbd()");
}
}

function modificaenbd() {
    var objetoaenviar = new Object();
     objetoaenviar.identificacion = document.getElementById("identificacion").value
        objetoaenviar.nombre = document.getElementById("nombre").value
         objetoaenviar.ganancia = document.getElementById("ganancia").value
        objetoaenviar.direccion = document.getElementById("direccion").value
       objetoaenviar.correo = document.getElementById("correo").value
    
     try {
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/tienda');
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onload = function() {
            if (xhr.status == 200) {
                console.log(JSON.parse(xhr.responseText));
                alert('Modificado');
                rellenaTabla(JSON.parse(xhr.responseText));
                document.getElementById('btnaccion').value = 'Guardar';
                document.getElementById('btnaccion').setAttribute("onClick", "guardar()");
                document.getElementById("identificacion").value = "";
                document.getElementById("nombre").value = "";
                document.getElementById("ganancia").value = "";
                document.getElementById("direccion").value = "";
                document.getElementById("correo").value = "";
            } else {
                console.log(xhr);
            }
        };
        xhr.send(JSON.stringify(objetoaenviar));
    } catch (err) {
        console.log(err.message);
    }
}

function eliminar(identificacion) {
    if (window.confirm("Desea eliminar el dato?")) {
        var objetoaenviar = new Object();
            objetoaenviar.identificacion = String(identificacion)   
          objetoaenviar.nombre = ""
            objetoaenviar.ganancia = ""
              objetoaenviar.direccion = ""
                objetoaenviar.correo = ""

        try {
            var xhr = new XMLHttpRequest();
            xhr.open('DELETE', '/tienda');
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.onload = function() {
                if (xhr.status == 200) {
                    console.log(JSON.parse(xhr.responseText));
                    alert('Eliminado');
                    rellenaTabla(JSON.parse(xhr.responseText));
                } else {
                    console.log(xhr);
                }
            };
            xhr.send(JSON.stringify(objetoaenviar));
        } catch (err) {
            console.log(err.message);
        }
    }
}
}
}

cargarDatos();
</script>
</body>
</html>'''
