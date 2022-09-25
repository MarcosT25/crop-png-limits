from PIL import Image
from matplotlib.pyplot import get

def get_limits(filename):
    im = Image.open(filename)
    width, height = im.size
    rgb_im = im.convert('RGBA')
    min_i = width
    max_i = 0
    min_j = height
    max_j = 0
    for i in range(width):
        for j in range(height):
            r, g, b, a = rgb_im.getpixel((i, j))
            if a != 0:
                if i < min_i:
                    min_i = i
                if i > max_i:
                    max_i = i
                if j < min_j:
                    min_j = j
                if j > max_j:
                    max_j = j
    print(min_i, min_j, max_i, max_j)
    return (min_i, min_j, max_i, max_j)

def crop_limits(filename, limits):
    im = Image.open(filename)
    left = limits[0] - 1
    top = limits[1] - 1
    right = limits[2] + 1
    bottom = limits[3] + 1
    newIm = im.crop((left, top, right, bottom))
    print(left, top, right, bottom)
    return newIm

def main():
    cropped = crop_limits('logo.png', get_limits('logo.png'))
    cropped.save('new.png')

if __name__ == '__main__':
    main()