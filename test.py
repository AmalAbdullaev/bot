a = {"а": [1,2,3], "б": [1,2,3]}

def get():
    return (a.get("а").pop())
print(get())

