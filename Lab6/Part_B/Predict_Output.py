# Lab 6 - Part B: Predict the Output
# Question 1 to Question 8

print("QUESTION 1")

d = {"a": 1, "b": 2}
d2 = d
d2["c"] = 3

print(len(d))


print("\nQUESTION 2")

d = {"x": [1]}
d2 = d.copy()
d2["x"].append(2)

print(d)


print("\nQUESTION 3")

result = {k: v for k, v in zip("abc", range(3)) if v}

print(result)


print("\nQUESTION 4")

d = {"a": 1}

print(d.setdefault("a", 9))
print(d.setdefault("b", 5))
print(d)


print("\nQUESTION 5")

d = {1: "a", 1.0: "b", True: "c"}

print(d)
print(len(d))


print("\nQUESTION 6")

d = {"a": 1, "b": 2, "c": 3}

try:
    for key in d:
        del d[key]
except RuntimeError as error:
    print(type(error).__name__ + ":", error)


print("\nQUESTION 7")

d = {"a": 1, "b": 2}

print(d.pop("z", None))
print(d.popitem())


print("\nQUESTION 8")

d = {"a": 1, "b": 1}

result = {v: k for k, v in d.items()}

print(result)


print("\nAll 8 questions completed.")

input("\nPress Enter to close the program...")