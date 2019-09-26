import cv2 as cv2
from skimage.measure import compare_ssim
import imutils
import json
import urllib
import numpy as np
# from flask import jsonify

def test_compare():
    image1 = cv2.imread("C:\\SourceCode\\github\\image_similarity_plus\\images\\hero1.jpg")
    image2 = cv2.imread("C:\\SourceCode\\github\\image_similarity_plus\\images\\hero3.jpg")

    image1 = cv2.resize(image1, (500, 500), interpolation=cv2.INTER_CUBIC)
    image2 = cv2.resize(image2, (500, 500), interpolation=cv2.INTER_CUBIC)

    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    (score, diff) = compare_ssim(gray1, gray2, full=True)
    diff = (diff * 255).astype("uint8")
    print("SSIM: {}".format(score))

def compare_image_in_json_file():
    comparision_result = []
    with open(".\\afu_userAccountId_5.json", 'r', encoding='UTF-8') as json_file:
        to_compare_dict = json.load(json_file)

    items = to_compare_dict['RECORDS']

    for item in items:
        similarity = image_compare(item['headUrl'], item['weixinAvatar'])
        item_result = {"headUrl": item['headUrl'], "weixinAvatar":item['weixinAvatar'], 
                "weixinId": item['weixinId'], "weixinNick": item['weixinNick'], 
                "similarity": similarity['similarity']}

        # comparision_result.append(",");
        comparision_result.append(str(item_result))
    
    print("comparision finished")
    return comparision_result

def image_compare(origin=None, destination=None):
    return_value = {}
    try:
        if  origin is None or destination is None or origin == '' or destination == '':
            return_value = json.dumps({"similarity": 0})
        else:
            first_image_url = origin
            second_image_url = destination

        origin = url_to_image(first_image_url)
        to_compare = url_to_image(second_image_url)

        origin = cv2.resize(origin, (132, 132), interpolation=cv2.INTER_CUBIC)
        to_compare = cv2.resize(to_compare, (132, 132), interpolation=cv2.INTER_CUBIC)

        gray1 = cv2.cvtColor(origin, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(to_compare, cv2.COLOR_BGR2GRAY)

        (score, diff) = compare_ssim(gray1, gray2, full=True)
        diff = (diff * 255).astype("uint8")
        print("SSIM: {}".format(score))
        # return_value = json.dumps({
        #     "similarity": score})
        return_value = score

    except ValueError:
        return_value = json.dumps({"similarity": 0})
        # continue
    except UnboundLocalError:
        return_value = json.dumps({"similarity": 0})
    finally:
        return return_value

def url_to_image(url):
	# download the image, convert it to a NumPy array, and then read
	# it into OpenCV format
	resp = urllib.request.urlopen(url)
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	# return the image
	return image

if __name__ == '__main__':
    output = compare_image_in_json_file()
    print(output)
    # test_compare()
    



