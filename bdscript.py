import sqlite3
con = sqlite3.connect('tiendaGorras.db')
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Persona (
    cedula TEXT PRIMARY KEY,
    nombre TEXT,
    apellidos TEXT,
    correo TEXT,
    telefono TEXT
);""")
con.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS Cliente (
    cedula TEXT PRIMARY KEY,
    tipo TEXT,
    CONSTRAINT fk_cliente_persona FOREIGN KEY (cedula)
    REFERENCES Persona (cedula)
);""")
con.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS gorra (
    identificacion TEXT PRIMARY KEY,
    color TEXT,
    marca TEXT,
    costo REAL
);""")
con.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS Factura (
    identificador TEXT PRIMARY KEY,
    fecha TEXT,
    montoTotal REAL,
    gorraComprada TEXT,
    CONSTRAINT fk_factura_gorra FOREIGN KEY (gorraComprada)
    REFERENCES gorra (identificacion)
);""")
con.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS Factura_Gorras (
    identificadorFactura TEXT,
    identificadorGorra TEXT,
    CONSTRAINT fk_factura_factura_gorra FOREIGN KEY (identificadorFactura)
    REFERENCES Factura (identificador),
    CONSTRAINT fk_gorra_factura_gorra FOREIGN KEY (identificadorGorra)
    REFERENCES gorra (identificacion)
);""")
con.commit()

con.close()
