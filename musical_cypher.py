from __future__ import annotations
import sys, string

INTRA_WORD_SEPERATOR = ':'
INTER_WORD_SEPERATOR = ' '
GROUND_NOTES = 'CDEFGAB'
def create_mapping():
    """Generates mapping of A, B ... Z to A1, B1 ... G4"""
    mapping = {}
    octave = 0
    for ii_letter, letter in enumerate(string.ascii_lowercase):

        current_ground_note_index = ii_letter % len(GROUND_NOTES)
        if current_ground_note_index == 0:
            octave += 1

        current_ground_note = GROUND_NOTES[current_ground_note_index]
        mapping[letter] = f"{current_ground_note}{octave}"

    return mapping

ALPABET_TO_NOTES_MAP = create_mapping()
NOTES_TO_ALPHABET_MAP = {value: key for key, value in ALPABET_TO_NOTES_MAP.items()}

def decode(args: list[str]):
    """Decodes a list of words represented as musical notes (mapped from the (latin) alphabetic). Can't handle punctuation."""
    words = []
    for arg in args:
        words.append(''.join(NOTES_TO_ALPHABET_MAP[note] for note in arg.split(INTRA_WORD_SEPERATOR)))
    return ' '.join(words)

def encode(args: list[str]):
    """Encodes a list of words in the latin alphabet to musical notes (A -> C1, B -> D1, ..., H -> C2, I -> D2, ... Z -> C4). Can't handle punctuation."""
    words = []

    for arg in args:
        word = INTRA_WORD_SEPERATOR.join([ALPABET_TO_NOTES_MAP[letter.upper()] for letter in arg])
        words.append(word)

    translation = INTER_WORD_SEPERATOR.join(words)
    return translation


def main():

    args = sys.argv[1:]
    if not args:
        print("You need to provide a sentence to [en|decode]...")
        sys.exit(1)
    if args[0].lower() in ('--reverse', '-r'):
        result = decode(args[1:])
    else:
        result = encode(args)

    print(result)


if __name__ == '__main__':
    main()
