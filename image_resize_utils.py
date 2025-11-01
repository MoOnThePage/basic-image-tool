import cv2
import numpy as np


def resize_to_square(input_image, size=1080):
    """
        Resize the image to square size format (1:1 ratio)
        :param input_image:
        :param size:
        :return:
    """
    img_height, img_width = input_image.shape[:2]
    img_ratio = img_width / img_height
    target_ratio = 1 / 1

    if img_ratio > target_ratio:
        # Wider than square - fit to width
        new_width = size
        new_height = int(size / img_ratio)
    else:
        # Taller than square - fit to height
        new_height = size
        new_width = int(size / img_ratio)

    # resie image
    dimensions = (new_width, new_height)
    resized_img = cv2.resize(input_image, dimensions, interpolation=cv2.INTER_AREA)

    # Create Square canvas
    result = np.full((size, size, 3), (0, 0, 0), dtype=np.uint8)

    # Center the image
    offset_x = (size - new_width) // 2
    offset_y = (size - new_height) // 2

    result[offset_y:offset_y + new_height, offset_x:offset_x + new_width] = resized_img

    return result


def resize_to_16_9(input_image, width=1920, height=1080):
    """
        Resize the image to rectangular size format (16:9 ratio)
        :param input_image:
        :param width:
        :param height:
        :return:
    """
    img_height, img_width = input_image.shape[:2]
    img_ratio = img_width / img_height
    target_ratio = 16 / 9

    if img_ratio > target_ratio:
        new_width = width
        new_height = int(width / img_ratio)
    else:
        new_height = height
        new_width = int(height / img_ratio)

    # resie image
    dimensions = (new_width, new_height)
    resized_img = cv2.resize(input_image, dimensions, interpolation=cv2.INTER_AREA)

    # Create Square canvas
    result = np.full((height, width, 3), (0, 0, 0), dtype=np.uint8)

    # Center the image
    offset_x = (width - new_width) // 2
    offset_y = (height - new_height) // 2

    result[offset_y:offset_y + new_height, offset_x:offset_x + new_width] = resized_img

    return result


def resize_to_4_5(input_image, width=1080, height=1920):
    """
        Resize the image to rectangular size format (4:9 ratio)
        :param input_image:
        :param width:
        :param height:
        :return:
    """
    img_height, img_width = input_image.shape[:2]
    img_ratio = img_width / img_height
    target_ratio = 4 / 5

    if img_ratio > target_ratio:
        new_width = width
        new_height = int(width / img_ratio)
    else:
        new_height = height
        new_width = int(height / img_ratio)

    # resie image
    dimensions = (new_width, new_height)
    resized_img = cv2.resize(input_image, dimensions, interpolation=cv2.INTER_AREA)

    # Create Square canvas
    result = np.full((height, width, 3), (0, 0, 0), dtype=np.uint8)

    # Center the image
    offset_x = (width - new_width) // 2
    offset_y = (height - new_height) // 2

    result[offset_y:offset_y + new_height, offset_x:offset_x + new_width] = resized_img

    return result


def resize_to_aspect_ration(input_image, width, height, bg_color = (0, 0, 0)):
    """
        Resize the image to custom respect ration with padding
        :param input_image:
        :param width:
        :param height:
        :param bg_color:
        :return:
    """
    img_height, img_width = input_image.shape[:2]
    img_ratio = img_width / img_height
    target_ratio = width / height

    if img_ratio > target_ratio:
        new_width = width
        new_height = int(width / img_ratio)
    else:
        new_height = height
        new_width = int(height / img_ratio)

    # resie image
    dimensions = (new_width, new_height)
    resized_img = cv2.resize(input_image, dimensions, interpolation=cv2.INTER_AREA)

    # Create Square canvas
    result = np.full((height, width, 3), bg_color, dtype=np.uint8)

    # Center the image
    offset_x = (width - new_width) // 2
    offset_y = (height - new_height) // 2

    result[offset_y:offset_y + new_height, offset_x:offset_x + new_width] = resized_img

    return result


# Resize Image Function.
# Currently, this function will resize any image size to instagram's
# vertical post (1080x1350 px) while maintaining the aspect ratio of
# the image.
def resize_image(input_image):
    """
    Master function show menu and apply selected resize preset
    :param input_image:
    :return:
    """
    print("\n🏞️ Resize Options:")
    print("\t[1] Square (1080x1808)")
    print("\t[2] Landscape 16:9 (1920x1080)")
    print("\t[3] Portrait 4:9 (1080x1350)")
    print("\t[4] Custom size")

    option_select =input("Select and option (1 - 4): ").strip()

    if option_select == "1":
        return resize_to_square(input_image)
    elif option_select == "2":
        return resize_to_16_9(input_image)
    elif option_select == "3":
        return resize_to_4_5(input_image)
    elif option_select == "4":
        width = int(input("Enter Width: "))
        height = int(input("Enter Height: "))
        return resize_to_aspect_ration(input_image, width, height)
    else:
        print("⚠️ Invalid choice.")
        return input_image