# Challenge 1-3-2
# my attempt
'''
def cleanup(dirtystr):
    noPunct = dirtystr.strip(" ,?.!")
    return noPunct.lower()

print(cleanup("    ..????!!!! heLlO   ???!!!!,,,"))
'''
# solution
def cleanup(s: str) -> str:
    for ch in "!?., ":
        if ch in s:
            s = s.replace(ch, "")
    return s.strip().lower()

s = " hELLo, WORLD!!!!    ???? ..."
cleaned = cleanup(s)
print(cleaned)