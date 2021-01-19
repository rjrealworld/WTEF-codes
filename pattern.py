STAR = "*"
HASH="#"
CRLF = "\n"
MINUS = "-"
SPACE = " "
SCREEN_WIDTH = 60


SP = HASH
RP = MINUS + MINUS
EP = '\b' + HASH

def pattern(size: int, width = SCREEN_WIDTH):
    return CRLF.join([line(line_no, width) for line_no in range(size)])

def line(n: int, width: int) -> str:
    return leading_space(n, width) + start_pattern(n) + repeat_pattern(n) + end_pattern(n)

def leading_space(n: int, w: int) -> str:
    return (w//2 - n) * SPACE

def start_pattern(n: int):
    return SP

def repeat_pattern(n: int):
    return n * RP

def end_pattern(n: int):
    return EP
print(pattern(int(input())))