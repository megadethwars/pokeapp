# pokeapp

## Esta es una aplicación web desarrollada con Flask que muestra información sobre estadisticas(Este servicio esta desplegado e Azure APP-service container).

### Requisitos previos
1. Tener python 3.9

## Pasos para correr el proyecto del pokeapp en local

1. Clona el repositorio en tu máquina local.
2. Ve al directorio del proyecto: `cd pokeapp`.
3. Configura un entorno virtual en un directorio llamado `venv`.
4. Activa el entorno virtual:
   - Para Windows: `venv\Scripts\activate`.
   - Para Linux/Mac: `source venv/bin/activate`.
5. Instala las dependencias del proyecto: `pip install -r requirements.txt`.
6. Agrega en la raiz del proyecto un archivo .env y agrega las siguientes variables:
   - FLASK_ENV=local
6. Ejecuta la aplicación: `python app.py`.
7. para probar unit test utiliza el comando `pytest test/pokeApiTest.py`

## probar los endpoints de API
1. la URL de implementacion es la siguiente: https://httppokeapiv1.azurewebsites.net/
2. Al entrar a dicha url, se desplegara la documentacion Swagger.
3. a continuacion se desplegaran dos endpoints tipo "GET":
   - https://pokeapiv1.azurewebsites.net/api/v1/pocket/allBerryStats  se desplegara el json de las estadisticas de los berrys (este endpoint se puede probar directo desde postman yo de manera local mediante http://127.0.0.1:5000/api/v1/pocket/allBerryStats)
   - https://pokeapiv1.azurewebsites.net/api/v1/pocket/allBerryStats/hist  se desplegara en formato json con una imagen en base64
4. En el navegador se puede consultar la url: https://pokeapiv1.azurewebsites.net/home se desplegaran estadisticas
   en html
5. La siguiente url https://pokeapiv1.azurewebsites.net/hist se desplegara el histograma de dichas estadisticas de matplotlib

