import torch
import cv2
import av
import os

model_path = '../trained_weights/best.pt' 
model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, force_reload=True)

def detect_logos_and_save_video(input_video_path, output_video_path, modified_frames_dir):
    if not os.path.exists(modified_frames_dir):
        os.makedirs(modified_frames_dir)
    
    input_container = av.open(input_video_path)
    output_container = av.open(output_video_path, mode='w')
    
    stream = input_container.streams.video[0]
    out_stream = output_container.add_stream('mpeg4', rate=stream.rate)
    out_stream.width = stream.width
    out_stream.height = stream.height
    out_stream.pix_fmt = 'yuv420p'
    
    frame_index = 0
    for frame in input_container.decode(video=0):
        img = frame.to_image()  
        img.save('frame.jpg')
        results = model('frame.jpg')
        results.render()  
        img = results.imgs[0]  
        

        if results.xyxy[0].shape[0] > 0:  
            img.save(os.path.join(modified_frames_dir, f'modified_frame_{frame_index}.jpg'))
        
        new_frame = av.VideoFrame.from_image(img, format='rgb24')
        for packet in out_stream.encode(new_frame):
            output_container.mux(packet)
        
        frame_index += 1

    for packet in out_stream.encode():
        output_container.mux(packet)
        
    input_container.close()
    output_container.close()

if __name__ == "__main__":
    input_video_path = '../data/input/inp.mp4'
    output_video_path = '../data/output/out.mp4'
    modified_frames_dir = '../data/frames/' 
    detect_logos_and_save_video(input_video_path, output_video_path, modified_frames_dir)
