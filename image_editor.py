#image editor
import cv2

# Load image
img = cv2.imread("soul.jpeg")   # put your image name here

if img is None:
    print("Image not found")
    exit()

while True:
    print("--- IMAGE EDITOR ---")
    print("1. Show Image")
    print("2. Resize Image")
    print("3. Rotate Image")
    print("4. Convert to Grayscale")
    print("5. Blur Image")
    print("6. draw shape")
    print("7. Save Image")
    print("8. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        cv2.imshow("Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif choice == 2:
        w = int(input("Enter new width: "))
        h = int(input("Enter new height: "))
        img = cv2.resize(img, (w,h))
        print("Image resized")
    elif choice == 3:
        angle = int(input("Enter angle (90/180/270): "))
        if angle == 90:
            img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        elif angle == 180:
            img = cv2.rotate(img, cv2.ROTATE_180)
        elif angle == 270:
            img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        else:
            print("Invalid angle")
        print("Image rotated")
    elif choice == 4:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        print("Converted to grayscale")
    elif choice == 5:
        img = cv2.GaussianBlur(img, (15, 15), 0)
        print("Image blurred")
    elif choice==6:
        x=int(input("enter shape choice: 1-rectangle 2-line 3-circle"))
        if x==1:
            cv2.rectangle(img, (50,50),(200,200),(0, 255, 0),2)
        elif x==2:
            cv2.line(img, (50, 50), (200, 200), (0, 255, 0), 2)
        elif x==3:
            cv2.circle(img, (150, 150), 50, (0, 0, 255), 2)
        else:
            print("invalid choice ")    
    elif choice == 7:
        cv2.imwrite("edited_image.jpg", img)
        print("Image saved as edited_image.jpg")
    elif choice == 8:
        print("Exiting editor")
        break
    else:
        print("Invalid choice")

