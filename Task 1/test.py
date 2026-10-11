def make_dif(old_lines, new_lines):
    n = len(old_lines)
    m = len(new_lines)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if old_lines[i] == new_lines[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

    result = []
    i = j = 0

    while i < n or j < m:
        if i < n and j < m and old_lines[i] == new_lines[j]:
            result.append(old_lines[i])
            i += 1
            j += 1
        elif i < n and (
            j == m or dp[i + 1][j] >= dp[i][j + 1]
        ):
            result.append("-" + old_lines[i])
            i += 1
        else:
            result.append("+" + new_lines[j])
            j += 1

    return result


with open("old.txt", "r", encoding="utf-8") as file:
    old_lines = file.read().splitlines()

with open("new.txt", "r", encoding="utf-8") as file:
    new_lines = file.read().splitlines()

diff_lines = make_diff(old_lines, new_lines)

with open("diff.txt", "w", encoding="utf-8") as file:
    if diff_lines:
        file.write("\n".join(diff_lines) + "\n")
