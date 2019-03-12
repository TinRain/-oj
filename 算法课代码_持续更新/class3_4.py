def search(pat, txt):
    M = len(pat)
    N = len(txt)

    result = ''
    # A loop to slide pat[] one by one */
    for i in range(N - M + 1):
        j = 0

        # For current index i, check
        # for pattern match */
        for j in range(0, M):
            if (txt[i + j] != pat[j]):
                break

        if (j == M - 1):
            result = result + str(i) + ' '

    return result

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        strings = input().split(",")
        txt = strings[0]
        pat = strings[1]
        print(search(pat, txt).strip())
