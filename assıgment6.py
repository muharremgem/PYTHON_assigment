#Task : Find out if the given word is "comfortable words" in relation to the ten-finger keyboard use.A comfortable word is a word which you can type always alternating the hand you type with (assuming you type using a Q-keyboard and use of the ten-fingers standard).The word will always be a string consisting of only letters from a to z.Write a program which returns True if it's a comfortable word or False otherwise.
#####################



left_hand = {"q", "w", "e", "r", "t", "g", "b", "v", "c", "x", "z", "a", "s", "d", "f"}
right_hand = {"y", "u", "i", "o", "p", "l", "k", "j", "h", "n", "m"}
text = set(input("a:"))
print(text.intersection(left_hand) != text and text.intersection(right_hand) != text)




