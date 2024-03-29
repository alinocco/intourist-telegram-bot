Intourist Telegram Bot
======================

## Overview
Intourist Telegram Bot is a bot to view tours' schedule, reserve a tour and make payments. The core funcionality will be focused on payment processing. Then I want to track all the info in DB (preferably PostgreSQL). Also I would love to figure out: Admin Panel for setting the schedule, checking reservasions and payments, and probably configure it with Trello (a current tool for tracking our signed up clients.

## Development Steps
* Set up a basic echo bot to understand the Telegram Bot package.
* Set up a test payment bot to understand the logic of payments.
* Decide the tools for Web side of application: Django, FastAPI, or custom solution. Most likely, it will be Django because of its access to Admin Panel available out-of-the-box.
* Implement the chosen framework project with existing Telegram Bot code.
* Implement proper admin panel.
* Provide integration with Trello to track clients/reservations/payments.

## Setup

### Install
* Python Version Management [Pyenv](https://github.com/pyenv/pyenv) with `curl https://pyenv.run | bash`
* Python Packaging and Dependency Management [Poetry](https://python-poetry.org/docs/) with `python3 install poetry`

### Steps
1. Clone repository:
   ```
   git clone https://github.com/alinocco/intourist-telegram-bot.git
   ```
2. Go to the project folder:
   ```
   cd wayof-backend
   ```
3. Set up a proper python version:
   ```
   pyenv install
   ```
4. Initialize and go to a virtual environment with Poetry:
   ```
   poetry shell
   ```
5. Install dependencies:
   ```
   poetry install
   ```

