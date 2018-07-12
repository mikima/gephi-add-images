# gephi-add-images
A silmpe script to add image to SVGs created with Gephi.

## Dependencies

The script need Beautiful soup 4 to run. [Here are the instruction on how to install it](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).

## How to use

1. In Gephi, use as label the name of the image
2. Export the SVG file using the Preview panel
3. Put the python script, the SVG and a folder with the images in the same place
4. run the python script:

`python replace-with-images.py <input_file.svg> <name_of_images_folder> <upscaling> <output_file_name>`

**input file:** the network exported from Gephi

**image folder:** path of the folder containing images, starting from the folder containing the script. Default value: `none`

**Upscaling: **multiplicator for the size of the images (e.g. 2 will double their size). Default value: `1`

**Output file name:** the name of the output file. Default value: `output`

e.g.

`python replace-with-images.py my-network.svg images/ 4 my-network-with-images`

Only the first parameter is compulsory.