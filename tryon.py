import streamlit as st
import requests
import random
from io import BytesIO
from base64 import b64encode
from PIL import Image
import requests, json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def extract_link_flipkart(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html5lib")
    return soup.find_all("img", {"class": "_2r_T1I _396QI4"})[0]["src"]


def extract_link_myntra(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }

    s = requests.Session()
    res = s.get(url, headers=headers, verify=False)

    soup = BeautifulSoup(res.text, "lxml")

    script = None
    for s in soup.find_all("script"):
        if "pdpData" in s.text:
            script = s.get_text(strip=True)
            break
    data = json.loads(script[script.index("{") :])
    try:
        link = data["pdpData"]["colours"][0]["image"]
    except TypeError as e:
        link = data["pdpData"]["media"]["albums"][0]["images"][0]["imageURL"]
    return link


def extract_link_amazon(
    url, DRIVER_PATH="E:\Setups\chromedriver_win32\chromedriver.exe"
):
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")
    try:
        driver = webdriver.Chrome("chromedriver", options=options)
    except Exception as e:
        driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html5lib")
    return soup.findAll("img", {"class": "a-dynamic-image a-stretch-horizontal"})[0][
        "src"
    ]


def extract_link(url):
    if "flipkart" in url:
        return extract_link_flipkart(url)
    if "myntra" in url:
        return extract_link_myntra(url)
    if "amazon" in url and "media" not in url:
        return extract_link_amazon(url)
    return None


API_KEY = "SG_afde642ca59f4f81"

def to_byte64str(img):
  byte_array = BytesIO()
  img.save(byte_array, format='PNG')
  return str(b64encode(byte_array.getvalue()))[2:-1]

def tryon(model_img, cloth_url):
    # Load model image from Streamlit input
    model_img = Image.open(model_img)

    data = {
        "model_image": to_byte64str(model_img),
        "cloth_image_url": cloth_url,
        "num_inference_steps": 35,
        "guidance_scale": 2.0,
        "seed": random.randint(0, 99999999)
    }

    out = requests.post("https://api.segmind.com/v1/try-on-diffusion", json=data, headers={'x-api-key': API_KEY})

    if out.ok:
        img = Image.open(BytesIO(out.content))
        return img
    else:
        print(out.content)
        raise Exception

# Add input for model image
model_img = st.file_uploader("Upload model image")

# Add input for amazon link URL
platform_url = st.text_input("Enter an amazon,mynthra of flipkart URL")

cloth_url=extract_link(platform_url)
# cloth_url="https://m.media-amazon.com/images/I/61qAoR1y1sS._SY741_.jpg"

# Display the output image
if model_img is not None and cloth_url and st.button("Try On"):
    try:
        output_img = tryon(model_img, cloth_url)
        st.image(output_img, caption="Output Image", use_column_width=True)
    except Exception as e:
        st.write("Error:", e)