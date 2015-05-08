"""
functions that use the perma-save file, not the temporary or "waypoint" save
"""
# store lines of file in an array for easy reading
def getFileLines():
    file = open('gameTextFile', 'r')
    lines = file.readlines()
    file.close()
    return lines

# blanks save file and replaces it with whatever is put into the parameter
def writeFile(writing):
    file = open('gameTextFile', 'w')
    #file.truncate(4)
    file.write(writing)
    file.close()