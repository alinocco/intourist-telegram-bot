import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import StateFilter
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove

import settings
from src.utils.keyboards import make_row_keyboard

logging.basicConfig(level=logging.INFO)
bot = Bot(token=settings.TELEGRAM_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


# FSM
TOURS = ["Kol-Tor", "Kegety", "Tuyuk"]


class SignupForTour(StatesGroup):
    choosing_tour = State()
    making_payment = State()
    registering_with_name = State()
    registering_with_phone = State()
    confirming_registration = State()


@dp.message(StateFilter(None, SignupForTour.choosing_tour), Command("tours"))
async def get_tours(message: types.Message, state: FSMContext):
    await message.answer(
        text=f"Please, choose a tour:",
        reply_markup=make_row_keyboard(TOURS)
    )
    await state.set_state(SignupForTour.choosing_tour)


@dp.message(SignupForTour.choosing_tour, F.text.in_(TOURS))
async def register_with_tour(message: types.Message, state: FSMContext):
    await state.update_data(tour=message.text)
    await message.answer(
        text="Please, enter your name.",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(SignupForTour.registering_with_name)


@dp.message(SignupForTour.registering_with_name, F.text)
async def register_with_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Please, enter your phone.")
    await state.set_state(SignupForTour.registering_with_phone)


@dp.message(SignupForTour.registering_with_phone, F.text)
async def register_with_name(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    user_data = await state.get_data()
    await message.answer(
        text=f"Enter yes/no for confirmation:\n"
             f"Tour: {user_data.get('tour')}\n"
             f"Name: {user_data.get('name')}\n"
             f"Phone: {user_data.get('phone')}\n",
    )
    await state.set_state(SignupForTour.confirming_registration)


@dp.message(SignupForTour.confirming_registration, F.text.in_(("yes", "no")))
async def confirm_registration(message: types.Message, state: FSMContext):
    is_confirmed = message.text == "yes"
    user_data = await state.get_data()
    if is_confirmed:
        # Payment
        await buy(message)
        await message.answer(
            text=f"Successfully registered.\n\n"
                 f"Tour: {user_data.get('tour')}\n"
                 f"Name: {user_data.get('name')}\n"
                 f"Phone: {user_data.get('phone')}\n\n"
                 f"Please, proceed with payment."
        )
    else:
        await message.answer("Declined.")
    await state.set_state(None)


# Payment
PRICE = types.LabeledPrice(label="Подписка на 1 месяц", amount=500*100)  # в копейках (руб)


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
