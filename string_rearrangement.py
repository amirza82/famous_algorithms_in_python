#   get inputs
inString = input('type input string:\n')
jump = int(input('type the jump value:\n'))
inLen = len(inString)

#   formath the input so the same chars come back to back
fString = {}

for char in inString:
    if char in fString:
        fString[char] += 1
    else:
        fString.update({char: 1})

ffString = {}
for i in range(len(fString)):
    max = ['', 0]
    for key in fString:
        if fString[key] > max[1]:
            max = [key, fString[key]]

    del fString[max[0]]
    ffString.update({max[0]: max[1]})
# now ffString is a sorted dictionary

# check for impossibility
mostFreq = next(iter(ffString.items()))[1]
if int(inLen / jump) < mostFreq:
    print('impossible')
    exit(0)

# make indexQ
loop = int(inLen/jump) + 1
indexQ = []
def makeIndexQ():
    for shift in range(jump):
        for i in range(loop):
            index = (i * jump) + shift
            if index >= inLen:
                break
            else:
                indexQ.append(index)
makeIndexQ()
# make indexQ iterable
indexQ = iter(indexQ)

# make the outpur string
outString = [0] * inLen

for char in ffString:
    for i in range(ffString[char]):
        outString[next(indexQ)] = char

out = ''.join(outString)
print(out)