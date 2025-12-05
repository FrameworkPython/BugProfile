import asyncio
import os
from rubpy import Client


async def main():
    try:
        async with Client("rubpy") as bot:
            profile = "photo.jpg" #عکس اصلی 
            thumb = "photo1.jpg" # عکس بیرون  

            if not os.path.isfile(profile):
                raise FileNotFoundError(f"فایل {profile} یافت نشد.")
            if not os.path.isfile(thumb):
                raise FileNotFoundError(f"فایل {thumb} یافت نشد.")

            thumb_id = (await bot.upload(thumb)).file_id

            result = await bot.upload_avatar(
                object_guid="me",
                image=profile,
                thumbnail_file_id=thumb_id,
            )

            if result:
                print("پروفایل و تامبنیل آپلود شدند")
    except Exception as e:
        print(f"خطا: {e}")


asyncio.run(main())
