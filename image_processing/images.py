from PIL import Image, ImageFilter

# img = Image.open('./Pokedex/pikachu.jpg')

# filtered_img = img.filter(ImageFilter.BLUR)

# filtered_img.save('blur.png', 'png')

img = Image.open('./astro.jpg')

img.thumbnail((400,400))

img.save('thumbnail.jpg')