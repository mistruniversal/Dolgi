import logging
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import filters
from aiogram.utils import executor

API_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
IMAGE_API_URL = 'YOUR_IMAGE_GENERATION_API_URL'
API_KEY = 'YOUR_API_KEY'

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Отправь мне описание, и я сгенерирую изображение!")

@dp.message_handler()
async def generate_image(message: types.Message):
    description = message.text
    await message.reply("Генерирую изображение...")

    # Запрос к API для генерации изображения
    try:
        response = requests.post(
            IMAGE_API_URL,
            headers={'Authorization': f'Bearer {API_KEY}'},  # Если требуется авторизация
            json={'prompt': description}  # Замените на нужные параметры для вашего API
        )

        if response.status_code == 200:
            image_url = response.json().get('url')  # Измените в зависимости от структуры ответа вашего API
            await message.reply_photo(image_url)
        else:
            await message.reply("Не удалось сгенерировать изображение. Попробуйте еще раз.")
    except Exception as e:
        logging.error(f"Error while generating image: {e}")
        await message.reply("Произошла ошибка при генерации изображения.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
