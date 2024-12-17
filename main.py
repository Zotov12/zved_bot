import telebot
from telebot import types
from telebot.types import WebAppInfo
from telebot.types import ReplyKeyboardMarkup
from telebot.types import KeyboardButton

#from гороскоп import bot
#bot=telebot.TeleBot('7543057010:AAFsNWqh1hxy50e1I8ulP5HVefvuIqkU_F8')
dp=telebot.TeleBot('8080304567:AAGH5MGkfMt8m2bK8Jbxz7AXD91B_RAFBY8')
web_app=WebAppInfo(url="https://zotov12.github.io/zved_bot/")
Keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
key_znak = types.KeyboardButton('Знаки зодиака',web_app=web_app)
Keyboard.add(key_znak)




keyboard = ReplyKeyboardMarkup(
    keyboard=[[types.KeyboardButton(text="Знаки зодиака", web_app=web_app)]], resize_keyboard=True)

DISC = {
    '1': 'Благоприятными для Овнов в этот день будут физические',
      #  упражнения, развлечения и активный отдых. Звезды
      #  гарантируют успех в любых творческих начинаниях.
       # Ваши увлечения и хобби дадут возможность получить
        #новый источник заработка. Если обстоятельства будут
        # складываться удачно, испытывая покровительство
        #Венеры, то вы обязательно станете центром внимания
        #лиц противоположного пола. Жизненный потенциал,
        #ваше личное обаяние и сексуальность пребывают сегодня
        #на самом высоком уровне и продолжают возрастать.
        #Трезво оценивайте действительность и свои
        # возможности. Будьте тверды в отстаивании убеждений и
        # взглядов. В этот День только откровенность и прямота
        # препятствуют на пути получения прибыли. Сдерживайте
        # свои желания, постарайтесь сильно не красоваться.'
     '2':   'В этот день новые действия и мысли по отношению к',
     # материальному благополучию будут у Тельцов
      # результативными. День хорош для активного занятия
       #спортом, а также коллективных мероприятий, где
#лидирующую позицию будете занимать только вы.
#Трудности в семейных отношениях и другие разногласия
#с партнером не исключены сегодня. Укротите свой нрав,
#постарайтесь не обижаться и забудьте об уязвленном
#самолюбии. Ваша энергия, находящаяся на самом пике,
#существенно повлияет на мировоззрение окружающих
#людей. Ждите неожиданной и приятной новости или
#выгодного предложения, которые нужно постараться
#использовать по максимуму исключительно для себя.',
}


@dp.message_handler(content_types='web_app_data')
async def buy_process(web_app_message, DISC=None):
     await bot.send_message(web_app_message.chat.id,
          DISC[f'{web_app_message.web_app_data}'])



