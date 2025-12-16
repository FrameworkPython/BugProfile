import asyncio
import os
from rubpy import Client


async def main():
    profile = "photo.jpg" #عکس اصلی
    thumb = "photo2.jpg" # عکس بیرون 

    if not (os.path.isfile(profile) and os.path.isfile(thumb)):
        raise FileNotFoundError("فایل‌های لازم یافت نشدند.")

    async with Client("rubpy") as bot:
        thumb_id = (await bot.upload(thumb)).file_id
        result = await bot.upload_avatar(
            object_guid="me",
            image=profile,
            thumbnail_file_id=thumb_id,
        )
        if result:
            print("پروفایل و تامبنیل آپلود شدند")


asyncio.run(main())
