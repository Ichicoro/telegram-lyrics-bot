from telegram.ext import Updater, CommandHandler, Filters
import logging
import lyricsgetter

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, 
        text="Hello! With this bot you'll be able to find lyrics for your favourite songs :) Please type the name of the artist and of the song you wanna search the lyrics for, separated by a comma (eg: dragonforce, through the fire and flames).")

def msgHandler(bot, update):
    songdata = update.message.text.split(',')
    response = getLyrics(songdata[0],songdata[1])
    if response != "lyrics not found":
        bot.send_message(chat_id=update.message.chat_id, text=response)
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Lyrics not found :(")


if __name__=="__main__":
    updater = Updater(token='DUMMY_API_KEY')    # heh, I still need an API key :(
    dispatcher = updater.dispatcher             # setting up the dispatcher for easier access

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO) # setting up the logger

    # print(bot.get_me())             # let's just print the bot info so I'm sure of what I'm doing :o

    # Adding start as the command handler
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Adding the text message handler
    msg_handler = CommandHandler(Filters.text, msgHandler)
    dispatcher.add_handler(msg_handler)

    updater.start_polling()
