from termcolor import colored
import pyfiglet


def ascii_art():
    message = input('Type in message: ')

    colors = ['grey', 'red', 'green', 'yellow',
              'blue', 'magenta', 'cyan', 'white']

    for color in colors:
        print(color)

    col = input('Which color? ')

    while col not in colors:
        col = input(
            'hey dawg, we dont got that color, scroll your ass up and choose one of the colors ')

    result = pyfiglet.figlet_format(message)
    return colored(result, color=col)


print(ascii_art())
