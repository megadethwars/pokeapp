from flask import Response, json

# Diccionario de return codes
app_codes = {
    "APP-1": "Creado exitosamente",
    "APP-2": "Error en la formación del json de entrada",
    "APP-3": "Consulta exitosa",
    "APP-4": "Recurso no encontrado",
    "APP-5": "El recurso ya existe",
    "APP-6": "Recurso actualizado correctamente",
    "APP-7": "Error interno del servidor",
    "APP-8": "Recursos creados exitosamente",
    "APP-9": "Recurso eliminado exitosamente",
    "APP-10": "Acceso no autorizado",
    "APP-11": "ocurrio un conflicto al llamar a la API",

}


def partial_response(app_code,message="",name="",id=0):
    if message=="":
        message = app_codes[app_code]
    
    return {
            app_code:app_code,
            "message":message,
            "errors":name,
            "id":id
            }

def custom_response(res, status_code, app_code, message="", item=[]):
    """
    Custom Response Function
    """
    messageSent = list()
    if message == "":
        messageSent.append({"status":app_codes[app_code]})
    else:
        messageSent.append({"status":str(message)})

    if type(item) == list:
        for x in item:
            messageSent.append(x)
    else:
        messageSent.append({"object":item})

    response = {
        "app_code": app_code,
        "message": messageSent,
        "data": res,
    }
    return Response(
        mimetype="application/json",
        response=json.dumps(response),
        status=status_code,
    )
