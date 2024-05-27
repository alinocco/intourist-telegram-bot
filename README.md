Intourist Telegram Bot
======================

## Overview

Intourist Telegram Bot is a bot to view tours' schedule, reserve a tour and make payments. The core functionality will
be focused on payment processing. Then I want to track all the info in DB (preferably PostgresSQL). Also, I would love
to figure out: Admin Panel for setting the schedule, checking reservations and payments, and probably configure it with
Trello (a current tool for tracking our signed up clients).

### Key Models

#### General

* User with administrative fields (group assignment client/guide/admin, permissions, is staff, is admin, is superuser)
  and profile information (photo, instagram etc.)
* Location
* Tour with location, schedule, common details
* TourInstance with tour, date, guide, tourists/group of tourists
* TouristAttendance?

#### Billing

* Reservation
* Payment

#### Loyalty Program

* History
* Balance
* Levels

## Development Steps

### Whole Product

- [x] Set up a basic echo bot to understand the Telegram Bot package
- [x] Set up a test payment bot to understand the logic of payments
- [x] Define the scope of work: web app, mobile app or **Telegram bot with Trello integration**
- [ ] Design architecture and database
- [ ] Decide the tools for Web side of application: Django, FastAPI, or custom solution. Most likely, it will be Django
  because of its access to Admin Panel available out-of-the-box
- [ ] Implement the chosen framework project with existing Telegram Bot code
- [ ] Implement proper admin panel
- [ ] Provide integration with Trello to track clients/reservations/payments

### Telegram-bot with Trello Integration

- [x] Basic payments
- [x] Basic FSM
- [x] Basic Trello API
- [ ] Design business flow
- [ ] Design architecture
- [ ] Design database
- [ ] Implement user flow
- [ ] Implement business flow
- [ ] Notifications

#### User Flow

Get schedule with `/tours` command as a clickable elements. Pick up a tour. Provide name, phone and additional info.
Make payment.

#### Business Flow

The schedule is preserved in Google Sheets file (or better DB and Admin). The user: gets the scheduled tours with `/tours` command. Pick up a
tour. Provide number of people, name, phone (for each) and additional info. Make payment. On successful payment, we
update Trello Board by adding the new tourists to the corresponding tour. Additionally, we can notify client the day
before the tour (DB needed).

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
6. Run the main script:
   ```
   python3 src/main.py
   ```

