from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
import logging
import lyricsgetter 
import os

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, 
        text="Hello! With this bot you'll be able to find lyrics for your favourite songs :) Please type the name of the artist and of the song you wanna search the lyrics for, separated by a comma (eg: through the fire and flames,dragonforce).")


def tryToFindLyrics():
    response = getLyrics(songdata[0],songdata[1])
    if response != "lyrics not found":
        bot.send_message(chat_id=update.message.chat_id, text=response)
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Lyrics not found :( Try with a different query")


def msgHandler(bot, update):
    print(update.message.text)
    print("It's a song!")
    bot.send_message(chat_id=update.message.chat_id, 
        text=lyricsgetter.getSongByName(update.message.text.strip()))  


if __name__=="__main__":
    print("LyrxBot v0.1")

    if "TELEGRAM_ACCESS_TOKEN" not in os.environ:
        print("TELEGRAM_ACCESS_TOKEN environment variable not set. Exiting!")
        exit()

    if "GENIUS_ACCESS_TOKEN" not in os.environ:
        print("GENIUS_ACCESS_TOKEN environment variable not set. Exiting!")
        exit()

    updater = Updater(token=os.environ["TELEGRAM_ACCESS_TOKEN"])    # reads from the environment variables!
    dispatcher = updater.dispatcher                                 # setting up the dispatcher for easier access

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO) # setting up the logger

    # print(bot.get_me())             # let's just print the bot info so I'm sure of what I'm doing :o

    # Adding start as the command handler
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Adding the text message handler
    msg_handler = MessageHandler(Filters.text, msgHandler)
    dispatcher.add_handler(msg_handler)

    # Let the polling begin
    updater.start_polling()
    print("Init done")
