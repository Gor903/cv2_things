import cv2

cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = cv2.CascadeClassifier('haarcascades/faces.xml')
    eye = cv2.CascadeClassifier('haarcascades/eye.xml')

    eye_results = eye.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    face_results = faces.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=3,
        flags=cv2.CASCADE_SCALE_IMAGE,
    )

    for (x, y, w, h) in eye_results:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255,255,255), thickness=-1)

    for (x, y, w, h) in face_results:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=3)
    img = cv2.flip(img, 1)

    cv2.imshow('Result', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyWindow(winname='Result')

