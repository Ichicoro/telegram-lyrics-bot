from PyLyrics import *

def getLyrics(songartist, songname):
    try:
        return PyLyrics.getLyrics(songartist,songname)  # Try returning the lyrics directly
    except ValueError:
        return "lyrics not found"                       # We might not find anything tho D:


if __name__ == "__main__":
    print(getLyrics("Dragonforce", "Through the fire and flames"))  # On a cold winter morning...
