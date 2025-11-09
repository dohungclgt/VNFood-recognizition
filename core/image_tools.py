import io
from PIL import Image, ImageDraw

def draw_bounding_box(image_bytes: bytes, bbox):
    """
    Vẽ khung vùng phát hiện món ăn (nếu có) vào ảnh.
    bbox = {"x": int, "y": int, "width": int, "height": int}
    """
    if not bbox:
        return Image.open(io.BytesIO(image_bytes))

    try:
        img = Image.open(io.BytesIO(image_bytes))
        draw = ImageDraw.Draw(img)
        x, y, w, h = bbox["x"], bbox["y"], bbox["width"], bbox["height"]
        draw.rectangle([(x, y), (x + w, y + h)], outline="red", width=5)
        return img
    except Exception:
        return Image.open(io.BytesIO(image_bytes))
