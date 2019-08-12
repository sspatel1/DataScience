import os
import gzip
import numpy as np
import requests


def load_mnist():
    

    """Load MNIST data from `path`"""
    response_labels = requests.get("https://data-bootcamp-0071.s3.us-east-2.amazonaws.com/t10k-labels-idx1-ubyte.gz")
    response_images = requests.get("https://data-bootcamp-0071.s3.us-east-2.amazonaws.com/t10k-images-idx3-ubyte.gz")

        
    labels = np.frombuffer(gzip.decompress(response_labels.content),dtype=np.uint8,offset=8)
    images = np.frombuffer(gzip.decompress(response_images.content),dtype=np.uint8,offset=16).reshape(len(labels), 784)
    
    return images, labels

if __name__ == '__main__':
    load_mnist()


    
