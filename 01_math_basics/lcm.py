def lcm(A, B):
    greater = max(A, B)
    smallest = min(A, B)
    i = greater
    while True:
        if i % smallest == 0:
            return i
        i += greater

if __name__ == "__main__":
    A, B = map(int, input().split())
    result = lcm(A, B)
    print(result)
