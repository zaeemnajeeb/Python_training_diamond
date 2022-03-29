############################################################
#
#    assert statements
#
############################################################


def CalculateQuartile(percent):
    assert type(percent).__name__ == 'int' #precondition here is that percent is an integer
    assert percent >= 0 and percent <= 100 #precondition here is the range
    quartile = 1
    if percent > 25:
        quartile = 2
    if percent > 50:
        quartile = 3
    if percent > 75:
        quartile = 4
    print(f"{percent} is in quartile {quartile}")

CalculateQuartile(17)
CalculateQuartile(34)
CalculateQuartile(56)
CalculateQuartile(87)
CalculateQuartile(104)
