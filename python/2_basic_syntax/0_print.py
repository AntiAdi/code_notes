# print(*values: object, sep: str | None = " ", end: str | None = "\n",)

print("Hello", "World", sep="")
print("Hello", "World", "How you doing?",sep="^")
print("Hello", "World", sep="&&", end="\n\n")


name = "Adam"
age = 100.23124124
print(f"Hello {name}", "Let's meet !", sep=">", end="\n")
print(f"Age is {age:.2f}")