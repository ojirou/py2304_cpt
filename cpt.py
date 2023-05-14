import pyautogui as pgui
import time
import os
import keyboard
def main():
    print('Input Movie Name')
    SeminarName = input('>> ')
    SeminarPath='C:\\Users\\user\\Downloads\\'+SeminarName
    folder_exists=os.path.exists(SeminarPath)
    if folder_exists:
        i = 1
        while True:
            new_foldername = f"{os.path.splitext(SeminarPath)[0]}_{i}{os.path.splitext(SeminarPath)[1]}"
            if not os.path.exists(new_foldername):
                break
            i += 1
        SeminarPath = new_foldername
    os.mkdir(SeminarPath)
    print('出力フォルダ:', SeminarPath)
    print('Movie Total Time [min]')
    TimeStr = input('>> ')
    Time = float(TimeStr)
    print('Capture Interval [s]:')
    IntervalStr = input('>> ')
    IntervalInt = int(IntervalStr)
    Interval = float(IntervalStr)
    MaxNum=int(Time*(60/Interval+1))+1
    i=0
    num=1
    count=1
    flag=0
    target_key = ['c', 'q']        
    while (count < MaxNum):   
        while True:
            print('Click at the Upper Left')
            user_input = input(">> ")
            PosUpperLeft=pgui.position()
            print('Click at the Lower Right')
            user_input = input(">> ")
            PosLowerRight=pgui.position()
            x1=PosUpperLeft[0]
            y1=PosUpperLeft[1]      
            dx=PosLowerRight[0]-PosUpperLeft[0]
            dy=PosLowerRight[1]-PosUpperLeft[1]               
            if (dx, dx) == (0,0):
                print('Error: Same coordinate')
            elif (dx <= 0):
                print('Error: Inapropriate x coordinate')
            elif (dy <= 0):
                print('Error: Inapropriate y coordinate')
            else:
                break
        print(x1, y1, dx, dy)
        print('Now capturing. ( reframe:c, quit:q )')
        while (count < MaxNum):                                                                                   
            if (flag==1):
                flag=0
                break
            else:
                for num in range(count, MaxNum):
                    if (flag==1):
                        break
                    else:
                        i+=1
                        num=int(num)
                        s=f'{i:03}'
                        filename=SeminarPath+'\\'+\
                        SeminarName+'_'+str(s)+'.png' 
                        pgui.screenshot(filename, region=(x1, y1, dx, dy))
                        count+=1
                        start_time = time.time()
                        while (flag==0) and (time.time() - start_time < IntervalInt): 
                            for key in target_key:
                                if flag==1:
                                    break
                                elif keyboard.is_pressed(key):
                                    if flag==1:
                                        break
                                    elif keyboard.read_event().event_type == keyboard.KEY_DOWN:
                                        if flag==1:
                                            break
                                        elif keyboard.read_key() == "c":
                                            flag=1
                                            print("You pressed c")
                                            break
                                        elif keyboard.read_key() == "q":
                                            os._exit(0)
    print("finished!")
if __name__ == "__main__":
    main()