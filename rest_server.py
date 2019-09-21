from flask import Flask, jsonify, request
import json
from main_multi import ImageSimilarity

from io import BytesIO
from multiprocessing import Pool

import os
import datetime
import numpy as np
import requests
import h5py

from model_util import DeepModel, DataSequence

app = Flask(__name__)

@app.route("/imagecompare", methods=['POST'])
def imagecompare():
    data = request.get_json()
    first_image_url = data['first']
    second_image_url = data['second']

    similarity = ImageSimilarity()

    '''Setup'''
    similarity.batch_size = 16
    similarity.num_processes = 2

    # '''Load source data'''
    # test1 = similarity.load_data_csv('./demo/test1.csv', delimiter=',')
    # test2 = similarity.load_data_csv('./demo/test2.csv', delimiter=',', cols=['id', 'url'])
    test1 = np.array(['1', first_image_url], ndmin=2)
    test2 = np.array(['1', second_image_url], ndmin=2)

    '''Save features and fields'''
    similarity.save_data('test1', test1)
    similarity.save_data('test2', test2)

    '''Calculate similarities'''
    result = similarity.iteration(['test1_id', 'test1_url', 'test2_id', 'test2_url'], thresh=0.845)

    similarity.dispose()

    return jsonify({"similiarity": float(result[0][0])})

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80,  debug=False)
