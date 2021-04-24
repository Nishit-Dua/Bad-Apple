import sys
import os
import glob
import cv2
import time
from playsound import playsound
import threading

from imageToAscii import convert_and_save_to_ascii


def progress_bar(current: int, total: int, barLength=25) -> None:
    # Yoined From SO
    progress = float(current) * 100 / total
    arrow = '#' * int(progress / 100 * barLength - 1)
    spaces = ' ' * (barLength - len(arrow))
    sys.stdout.write('\rProgress: [%s%s] %d%% Frame %d of %d frames' % (
        arrow, spaces, progress, current, total))


# TODO extract Frames from video and convert them to ascii.

# def get_frames_from_video(video_path: str) -> None:
#     '''
#     Extracts frames from the video if it already exits says lite
#     '''
#     if os.path.exists(video_path):
#         FILE_NAME = video_path.split(".")[0]
#         FOLDER_NAME = "{}Extracted".format(FILE_NAME)
#         if not os.path.exists(FOLDER_NAME):
#             os.mkdir(FOLDER_NAME)
#             os.system(
#                 'ffmpeg -i {} {}Extracted/{}%06d.jpg'.format(video_path, FILE_NAME, FILE_NAME))
#         else:
#             print("Frames Already Exists, Dont they?")

def get_frames_from_video(video_path: str) -> None:
    # Yoinked from Github
    cap = cv2.VideoCapture(video_path)
    current_frame = 1
    # gets the total number of frames
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print("Video frame extraction, total number of frames")
    while current_frame < total_frames:
        ret, frame = cap.read()
        # sys.stdout.write("\rExtracting " + str(frame_count) + " of " + str(total_frames) + " frames")
        progress_bar(current_frame, total_frames - 1)
        frame_name = r"BadAppleExtracted/" + \
            "BadApple" + str(current_frame).zfill(4) + ".jpg"
        cv2.imwrite(frame_name, frame)
        current_frame += 1
    cap.release()
    sys.stdout.write("\nVideo frame extraction completed\n")


def save_all_frames_as_ascii(input_folder: str, output_folder: str) -> None:
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    for file in glob.glob(input_folder+"/*"):
        txt_file_name = file.split("/")[-1].split('.')[0]
        print(txt_file_name)
        convert_and_save_to_ascii(file, output_folder+f'/{txt_file_name}.txt')


if __name__ == "__main__":
    FILE_NAME = "BadApple.mp4"
    #! HardCoding Duration
    DURATION = 219.15
    total_frames = int(cv2.VideoCapture(FILE_NAME)
                       .get(cv2.CAP_PROP_FRAME_COUNT))

    sleep_time = DURATION/total_frames

    # get_frames_from_video(FILE_NAME)
    # save_all_frames_as_ascii("BadAppleExtracted", "BadAppleTxt")
    threading.Thread(target=playsound, args=(
        'bad-apple-audio.mp3',), daemon=True).start()
    # playsound('bad-apple-audio.mp3')

    for f in glob.glob('BadAppleTxt/*'):
        with open(f, "r") as f2:
            start = time.time()
            sys.stdout.write(f'{f2.read()}\n')
            time.sleep(max(sleep_time-(time.time()-start), 0))
    #
            # os.system('cls' if os.name == 'nt' else 'clear')
    #         # TODO add sleep Logic
    #         #? Let's think, python thake lets say -> 0 amount of time to write to console,
    #         #? and there are 6500 something frames which we need to display over a length
    #         #? of "k" sec so sleep for k/6500??

    #         #? Retard Alert apparently python is such a fast language it takes time to
    #         #? Print to the damn console (tbf also reading file but still), so yeah the
    #         #? audio gets out of sync! Solution remove the delay it takes to print lmfao
