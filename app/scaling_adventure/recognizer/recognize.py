import os
import sys
import cv2
import numpy as np

class Recognizer(object):
    """ docstring for Recognizer """
    def __init__(self, directory_path, compareFile, compareThreshold):
        super(Recognizer, self).__init__()
        self.path = directory_path
        self.file = compareFile
        self.threshold = float(compareThreshold)

    """_"""
    def compareWith(self, eigenModelFile):
        model = cv2.createEigenFaceRecognizer(threshold=self.threshold)

        # Load the model
        model.load(eigenModelFile)

        # Read the image we're looking for
        sampleImage = cv2.imread(self.file, cv2.IMREAD_GRAYSCALE)
        sampleImage = cv2.resize(sampleImage, (256,256))

        # Look through the model and find the face it matches
        model_prediction = model.predict(sampleImage)

        [p_label, p_confidence] = model_prediction

        # Print the confidence levels
        # print "Predicted label = {0} (confidence={1})".format(p_label, p_confidence)

        # hold all the found images paths
        result_paths = []

        # If the model found something, print the file path
        if (p_label > -1):
            count = 0
            for dirname, dirnames, filenames in os.walk(self.path):
                for subdirname in dirnames:
                    subject_path = os.path.join(dirname, subdirname)
                    if (count == p_label):
                        for filename in os.listdir(subject_path):
                            result_paths.append(subject_path)

                    count = count+1

        return (result_paths, model_prediction)


# [SAMPLE USAGE]
# recognizer = Recognizer(os.path.abspath('eigen_models/'), 'test.jpg', 1000)
# recognizer.compareWith('eigenModel_1.xml')
