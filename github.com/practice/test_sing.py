from functools.singleddispatch import singleddispatch

@singleddispatch
def runcase(case):
    print(case)

@runcase.register(int)
def _(num):
	print(num)


if __name__ == '__main__':
	runcase(1)