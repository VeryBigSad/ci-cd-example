import time


def print_greeting():
    return "Hello, World!"


if __name__ == "__main__":
    while True:
        message = print_greeting()
        print(message)
        time.sleep(2)
