# loading the needed libraries
import cv2

# Constant Variables
asset_folder = "sample_images/"
output_folder = "output/"

# Reading/Loading the image function
def load_image(image_name):
    """
    Load an image from the given path

    :param image_name:
    :return: Numpy array "image_handler"
    """
    image_to_process = asset_folder + image_name
    image_handler = cv2.imread(image_to_process)
    # Check if the image is loaded or not
    if image_handler is None:
        print(f"Error: {image_to_process} is not a valid image could not be loaded.")
        exit()
    else:
        print("Image loaded successfully.")
        return image_handler

# Saving the image as is
def save_image(image_name, image_handler):
    """
    Save an image from the given path
    :param image_name:
    :param image_handler:
    :return: void
    """
    image_to_save = output_folder + image_name
    cv2.imwrite(image_to_save, image_handler)
    print(f"Image saved to {image_to_save}")

# Color space conversion function
def convert_color_space(input_image, color_space):
    """
    Transform from BGR color space to another color space
    :param input_image:
    :param color_space:
    :return: new color space
    """
    if color_space == "gray": # convert to grayscale
        return cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    elif color_space == "hsv": # convert to hsv
        return cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV)
    elif color_space == "lab": # convert to lab
        return cv2.cvtColor(input_image, cv2.COLOR_BGR2LAB)
    else:
        print(f"Error: {color_space} is not a valid color space.")
        return input_image

# resize the image
# TODO: to resize the image to social media post like Instagram
#       vertical post with the size of 1080x1350px, I think this
#       is a good use, currently it resize to the learned sizing
#       value, I have to learn how to make it work.....
# def resize_image(input_image, width, height):
def resize_image(input_image):
    """
    Resize an image to fit the desired size
    :param input_image:
    :return: resized image
    """
    # Resize the image but maintain aspect ratio
    desired_width = 200
    aspect_ratio = input_image.shape[1] / input_image.shape[0]
    desired_height = int(desired_width * aspect_ratio)
    dim = (desired_width, desired_height)
    return cv2.resize(input_image, dsize=dim, interpolation=cv2.INTER_AREA)

# Crop the image
# TODO: currently this function crops the image to the center.
#       "center cropping" is an improvising thing, I need to find
#       a useful way to crop the image automatically with a good
#       result, like the smart cropping used by Instagram.
# This has nothing to do with why cropping found in OpenCV, since
# cropping is ment to remove unwanted data fromm the image, and focus
# on the wanted one for processing, may be I can make something out of
# this, maybe I can make OpenCV with AI to act in smart way to analyse
# the image and crop the un-needed thing from the image, and keep the
# needed things, like automatic cropping mechanism, to upload the image
# keeping the wanted data, or the user can tell it what to keep and what
# to crop, in prompt or voice command, or using hand gesture, I need to
# learn more about this stuff...
# def crop_image(input_image, x1, y1, x2, y2):
def crop_image(input_image):
    """
    Crop an image to fit the desired size
    :param input_image:
    :return: cropped image
    """
    # Crop the image "center cropping"
    image_height = input_image.shape[0]
    image_width = input_image.shape[1]
    crop_height = int(image_height * 0.8) # Keep 80% of the heigh
    crop_width = int(image_width * 0.8)  # keep 80% of the width
    start_y = (image_height - crop_height) // 2
    start_x = (image_width - crop_width) // 2
    return input_image[start_y:start_y+crop_height, start_x:start_x+crop_width]

# Image Annotation function
# this function will annotate the image with a text
# TODO: I have to mek more controllable by the user, or I can train an
#       AI model that can annotate the image my telling the content of
#       the image animals, humans, objects... when I advance more in the
#       course.
def annotate_image(input_image, text, position = 0, color = (0,255,0), size = 5):
    """
    Annotate an image with text
    :param input_image:
    :param text:
    :param position:
    :param color:
    :param size:
    :return:
    """
    position  = (int(input_image.shape[1]/2),int(input_image.shape[0]/2))
    return cv2.putText(input_image, text, position, cv2.FONT_HERSHEY_SIMPLEX, size, color, 10)


# Image Display function and wait for the ESC key to be pressed
def display_image(input_image):
    # Display the image to the window
    cv2.imshow("image", input_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    test_load_image = load_image("magda-ehlers.jpg")
    # test_convert_color_space = convert_color_space(test_load_image, "hsv")
    # test_resize_image = resize_image(test_load_image)
    # test_crop_image = crop_image(test_load_image)
    test_annotate_image = annotate_image(test_load_image, "Image Annotated")
    display_image(test_annotate_image)
    save_image("output.jpg", test_load_image)


if __name__ == "__main__":
    main()