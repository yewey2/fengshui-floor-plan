from PIL import Image, ImageDraw
import io


def overlay(img_path, angle=0, center=(0,0)):
    center = tuple(int(i) for i in center)
    # center = (100,200)
    # img1 = Image.open(r'{}'.format(img_path)).convert('RGBA')
    # img1 = Image.Image.frombytes(data=img_path).convert('RGBA')
    img1 = Image.open(io.BytesIO(img_path)).convert('RGBA')
    # img1.show()
    img2 = Image.open(r'app/static/octa.png').convert('RGBA')
    width, height = img1.size
    # img2.show()
    img2 = img2.resize((max(width, height),max(width, height))).rotate(angle)
    length = img2.size[0]
    img1.paste(img2, (center[0]-length//2, center[1]-length//2), img2)

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
    overlay('app/static/floorplan.png', 'app/static/octa.png')