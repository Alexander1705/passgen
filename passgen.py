#!/usr/bin/env python3

import argparse
import secrets

alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
alphabet = ''.join(alphabet)

all_chars = alphabet + alphabet.upper()

vowels = 'aoeiuAOEIU'
consonants = [l for l in all_chars if l not in vowels]

def generate_password(length):
    password = ''

    for _ in range(length):
        if password and password[-1] in vowels:
            password += secrets.choice(consonants)
        elif (len(password) > 1 and
              password[-1] in consonants and
              password[-2] in consonants):
            password += secrets.choice(vowels)
        else:
            password += secrets.choice(all_chars)

    return password

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Securely generate simple passwords.')

    parser.add_argument(
        '-l', '--length',
        metavar='LENGTH',
        type=int, default=8,
        help='set length of generated passwords',
        dest='length',
    )

    parser.add_argument(
        '-n', '--count',
        metavar='COUNT',
        type=int, default=16,
        help='set number of generated passwords',
        dest='count',
    )

    parser.add_argument(
        '-p', '--per-line',
        metavar='COUNT',
        type=int, default=4,
        help='set number of passwords displayed at one line',
        dest='per_line',
    )

    args = parser.parse_args()

    passwords = [generate_password(args.length) for _ in range(args.count)]

    while passwords:
        n = min(args.per_line, len(passwords))
        print(' '.join(passwords[:n]))
        passwords = passwords[n:]
