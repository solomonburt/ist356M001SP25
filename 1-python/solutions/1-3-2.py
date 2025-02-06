'''
def cleanup(dirtystr):
    noPunct = dirtystr.strip(" ?!.,")
    return noPunct.lower()
    
print(cleanup(" hEllo, WORLD!!!    ??? ..."))
'''

def cleanup(s: str) -> str:
    for ch in "!?., ":
        if ch in s:
            s = s.replace(ch, "")

    return s.strip().lower()

s = " hEllo, WORLD!!!    ??? ..."
cleaned = cleanup(s)
print(cleaned)

    