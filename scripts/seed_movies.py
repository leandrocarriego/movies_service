import requests


API_URL = "http://localhost:8000/api/v1/movies/"

movies = [
    "Inception",
    "The Dark Knight",
    "Interstellar",
    "Parasite",
    "Whiplash",
    "The Social Network",
    "Mad Max: Fury Road",
    "Spider-Man: Into the Spider-Verse",
    "The Grand Budapest Hotel",
    "Get Out",
    "Joker",
    "The Wolf of Wall Street",
    "Avengers: Endgame",
    "La La Land",
    "Django Unchained",
    "1917",
    "The Irishman",
    "Toy Story 3",
    "The Revenant",
    "Shutter Island",
    "Once Upon a Time in Hollywood",
    "Her",
    "Ford v Ferrari",
    "Black Panther",
    "Guardians of the Galaxy",
    "Logan",
    "Blade Runner 2049",
    "Marriage Story",
    "Tenet",
    "A Quiet Place",
    "Inside Out",
    "The Big Short",
    "The Martian",
    "Moonlight",
    "Birdman",
    "Dune",
    "Arrival",
    "Knives Out",
    "Soul",
    "Jojo Rabbit",
]


def create_movies():
    for title in movies:
        response = requests.post(API_URL, json={"title": title})
        if response.status_code == 201:
            print(f"Creada '{title}'")
        else:
            print(f"Error '{title}': {response.json()}")


create_movies()
