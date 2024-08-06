from pydantic import BaseModel
class Persona(BaseModel):
    cedula : str
    nombre : str
    primerapellido: str
    segundoapellido : str
    direccion: str
    correolectronico: str
    tipo:str
    clave :str

      