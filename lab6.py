# Daniel Rodriguez
# Encode string of 8 numbers by shifting each digit up by 3
def encode(pwd):
    encoded_pwd = ''
    for digit in pwd:
        encoded_pwd += str(int(digit) + 3)
    return encoded_pwd

if __name__ == '__main__':
    encoded_pwd = None
    while True:
        print('Menu')
        print('------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit\n')
        option = int(input('Please enter an option: '))

        if option == 1:
            pwd = input('Please enter your password to encode: ')
            encoded_pwd = encode(pwd)
            print('Your password has been encoded and stored!')
        elif option == 2:
            decoded_pwd = '' #FIXME
            print(f'The encoded password is {encoded_pwd}, and the original password is {decoded_pwd}.')
        elif option == 3:
            break        
        print()