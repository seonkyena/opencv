import sys
import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Camera open failed")
    sys.exit()


while True:
    status, frame = cam.read()

    if not status:
        break

    # apply object detection (물체 검출)
    bbox, label, conf = cv.detect_common_objects(frame)

    print(bbox, label, conf)

    if bbox[0]:
        location = sum(bbox[0])
        want_loc = location * 0.25
    print(want_loc)

    # draw bounding box over detected objects (검출된 물체 가장자리에 바운딩 박스 그리기)
    out = draw_bbox(frame, bbox, label, conf, write_conf=True)

    # display output
    cv2.imshow("Real-time object detection", out)

    # while로 음성 인식이 True라면 밑의 코드 실행
    voice = input("찾는 물건이 뭡니까 : ")

    if not voice:
        pass
    if voice == 'Nan':
        sys.exit()
    else:
        for i in range(len(label)):
            if label[i] == voice:
                if want_loc and label:
                    if want_loc < 250:
                        print("{}는 1번에 있습니다.".format(label[i]))
                    elif 250 <= want_loc < 300:
                        print("{}는 2번에 있습니다.".format(label[i]))
                    elif 300 <= want_loc:
                        print("{}는 3번에 있습니다.".format(label[i]))
                    elif 350 <= want_loc:
                        print("{}는 4번에 있습니다.".format(label[i]))

    # if voice:
    #     for i in range(len(label)):
    #         if label[i] == 'apple':
    #             if bbox[0][3] < 300:
    #                 print("사과는 1번에 위치해 있습니다.")
    #             else:
    #                 print("사과는 2번에 위치해 있습니다.")
    #         elif label[i] == 'cell phone':
    #             if bbox[0][3] < 480:
    #                 print("휴대폰은 1번에 위치해 있습니다.")
    #             elif bbox[0][3] > 480:
    #                 print("휴대폰은 2번에 위치해 있습니다.")

    # press "Q" to stop
    if cv2.waitKey(1) == 27:
        break

# release resources
cam.release()
cv2.destroyAllWindows()
