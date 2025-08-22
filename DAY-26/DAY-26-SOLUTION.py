def library_fine(d1, m1, y1, d2, m2, y2):
    if y1 < y2 or (y1 == y2 and m1 < m2) or (y1 == y2 and m1 == m2 and d1 <= d2):
        return 0
    elif y1 == y2 and m1 == m2:
        return 15 * (d1 - d2)
    elif y1 == y2:
        return 500 * (m1 - m2)
    else:
        return 10000

# Input
d1, m1, y1 = map(int, input().split())
d2, m2, y2 = map(int, input().split())

# Output
print(library_fine(d1, m1, y1, d2, m2, y2))
