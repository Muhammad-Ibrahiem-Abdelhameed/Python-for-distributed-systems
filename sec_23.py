

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
def grep(substring, case_insensitive, child):
    word = ''
    while True:
        text = (yield)
        for i in substring:
            if case_insensitive:
                word = i.lower()
            child.send([i, text.count(word)])

@coroutine
def count():
    dict = {}
    try:
        while True:
            wordNumber = (yield)
            word = wordNumber[0]
            if dict.get(word) is not None :
                dict[word] += wordNumber[1]
            else:
                dict[word] = wordNumber[1]
    except GeneratorExit:
        print(dict)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', action='store_true', dest='case_insensitive')
    parser.add_argument('pattern', type=str, nargs='+')
    parser.add_argument('infile', type=argparse.FileType('r'))
    args = parser.parse_args()

    cat(args.infile, args.case_insensitive,
        grep(args.pattern, args.case_insensitive,
             count()))
