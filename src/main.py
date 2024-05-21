import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command

import settings

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.TOKEN)
dp = Dispatcher()

PRICE = types.LabeledPrice(label="Подписка на 1 месяц", amount=500*100)  # в копейках (руб)


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


@dp.message(Command("bye"))
async def cmd_bye(message: types.Message):
    await message.answer("Bye!")


@dp.message(Command("buy"))
async def buy(message: types.Message):
    if settings.PAYMENTS_TOKEN.split(':')[1] == 'TEST':
        await bot.send_message(message.chat.id, "Тестовый платеж!!!")

    await bot.send_invoice(message.chat.id,
                           title="Подписка на бота",
                           description="Активация подписки на бота на 1 месяц",
                           provider_token=settings.PAYMENTS_TOKEN,
                           currency="kgs",
                           photo_url="https://www.aroged.com/wp-content/uploads/2022/06/Telegram-has-a-premium-subscription.jpg",
                           photo_width=416,
                           photo_height=234,
                           photo_size=416,
                           is_flexible=False,
                           prices=[PRICE],
                           start_parameter="one-month-subscription",
                           payload="test-invoice-payload")


@dp.pre_checkout_query()
async def pre_checkout_query(pre_checkout_query_: types.PreCheckoutQuery):
    """
    Telegram sends pre-checkout after User clicks Pay.
    Must be answered in 10 seconds.
    """
    await bot.answer_pre_checkout_query(pre_checkout_query_.id, ok=True)


@dp.message(F.successful_payment)
async def successful_payment(message: types.Message):
    """
    Telegram sends after successful payment.
    Business logic for successful payment should get applied.
    """
    print("SUCCESSFUL PAYMENT:")
    payment_info = message.successful_payment.model_dump()
    for k, v in payment_info.items():
        print(f"{k} = {v}")

    await bot.send_message(message.chat.id,
                           f"Платеж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошел успешно!!!")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
