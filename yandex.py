import yadisk


def yandex(TOKEN):

    y = yadisk.YaDisk(token=TOKEN)

    if y.exists('TESTS'):
        y.remove('TESTS', permanently = True)
    print('Папка TESTS перезаписана')
    #y.mkdir(f'TESTS')
    print(y.exists('TESTS'))
    return y.mkdir(f'TESTS')

if __name__ == '__main__':

    with open('tests/TOKEN.txt', 'r') as token_file:
        TOKEN = token_file.readline()
    yandex(TOKEN)
