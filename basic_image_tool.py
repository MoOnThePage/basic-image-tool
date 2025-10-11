# TODO: annotate the image
# TODO: check basic operation to be applied
# ------ TODO: convert
# ------ TODO: crop
# ------ TODO: resize
# ------ TODO: recolor
# ------ TODO: annotate
# ------ TODO: save

# loading the needed libraries
import cv2

# Constant Variables
asset_folder = "sample_images/"

# Reading/Loading the image function
def load_image(image_name):
    """
    Load an image from the given path

    :param image_name:
    :return: Numpy array "image_handler"
    """
    image_to_process = asset_folder + image_name # "magda-ehlers.jpg"
    image_handler = cv2.imread(image_to_process)
    # Check if the image is loaded or not
    if image_handler is None:
        print(f"Error: {image_to_process} is not a valid image could not be loaded.")
        exit()
    else:
        print("Image loaded successfully.")
        return image_handler

    # convert the image into grayscale
    # image_handler_gray = cv2.cvtColor(image_handler, cv2.COLOR_BGR2GRAY)
    #--------------------------------------| TBD |----------------------------------------
    # Display the image to the window
    # cv2.imshow("image", image_handler_gray)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # ------------------------------------------------------------------------------------
    # convert the image into L-A-B Color space
    # This color space to the C-I-E color space (L-A-B) I don't understand it fully but a quick skimming
    # through the docs and a simple google search I found that it separate color information for analysis,
    # as it uses Lightness/Brightness 'L' information, and color information from the green to magenta range
    # 'A' and 'B'
    # image_handler_lab = cv2.cvtColor(image_handler, cv2.COLOR_BGR2LAB)
    #--------------------------------------| TBD |----------------------------------------
    # Display the image to the window
    # cv2.imshow("image", image_handler_lab)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # ------------------------------------------------------------------------------------
    # Crop the image "center cropping"
    # image_height = image_handler.shape[0]
    # image_width = image_handler.shape[1]
    # crop_height = int(image_height * 0.8) # Keep 80% of the heigh
    # crop_width = int(image_width * 0.8)  # keep 80% of the width
    # start_y = (image_height - crop_height) // 2
    # start_x = (image_width - crop_width) // 2
    # image_handler_crop = image_handler[start_y:start_y+crop_height, start_x:start_x+crop_width]
    # --------------------------------------| TBD |----------------------------------------
    # Display the image to the window
    # cv2.imshow("image", image_handler_crop)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # ------------------------------------------------------------------------------------
    # Resize the image but maintain aspect ratio
    desired_width = 200
    aspect_ratio = image_handler.shape[1] / image_handler.shape[0]
    desired_height = int(desired_width * aspect_ratio)
    dim = (desired_width, desired_height)
    image_handler_resized = cv2.resize(image_handler, dsize=dim, interpolation=cv2.INTER_AREA)

    # Display the image to the window
    cv2.imshow("image", image_handler_resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Saving the image as is
    # cv2.imwrite("output/output.jpg", image_handler)

    # Saving the image as PNG (Convert from JPG -> PNG)
    # cv2.imwrite("output/output.png", image_handler)