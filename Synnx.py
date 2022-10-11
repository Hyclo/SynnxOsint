
#This Is a osint tool just for the users of "en tisch"
#it's main use is to find every piece of information over a person

# Author:  Hyclo
# Version: 1.0.0

#IMPORTS START:
import sys
#FILE IMPORTS START:

#FILE IMPORTS END
#IMPORTS END

for arg in sys.argv:
    if arg != "Synnx.py":
        if arg == "baum":
            print("baum")
        else:
            print("tree")