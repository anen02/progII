def _ipl(r):
    if r is None:
        heights.append(0)  # basfall
    else:
        # heights.append(1)
        if r.left is not None:
            heights.append(1 + _ipl(r.left))
        if r.right is not None:
            heights.append(1 + _ipl(r.right))
    return sum(heights)



for key in nyckel:
    lex[key] = value