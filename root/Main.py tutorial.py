user_choice = None

story = """
Mr. Forsyth is teaching a computer science class when an alarm suddenly begins
blaring throughout the school.

A voice comes over the intercom:

"Attention. This is not a drill. We are short one astronaut."

The classroom falls silent.

A few seconds later, another announcement follows:

"Correction. We are short one astronaut who knows how to troubleshoot technology."

Every student in the room slowly turns to look at Mr. Forsyth.

Five minutes later, he finds himself being escorted onto a rocket.

The rocket launches successfully and reaches orbit.

Mission Control contacts Mr. Forsyth.

"Which would you like to investigate first?"

A : A mysterious signal coming from the Moon.
OR
B : A satellite that has suddenly stopped responding.
"""

print(story)

user_choice = input().lower()

if user_choice == "a":
    story = """
Mr. Forsyth lands near the source of the signal.

The signal leads him to a giant metal door built into the surface of the Moon.

The door has a keypad.

A : Ask why there are spare moons.
OR
B : Open one of the boxes.
"""

    print(story)
    user_choice = input().lower()

    if user_choice == "a":
        story = """
The caretaker explains that moons occasionally wear out and must be replaced.

Mr. Forsyth spends the afternoon learning things humanity was never supposed to know.

THE END
"""
        print(story)

    else:
        story = """
Inside the box is a tiny moon.

It immediately escapes and begins orbiting Mr. Forsyth's helmet.

Scientists later name it Forsyth Minor.

THE END
"""
        print(story)

else:
    story = """
Mr. Forsyth docks with the satellite.

A maintenance hatch is hanging open.

Inside he discovers a raccoon wearing a space suit.

The raccoon is eating wires.

A : Attempt to communicate with the raccoon.
OR
B : Chase the raccoon away from the wires.
"""

    print(story)
    user_choice = input().lower()

    if user_choice == "a":
        story = """
Mr. Forsyth successfully communicates with the raccoon.

The raccoon explains that it accidentally activated a mysterious button.

THE END
"""
        print(story)

    else:
        story = """
Mr. Forsyth successfully stops the raccoon.

Later inspection reveals the button would have released ten thousand rubber ducks into orbit.

Earth narrowly avoids a very unusual space age.

THE END
"""
        print(story)
