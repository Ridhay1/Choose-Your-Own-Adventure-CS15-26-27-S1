user_choice = None

story = """
You are playing in the championship match of a volleyball tournament.

The opponent hits a straight ball high over the net toward your court. 

Your back row gets ready to make the first contact.

Which play do you make?

A : You get under the ball cleanly for a forearm bump pass.
OR
B : The hit comes in quick, forcing a low dig play.
"""

print(story)

user_choice = input().lower()

if user_choice == "a":
    story = """
    You pass the ball like straight perfection into the air right to your setter at the front of the net.

Your setter has a quick and wide open look at the court and needs to choose the second contact option.

A : Overhead Hand Set toward the Outside Hitter.
OR
B : Overhead Hand Set toward the outside/Right-Side Hitter.
"""
    print(story)

    user_choice = input().lower()

    if user_choice == "a":
        story = """
        The setter lofts a high, accurate ball to the front-left pin. 

The Outside Hitter times their approach, jumps high, and prepares for the attack.

A : Go for a powerful spike down the line into open space.
OR
B : Softly tip the ball over the block into the middle zone.
"""
        print(story)

        user_choice = input().lower()

        if user_choice == "a":
            story = """The hitter smashes the ball straight past the block and down onto the opponents floor! 

Point scored!

THE END
"""
            print(story)
        else:
            story = """The hitter lightly rolls the ball right over the outstretched arms of the blockers. 

It drops softly into the empty middle court before anyone can dig it.

Point scored

THE END
"""
            print(story)

    else:
        story = """The setter delivers a swift set across the court to the Opposite Hitter on the right side.

The front row defense jumps up to block.

A : Go for a heavy power hit off the blockers hands.
OR
B : roll shot the ball over the block into deep court where top right is.
"""
        print(story)

        user_choice = input().lower()

        if user_choice == "a":
            story = """The hitter drives the ball hard off the outside blockers fingertips and out of bounds.

Tool off the block! Point scored!

THE END
"""
            print(story)
        else:
            story = """The opponent's back row defender reads the tip early, dives forward, and keeps the ball alive.

The rally continues!

THE END
"""
            print(story)

else:
    story = """You barely pop the hard-driven ball up, but it drifts out of system toward the sideline.

Your setter has to chase it down for the second contact.

A : Execute a bump set back toward the middle hitter.
OR
B : The ball is too far off, so you just scramble to push a bump set safe.
"""
    print(story)

    user_choice = input().lower()

    if user_choice == "a":
        story = """The setter manages to bump set the ball up into the middle area.

The middle hitter adjusts their feet and prepares for the third contact.

A : Take a hard swing on the out-of-system ball.
OR
B : Push a safe free ball high and deep into the opponent's backcourt.
"""
        print(story)

        user_choice = input().lower()

        if user_choice == "a":
            story = """Due to the weird set, the hitter swings straight into the net tape.

Unforced error point to the opposition.

THE END
"""
            print(story)
        else:
            story = """The middle hitter lofts the ball safely over the net. 

The rally stays alive as the opponent sets up their offense.

THE END
"""
            print(story)

    else:
        story = """The setter gets under the ball late and can't direct a proper set to a hitter.

A decision must be made on the third contact.

A : Send an emergency high free ball back over the net.
OR
B : Try a scary backhand push deep into the corner.
"""
        print(story)

        user_choice = input().lower()

        if user_choice == "a":
            story = """The ball sails high over the net into deep court. 

Your team recovers into base defense as the opponent prepares their counter attack.

THE END
"""
            print(story)
        else:
            story = """The push shot goes just an inch too far and lands beyond the end line.

Out of bounds—point to the opposition.

THE END
"""
            print(story)