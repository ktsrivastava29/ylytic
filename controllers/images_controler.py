import base64


def encoder_base64_image(url_image) -> str:
    with open(url_image, 'rb') as file:
        encode_file = base64.b64encode(file.read())
    return encode_file.decode('utf-8')


def decode__image(image_folder: str, file_name: str, data) -> str:
    file_url = image_folder + file_name + '.png'
    image_data = base64.b64decode(data)
    with open(file_url, 'wb') as file:
        file.write(image_data)
    return file_url

