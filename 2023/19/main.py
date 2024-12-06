from re import A


data = open("input.txt", "r").read().splitlines()
workflows = {}


def rate_part(x, m, a, s, flow):
    # print(next)
    if flow == "A":
        return "A"
    if flow == "R":
        return "R"
    next = workflows[flow][-1][:-1]
    for check in workflows[flow][:-1]:
        if check[0] == "s":
            if check[1] == "<":
                # print("is " + x + "<" + check.split(":")[0][2:])
                if int(s) < int(check.split(":")[0][2:]):
                    return rate_part(x, m, a, s, check.split(":")[1])
            else:
                if int(s) > int(check.split(":")[0][2:]):
                    return rate_part(x, m, a, s, check.split(":")[1])
        elif check[0] == "m":
            if check[1] == "<":
                # print("is " + x + "<" + check.split(":")[0][2:])
                if int(m) < int(check.split(":")[0][2:]):
                    return rate_part(x, m, a, s, check.split(":")[1])
            else:
                if int(m) > int(check.split(":")[0][2:]):
                    return rate_part(x, m, a, s, check.split(":")[1])
        elif check[0] == "a":
            if check[1] == "<":
                # print("is " + x + "<" + check.split(":")[0][2:])
                if int(a) < int(check.split(":")[0][2:]):
                    return rate_part(x, m, a, s, check.split(":")[1])
            else:
                if int(a) > int(check.split(":")[0][2:]):
                    return rate_part(x, m, a, s, check.split(":")[1])
        else:
            if check[1] == "<":
                # print("is " + x + "<" + check.split(":")[0][2:])
                if int(x) < int(check.split(":")[0][2:]):
                    return rate_part(x, m, a, s, check.split(":")[1])
            else:
                if int(x) > int(check.split(":")[0][2:]):
                    return rate_part(x, m, a, s, check.split(":")[1])
    return rate_part(x, m, a, s, next)


def part1():
    metNewline = False
    sum = 0
    for line in data:
        if len(line.strip()) == 0:
            metNewline = True
            continue
        if metNewline == False:
            # print(line)
            workflow = line.split("{")[0]
            workflows[workflow] = line.split("{")[1].split(",")
        else:
            fixed_line = line[1:-1]
            x, m, a, s = fixed_line.split(",")
            x = x[2:]
            m = m[2:]
            a = a[2:]
            s = s[2:]
            if rate_part(x, m, a, s, "in") == "A":
                sum += int(x) + int(m) + int(a) + int(s)

    print("Part 1: " + str(sum))


part1()
