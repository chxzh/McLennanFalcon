import requests as rq
import re, ctypes
from spyderlib.baseconfig import IMG_PATH
def get_img_url(url, pattern):
    page = rq.get(url)
    img_addr = re.search(pattern, page.content).group(1)
    return url+img_addr

def save_img(url, path):
    with open(path, 'wb') as img_file:
        img_file.write(rq.get(url).content)

def set_wallpaper(img_path):
    SPI_SETDESKWALLPAPER = 20
    return ctypes.windll.user32.SystemParametersInfoA(
            SPI_SETDESKWALLPAPER, 0, img_path, 0)

def set_wallpaper_cmd(img_path):
    if not img_path.lower().endswith(".bmp"):
        from PIL import Image
        img = Image.open(img_path)
        img.save(img_path+'.bmp')
        img_path += ".bmp"
    import os
    cmd = "reg add \"HKEY_CURRENT_USER\Control Panel\Desktop\" /v Wallpaper /t REG_SZ /d  %s /f" % img_path.replace('/','\\')
    os.system(cmd)
    os.system("RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters")

def __main__():
    bing_url = "http://www.bing.com"
    pattern = r'g_img=\{url:\'([^\']*)\''
    img_dir = 'C:/Users/cxz/Desktop/temp/'
    img_url = get_img_url(bing_url, pattern)
    img_fname = img_url.split('/')[-1]
    img_path = img_dir+img_fname
    save_img(img_url, img_path)
    if set_wallpaper(img_path) == 0:
        set_wallpaper_cmd(img_path)
    pass

if __name__ == "__main__":
    __main__()
