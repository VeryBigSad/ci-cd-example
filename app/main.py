import time


def print_greeting():
    return "Hello, World! <злостная бага>"


if __name__ == "__main__":
    while True:
        message = print_greeting()
        print(message)
        time.sleep(2)
