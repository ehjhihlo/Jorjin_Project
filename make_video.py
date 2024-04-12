import cv2
import numpy as np
import glob
import argparse



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--use_2d', help='input video', action='store_true')
    parser.add_argument('--filename', default='video_0408.mp4', type=str, help='file_name')
    # parser.add_argument('--gpu', type=str, default='0', help='input video')
    # parser.add_argument('--pose2d', type=str, default='hrnet', help='type of 2d pose estimator')
    # parser.add_argument('--cfg', type=str, default='./lib/hrnet/experiments/w48_384x288_adam_lr1e-3.yaml')
    args = parser.parse_args()


    img_array = []
    filename_list = []
    for filename in glob.glob('./temp/out/*.png'):
        filename_list.append(filename)

    if args.use_2d:
        filename_list = []
        for filename in glob.glob('./temp_2d/*.png'):
            filename_list.append(filename)
    else:
        filename_list = []
        for filename in glob.glob('./temp/out/*.png'):
            filename_list.append(filename)

    filename_list = sorted(filename_list)
    # print(filename_list)

    for filename in filename_list:
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)
    

    # out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    # videoWriter = cv2.VideoWriter('video_offline_0408.mp4', fourcc, 3, size)
    videoWriter = cv2.VideoWriter(args.filename, fourcc, 3, size)

    for i in range(len(img_array)):
        videoWriter.write(img_array[i])
    videoWriter.release()