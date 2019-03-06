from main import Image, Core

i = Image('lena.ppm')
c = Core('core.txt')

i.make_filter(c)

i.save_image('save.ppm')
print(i.counter)