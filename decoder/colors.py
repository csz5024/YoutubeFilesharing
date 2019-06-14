from scipy.spatial import distance as dist
from collections import OrderedDict
import numpy as np
import cv2

class ColorLabeler:
    def __init__(self):
        # 39 unique colors in first 400 characters of Norf Norf by Vince Staples
        colors = OrderedDict({
             'c00': (72, 0, 72), 'c01': (109, 72, 36), 'c02': (109, 182, 0), 'c03': (109, 0, 109), 'c04': (109, 72, 0),
             'c05': (36, 0, 0), 'c06': (109, 218, 36), 'c07': (109, 109, 109), 'c08': (109, 182, 36),
             'c013': (109, 145, 72), 'c014': (109, 145, 109), 'c017': (36, 109, 0), 'c019': (109, 145, 0),
             'c10': (109, 109, 0), 'c11': (109, 36, 36), 'c12': (109, 0, 36), 'c16': (109, 36, 109),
             'c19': (109, 0, 72), 'c113': (72, 145, 109), 'c119': (0, 72, 72), 'c20': (72, 109, 36),
             'c23': (72, 0, 109), 'c212': (109, 72, 109), 'c214': (109, 109, 72), 'c215': (36, 36, 109),
             'c218': (109, 36, 0), 'c316': (72, 72, 36), 'c318': (109, 72, 72), 'c43': (109, 182, 109),
             'c512': (72, 72, 72), 'c63': (109, 109, 36), 'c65': (109, 182, 72), 'c612': (109, 36, 72),
             'c79': (109, 218, 72), 'c910': (72, 182, 0), 'c1017': (72, 182, 109), 'c1511': (72, 145, 0),
             'c166': (72, 218, 36), 'c1913': (36, 255, 109)})

        self.lab = np.zeros((len(colors), 1, 3), dtype='uint8')
        self.colorNames = []

        for (i, (name, rgb)) in enumerate(colors.items()):
            self.lab[i] = rgb
            self.colorNames.append(name)

        self.lab = cv2.cvtColor(self.lab, cv2.COLOR_RGB2LAB)

    def label(self, image, c):
        mask = np.zeros(image.shape[:2], dtype="uint8")
        cv2.drawContours(mask, [c], -1, 255, -1)
        mask = cv2.erode(mask, None, iterations=2)
        mean = cv2.mean(image, mask=mask)[:3]

        minDist = (np.inf, None)

        for (i, row) in enumerate(self.lab):
            d = dist.euclidean(row[0], mean)

            if d < minDist[0]:
                minDist = (d, i)

        return self.colorNames[minDist[1]]