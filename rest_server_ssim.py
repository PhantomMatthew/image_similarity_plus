from flask import Flask, jsonify, request
import cv2 as cv2
from skimage.measure import compare_ssim
import imutils
import urllib
import numpy as np

app = Flask(__name__)
app.config.from_pyfile('settings.py')


@app.route("/imagecompare", methods=['POST'])
def imagecompare():
    data = request.get_json()
    first_image_url = data['first']
    second_image_url = data['second']

    origin = url_to_image(first_image_url)
    to_compare = url_to_image(second_image_url)

    gray1 = cv2.cvtColor(origin, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(to_compare, cv2.COLOR_BGR2GRAY)

    (score, diff) = compare_ssim(gray1, gray2, full=True)
    diff = (diff * 255).astype("uint8")
    print("SSIM: {}".format(score))
    return jsonify({"similarity": score})

def url_to_image(url):
	# download the image, convert it to a NumPy array, and then read
	# it into OpenCV format
	resp = urllib.request.urlopen(url)
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	# return the image
	return image

if __name__ == "__main__":
    app.run(host='0.0.0.0')