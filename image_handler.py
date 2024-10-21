from io import BytesIO
from PIL import Image

SIZE = (300, 300)


def merge_two_images_horizontally(image_list):

    loaded_imgs = [Image.open(image) for image in image_list]
    resized_imgs = [image.resize(SIZE) for image in loaded_imgs]
    image_sizes = [image.size for image in resized_imgs]

    new_image = Image.new("RGB", (SIZE[0] * len(image_sizes), SIZE[1]), (250, 250, 255))
    for i, img in enumerate(resized_imgs):
        offset_size = i * image_sizes[i][0]
        align = 0
        new_image.paste(img, (offset_size, align))
    result = BytesIO()
    new_image.save(result, format="PNG")
    return result


if __name__ == "__main__":
    merge_two_images_horizontally(["Aatrox.png", "Aatrox.png"])
