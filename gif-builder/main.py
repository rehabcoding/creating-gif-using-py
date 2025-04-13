import imageio.v3 as iio
# .v3 to indicate specifically that i wish to work on version 3
# `as` means nickname/alias, so that we can use the shorter name instead of the whole real name

filenames = ['download.jpg', 'download1.jpg'] # list to store location of the images
images = [] # empty list for storing data

for filename in filenames:
  images.append(iio.imread(filename))
# looping through the above list
# `.imread()` method to append pictures into images from given filepath

iio.imwrite('team.gif', images, duration = 500, loop = 0)
# `team.gif` name of the new file
# images, that we previously appended
# duration of each picture in millisecond, currently set to 500 millisecond or .5 second
# loop means how many times the images should be repeated, here 0 means forever