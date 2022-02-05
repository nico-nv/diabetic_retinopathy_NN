#NN: Nuevo

#def hello_world():
#    return "Hello world"

#if __name__ == "__main__":
#    print(hello_world())


from io import BytesIO
from PIL import Image


def read_imagen(file) -> Image.Image:
    image = Image.open(BytesIO(file))
    return image


#if __name__ == "__main__":
#    print(read(imagen))
