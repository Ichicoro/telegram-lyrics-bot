from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
import telegram
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
    bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    print(update.message.text)
    print("It's a song!")
    try:
        lyrics = lyricsgetter.getSongByName(update.message.text.strip())
        songdata = lyricsgetter.getSongData(update.message.text.strip())
        if "default" not in songdata['result']['header_image_url']:
            bot.send_photo(chat_id=update.message.chat_id, photo=songdata['result']['header_image_url'], caption=songdata['result']['full_title'])
        else:
            bot.send_message(chat_id=update.message.chat_id, text=songdata['result']['full_title'])
        bot.send_message(chat_id=update.message.chat_id, 
            text=lyrics.replace("[", "<b>[").replace("]", "]</b>"), 
            parse_mode=telegram.ParseMode.HTML)
    except IndexError:
        bot.send_message(chat_id=update.message.chat_id, 
        text="Lyrics not found for your song :(")
        pass


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
