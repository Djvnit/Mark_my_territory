import numpy as np
import cv2

class chess_board(object):
    def __init__(self,img_path):
        self.img = cv2.imread(img_path)

    def resizing(self,new_dim):
        self.new_dim = new_dim
        self.img_resized = cv2.resize(self.img, (self.new_dim, self.new_dim))

    def drawing(self, position):
        self.position = position
        unit_dim = self.new_dim/8
        decoded = []
        while len(self.position) != 2:
            self.position = input("Invalid code dear. Try to enter a alpha-numeric code of length 2. :")
        if self.position[0].lower() == 'a':
            decoded.append(1)
        elif self.position[0].lower() == 'b':
            decoded.append(2)
        elif self.position[0].lower() == 'c':
            decoded.append(3)
        elif self.position[0].lower() == 'd':
            decoded.append(4)
        elif self.position[0].lower() == 'e':
            decoded.append(5)
        elif self.position[0].lower() == 'f':
            decoded.append(6)
        elif self.position[0].lower() == 'g':
            decoded.append(7)
        elif self.position[0].lower() == 'h':
            decoded.append(8)
        else:
            print("Sorry!!! Territory out of the chess board can not be marked.")
            exit(0)

        if self.position[1] == '8':
            decoded.append(1)
        elif self.position[1] == '7':
            decoded.append(2)
        elif self.position[1] == '6':
            decoded.append(3)
        elif self.position[1] == '5':
            decoded.append(4)
        elif self.position[1] == '4':
            decoded.append(5)
        elif self.position[1] == '3':
            decoded.append(6)
        elif self.position[1] == '2':
            decoded.append(7)
        elif self.position[1] == '1':
            decoded.append(8)
        else:
            print("Sorry!!! Territory out of the chess board can not be marked.")
            exit(0)
        bottom_right = [decoded[0]*unit_dim, decoded[1]*unit_dim]
        top_left = [bottom_right[0]-unit_dim, bottom_right[1]-unit_dim]
        b,g,r = (self.img_resized[int(top_left[0]+(unit_dim//2)),int(top_left[1]+(unit_dim//2))])
        if b < 100 and g < 100 and r < 100:
            cv2.circle(self.img_resized,(int(top_left[0]+(unit_dim/2)),int(top_left[1]+(unit_dim/2))),int(unit_dim/2) , (255,255,255), -1)
        else:
            cv2.circle(self.img_resized,(int(top_left[0]+(unit_dim/2)),int(top_left[1]+(unit_dim/2))),int(unit_dim/2) , (0,0,0), -1)

    def displaying(self):
        cv2.imshow("Marked My Location.", self.img_resized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



        

        
