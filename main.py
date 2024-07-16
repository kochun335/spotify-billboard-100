from pprint import pprint

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"
scope = "playlist-modify-private"
client_id = "c18cc120704040d881aae1c97dab0bcc"
client_secret = "36b6cb24eb6e405f91174e599e33291e"

date = input("What year do you want to travel back to? (YYYY-MM-DDDD): ")
year = int(date[0:4])
year_range = f"{year-5}-{year+5}"
print(year_range)

billboard_html = requests.get(f"{BILLBOARD_URL}{date}/")
soup = BeautifulSoup(billboard_html.text, "html.parser")
#song_list_with_tags = soup.find_all(name="h3", id="title-of-a-story", class_="c-title")
song_list_with_tags = soup.select("li > h3#title-of-a-story")
song_list = [song.getText().strip() for song in song_list_with_tags]
print(song_list)
print(len(song_list))

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri="https://example.com/callback"))
user_id = sp.current_user()['id']

uri_list = []

for song in song_list:
    results = sp.search(q=f'track:{song} year:{year_range}', type='track')
    try:
        uri_list.append(results["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"Song {song} in year {year} not found on Spotify")
        results_without_year = sp.search(q=f'track:{song}', type='track')
        try:
            uri_list.append(results_without_year["tracks"]["items"][0]["uri"])
        except IndexError:
            print(f"=====Song {song} not found on Spotify!=====")

# uri_list = ['spotify:artist:43ZHCT0cAZBISjO8DG9PnE', 'spotify:artist:1UUYAQ9LiRsZF0ZukQNWXM', 'spotify:artist:7guDJrEfX3qb6FEbdPA5qi', 'spotify:artist:3RwQ26hR2tJtA8F9p2n7jG', 'spotify:artist:67ea9eGLXYMsO2eYQRui3w', 'spotify:artist:5m8H6zSadhu1j9Yi04VLqD', 'spotify:artist:3sFhA6G1N0gG1pszb6kk1m', 'spotify:artist:0oSGxfWSnnOXhD2fKuz2Gy', 'spotify:artist:1VKy7hIBFmlBnfKPgPkuLH', 'spotify:artist:2DghgxF3jV3G5xfcTpZpKr', 'spotify:artist:3WrFJ7ztbogyGnTHbHJFl2', 'spotify:artist:1IAnol1a8KjeHfkSOaFe2S', 'spotify:artist:602DnpaSXJB4b9DZrvxbDc', 'spotify:artist:5xLSa7l4IV1gsQfhAMvl0U', 'spotify:artist:5bLcI9Jo6RyrrHzG9veVyn', 'spotify:artist:2KK4fR5VwOjGzJxjbGxMIu', 'spotify:artist:24GaH9tRBgZjlvOhpFuKi2', 'spotify:artist:43ZHCT0cAZBISjO8DG9PnE', 'spotify:artist:1T0wRBO0CK0vK8ouUMqEl5', 'spotify:artist:7kur1FACDVzvkdJFrliSzX', 'spotify:artist:1BdNzKPyPDOhHdFhvwytQt', 'spotify:artist:11EZGTWr2pY0VZPlWokAbl', 'spotify:artist:4FAEZeJcsYYBkNq2D3KGTV', 'spotify:artist:01hRNr3yF5bYnPq4wZ88iI', 'spotify:artist:3lQpSzdPxoF1FYk7ilbe37', 'spotify:artist:2zyz0VJqrDXeFDIyrfVXSo', 'spotify:artist:4asCC4oxQcDzFXhCth2SgQ', 'spotify:artist:7gi3jmwpUpNWdswT8eEprF', 'spotify:artist:70ZTdbPEcEugBNay4MvxfL', 'spotify:artist:7GaxyUddsPok8BuhxN6OUW', 'spotify:artist:3IKV7o6WPphDB7cCWXaG3E', 'spotify:artist:7guDJrEfX3qb6FEbdPA5qi', 'spotify:artist:59hLmB5DrdihCYtNeFeW1U', 'spotify:artist:2pdvghEHZJtgSXZ7cvNLou', 'spotify:artist:1P9syEkl41IFowWIJN7ZBY', 'spotify:artist:2M91bpXBMUp6DUvSwCn6wh', 'spotify:artist:1USHlPahTZrCeJXS2v5pkF', 'spotify:artist:4WFTfNjxQYskBioYk39r9n', 'spotify:artist:0GQkTwFb7D3ePIpnxwYavf', 'spotify:artist:1EtaYpGNKSdI7fYF1CqYfz', 'spotify:artist:22WZ7M8sxp5THdruNY3gXt', 'spotify:artist:2ubLClBEuddw29m7QRx4IL', 'spotify:artist:24uSD486ywQ4VJ2OMDXv8y', 'spotify:artist:2AV6XDIs32ofIJhkkDevjm', 'spotify:artist:02oFrWT7l0AKMEnJI6iTIB', 'spotify:artist:24qtJegdRiX2TPRvPN6rzk', 'spotify:artist:7s2L0cftC6UBVVxADuyfwS', 'spotify:artist:2vDV0T8sxx2ENnKXds75e5', 'spotify:artist:0qEcf3SFlpRcb3lK3f2GZI', 'spotify:artist:4FAEZeJcsYYBkNq2D3KGTV', 'spotify:artist:0cQuYRSzlItquYxsQKDvVc', 'spotify:artist:4MUVyyvIuoljgT4cDIhjLa', 'spotify:artist:7kSG6Dyyvf4MM8qWWrgKJq', 'spotify:artist:0JDkhL4rjiPNEp92jAgJnS', 'spotify:artist:5jX7X3kRkfJTRqAdT7RcHk', 'spotify:artist:6yrBBtqX2gKCHCrZOYBDrB', 'spotify:artist:3IYUhFvPQItj6xySrBmZkd', 'spotify:artist:3VNITwohbvU5Wuy5PC6dsI', 'spotify:artist:3KGQvnOoqUHi3KxKQMZtXr', 'spotify:artist:2eHFawPAARjoxXETpHGQ0Y', 'spotify:artist:0LyfQWJT6nXafLPZqxe9Of', 'spotify:artist:6QvgWa4x3Ij4tvBpFMo11P', 'spotify:artist:3i9hP422d2KMjaupTzBNVS', 'spotify:artist:3RwQ26hR2tJtA8F9p2n7jG', 'spotify:artist:1SQRv42e4PjEYfPhS0Tk9E', 'spotify:artist:0cQuYRSzlItquYxsQKDvVc', 'spotify:artist:3IYUhFvPQItj6xySrBmZkd', 'spotify:artist:5JJxBX97vBHW7KMsBqIJre', 'spotify:artist:7mEIug7XUlQHikrFxjTWes', 'spotify:artist:30ubKuh11o6hVK83WNBgm0', 'spotify:artist:3pFCERyEiP5xeN2EsPXhjI', 'spotify:artist:4vpDg7Y7fU982Ds30zawDA', 'spotify:artist:1sXbwvCQLGZnaH0Jp2HTVc', 'spotify:artist:5M52tdBnJaKSvOpJGz8mfZ', 'spotify:artist:73sSFVlM6pkweLXE8qw1OS', 'spotify:artist:5zaXYwewAXedKNCff45U5l', 'spotify:artist:530Sdm7eqqzWBdDmILMgnu', 'spotify:artist:6kACVPfCOnqzgfEF5ryl0x', 'spotify:artist:60df5JBRRPcnSpsIMxxwQm', 'spotify:artist:3RTzAwFprBqiskp550eSJX', 'spotify:artist:3XQexYaGsSsNNEpsdLfJ2l', 'spotify:artist:0AD4odMWVQ2wUSlgxOB5Rl', 'spotify:artist:17XXKfRBMCWvLrqGoNkJXm', 'spotify:artist:1NqEdHZu5o9r4I37uGUNHI', 'spotify:artist:1b1N51wmSK0ckxFAMPSSHO', 'spotify:artist:19eLuQmk9aCobbVDHc6eek', 'spotify:artist:0iVed2Qu7dmL0pIYCj1Xw8', 'spotify:artist:3mSAqBoXQgdlpwzWsIgBzL', 'spotify:artist:1PCZpxHJz7WAMF8EEq8bfc', 'spotify:artist:1BdNzKPyPDOhHdFhvwytQt', 'spotify:artist:3IKV7o6WPphDB7cCWXaG3E', 'spotify:artist:74ASZWbe4lXaubB36ztrGX', 'spotify:artist:6GI52t8N5F02MxU0g5U69P', 'spotify:artist:6Bfy6QzadCXS92y0T8dDZF', 'spotify:artist:3RTzAwFprBqiskp550eSJX', 'spotify:artist:5zaXYwewAXedKNCff45U5l']

print(uri_list)

playlist_cr_res = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
pprint(playlist_cr_res)
playlist_id = playlist_cr_res['id']
sp.playlist_add_items(playlist_id=playlist_id, items=uri_list)
