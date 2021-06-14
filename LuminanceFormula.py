THRESHOLD = 18

def luminance(pixel):
    return (0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2])


def is_similar(pixel_a, pixel_b, threshold):
    return abs(luminance(pixel_a) - luminance(pixel_b)) < threshold


d = is_similar((109,72,46),(170,123,97), 18)
print(d)
# width, height = img.size
# pixels = img.load()

# for x in range(width):
#     for y in range(height):
#         if is_similar(pixels[x, y], (0, 0, 0), THRESHOLD):
#             pixels[x, y] = (0, 0, 0)