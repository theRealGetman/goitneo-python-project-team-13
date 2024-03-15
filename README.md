# Muad'Dib
## _Hello freeman, this is your personal assistant Muad'Dib_

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Version [1.0.0-beta]

A personal assistant with a command line interface.

## Features

- Saves contacts with names, addresses, phone numbers, emails, and birthdays to your contacts book.
- Displays a list of contacts whose birthdays are within a specified number of days from the current date.
- Checks the correctness of the entered phone number and email when creating or editing a record and notifies the user in case of incorrect entry.
- Searches for contacts among the contacts in the book.
- Edits and deletes entries from the contact book.
- Stores notes with textual information.
- Search by notes.
- Edit and delete notes.

## Installation

Muad'Dib requires [Node.js](https://nodejs.org/) v10+ to run.

To get started with Muad'Dib:

```sh
pip3 install -r requirements.txt
```

## Available commands:

Muad'Dib has now been extended with the following functionality.
Instructions on how to use them are provided below.

| Сommands | Response |
| ------ | ------ |
| help | Shows all available commands |
| hello | Greeting command |
| add-contact | Adds new contact. Required arguments: name, phone (10 digits) |
| change-contact | Changes existing contact. Required arguments: name, old phone, new phone |
| find-contact | Shows contact phones. Required arguments: name or phone search query |
| all-contacts | Shows all contacts |
| add-birthday | Adds birthday to contact. Date format: dd.mm.yyyy |
| show-birthday | Shows contact birthday. Required arguments: name |
| birthdays | Shows upcoming birthdays |
| exit | Exits assistant |
| close | Alias for Exit command |

## License

Shai-Hulud

**Free Software, Hell Yeah!**
