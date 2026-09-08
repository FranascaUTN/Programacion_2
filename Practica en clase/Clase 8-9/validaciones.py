import re

#COn el guion al inicio indico que va a ser solo de uso local
_PATRON_NOMBRE = re.compile(r"^[^\W\d_]+(?:[ '\-][^\W\d_]+)*$", re.UNICODE)

def validar_nombre (nom) :
    #Primero filtrar si la variable es del tipo correcto
    if not isinstance(nom, str) :
        raise TypeError("Ingrese un valor valido")

    #Normalizamos el str para sacar espacios dobles y a la vez chequeamos que no este vacia la variable
    limpio = re.sub(r"\s", " ", nom).strip()
    if not limpio:
        raise ValueError("Debe ingresar al menos un caracter")

    #Si no cumple con el patron armado lanzamos una exepcion
    if not _PATRON_NOMBRE.match(limpio):
        raise ValueError("Debe ingresar caracteres validos")

    nom = limpio
    return nom

""" EL raise corta la ejecucion y clasifica el error segun se aclare y envia el mensaje
"""