'''
     ______                 _          
    / ____/___  __  _______(_)__  _____
   / /_  / __ \/ / / / ___/ / _ \/ ___/
  / __/ / /_/ / /_/ / /  / /  __/ /    
 /_/ __ \____/\__,_/_/  /_/\___/_/     
    / /__     ____  (_)___    (_)___ _ 
   / / _ \   / __ \/ / __ \  / / __ `/ 
  / /  __/  / / / / / / / / / / /_/ /  
 /_/\___/  /_/ /_/_/_/ /_/_/ /\__,_/   
                        /___/          

You have to complete the `DFT(signal)` function to Implement a way to compute the discrete Fourier transform of a signal using the fast Fourier transform (FFT) algorithm.
⚠ Don't touch the `signal` variable
---
For exemple, with [1, 2, 3, 4] as a signal, the DTF function should return [(10+0j), (-2+2j), (-2+0j), (-1.9999999999999998-2j)] and the flag would be JP2023{(4+0j)} (it's not the actual flag of this chall)
'''

import cmath,math

def DFT(signal):
    signal_len = len(signal)

    if signal_len == 1:
        return signal

    even = DFT(signal[::2])
    odd = DFT(signal[1::2])

    result = [0] * signal_len
    for i in range(signal_len // 2):
        angle = -2j * cmath.pi * i / signal_len
        twiddle = cmath.exp(angle)
        result[i] = even[i] + twiddle * odd[i]
        result[i + signal_len // 2] = even[i] - twiddle * odd[i]

    return result

#The "get_the_flag" function is essential, don't modify it to get a correct flag.... only if your algo is good
def get_the_flag(DFT_list):
    sum = 0
    for i in DFT_list:
        sum = sum + i
    print("If your algo is good, The flag is : JP2023{"+str(sum)+"}")

if __name__ == '__main__':
    # ⚠ The `signal` variable must not be changed
    signal = [7153100.96, 1073, -917, 9922610, 66271, 19335579.9856, 114933, 4708428, -5660849.98416, 4340007]
    print(len(signal))
    #signal = [1,2,3,4]
    # Run the DFT function
    result = DFT(signal)
    get_the_flag(result)