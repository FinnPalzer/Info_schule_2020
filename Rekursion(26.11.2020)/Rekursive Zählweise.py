
def zahlen(steine):
    if steine == 0:
        return 0
    else:
        return zahlen(steine - 1) +1