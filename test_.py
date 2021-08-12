import av
import cv2
import os
from datetime import datetime
import random 
from aiortc.contrib.media import MediaRecorder
from streamlit_webrtc import webrtc_streamer
from streamlit_webrtc import (
    ClientSettings,
    VideoProcessorBase,
    WebRtcMode,
    webrtc_streamer,
)

def app(data_path, number, usr_name):
  
    class OpenCVEdgeProcessor(VideoProcessorBase):
        def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
            img = frame.to_ndarray(format="bgr24")

            # perform edge detection
            img = cv2.cvtColor(cv2.Canny(img, 100, 200), cv2.COLOR_GRAY2BGR)

            return av.VideoFrame.from_ndarray(img, format="bgr24")

    def in_recorder_factory(number, data_path) -> MediaRecorder:
        num_order = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
        file_name = usr_name + str(num_order)+str(random.randint(0,10))+'input.wav'
        path = os.path.join(data_path,str(number))
        # path = data_path +'/'+ number + '/' + '/' + usr_name + str(numerical_order) + str(random.randint(0,10)) + "input.wav"
        return MediaRecorder(f'{path}/{file_name}', format="wav")  # HLS does not work. See https://github.com/aiortc/aiortc/issues/331
    def out_recorder_factory(number, data_path) -> MediaRecorder:
        # numerical_order = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
        # path = os.path.join(data_path,str(number),usr_name+str(numerical_order)+str(random.randint(0,10))+'output.wav')
        # os.mkdir(path)
        # path = data_path + '/'+ number + '/' + '/'+ usr_name + str(numerical_order) + str(random.randint(0,10)) + "output.wav"
        path = '/data/1/vutuan20209input.wav'
        return MediaRecorder(path, format="wav")
    webrtc_streamer(
        key="loopback",
        mode=WebRtcMode.SENDRECV,
        client_settings=ClientSettings(
            rtc_configuration={
                "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
            },
            media_stream_constraints={
                "video": False,
                "audio": True,
            },
        ),
        video_processor_factory=OpenCVEdgeProcessor,
        in_recorder_factory=in_recorder_factory(number,data_path),
        out_recorder_factory=out_recorder_factory(number,data_path),
    )


# if __name__ == "__main__":
    # app()