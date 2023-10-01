from PIL import Image, ImageDraw
import io


def overlay(img_byte = None, img_path = None, angle=0, center=(0,0), factor=2):
    #factor is rescale factor
    center = tuple(int(int(i)*factor) for i in center)
    # center = (100,200)
    # img1 = Image.Image.frombytes(data=img_path).convert('RGBA')
    if img_path:
        img1 = Image.open(r'{}'.format(img_path)).convert('RGBA')
    elif img_byte:
        img1 = Image.open(io.BytesIO(img_byte)).convert('RGBA')
    else:
        raise Exception
    
    width, height = img1.size
    img1 = img1.resize((int(factor*width), int(factor*height)), resample=Image.Resampling.LANCZOS)
    # img1.show()
    img2 = Image.open(r'app/static/octa.png').convert('RGBA')
    # img2.show()
    img2 = img2.resize((int(factor*max(width, height)), int(factor*max(width, height)))).rotate(-angle)
    length = img2.size[0]
    img1.paste(img2, (center[0]-length//2, center[1]-length//2), img2)

    img1 = img1.resize((width, height), resample=Image.Resampling.LANCZOS)
    # test = img1.copy()
    # test.paste(img2, (center[0]-length//2, center[1]-length//2), img2)

    # test.convert('RGB').save('test.jpeg')

    # return Image.open(r'test.jpeg').tobytes()

    # img1.paste(img2, (center[0]-length//2, center[1]-length//2), img2)
    # img1.show()

    saved = io.BytesIO()
    img1.save(saved, format='PNG')
    return saved.getvalue()
    

if __name__ == '__main__':
    overlay(img_path='app/static/floorplan.png', angle=86, center=(300,300), factor=2.5)