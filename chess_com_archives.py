# chess.com API -> https://www.chess.com/news/view/published-data-api
# The API has been used to download monthly archives for a user using a Python3 program.
# This program works as of 26/09/2018

import urllib
import urllib.request

def main(username, directory):
    baseUrl = f"https://api.chess.com/pub/player/{username}/games/"
    archivesUrl = baseUrl + "archives"

    #read the archives url and store in a list
    f = urllib.request.urlopen(archivesUrl)
    archives = f.read().decode("utf-8")
    archives = archives.replace('{"archives":["', '","')
    archives = archives.rstrip('"]}')
    archivesList = archives.split(f'","{baseUrl}')

    #download all the archives
    for i in range(len(archivesList)-1):
        url = f"{baseUrl}{archivesList[i+1]}/pgn"
        filename = f"{archivesList[i+1].replace('/', '-')}"
        urllib.request.urlretrieve(url, f"{directory}{filename}.pgn")
        print(f"{filename}.pgn has been downloaded.")
    print("All files have been downloaded.")
    
main("magnuscarlsen", f"/Users/Magnus/Desktop/THINGS/My Chess Games/")
