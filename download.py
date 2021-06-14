import random
import ffmpeg
from TikTokApi import TikTokApi
api = TikTokApi.get_instance()

VERIFY_FP = ""
did = str(random.randint(10000, 999999999))

results = 10

trending = api.trending(count=results, custom_verifyFp=VERIFY_FP, custom_did = did)

for tiktok in trending:
    print(tiktok['id'])
    videobuffer = api.get_video_by_tiktok(tiktok, custom_did=did)
    with open(tiktok['id'] + ".mp4", "wb") as out:
        out.write(videobuffer)
    ffmpeg.input(tiktok['id'] + '.mp4').output(tiktok['id'] + "_encoded.mp4", vcodec='libx264').run()