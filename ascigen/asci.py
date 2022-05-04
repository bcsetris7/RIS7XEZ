# code by bcsetris7
print(r"Welcome to TheVoxcraft's ASCII ART GENERATOR!")
word = raw_input("Type in a word: ")
 
current_letter = ""
current_count = 0
line1 = ""
line2 = ""
line3 = ""
line4 = ""
line5 = ""
line6 = ""
 
for letter in word:
    current_letter = word[current_count]
    if letter.lower() == "a":
            line1 += "  "+"#########"
            line2 += "  "+"#       #"
            line3 += "  "+"#       #"
            line4 += "  "+"#########"
            line5 += "  "+"#       #"
            line6 += "  "+"#       #"
    elif letter.lower() == "b":
            line1 += "  "+"######## "
            line2 += "  "+"#       #"
            line3 += "  "+"#       #"
            line4 += "  "+"######## "
            line5 += "  "+"#       #"
            line6 += "  "+"######## "
    elif letter.lower() == "c":
            line1 += "  "+"#########"
            line2 += "  "+"#       #"
            line3 += "  "+"#        "
            line4 += "  "+"#        "
            line5 += "  "+"#       #"
            line6 += "  "+"#########"
    elif letter.lower() == "d":
            line1 += "  "+"######## "
            line2 += "  "+"#       #"
            line3 += "  "+"#       #"
            line4 += "  "+"#       #"
            line5 += "  "+"#       #"
            line6 += "  "+"######## "
    elif letter.lower() == "e":
            line1 += "  "+"#########"
            line2 += "  "+"#        "
            line3 += "  "+"#########"
            line4 += "  "+"#        "
            line5 += "  "+"#        "
            line6 += "  "+"#########"
    elif letter.lower() == "f":
            line1 += "  "+"#########"
            line2 += "  "+"#        "
            line3 += "  "+"#########"
            line4 += "  "+"#        "
            line5 += "  "+"#        "
            line6 += "  "+"#        "
    elif letter.lower() == "g":
            line1 += "  "+"#########"
            line2 += "  "+"#        "
            line3 += "  "+"#    ####"
            line4 += "  "+"#       #"
            line5 += "  "+"#       #"
            line6 += "  "+"#########"
    elif letter.lower() == "h":
            line1 += "  "+"#       #"
            line2 += "  "+"#       #"
            line3 += "  "+"#########"
            line4 += "  "+"#       #"
            line5 += "  "+"#       #"
            line6 += "  "+"#       #"
    elif letter.lower() == "i":
            line1 += "  "+"#"
            line2 += "  "+" "
            line3 += "  "+"#"
            line4 += "  "+"#"
            line5 += "  "+"#"
            line6 += "  "+"#"
    elif letter.lower() == "j":
            line1 += "  "+"#####"
            line2 += "  "+"    #"
            line3 += "  "+"    #"
            line4 += "  "+"    #"
            line5 += "  "+"#   #"
            line6 += "  "+"#####"
    elif letter.lower() == "k":
            line1 += "  "+"#     #"
            line2 += "  "+"#   #  "
            line3 += "  "+"# #    "
            line4 += "  "+"#  #   "
            line5 += "  "+"#   #  "
            line6 += "  "+"#    # "
    elif letter.lower() == "l":
            line1 += "  "+"#      "
            line2 += "  "+"#      "
            line3 += "  "+"#      "
            line4 += "  "+"#      "
            line5 += "  "+"#      "
            line6 += "  "+"#######"
    elif letter.lower() == "m":
            line1 += "  "+"#       #"
            line2 += "  "+"# #   # #"
            line3 += "  "+"#  # #  #"
            line4 += "  "+"#   #   #"
            line5 += "  "+"#       #"
            line6 += "  "+"#       #"
    elif letter.lower() == "n":
            line1 += "  "+"##     #"
            line2 += "  "+"# #    #"
            line3 += "  "+"#  #   #"
            line4 += "  "+"#   #  #"
            line5 += "  "+"#    # #"
            line6 += "  "+"#     ##"
    elif letter.lower() == "o":
            line1 += "  "+" ####### "
            line2 += "  "+"#       #"
            line3 += "  "+"#       #"
            line4 += "  "+"#       #"
            line5 += "  "+"#       #"
            line6 += "  "+" ####### "
    elif letter.lower() == "p":
            line1 += "  "+"######## "
            line2 += "  "+"#       #"
            line3 += "  "+"#       #"
            line4 += "  "+"######## "
            line5 += "  "+"#        "
            line6 += "  "+"#        "
    elif letter.lower() == "q":
            line1 += "  "+" ####### "
            line2 += "  "+"#       #"
            line3 += "  "+"#       #"
            line4 += "  "+"#     # #"
            line5 += "  "+"#      ##"
            line6 += "  "+" ########"
    elif letter.lower() == "r":
            line1 += "  "+"######## "
            line2 += "  "+"#       #"
            line3 += "  "+"#       #"
            line4 += "  "+"######## "
            line5 += "  "+"# #      "
            line6 += "  "+"#  #     "
    elif letter.lower() == "s":
            line1 += "  "+" ########"
            line2 += "  "+"#        "
            line3 += "  "+" ####### "
            line4 += "  "+"        #"
            line5 += "  "+"        #"
            line6 += "  "+"######## "
    elif letter.lower() == "t":
            line1 += "  "+"#########"
            line2 += "  "+"    #    "
            line3 += "  "+"    #    "
            line4 += "  "+"    #    "
            line5 += "  "+"    #    "
            line6 += "  "+"    #    "
    elif letter.lower() == "u":
            line1 += "  "+"#       #"
            line2 += "  "+"#       #"
            line3 += "  "+"#       #"
            line4 += "  "+"#       #"
            line5 += "  "+"#       #"
            line6 += "  "+" ####### "
    elif letter.lower() == "v":
            line1 += "  "+"#       #"
            line2 += "  "+"#       #"
            line3 += "  "+"#       #"
            line4 += "  "+" #     # "
            line5 += "  "+"  #   #  "
            line6 += "  "+"   ###   "
    elif letter.lower() == " ":
            line1 += "  "+"  "
            line2 += "  "+"  "
            line3 += "  "+"  "
            line4 += "  "+"  "
            line5 += "  "+"  "
            line6 += "  "+"  "
    elif letter.lower() == "!":
            line1 += "  "+" #"
            line2 += "  "+" #"
            line3 += "  "+" #"
            line4 += "  "+" #"
            line5 += "  "+"  "
            line6 += "  "+" #"
    elif letter.lower() == "w":
            line1 += "  "+"#          #"
            line2 += "  "+"#          #"
            line3 += "  "+"#          #"
            line4 += "  "+" #   ##   # "
            line5 += "  "+"  # #  # #  "
            line6 += "  "+"   #    #   "
    elif letter.lower() == "x":
            line1 += "  "+"#    #"
            line2 += "  "+" #  # "
            line3 += "  "+"  ##  "
            line4 += "  "+"  ##  "
            line5 += "  "+" #  # "
            line6 += "  "+"#    #"
    elif letter.lower() == "y":
            line1 += "  "+"#     #"
            line2 += "  "+" #   # "
            line3 += "  "+"  # #  "
            line4 += "  "+"   #   "
            line5 += "  "+"  #    "
            line6 += "  "+" #     "
    elif letter.lower() == "z":
            line1 += "  "+"#########"
            line2 += "  "+"  #      "
            line3 += "  "+"   #     "
            line4 += "  "+"    #    "
            line5 += "  "+"     #   "
            line6 += "  "+"#########"
    else:
        print("Current letter is not available: " + current_letter)
 
print line1
print line2
print line3
print line4
print line5
print line6
