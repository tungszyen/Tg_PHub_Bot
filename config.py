HEROKU = False  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku.
if HEROKU:
    from os import environ

    Bot_token = environ["Bot_token"]
    ARQ_API_KEY = environ["ARQ_API_KEY"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    Bot_token = "5037896180:AAHi3GyUiUjo8XWGkL69Jc13OObLIZXgwyk"
    ARQ_API_KEY = "IYXBEO-IGEQZC-XLRGWO-GAAEZR-ARQ"
