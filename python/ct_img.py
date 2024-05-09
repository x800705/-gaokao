import cv2

img = cv2.imread("../p_img/ct/a.jpg")

img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


wo = img[46:50,90:100]  


for i in range(10,65,13):
    for j in range(32,100,22):  
        if img[i,j] < 50:
            if j == 32:
                print("A")
            elif j == 54:
                print("B")
            elif j == 76:
                print("C")
            elif j == 98:
                print("D")
# 10 22 35 48 60
a = img[10,30]
b = img[10,50]
c = img[10,70]
d = img[10,90]



#cv2.imshow("123",wo)
#cv2.waitKey(0)
#print(img)
