import os
import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic
import ytmusicapi

if not os.path.exists("browser.json"):
    print("browser.json not found.")
    print("You need to authenticate with YouTube Music first.")
    print("Run one of these commands in your terminal from this project folder:\n")
    print("  Mac:     pbpaste | ytmusicapi browser")
    print("  Windows: ytmusicapi browser\n")
    print("Copy the request headers from Firefox first.")
    print("This will create browser.json.")
    exit()

chosen_date = input(
    "WHat year would you like to travel to? (Type the data in this format YYYY-MM-DD): ")


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
}

response = requests.get(
    url=f"https://appbrewery.github.io/bakeboard-hot-100/{chosen_date}", headers=header)
print(response)

soup_website = BeautifulSoup(response.text, "html.parser")


song_titles = soup_website.find_all(name="h3", class_="chart-entry__title")
song_titles = [song.get_text() for song in song_titles]

yt = YTMusic("browser.json")
playlists = yt.get_library_playlists()
print(f"Found {len(playlists)} playlists in your library.")

playlist_exists = False

for playlist in playlists:
    if playlist["title"] == f"{chosen_date} Billboard 100":
        playlist_exists = True
        print("Already have a playlist with that name! (❁´◡`❁)")

if not playlist_exists:
    new_playlist = yt.create_playlist(f"{chosen_date} Billboard 100",
                                      "2017 hits baby!", "PRIVATE")

    for song in song_titles:
        try:
            search_result = yt.search(song, "songs")
            yt.add_playlist_items(
                new_playlist, [search_result[0]["videoId"]], False)
        except ytmusicapi.exceptions.YTMusicServerError:
            print(f"The song couldn't be added.")
