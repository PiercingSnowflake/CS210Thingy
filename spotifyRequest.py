import requests
import base64
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from io import BytesIO

def requestArtist(artistID, accessToken):
    # Replace 'your_artist_id' with the actual Spotify Artist ID
    endpoint = f'https://api.spotify.com/v1/artists/{artistID}'

    # Include the access token in the Authorization header
    headers = {'Authorization': f'Bearer {accessToken}'}

    # Make GET request to get artist information
    response = requests.get(endpoint, headers=headers)
    if response.status_code == 200:
        # Print the artist information
        artistData = response.json()
        artistName = artistData.get("name")
        artistImages = artistData.get("images")
        greatestArtistImage = artistImages[0]
        imageURL = greatestArtistImage.get("url")
        """
        responseOfURL = requests.get(imageURL)
        image = mpimg.imread(BytesIO(responseOfURL.content))
        plt.imshow(image)
        plt.show()
        """

        print(artistData, "\n", artistName , "\n", imageURL)

    else:
        print("There is no such artist")

with open('activeSpotifyAccessToken.txt', 'r') as file:
    accessToken = file.read()

ArtistCheck = True
while(ArtistCheck):
    userInput= input("Please enter an artist URI or type 'Exit' to terminate the process: ")
    validity = userInput.startswith("spotify:artist:")
    if validity:
        userInputStripped=userInput.strip("spotify:artist:")
        requestArtist(userInputStripped, accessToken)
    elif userInput == "exit":
        ArtistCheck = False
    else:
        print("Please enter a valid Spotify URI")



#Sakuzyo = requestArtist("53BVcGSlpWPF7iYsSN0Oe1", accessToken)
#spotify:artist:53BVcGSlpWPF7iYsSN0Oe1
#spotify:artist:6RTC1abMgBC7Krg6qJQHJh
