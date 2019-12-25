import numpy as np

def comp_recip(values):
    outp = np.empty(len(values))
    for i in range(len(values)):
        outp[i] = 1.0/values[i]
    return outp

def main():
    values = np.random.randint(1,10, size=5)
    output = comp_recip(values)
    print(output)

main()

#루프마다 타입확인과 함수 디스패치로 매우 느림
