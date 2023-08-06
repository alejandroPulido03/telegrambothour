# Telegram Bot Hour 🤖⌚

Un pequeño y simple bot para telegram que escribirá la hora en determinados paises 

(Este proyecto usa la librería pyTelegramBotAPI de [eternnoir
](https://github.com/eternnoir)).

## Instalación 🛠

Instala la librería con pip

```bash
pip install pyTelegramBotAPI
```
O clona el [repo](https://github.com/eternnoir/pyTelegramBotAPI) en github

```bash
$ git clone https://github.com/eternnoir/pyTelegramBotAPI.git
$ cd pyTelegramBotAPI
$ python setup.py install
```

## Adquiriendo un Token 🗝 
Ve a [@BotFather](https://telegram.me/BotFather) y sigue las instrucciones para obtener el token de tu bot

Por ultimo agrega el Token en la constante TOKEN en main.py 



## Agregando paises 🌎 
Por último puedes agregar el país que desees como una variable que llame a la función crear_mensaje. Tienes que tener en cuenta la diferencia horaria de la hora de el país en el que está configurado __Tu Máquina__

Por ejemplo la hora estandar que uso es la de Colombia por lo que tengo que agregar la diferencia en cuanto a Colombia

```python
colombia = crear_mensaje(0,"Bogotá","🇨🇴") #Diferencia,Ciudad,Bandera(Emoji)
mexico = crear_mensaje(-1,"CDMX","🇲🇽")

```

## Contribuye al proyecto 🦾 
Puedes hacer un pull request a [este repositorio](https://github.com/diegop384/telegrambothour/pulls)

## Licencia
[MIT](https://choosealicense.com/licenses/mit/)


## Hecho con ❤ por [Alejandro Pulido](https://twitter.com/diego_pulidoo_)
