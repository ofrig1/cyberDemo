import sys
import logging


def main():
    logging.basicConfig(filename="main.log", level=logging.DEBUG)
    logger = logging.getLogger('my_logger')
    if len(sys.argv) == 1:
        msg = input("Please enter the msg you would like to encrypt/decrypt: ")
        logger.debug("from input")
    else:
        logger.debug("take input from command line")
        msg = sys.argv[1]
    dict_encrypt = {
        'A': 56,
        'B': 57,
        'C': 58,
        'D': 59,
        'E': 40,
        'F': 41,
        'G': 42,
        'H': 43,
        'I': 44,
        'J': 45,
        'K': 46,
        'L': 47,
        'M': 48,
        'N': 49,
        'O': 60,
        'P': 61,
        'Q': 62,
        'R': 63,
        'S': 64,
        'T': 65,
        'U': 66,
        'V': 67,
        'W': 68,
        'X': 69,
        'Y': 10,
        'Z': 11,
        'a': 12,
        'b': 13,
        'c': 14,
        'd': 15,
        'e': 16,
        'f': 17,
        'g': 18,
        'h': 19,
        'i': 30,
        'j': 31,
        'k': 32,
        'l': 33,
        'm': 34,
        'n': 35,
        'o': 36,
        'p': 37,
        'q': 38,
        'r': 39,
        's': 90,
        't': 91,
        'u': 92,
        'v': 93,
        'w': 94,
        'x': 95,
        'y': 96,
        'z': 97,
        ' ': 98,
        ',': 99,
        '.': 100,
        ';': 101,
        "'": 102,
        '?': 103,
        '!': 104,
        ':': 105
    }
    dict_decrypt = {
        '56': 'A',
        '57': 'B',
        '58': 'C',
        '59': 'D',
        '40': 'E',
        '41': 'F',
        '42': 'G',
        '43': 'H',
        '44': 'I',
        '45': 'J',
        '46': 'K',
        '47': 'L',
        '48': 'M',
        '49': 'N',
        '60': 'O',
        '61': 'P',
        '62': 'Q',
        '63': 'R',
        '64': 'S',
        '65': 'T',
        '66': 'U',
        '67': 'V',
        '68': 'W',
        '69': 'X',
        '10': 'Y',
        '11': 'Z',
        '12': 'a',
        '13': 'b',
        '14': 'c',
        '15': 'd',
        '16': 'e',
        '17': 'f',
        '18': 'g',
        '19': 'h',
        '30': 'i',
        '31': 'j',
        '32': 'k',
        '33': 'l',
        '34': 'm',
        '35': 'n',
        '36': 'o',
        '37': 'p',
        '38': 'q',
        '39': 'r',
        '90': 's',
        '91': 't',
        '92': 'u',
        '93': 'v',
        '94': 'w',
        '95': 'x',
        '96': 'y',
        '97': 'z',
        '98': ' ',
        '99': ',',
        '100': '.',
        '101': ';',
        '102': "'",
        '103': '?',
        '104': '!',
        '105': ':',
    }
    try:
        if not msg:
            print("")
            logger.debug("Empty message")
        elif (msg >= '0') and (msg <= '9'):
            msg_decrypt = msg.split(',')
            for item in msg_decrypt:
                print(dict_decrypt[item], end='')
            logger.debug("Decrypt")
        else:
            for char in msg:
                print(dict_encrypt[char], end=",")
            logger.debug("Encrypt")
    except Exception as e:
        print()
        print(f"error: {e}")
        logger.debug("Error")


if __name__ == "__main__":
    main()
