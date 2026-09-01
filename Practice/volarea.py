def area(l, w):
    ar = l * w 
    return ar

def volume(l,w,h):
    vol = l * w * h 
    return vol

def surfaceArea(l,w,h):
    sur = (l*w*2) + (l*h * 2) + 2*(h * w)
    return sur 

def perimeter(l,w):
    per = l+w+l+w
    return per

print(area(10, 10) == 100)
print(area(0, 9999) == 0)
print(area(5, 8) == 40)
print(perimeter(10, 10) == 40)
print(perimeter(0, 9999) == 19998)
print(perimeter(5, 8) == 26)
print(volume(10, 10, 10) == 1000)
print(volume(9999, 0, 9999) == 0)
print(volume(5, 8, 10) == 400)
print(surfaceArea(10, 10, 10) == 600)
print(surfaceArea(9999, 0, 9999) == 199960002)
print(surfaceArea(5, 8, 10) == 340)