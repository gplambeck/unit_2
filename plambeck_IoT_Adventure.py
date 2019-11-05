from microbit import *

# Animation of a boat sinking
# boat1 = Image("05050:"
#               "05050:"
#               "05050:"
#               "99999:"
#               "09990")

# boat2 = Image("00000:"
#               "05050:"
#               "05050:"
#               "05050:"
#               "99999")

# boat3 = Image("00000:"
#               "00000:"
#               "05050:"
#               "05050:"
#               "05050")

# boat4 = Image("00000:"
#               "00000:"
#               "00000:"
#               "05050:"
#               "05050")

# boat5 = Image("00000:"
#               "00000:"
#               "00000:"
#               "00000:"
#               "05050")

# boat6 = Image("00000:"
#               "00000:"
#               "00000:"
#               "00000:"
#               "00000")

# all_boats = [boat1, boat2, boat3, boat4, boat5, boat6]
# display.show(all_boats, delay=200)

# Improvement
# Image fades out and then fades in again.
# boat1 = Image("05050:"
#               "05050:"
#               "05050:"
#               "99999:"
#               "09990")

# boat2 = Image("05050:"
#               "05050:"
#               "00000:"
#               "99999:"
#               "09990")

# boat3 = Image("05050:"
#               "00000:"
#               "00000:"
#               "00000:"
#               "99999")

# boat4 = Image("00000:"
#               "00000:"
#               "00000:"
#               "00000:"
#               "00000")

# boat5 = Image("05050:"
#               "00000:"
#               "00000:"
#               "00000:"
#               "99999")

# boat6 = Image("05050:"
#               "05050:"
#               "00000:"
#               "99999:"
#               "09990")
              
# boat7 = Image("05050:"
#               "05050:"
#               "05050:"
#               "99999:"
#               "09990")             

# all_boats = [boat1, boat2, boat3, boat4, boat5, boat6, boat7]
# display.show(all_boats, loop=True, delay=200)


# IoT Prototype
# Shake to hear music or push a to see a message.
# import random, music

# # Complete list of built-in melodies listed on
# # https://microbit-micropython.readthedocs.io/en/latest/tutorials/music.html
# tune = [music.DADADADUM, music.ENTERTAINER, music.PRELUDE, music.ODE, music.NYAN,
#         music.RINGTONE, music.FUNK, music.BLUES, music.BIRTHDAY, music.WEDDING,
#         music.FUNERAL, music.PUNCHLINE, music.PYTHON, music.BADDY, music.CHASE,
#         music.BA_DING, music.WAWAWAWAA, music.JUMP_UP, music.JUMP_DOWN,
#         music.POWER_UP, music.POWER_DOWN]

# s1 = "General Kenobi. "
# s2 = "Years ago you served my father in the Clone Wars. "
# s3 = "Now he begs you to help him in his struggle against the Empire. "
# s4 = "I regret that I am unable to present my father's request to you in person, but my ship has fallen under attack, and I'm afraid my mission to bring you to Alderaan has failed. "
# s5 = "I have placed information vital to the survival of the Rebellion into the memory systems of this micro:bit. "
# s6 = "My father will know how to retrieve it. "
# s7 = "You must see this micro:bit safely delivered to him on Alderaan. "
# s8 = "This is our most desperate hour. "
# s9 = "Help me, Obi-Wan Kenobi. "
# s10 = "You're my only hope."

# def userInput():
#     while True:
#         # Shake micro:bit to play music.
#         # shake code from https://microbit-micropython.readthedocs.io/en/latest/tutorials/gestures.html
#         if accelerometer.was_gesture("shake"):
#             music.play(random.choice(tune))

#         # Display a message when button a is pressed.
#         # button press code from https://microbit-micropython.readthedocs.io/en/latest/button.html
#         elif button_a.was_pressed():
#             # scrolling display code from https://microbit-micropython.readthedocs.io/en/latest/tutorials/buttons.html
#             display.scroll(s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10)

# userInput()
