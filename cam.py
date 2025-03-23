import cv2

class Application:

    def __init__(self):
        self.vs = cv2.VideoCapture(0)
        ok, frame = self.vs.read()
        cv2.imwrite("a.jpg", frame)


    def destructor(self):
        print("Closing Application...")
        self.root.destroy()
        self.vs.release()
        cv2.destroyAllWindows()



obj=Application()