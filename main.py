import cv2
import os

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        file=os.path.join(folder,filename)
        img = cv2.imread(file)
        if img is not None:
            images.append(img)
    return images


finalCascadeFile = 'cascade/cascade.xml'
cascade_limestone = cv2.CascadeClassifier(finalCascadeFile)


images = load_images_from_folder("test")
for i in range(0, len(images)):
    image = images[i]
    rectangles = cascade_limestone.detectMultiScale(image)
    print(rectangles)
    print("no of objects in the image: "+str(len(rectangles)))
    for cords in rectangles:
        print(type(cords[0]))
        image = cv2.rectangle(image,(cords[0],cords[1]),(cords[0]+cords[2],cords[1]+cords[3]), (255, 0, 0), 2)
            
        cv2.imwrite("op/newImage_"+str(i)+".jpg",image)

print("all images detected")