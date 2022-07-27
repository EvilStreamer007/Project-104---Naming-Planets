import cv2


img = cv2.imread('/Users/chaitalishah/Desktop/Krsna_WHJ/Projects/Project-104/solar-system.jpg')
cv2.putText(img,"Sun",(20,100),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Mercury",(110,180),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Venus",(190,170),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Earth",(280,170),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Moon",(320,150),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255))
cv2.putText(img,"Mars",(390,170),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Jupiter",(425,130),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Saturn",(780,130),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Uranus",(965,130),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Neptune",(1120,135),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.imshow("Original Image:",img)

cv2.waitKey(0)
#print(img) - Shows the boolean form

