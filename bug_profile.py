from rubpy import Client
import asyncio
import os


async def main():
    try:
        async with Client(name='rubpy', display_welcome=False) as bot:
            files = {
                "profile_img": "img1.jpg",  # عکس پروفایل اصلی
                "thumb_img": "img2.jpg"     # عکسی که از بیرون میخواین ببینین
            }
            
            for file_name, file_path in files.items():
                if not os.path.exists(file_path):
                    raise FileNotFoundError(f"فایل {file_path} یافت نشد.")
            
            profile_res = await bot.upload(files["profile_img"])
            thumb_res = await bot.upload(files["thumb_img"])
            
            profile_id = profile_res["file_id"]
            thumb_id = thumb_res["file_id"]
            
            me = await bot.get_me()
            guid = me["user"]["user_guid"]
            
            upload_data = {
                "object_guid": guid,
                "thumbnail_file_id": thumb_id,
                "main_file_id": profile_id,
            }
            
            result = await bot.builder(name='uploadAvatar', input=upload_data)

            if result:
                print("پروفایل و تامبنیل آپلود شدند")
   
    except Exception as e:
        print(f"خطا: {e}")


asyncio.run(main()) 
