def check(buf, val):
    for x in buf:
        for y in buf:
            if x + y == val:
                return True
    return False

def find_xmas_weakness(nums):
    buf = []
    ctr = 0
    invalid = None
    for x in nums:
        if ctr >= 25:
            if not check(buf, x):
                invalid = x
                break
            buf[ctr % 25] = x
        else:
            buf.append(x)

        ctr +=1 

    if invalid == None:
        return ("failed", None)

    # Maybe see if this can be made more efficient?    
    sums = []
    for x in nums:
        for s in sums:
            if sum(s) == invalid:
                return ("ok", min(s) + max(s))
            else:
                s.append(x)
        sums.append([x])

# from input import x
# print(find_xmas_weakness([int(line) for line in x.split("\n")]))