Intourist Telegram Bot
======================

## General
Intourist Telegram Bot is a bot to view tours' schedule, reserve a tour and make payments. The core funcionality will be focused on payment processing. Then I want to track all the info in DB (preferably PostgreSQL). Also I would love to figure out: Admin Panel for setting the schedule, checking reservasions and payments, and probably configure it with Trello (a current tool for tracking our signed up clients.

## Development steps
* Set up a basic echo bot to understand the Telegram Bot package.
* Set up a test payment bot to understand the logic of payments.
* Decide the tools for Web side of application: Django, FastAPI, or custom solution. Most likely, it will be Django because of its access to Admin Panel available out-of-the-box.
* Implement the chosen framework project with existing Telegram Bot code.
* Implement proper admin panel.
* Provide integration with Trello to track clients/reservations/payments.
