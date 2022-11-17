# import basic modules
import os
import sys
import time
import copy
import numpy as np
import torch

"""
json_data_imagenet100 = {
    "img100_data_folder": {
      "train": [
        "/mnt/logicNAS/Exchange/vivek/ImageNet_100/train_20", "/mnt/logicNAS/Exchange/vivek/ImageNet_100/train_20"
      ],
      "val": [
        "/mnt/logicNAS/Exchange/vivek/ImageNet_100/val", "/mnt/logicNAS/Exchange/vivek/ImageNet_100/val"
      ]
    }
}

from vissl.utils.io import save_file
save_file(json_data_imagenet100, "./configs/config/dataset_catalog_img100.json", append_to_json=False)
"""

json_data = {
    "dummy_data_folder": {
      "train": [
        "/content/dummy_data/train", "/content/dummy_data/train"
      ],
      "val": [
        "/content/dummy_data/val", "/content/dummy_data/val"
      ]
    }
}

# use VISSL's api to save or you can use your custom code.
from vissl.utils.io import save_file
save_file(json_data, "./configs/config/dataset_catalog.json", append_to_json=False)