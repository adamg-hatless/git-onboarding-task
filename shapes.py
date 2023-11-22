
def heart():
    space = " "
    body = "#"
    newline = "\n"
    heart = ((space * 5) + (body * 3) + (space * 2) + (body * 3) + newline 
             + (space * 3) + (body * 12) + newline
             + (space * 4) + (body * 10) + newline
             + (space * 6) + (body * 6)  + newline
             + (space * 8) + (body * 2))
    return heart