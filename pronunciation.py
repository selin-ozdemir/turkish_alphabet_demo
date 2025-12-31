# turkish_pronunciation.py

def translate_turkish(text):
    rules = {
        'c': 'j', 'ç': 'ch', 'ğ': '', 'ı': 'uh', 'i': 'ee', 'İ': 'ee',
        'j': 'zh', 'ö': 'uh', 'ş': 'sh', 'ü': 'ew', 'u': 'oo',
        'C': 'J', 'Ç': 'Ch', 'Ğ': '', 'I': 'Uh', 'Ö': 'Uh',
        'Ş': 'Sh', 'Ü': 'Ew', 'U': 'Oo'
    }
    result = ''.join(rules.get(char, char) for char in text)
    return result

# Run it
while True:
    word = input("\nEnter Turkish word (or 'quit' to exit): ")
    if word.lower() == 'quit':
        break
    print(f"Pronunciation: {translate_turkish(word)}")

# This program translates Turkish text into a phonetic representation.


