from curve_attributes import points
from fourier import p
import cmath
from svgpathtools import svg2paths

SAMPLE = 10000

cpos = list()
cneg = list()
N = 75 # p

filename = "srm2"
paths, attributes = svg2paths(f'{filename}.svg')
if len(paths) == 1: 
    path = paths[0]

def point_t(t):
    return (path.point(t).real - path.point(t).imag*1j)

for i in range(N):
    sum=0
    for j in range(SAMPLE):
        sum += 1e-4*point_t(j/SAMPLE)*cmath.exp(i*-2*cmath.pi*1j*j/SAMPLE)
        
    cpos.append(sum)
    
for i in range(N):
    sum=0
    for j in range(SAMPLE):
        sum += 1e-4*point_t(j/SAMPLE)*cmath.exp(i*2*cmath.pi*1j*j/SAMPLE)
        
    cneg.append(sum)
        
print(cpos)
print(cneg)