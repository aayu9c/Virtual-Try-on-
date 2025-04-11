# Virtual Try-On Clothing App

This is a Streamlit-based web application that allows users to upload an image of themselves and virtually try on clothing by providing a product URL from popular online shopping platforms such as **Amazon**, **Myntra**, or **Flipkart**. The app uses deep learning models to generate a "try-on" effect where the uploaded image is processed to show the person wearing the selected clothing.

## Features

- Upload a personal model image.
- Enter a clothing product URL from **Amazon**, **Myntra**, or **Flipkart**.
- Extracts the clothing image automatically from the provided URL.
- Uses a deep learning model to generate an image of the user virtually wearing the selected clothing.
- Displays the final output image for the user.

## Requirements

### Prerequisites

- **Python 3.7+**
- **Streamlit**: For creating the web application interface.
- **Requests**: To make HTTP requests to fetch product images.
- **Pillow**: For image processing (e.g., opening and saving images).
- **BeautifulSoup4**: For parsing HTML and extracting product images.
- **Selenium**: For web scraping to handle dynamic content from Amazon.
- **lxml**: For parsing HTML content with BeautifulSoup.
- **json**: For parsing API response data.
- **Base64**: For encoding image data as base64.
- **Segmind API**: To process the virtual try-on functionality.

### Installing the Dependencies

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/virtual-tryon-app.git
    cd virtual-tryon-app
    ```

2. Install the necessary dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Obtain an API Key from [Segmind](https://segmind.com/) and set the `API_KEY` variable in the script. Replace `SG_afde642ca59f4f81` in the `API_KEY` variable with your actual API key.

4. Download and install [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) to use Selenium for scraping Amazon product images. Make sure that the `DRIVER_PATH` in the `extract_link_amazon` function points to your ChromeDriver executable.

## Running the Application

1. Once the dependencies are installed and configurations are done, run the Streamlit app using the following command:

    ```bash
    streamlit run app.py
    ```

2. After running the command, open your browser and navigate to `http://localhost:8501` to use the app.

## Usage

1. **Upload Model Image**: Click on the file uploader button to upload an image of the person who will virtually try on the clothing.
2. **Enter Clothing URL**: Copy and paste the product URL from **Amazon**, **Myntra**, or **Flipkart** into the text input field.
3. **Click "Try On"**: After both the model image and clothing URL are provided, click the "Try On" button. The app will fetch the clothing image and perform the virtual try-on.
4. **View Result**: The final output image will be displayed with the model wearing the chosen clothing.

## Code Overview

- **`extract_link_flipkart(url)`**: Extracts the clothing image URL from a Flipkart product page.
- **`extract_link_myntra(url)`**: Extracts the clothing image URL from a Myntra product page.
- **`extract_link_amazon(url, DRIVER_PATH)`**: Uses Selenium to extract the clothing image URL from an Amazon product page.
- **`extract_link(url)`**: Determines the platform (Flipkart, Myntra, or Amazon) and calls the respective function to extract the product image URL.
- **`to_byte64str(img)`**: Converts the model image to a base64-encoded string.
- **`tryon(model_img, cloth_url)`**: Makes a request to the Segmind API to generate the virtual try-on image.
- **Streamlit UI**: Provides the file upload input for the model image and text input for the product URL.

## Troubleshooting

- Ensure that **ChromeDriver** is installed and properly configured for Selenium. If there are issues with the web scraping functionality, verify that the path to `chromedriver.exe` is correct.
- If the application doesn't work, ensure that your API key is valid and that the Segmind API is accessible.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Segmind API](https://segmind.com/) for the virtual try-on service.
- [Streamlit](https://streamlit.io/) for providing an easy interface to build the app.
- [Selenium](https://www.selenium.dev/) for automating the web scraping.
