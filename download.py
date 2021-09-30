import random
import datetime
import ffmpeg
import os
import pathlib
from pathlib import Path
from TikTokApi import TikTokApi

api = TikTokApi.get_instance()
did = str(random.randint(10000, 999999999))
date = str(datetime.date.today().month) + "." + str(datetime.date.today().day)
abs_path = pathlib.Path(__file__).parent.absolute()
save_to_path = os.path.join("/", abs_path, date)

VERIFY_FP = ""

results = 95

videoList = api.trending(
    count=results,
    custom_verifyFp=VERIFY_FP,
    custom_did=did
)

encoded_files = []

Path(save_to_path).mkdir(parents=True, exist_ok=True)

for tiktok in videoList:
    print("Writing: " + str(tiktok['id']))

    video_filename = tiktok['id'] + ".mp4"

    full_path_to_unencoded = os.path.join("/", save_to_path, video_filename)

    videobuffer = api.get_video_by_tiktok(tiktok, custom_did=did)

    with open(full_path_to_unencoded, "wb") as out:

        out.write(videobuffer)

    full_path_to_encoded = os.path.join("/", save_to_path, str(tiktok['id']) + "_encoded.mp4")

    ffmpeg.input(full_path_to_unencoded).output(full_path_to_encoded, vcodec='libx264').run()

    encoded_files.append(full_path_to_encoded)

    if(os.path.exists(full_path_to_unencoded)):
        os.remove(save_to_path + "/" + video_filename)
