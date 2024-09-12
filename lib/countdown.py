# your code goes here!
import time
def countdown(number):
    while number > 0:
        if number == 1:
            print(f"{number} SECOND!")
        else:
            print(f"{number} SECONDS!")
            number -=1
            print("HAPPY NEW YEAR!")


def countdown_with_sleep(number):
    while number > 0:
        if number == 1:
            print(f'{number} SECOND!')
        else:
            print(f'{number} SECONDS!')
        time.sleep(1)  # Pause for 1 second
        number -= 1
    print("HAPPY NEW YEAR!")

countdown_with_sleep(10)