import regex as re

while True:
    try:
        words_set = {word for word in re.split(r'\W+', input("Insert your text here: ").lower()) if word}
        break
    except Exception as e:
        print(f"Sorry the probles is {e}. Try again!!")

for word in sorted(words_set):
    print(f'* {word}')

