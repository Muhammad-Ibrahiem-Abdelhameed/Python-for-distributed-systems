
words = {}
def coroutine(fn):
    def wrapper(*args, **kwargs):
        c = fn(*args, **kwargs)
        next(c)
        return c
    return wrapper

def cat(f, case_insensitive, child):
    if case_insensitive:
        line_processor = lambda l: l.lower()
    else:
        line_processor = lambda l:l

    for line in f:
        child.send(line_processor(line))

@coroutine
def grep(listStrs, case_insensitive, child):
    global words
    for index in range(listStrs.__len__()):
        if case_insensitive:
            listStrs[index] = listStrs[index].lower()

    while True:
        text = (yield)
        child.send(text.count(listStrs[0]))



@coroutine
def count(listStrs):
    global words
    #global nums
    #nums = [0 for i in range(listStrs.__len__())]

    n = 0
    #print(kwargs.__len__())
    try:
        while True:
            n += (yield)
            #print(n)
            #nums = n
    except GeneratorExit:
        #print(nums)
        for index in range(listStrs.__len__()):
            print(words[0])
            #print("nums", nums)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', action='store_true', dest='case_insensitive')
    parser.add_argument('pattern', type=str, nargs='+')
    parser.add_argument('infile', type=argparse.FileType('r'))
    args = parser.parse_args()

    cat(args.infile, args.case_insensitive,
        grep(args.pattern, args.case_insensitive,
             count(args.pattern)))
