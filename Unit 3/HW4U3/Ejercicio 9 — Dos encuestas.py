encuesta1 = ["Python", "Java", "C", "Python", "Go"]
encuesta2 = ["Go", "Rust", "Java", "Java"]

s1 = set(encuesta1)
s2 = set(encuesta2)

print("En ambas:", sorted(s1 & s2))
print("En solo una:", sorted((s1 - s2) | (s2 - s1)))
