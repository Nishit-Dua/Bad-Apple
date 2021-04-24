import PIL.Image as Image


# Shit doesn't works in Powershell or cmd wtfff (these ⣩ chars)😣
# ASCII_CHARS = ['⣿', '⣾', '⣫', '⣪', '⣩', '⡶', '⠶', '⠖', '⠆', '⠄', '⠀']
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", " "]
new_width = 115


def resize(image: Image) -> Image:
    '''
    Resizes the PIL.Image object to a new height and width
    to change your output change new_width variable defined
    above
    #! Retarded to use a global variable
    '''

    width, height = image.size
    aspect_ratio = height/float(width * 2.5)
    new_height = int(aspect_ratio*new_width)
    return image.resize((new_width, new_height))


def Grey(image: Image) -> Image:
    return image.convert(mode="L")


def image_to_ascii(image: Image) -> str:
    '''
    takes a monochannel PIL.Image object, gets the pixel val
    (which is always < 255) and gets the questiont val of 25
    (b/w 0 and 10), if you want to change the Ascii characters
    in your image file change ASCII_CHARS list 'high intensity'
    characters first and 11 string constituents.
    '''
    data = image.getdata()
    return ''.join(ASCII_CHARS[val//25] for val in data)


def convert_and_save_to_ascii(image_path: str, write_to: str) -> None:
    try:
        image = Image.open(image_path)
    except Exception:
        print('Not a valid image path')
        return

    new_img = Grey(resize(image))
    text = image_to_ascii(new_img)
    pix_count = len(text)

    final_ascii = '\n'.join(text[i:i+new_width]
                            for i in range(0, pix_count, new_width))

    with open(write_to, 'w') as f:
        f.write(final_ascii)


if __name__ == "__main__":
    image_path = ''
    convert_and_save_to_ascii("BadAppleExtracted/BadApple5000.jpg", "haha.txt")
