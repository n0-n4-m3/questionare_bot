from tech_fields import *
import asyncio

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message
import json

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML)) 
    
async def main():
    users = json.loads(open("users/users_questionnaire_masair.json","r").read())["users"]
    text = "Доброго воскресного дня!\n\nПишем тебе с желанием выразить благодарность за участие в служении на Кристмас Эйр! \n\nНадеемся, и для тебя это время было благословением!\n\nДо встречи на следующих общих служениях 🙏"
    for user in users:
        await bot.send_message(chat_id=user,text=text)
        print(f"Sent to {user}")
        
if __name__ == "__main__":
    asyncio.run(main())