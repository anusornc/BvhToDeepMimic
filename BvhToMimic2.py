# Imports
# ===========================================================================

from bvh import Bvh
import numpy as np
import math
import json
import os
from os import listdir
from os.path import isfile, join

# Function declarations
# ===========================================================================

# Remove all files in given directory


def removeAllFilesInDirectory(directory):
    onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]
    for i in range(0, len(onlyfiles)):
        os.remove(f"{directory}{onlyfiles[i]}")


def euler_to_quaternion(heading, attitude, bank):
    c1 = np.cos(heading/2)
    s1 = np.sin(heading/2)
    c2 = np.cos(attitude/2)
    s2 = np.sin(attitude/2)
    c3 = np.cos(bank/2)
    s3 = np.sin(bank/2)
    c1c2 = c1 * c2
    s1s2 = s1 * s2
    w = c1c2*c3 - s1s2*s3
    x = c1c2*s3 + s1s2*c3
    y = s1*c2*c3 + c1*s2*s3
    z = c1*s2*c3 - s1*c2*s3

    return [w, x, y, z]


# Initialization
# ===========================================================================

removeAllFilesInDirectory("./OutputMimic/")

# Sets up list of bones used by DeepMimic humanoid
# Order is important
deepMimicHumanoidJoints = ["seconds", "hip", "hip", "chest", "neck", "right hip", "right knee", "right ankle",
                           "right shoulder", "right elbow", "left hip", "left knee", "left ankle", "left shoulder", "left elbow"]
dimensions = [1, 3, 4, 4, 4, 4, 1, 4, 4, 1, 4, 1, 4, 4, 1]

# Locks root rotation for dev testing
posLocked = True

# sets onlyfiles to a list of files founds in the "mypath" directory
mypath = "./inputBvh/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# Start of main program
# ===========================================================================

# for all files to convert
for j in range(0, len(onlyfiles)):

    # open file to convert
    with open("./inputBvh/" + onlyfiles[j]) as f:
        mocap = Bvh(f.read())

        # For every keyFrame
        keyFrame = []
        for i in range(0, mocap.nframes):
            print(i)

            # print(mocap.frame_joint_channel(22, 'Head', 'Xrotation'))
