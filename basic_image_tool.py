# loading the needed libraries
import cv2
import numpy as np

# image global variable
img = np.zeros((512,512,3), np.uint8)

# Constant Variables
asset_folder = "sample_images/" # image samples directory
output_folder = "output/" # output folder

# Constant Variable for terminal colors
BLUE = "\033[94m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Image Samples as a list
images_list = ["alexasfotos.jpg", "alex-souza.jpg","arlindphotography-.jpg", "brongkie-brongkie.jpg", "chevanon-.jpg",
               "cottonbro.jpg", "d-minh-ha-tu-n-.jpg", "ewei2805.jpg", "fatih-aytekin.jpg", "icon0.jpg", "irina-bekhtereva.jpg",
               "iriser-.jpg", "jcmotive.jpg", "katierainbow-1.jpg", "katierainbow-2.jpg", "led-supermarket.jpg", "lee-dunican.jpg",
               "magda-ehlers.jpg", "neosiam.jpg", "ninobur-.jpg", "pixabay-1.jpg", "pixabay-2.jpg", "pixabay-3.jpg", "robert-clark.jpg",
               "roman-odintsov.jpg", "ryank.jpg", "scholtz-buys.jpg", "spacex-1.jpg", "spacex-2.jpg", "spacex-3.jpg", "syed-abdul-moiz.jpg",
               "tima-miroshnichenko.jpg", "tswegha.jpg", "visax.jpg", "vladimirsrajber.jpg", "wahyu-widiatmoko.jpg", "zba-banner.jpg"]

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

    # Show the saved image
    cv2.imshow("Saved Image Preview", image_handler)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Color space conversion function
def convert_color_space(input_image, color_space):
    """
    Transform from BGR color space to another color space
    :param input_image:
    :param color_space:
    :return: new color space
    """
    if color_space == '1': # convert to grayscale
        print("Converting from BGR to GRAY")
        return cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    elif color_space == '2': # convert to hsv
        print("Converting from BGR to HSV")
        return cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV)
    elif color_space == '3': # convert to lab
        print("Converting from BGR to LAB")
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

def print_greeting_message():
    print(BOLD + CYAN + "=" * 80 + RESET)
    print("🖼️ Basic Image Tool - OpenCV Mini Project 😊" + RESET)
    print("=" * 80)
    print(BLUE + "Welcome!" + RESET + " This tool lets you perform basic image operations:")
    print(YELLOW + "\t[1] " + RESET + "Load an image")
    print(YELLOW + "\t[2] " + RESET + "Display an image")
    print(YELLOW + "\t[3] " + RESET + "Convert a color space to another color space")
    print(YELLOW + "\t[4] " + RESET + "Resize an image")
    print(YELLOW + "\t[5] " + RESET + "Crop an image")
    print(YELLOW + "\t[6] " + RESET + "Annotate an image")
    print(YELLOW + "\t[7] " + RESET + "Save an image")
    print(YELLOW + "\t[8] " + RESET + "Save an image to another format\n\n")
    print(YELLOW + "    👉 Type the number of the actio you want to perform: " + RESET)
    print(YELLOW + "    👉 Type 'q' to quit" + RESET)
    print(BOLD + CYAN + "=" * 80 + RESET)

def main():
    global img
    print_greeting_message()
    while True:
        user_input = input("Enter number of operations: ").strip().lower()
        if user_input == 'q':
            print("Thank you for using Basic Image Tool.!\nHave a nice day!")
            break
        elif user_input == '1': # Load an image from sample image list
            print("Loading an image...")
            index = int(input("Pick a number between 1 and 37, to select an image: "))
            img = load_image(images_list[index - 1])
            continue
        elif user_input == '2': # Display the loaded image or the as is or after an operation
            display_image(img)
            continue
        elif user_input == '3': # convert color space
            print(BOLD + CYAN + "-" * 50 + RESET)
            print(BOLD + RED + "CONVERT COLOR SPACE OPERATION" + RESET)
            print(BLUE + "\n\nSelect between 3 options:" + RESET)
            print(YELLOW + "\t[1] " + RESET + "Gray Color Space")
            print(YELLOW + "\t[2] " + RESET + "HSV Color Space")
            print(YELLOW + "\t[3] " + RESET + "LAB Color Space")
            print(BOLD + CYAN + "-" * 50 + RESET)
            operation_number = input("Select an operation: ")
            img = convert_color_space(img, operation_number)
            continue
        elif user_input == '4': #resize the image
            print("Image Resizing...")
            img = resize_image(img)
            continue
        elif user_input == '5': # crop the image
            print("Image Cropping...")
            img = crop_image(img)
            continue
        elif user_input == '6': # annotate the image
            print("Annotate an image...")
            img = annotate_image(img, "Image Annotated")
            continue
        elif user_input == '7': # save the image
            save_image("output.jpg", img)
            continue
        elif user_input == '8': # save in another formate
            print(BOLD + CYAN + "*" * 50 + RESET)
            print(BOLD + RED + "Convert the image to another format and save it" + RESET)
            print(BLUE + "\n\nCurrently it only support PNG:" + RESET)
            print(YELLOW + "\t[1] " + RESET + "Convert to PNG")
            # print(YELLOW + "\t[2] " + RESET + "HSV Color Space")
            # print(YELLOW + "\t[3] " + RESET + "LAB Color Space")
            print(BOLD + CYAN + "*" * 50 + RESET)
            operation_number = input("Select an operation: ")
            save_image("output.png", img)
            continue
        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()