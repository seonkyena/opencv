import sys
import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2

cam = cv2.VideoCapture("http://192.168.137.107:8090/?action=stream")

if not cam.isOpened():
    print("Camera open failed")
    sys.exit()

w_frame, h_frame = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH)), int(
    cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps, frames = cam.get(cv2.CAP_PROP_FPS), cam.get(cv2.CAP_PROP_FRAME_COUNT)
x, y, h, w = 0, 0, int(h_frame/2), int(w_frame/2)

while True:
    ret, frame = cam.read()

    if not ret:
        break

    crop_frame1 = frame[y:h, x:w]
    bbox1, label1, conf1 = cv.detect_common_objects(crop_frame1)
    out1 = draw_bbox(crop_frame1, bbox1, label1, conf1, write_conf=True)

    crop_frame2 = frame[y:h, w:w_frame]
    bbox2, label2, conf2 = cv.detect_common_objects(crop_frame2)
    out2 = draw_bbox(crop_frame2, bbox2, label2, conf2, write_conf=True)

    crop_frame3 = frame[h:h_frame, x:w]
    bbox3, label3, conf3 = cv.detect_common_objects(crop_frame3)
    out3 = draw_bbox(crop_frame3, bbox3, label3, conf3, write_conf=True)

    crop_frame4 = frame[h:h_frame, w:w_frame]
    bbox4, label4, conf4 = cv.detect_common_objects(crop_frame4)
    out4 = draw_bbox(crop_frame4, bbox4, label4, conf4, write_conf=True)

    try:
        f = open("C:/Users/IBK/Documents/kyx/python_ex/fruit/예시.txt", 'w')
        for i in range(len(label1)):
            try:
                if label1[i] == label1[i+1]:
                    pass
                else:
                    data = label1[i] + ' 1번에 있습니다.\n'
                    f.write(data)
            except IndexError:
                if label1[i] == label1[i-1]:
                    data = label1[i] + ' 1번에 있습니다.\n'
                    f.write(data)
                else:
                    pass
        for i in range(len(label2)):
            try:
                if label2[i] == label2[i+1]:
                    pass
                else:
                    data = label2[i] + ' 2번에 있습니다.\n'
                    f.write(data)
            except IndexError:
                if label2[i] == label2[i-1]:
                    data = label2[i] + ' 2번에 있습니다.\n'
                    f.write(data)
                else:
                    pass
        for i in range(len(label3)):
            try:
                if label3[i] == label3[i+1]:
                    pass
                else:
                    data = label3[i] + ' 3번에 있습니다.\n'
                    f.write(data)
            except IndexError:
                if label3[i] == label3[i-1]:
                    data = label3[i] + ' 3번에 있습니다.\n'
                    f.write(data)
                else:
                    pass
        for i in range(len(label4)):
            try:
                if label4[i] == label4[i+1]:
                    pass
                else:
                    data = label4[i] + ' 4번에 있습니다.\n'
                    f.write(data)
            except IndexError:
                if label4[i] == label4[i-1]:
                    data = label4[i] + ' 4번에 있습니다.\n'
                    f.write(data)
                else:
                    pass
        f.close()
    except IndexError:
        pass

    cv2.imshow('ex', frame)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()
