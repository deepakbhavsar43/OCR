import io
import json
import cv2 as cv
import requests

def read_text(filename):
    #Reading Image
    file_path = "uploads/"+filename
    img = cv.imread(file_path)
    height, width, _ = img.shape

    roi = img[80:height-90, 15:width-300]

    # Ocr
    url_api = "https://api.ocr.space/parse/image"
    api_key = "9e6444153088957"

    _, compressedimage = cv.imencode(".jpg", roi, [1, 90])
    file_bytes = io.BytesIO(compressedimage)

    result = requests.post(url_api, files = {"screenshot.jpg": file_bytes},
                           data = {"apikey": api_key, "language": "eng"})

    result = result.content.decode()
    result = json.loads(result)

    parsed_results = result.get("ParsedResults")[0]
    text_detected = parsed_results.get("ParsedText")
    return text_detected
