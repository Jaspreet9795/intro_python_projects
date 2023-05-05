# GOAL
# Create a program that prints out every line to the song "99 bottles of beer on the wall." This should be a pretty simple program, so to make it a bit harder, here are some rules to follow.

# RULES
# If you are going to use a list for all of the numbers, do not manually type them all in. Instead, use a built in function.
# Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
# Remember, when you reach 1 bottle left, the word "bottles" becomes singular.
# Put a blank line between each verse of the song.


# 99 bottles of beer on the wall, 99 bottles of beer.
# Take one down and pass it around, 98 bottles of beer on the wall.
def bottles():
    for i in range(99,0,-1):
        if i==1:
            print("1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\n")
        else:
             print(str(i)+" bottles of beer on the wall, " +str(i) + " bottles of beer.\nTake one down and pass it around, " +str(i-1)+ " bottles of beer on the wall.\n" )
bottles()