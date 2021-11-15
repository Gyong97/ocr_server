import os
import cv2
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


#시간정보를 받아서 영상의fps와 함께 계산해서 원하는 frame번호 얻는 함수.
# @@@@@@@@@ time 받는 형식 정해지면 수정 필요.@!@@@@@@@@@@@
def cal_time_to_frame(time, fps):
    hms = time.split(':')
    time_second = int(hms[0]) * 60 * 60 + int(hms[1]) * 60 + int(hms[2])
    frame_number = (time_second * fps)
    # fps는 flaot값으로 나오기 때문에 float값 상태에서 곱해준 뒤, 반올림을 해야 가장 근접한 프레임이 나온다.
    return round(frame_number)

if __name__ == '__main__':
    # parameter (video_time, video_name)
    video_time = sys.argv[1]
    video_name = sys.argv[2]

    #create our directory for the frames
    if not os.path.exists('./image_frames'):
        os.makedirs('./image_frames')
    
    #  create our video path
    vidpath = os.path.join(os.getcwd(),'Downloads')
    test_vid = cv2.VideoCapture(os.path.join(vidpath, video_name + '.mp4'), cv2.CAP_FFMPEG)
    #video의 fps
    fps = (test_vid.get(cv2.CAP_PROP_FPS))    
    #원하는 frame값을 구한다.
    want_frame = cal_time_to_frame(video_time, fps)
    #원하는 frame 이미지를 저장할 이름을 정한 뒤 ( video name + frame number + .png )
    name = './image_frames/' + video_name + str(want_frame) + '.png'
    # test_vid 객체 ( VideoCapture 객체 ) 의 프레임을 원하는 프레임 바로 이전 프레임으로 옮긴다.
    test_vid.set(cv2.CAP_PROP_POS_FRAMES, want_frame -1)
    # read()함수를 통해서 test_vid 의 다음 프레임을 받아온다. (그래서 이전 프레임으로 set한다.)
    ret, frame = test_vid.read() 
    # 받아온 이미지 프레임 저장.
    # @@@이미지 처리는 여기서도 가능 ( 잘라내기 or OCR이미지 전처리 ) @@@
    cv2.imwrite(name, frame) 
    
    # 종료.
    test_vid.release()
    #이미지 파일 이름(경로) return.
    print(name, end='')
    
