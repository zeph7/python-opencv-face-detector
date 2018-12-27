import os, time
import sys, msvcrt
import cv2


def image_detector():
    
    os.system('cls')
    print('\n' * 4)
    print('---<  I M A G E  D E T E C T I O N  >---'.center(100))
    print('\n' * 5)
    print(' T Y P E  I M A G E  N A M E : '.center(100), end = '')
    print('\n' * 2)
    print(' ' * 40, end = '')
    name = input()
    if name == 'q': screen2()
    
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    img = cv2.imread(name, 1)

    try:
        img.shape
    except AttributeError:
        image_detector()
    
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.1, minNeighbors = 5)
    face_count = 0
    
    for x,y,w,h in faces:
        face_count += 1
        img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)

    print('\n' * 2)
    print(' N U M B E R  O F  F A C E S  D E T E C T E D = %s '.center(100) % face_count)

    # size adjustment of output image
    shape = img.shape
    if shape[1] > shape[0]:
        ratio = shape[0] * 860 // shape[1]
        img = cv2.resize(img, (860, ratio))
    else:
        ratio = shape[1] * 540 // shape[0]
        img = cv2.resize(img, (ratio, 540))
    
    cv2.imshow("Face Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    screen2()


def main():
    
    # main screen 1
    os.system('mode con: cols=100 lines=30')
    os.system('color 2f')
    print('\n'*12)
    print('F A C E  D E T E C T O R'.center(100))
    time.sleep(2)
    screen2()


def webcam_detector():
    
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    video = cv2.VideoCapture(0)
    frame_count = 1

    try:
        check, frame = video.read()
        frame.shape
    except AttributeError:
        screen2()

    while True:
        
        frame_count += 1
        check, frame = video.read()

        faces = face_cascade.detectMultiScale(frame, scaleFactor = 1.1, minNeighbors = 5)

        for x,y,w,h in faces:
            frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)

        cv2.imshow("WebCam Detector", frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()
    screen2()


def video_detector():
    
    os.system('cls')
    print('\n' * 4)
    print('---<  V I D E O  D E T E C T I O N  >---'.center(100))
    print('\n' * 5)
    print(' T Y P E  V I D E O  N A M E : '.center(100), end = '')
    print('\n' * 2)
    print(' ' * 40, end = '')
    name = input()
    if name == 'q': screen2()

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    video = cv2.VideoCapture(name)
    frame_count = 1

    try:
        check, frame = video.read()
        frame.shape
    except AttributeError:
        video_detector()

    while True:
        
        frame_count += 1
        check, frame = video.read()

        faces = face_cascade.detectMultiScale(frame, scaleFactor = 1.1, minNeighbors = 5)

        for x,y,w,h in faces:
            frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)

        cv2.imshow("Video Detector", frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()
    screen2()


def screen2():
    
    # main screen 2
    os.system('cls')
    print('\n' * 4)
    print('---<  D E T E C T I N G  T A S K  >---'.center(100))
    print('\n' * 5)
    print('*  I M A G E  F A C E  D E T E C T I O N : P R E S S  I   '.center(100))
    print('\n')
    print('*  V I D E O  F A C E  D E T E C T I O N : P R E S S  V   '.center(100))
    print('\n')
    print('*  W E B C A M  F A C E  D E T E C T I O N : P R E S S  W  '.center(100))
    print('\n')
    print('*  T O  Q U I T  A N Y T I M E : P R E S S  Q  '.center(100))
    task = msvcrt.getwch().lower()
    if task == 'i': image_detector()
    elif task == 'v': video_detector()
    elif task == 'w': webcam_detector()
    elif task == 'q': sys.exit()
    else: main()
    

if __name__ == '__main__':
    main()
