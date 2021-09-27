from html2image import Html2Image

DEFAULT_IMAGE_HEIGHT = 840
DEFAULT_IMAGE_WIDTH = 480


def create_image(html: str, css: str, filename: str) -> str:
    hti = Html2Image()
    hti.screenshot(html_str=html, css_str=css, save_as=filename, size=(DEFAULT_IMAGE_HEIGHT, DEFAULT_IMAGE_WIDTH))
    
    return filename
