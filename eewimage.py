from PIL import Image
import numpy as np
import io


def generateEewImage(Base,Layer):
    base_data = Image.open(Base).convert("RGB")
    Layer_data = Image.open(Layer)
    Layer_gray = np.array(Layer_data.convert("L"))
    Layer_mask = np.array(Image.new("L", Layer_data.size, 0))
    width,height = Layer_data.size
    for y in range(height): 
        for x in range(width):
            if Layer_gray[y][x] > 10:
                Layer_mask[y][x] = 255
            else:
                Layer_mask[y][x] = 0
    Layer_mask = Image.fromarray(Layer_mask)
    base_data.paste(Layer_data,None,Layer_mask)
    img_br = io.BytesIO()
    base_data.save(img_br,format='PNG')
    img_br=img_br.getvalue()
    return(img_br)
