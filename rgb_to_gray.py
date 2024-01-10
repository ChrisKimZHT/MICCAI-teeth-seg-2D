import os
from PIL import Image
from tqdm import tqdm


def rgb2gray(image_path):
    img = Image.open(image_path).convert("L")
    img.save(image_path)


def process(directory):
    images = os.listdir(directory)
    for image in tqdm(images):
        rgb2gray(os.path.join(directory, image))


if __name__ == "__main__":
    process("./data/labelled/image/")
    process("./data/unlabelled/image/")
