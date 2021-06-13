"""
This is a simple example of using data structures and loops.

Code reformatting needed
"""




import random
from enum import Enum
from time import sleep


def find_approx_value(value, percent_range):
    lowest_value = value - (percent_range / 100) * value
    highest_value = value + (percent_range / 100) * value
    return random.randint(lowest_value, highest_value)


event = Enum('Event', ['Black', 'NotBlack'])

event_dictionary = {
    event.Black: 0.4,
    event.NotBlack: 0.6
}

event_list = list(event_dictionary.keys())
event_probability = list(event_dictionary.values())

colours = Enum('Colours', {'Yellow': 'yellow',
                           'Green': 'green',
                           'Red': 'red',
                           'Purple': 'purple',
                           'White': 'white'
                           }
               )

dice_colours_dictionary = {
    colours.Yellow: 0.65,
    colours.Green: 0.15,
    colours.Red: 0.1,
    colours.Purple: 0.08,
    colours.White: 0.02
}

dice_colours_list = list(dice_colours_dictionary.keys())
dice_colours_prob = list(dice_colours_dictionary.values())

rewards_for_colour = {dice_colours_list[reward]: (reward + 1) * (reward + 1) * 1000
                      for reward in range(len(dice_colours_list))
                      }


print("""Welcome to my game, Stranger!
         You will roll a dice. Black dice result gives nothing.
         Let's see how much gold you gonna acquire till the end!""")


def play():
    turns = 0
    gold_acquired = 0

    while True:
        gamer_answer = input("Do you want roll the dice?[Y/N]").lower()

        if gamer_answer == 'y':
            print("\nLet's see what you got...\n")
            sleep(1)
            rolled_event = random.choices(event_list, event_probability)[0]

            if rolled_event == event.NotBlack:
                rolled_colour = random.choices(dice_colours_list, dice_colours_prob)[0]
                print("Congratulations, you have rolled", rolled_colour.value, "dice.")
                gamer_reward = find_approx_value(rewards_for_colour[rolled_colour], 10)
                print('You have acquired ', gamer_reward, 'in this turn.')
                gold_acquired += gamer_reward

            elif rolled_event == event.Black:
                print("You have rolled black dice. You have acquired nothing.")

        elif gamer_answer == 'n':
            print("\nSo, goodbye :(")
            break

        turns += 1

    return turns, gold_acquired


if __name__ == "__main__":
    turns, gold_acquired = play()
    print(f'You rolled dice {turns} times. You acquired: {gold_acquired}. Congratulations!')
