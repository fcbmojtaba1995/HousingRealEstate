def client():
    while True:
        client_options_input = input('Please choose search(s) or exit(e):')
        if client_options_input == 's':
            pass
        elif client_options_input == 'e':
            print('#' * 40, 'BY', '#' * 40)
            break


if __name__ == '__main__':
    print('#' * 40, 'WELCOME', '#' * 40)
    client()
