import cv2
import os

#学生名
name = "d"

#读取学生试卷
img = cv2.imread("../img/d.jpg")
img =cv2.resize(img,(1200,800),interpolation=cv2.INTER_CUBIC)





#os.makedirs("../p_img/ct")
#选择题
ct = img[280:350,50:400]

gray = cv2.cvtColor(ct,cv2.COLOR_BGR2GRAY)

for i in range(10,65,13):
    for j in range(32,100,22):  
        if gray[i,j] < 50:
            if j == 32:
                print("A")
            elif j == 54:
                print("B")
            elif j == 76:
                print("C")
            elif j == 98:
                print("D")
#保存文件
cv2.imwrite("../p_img/ct/" + name + ".jpg",ct)
cv2.imshow("123",ct)
cv2.waitKey(0)

#os.makedirs("../p_img/blank")
#填空题
blank = img[390:480,60:400]
cv2.imwrite("../p_img/blank/" + name + ".jpg",blank)
cv2.imshow("123",blank)
cv2.waitKey(0)

#os.makedirs("../p_img/one")
#os.makedirs("../p_img/one_2")
#第一道大题
one = img[490:750,60:400]  
one_2 = img[40:220,430:770]

#one = cv2.vconcat([one,one_2])
cv2.imwrite("../p_img/one/" + name + ".jpg",one)
cv2.imwrite("../p_img/one_2/" + name + ".jpg",one_2)
cv2.imshow("123",one)
cv2.waitKey(0)
cv2.imshow("123",one_2)
cv2.waitKey(0)


#os.makedirs("../p_img/two")
#os.makedirs("../p_img/two_2")
#第二道大题
two = img[220:500,430:770]
two_2 = img[500:750,430:770]
cv2.imwrite("../p_img/two/" + name + ".jpg",two)
cv2.imwrite("../p_img/two_2/" + name + ".jpg",two_2)
cv2.imshow("123",two)
cv2.waitKey(0)
cv2.imshow("123",two_2)
cv2.waitKey(0)


#os.makedirs("../p_img/three")
#os.makedirs("../p_img/three_2")
#第三道大题
three = img[20:400,800:1180]
three_2 = img[400:750,800:1180]
cv2.imwrite("../p_img/three/" + name + ".jpg",three)
cv2.imwrite("../p_img/three_2/" + name + ".jpg",three_2)
cv2.imshow("123",three)
cv2.waitKey(0)
cv2.imshow("123",three_2)
cv2.waitKey(0)






#cv2.imshow("123",three_2)
#cv2.waitKey(0)
