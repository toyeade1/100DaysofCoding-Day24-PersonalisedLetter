# This program appends the name part of a letter so it can address whoever the letter is being sent to. The hardest part was finding the path file but pycharm helps a lot with that.

PLACEHOLDER = '[name]'

with open('../../Downloads/Mail Merge Project Start/Input/Names/invited_names.txt', mode='r') as file:
    names_to_append = file.readlines()

with open('../../Downloads/Mail Merge Project Start/Input/Letters/starting_letter.txt') as letter:
    lines_in_letter = letter.read()

for name in names_to_append:
    stripped_name = name.strip()
    new_letter = lines_in_letter.replace(PLACEHOLDER, stripped_name)
    with open(f'./Output/ReadyToSend/letter_for_{stripped_name}.txt', mode='w') as completed_letter:
        completed_letter.write(new_letter)


