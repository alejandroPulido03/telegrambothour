import telebot  #librería de:https://github.com/eternnoir/pyTelegramBotAPI.git 
from tokenvalue import (GENERATETOKEN)
from datetime import datetime

TOKEN = GENERATETOKEN #Token de @thebotfather

bot = telebot.TeleBot(TOKEN)

def crear_mensaje(diferencia, lugar,bandera): #Lógica del programa
    time = datetime.now()
    hora = time.hour + diferencia #hora de Colombia + la diferencia del país a calcular
    tiempo = "AM"
    auxhora = ""
    auxmin = ""

    if hora > 24: #Si en el país a calcular ya se encuentran al otro día sobrepasará el 24 por lo que se tiene que restar 
        hora -=24

    if hora > 12:
        tiempo = "PM"
        hora -= 12 #cambio de hora militar a estandar
    if hora < 10:
        auxhora = '0'
        auxhora = "0"
    if time.minute < 10:
        auxmin = "0"

    


    mensaje = "En " + lugar + bandera +" son las " + auxhora + str(hora) + ":" + auxmin + str(time.minute) + tiempo + "\n"
    return mensaje

colombia = crear_mensaje(0,"Bogotá","🇨🇴")
mexico = crear_mensaje(-1,"CDMX","🇲🇽")
espana = crear_mensaje(5,"Madrid","🇪🇸")
venezuela = crear_mensaje(1,"Caracas","🇻🇪")

chat_mensaje = colombia + mexico + espana + venezuela

@bot.message_handler(commands=['hora']) #Encargado de los comandos entre la lista
def send_message(message): 
    bot.reply_to(message, chat_mensaje)

bot.polling()