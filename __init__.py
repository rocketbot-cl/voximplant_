# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""
import os
import sys
base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'voximplant_' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)
from voximplant.apiclient import VoximplantAPI, VoximplantException


"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

if module == "voximplant":
    credentials = GetParams("credentials")
    source = GetParams("source")
    destination = GetParams("destination")
    message = GetParams("message")

    if "+" in source:
        source = source.split('+')[1]

    if "+" in destination:
        destination = destination.split('+')[1]

    try:
        api = VoximplantAPI(credentials)

        # Send the SMS with the "Test message" text from the phone number 447443332211 to the phone number 447443332212

        SOURCE = source
        DESTINATION = destination
        SMS_BODY = message

        try:
            res = api.send_sms_message(SOURCE, DESTINATION, SMS_BODY)
            print(res)
        except VoximplantException as e:
            print("Error: {}".format(e.message))

    except Exception as e:
        PrintException()
        raise e


