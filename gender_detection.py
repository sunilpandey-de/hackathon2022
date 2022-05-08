
def gender_guess(gender_map):
    #Male
    male_title=['mr.','sir','master','mr','he','him']
    #### Female
    female_title=['mrs.','ms.','miss','lady','mrs','ms','madam','she','her']

    for title in gender_map:
        if title in male_title:
            return 'male'
        elif title in female_title:
            return 'female'
        else:
            return('unknown')
            break

from genderize import Genderize
print(Genderize().get(['praveen']))

print(gender_guess(['she']))