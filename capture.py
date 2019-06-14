import time
from multiprocessing import Process, Queue
import cv2
import mss
import numpy
import msvcrt as m
import PyWinMouse as mouse

#about 13fps with multiprocessing queue
def screen_record_efficient(queue):
    # 800x600 windowed mode
    mon = {"top": 52, "left": 1, "width": 800, "height": 600}

    # sandwich frames with grayscale "stop start" opencv QR code
    startfps=time.time()
    with mss.mss() as sct:
        for i in range(425):
            start = time.time()
            img = numpy.asarray(sct.grab(mon))
            queue.put(img)
            end = time.time()
            if(end-start<.046):
                time.sleep(.046-(end-start))
            if i == 0:
                a = mouse.Mouse()
                a.move_mouse(17, 687)
                a.left_click()
    endfps=time.time()
    print(endfps-startfps)

    queue.put(None)


#7fps but doesnt matter
def save(queue):
    number = 0

    start = time.time()
    while "there are screenshots":
        img = queue.get()
        if img is None:
            break

        cv2.imwrite("download/img"+str(number)+".png", img)
        #cv2.imshow("download/img"+str(number)+".jpg", img)
        number += 1
    end = time.time()
    print("Saving ", end-start)


if __name__ == "__main__":
    queue = Queue()

    input("Press Enter to continue...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")


    Process(target=screen_record_efficient, args=(queue,)).start()
    Process(target=save, args=(queue,)).start()
