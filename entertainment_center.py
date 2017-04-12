import media
import fresh_tomatoes

# Create movie instance for Toy Story
john_wick = media.Movie("John Wick",
                        "An ex-hitman comes out of retirement to track down the gangsters that took everything from him.",
                        "https://upload.wikimedia.org/wikipedia/en/9/98/John_Wick_TeaserPoster.jpg",
                        "https://www.youtube.com/watch?v=2AUmvWm5ZDQ")

# Create movie instance for Avatar
fist_fight = media.Movie("Fist Fight",
                         " When one school teacher gets the other fired, he is challenged to an after-school fight. ",
                         "https://upload.wikimedia.org/wikipedia/en/b/b2/Fist_Fight.png",
                         "https://www.youtube.com/watch?v=6YVBj2o_3mg")

# Create movie instance for Office Christmas Party
office_xmas_party = media.Movie("Office Christmas Party",
                                "When his uptight CEO sister threatens to shut down his"
                                " branch, the branch manager throws an epic Christmas"
                                " party in order to land a big client and save the day,"
                                " but the party gets way out of hand...",
                                "https://upload.wikimedia.org/wikipedia/en/8/8a/Office_Christmas_Party.png",
                                "https://www.youtube.com/watch?v=z4PHjxRiT2I")

# Create movie instance for This is 40
this_is_40 = media.Movie("This is 40", "Pete and Debbie are both about to turn 40, their kids hate each other, both of"
                                       " their businesses are failing, they're on the verge of losing their house, and"
                                       " their relationship is threatening to fall apart.",
                         "https://upload.wikimedia.org/wikipedia/en/e/eb/This_is_40.jpg",
                         "https://www.youtube.com/watch?v=6sGkPwrze0o")

# Create movie instance for Skyfall
skyfall = media.Movie("Skyfall", "Bond's loyalty to M is tested when her past comes back to haunt her."
                                 " Whilst MI6 comes under attack, 007 must track down and destroy the"
                                 " threat, no matter how personal the cost.",
                      "https://upload.wikimedia.org/wikipedia/en/a/a7/Skyfall_poster.jpg",
                      "https://www.youtube.com/watch?v=24mTIE4D9JM")

# Create movie instance for Deadpool
deadpool = media.Movie("Deadpool", "A fast-talking mercenary with a morbid sense of humor is subjected to a rogue"
                                   " experiment that leaves him with accelerated healing powers and a quest for revenge.",
                       "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
                       "https://www.youtube.com/watch?v=ONHBaC-pfsk")

# Create list of favorite movie  instances
movies = [john_wick, fist_fight, office_xmas_party, this_is_40, skyfall, deadpool]

# Pass list of movies to generate website to display movies
fresh_tomatoes.open_movies_page(movies)
