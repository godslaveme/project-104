import cv2

img = cv2.imread("solar-system.jpg")
cv2.putText(img,
            "sun",
            (100, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (60, 255, 0)
            )
cv2.putText(img,
            "mercury",
            (110, 192),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
cv2.putText(img,
            "venus",
            (190, 255),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
cv2.putText(img,
            "earth",
            (280, 175),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
cv2.putText(img,
            "moon",
            (325, 160),
            cv2.FONT_HERSHEY_COMPLEX,
            0.25,
            (255, 255, 255)
            )
cv2.putText(img,
            "mars",
            (383, 252),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
cv2.putText(img,
            "jupiter",
            (570, 375),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
cv2.putText(img,
            "saturn",
            (730, 125),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
cv2.putText(img,
            "uranus",
            (965, 140),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
cv2.putText(img,
            "neptune",
            (1110, 280),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
cv2.imshow("output", img)
cv2.waitKey(0)
cv2.imwrite('solar-system.jpg',img)