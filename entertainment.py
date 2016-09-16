import fresh_tomatoes
import movie

dark_knight = movie.Movie("The Dark Night",
                         "When the menace known as the Joker wreaks havoc and chaos"
                         " on the people of Gotham, the caped crusader must come to terms"
                         "with one of the greatest psychological tests of his ability to fight injustice.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg", # noqa
                         "https://youtu.be/EXeTwQWrcwY")

mad_max = movie.Movie("Mad Max Fury Road",
                      "A woman rebels against a tyrannical ruler in postapocalyptic Australia"
                      "in search for her home-land with the help of a group of female prisoners,"
                      "a psychotic worshipper, and a drifter named Max.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUyMTE0ODcxNF5BMl5BanBnXkFtZTgwODE4NDQzNTE@._V1_SY1000_CR0,0,687,1000_AL_.jpg", # noqa
                      "https://youtu.be/hEJnMQG9ev8")

inception = movie.Movie("Inception",
                        "A thief, who steals corporate secrets through use of dream-sharing "
                        "technology, is given the inverse task of planting an idea into "
                        "the mind of a CEO.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg", # noqa
                        "https://youtu.be/8hP9D6kZseM")

godfather = movie.Movie("Godfather",
                        "The aging patriarch of an organized crime dynasty transfers control "
                        "of his clandestine empire to his reluctant son.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjEyMjcyNDI4MF5BMl5BanBnXkFtZTcwMDA5Mzg3OA@@._V1_.jpg", # noqa
                        "https://youtu.be/sY1S34973zA")

scarface = movie.Movie("Scarface",
                        "In Miami in 1980, a determined Cuban immigrant takes over a drug "
                       "cartel and succumbs to greed.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAzOTM4MzEwNl5BMl5BanBnXkFtZTgwMzU1OTc1MDE@._V1_.jpg", # noqa
                        "https://youtu.be/7pQQHnqBa2E")

creed = movie.Movie("Creed",
                    "The former World Heavyweight Champion Rocky Balboa serves as a trainer and "
                    "mentor to Adonis Johnson, the son of his late friend and former "
                    "rival Apollo Creed.",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BODg5NDM1MDI4NF5BMl5BanBnXkFtZTgwMzg0MzQxNzE@._V1_SY1000_CR0,0,674,1000_AL_.jpg", # noqa
                    "https://youtu.be/Uv554B7YHk4")

#the following is a list of all the movies that will end up being passed through to be presented
#in order to be displayed
movie_list = [dark_knight, mad_max, inception, godfather, scarface, creed]

#The follwoing function call what is going to be setting up the html document that is going to be
#displaying the movies in the browser
fresh_tomatoes.open_movies_page(movie_list)

