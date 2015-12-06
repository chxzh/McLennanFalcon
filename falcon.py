import requests as rq
import re, ctypes
def get_img_url(url, pattern):
    page = rq.get(url)
    img_addr = re.search(pattern, page.content).group(1)
    return url+img_addr
    pass

def save_img(url, path):
    with open(path, 'wb') as img_file:
        img_file.write(rq.get(url).content)

def set_wallpaper(img_path):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoA(
            SPI_SETDESKWALLPAPER, 0, img_path, 0)

def __main__():
    bing_url = "http://www.bing.com"
    pattern = r'g_img=\{url:\'([^\']*)\''
    img_path = 'D:/TemporaryFile/bingBG.png'
    img_url = get_img_url(bing_url, pattern)
    save_img(img_url, img_path)
    set_wallpaper(img_path)
    pass

if __name__ == "__main__":
    __main__()
