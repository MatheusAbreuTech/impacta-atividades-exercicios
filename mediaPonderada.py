n1 = float(input(''))
n2 = float(input(''))
n3 = float(input(''))

weightN1 = 2
weightN2 = 4
weightN3 = 8

weightedAverage = (n1 * weightN1 + n2 * weightN2 + n3 * weightN3) / (weightN1 + weightN2 + weightN3)

print(f'{weightedAverage:.2f}')