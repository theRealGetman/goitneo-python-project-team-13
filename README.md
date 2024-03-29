# Muad'Dib
## _Hello fremen, this is your personal assistant Muad'Dib_

![](img/pol.jpg)

## Version [1.0.0-beta]

A personal assistant with a command line interface.

## Main features

- Saves contacts with names, addresses, phone numbers, emails, and birthdays to your contacts book.
- Displays a list of contacts whose birthdays are within a specified number of days from the current date.
- Checks the correctness of the entered phone number and email when creating or editing a record and notifies the user in case of incorrect entry.
- Searches for contacts among the contacts in the book.
- Edits and deletes entries from the contact book.
- Stores notes with textual information.
- Search by notes.
- Edit and delete notes.

## Muad'Dib can also work with notes

- Ability to add text notes.
- Search, edit, and delete notes.
- You can add "tags" to your notes, keywords that describe the topic and subject of the record.
- Search and sort notes by keywords (tags).

## Installation

Muad'Dib requires [Python](https://www.python.org/) to run.

To get started with Muad'Dib from root directory run:

```sh
pip install .
```

And now you can use `muaddib` as a command from terminal.

## Available commands:

Muad'Dib has now been extended with the following functionality.
Instructions on how to use them are provided below.

| Сommands | Response |
| ------ | ------ |
| help | Shows all available commands |
| hello | Greeting command |
| add-contact | Adds new contact |
| change-contact | Changes existing contact |
| remove-contact | Delete a contact by name. Required arguments: name |
| find-contact | Shows contact phones. Required arguments: name or phone search query |
| all-contacts | Shows all contacts |
| add-birthday | Adds birthday to contact. Date format: dd.mm.yyyy |
| show-birthday | Shows contact birthday. Required arguments: name |
| birthdays | Shows upcoming birthdays. Optional argument: number of days |
| add-email | Adds an email to a contact by name. Required argument: name |
| show-email | Shows an email of contact by name. Required argument: name |
| change-email | Changes existing email. Required arguments: name, old email, new email |
| exit | Exits assistant |
| close | Alias for Exit command |

## Aditional features

Muad'Dib can store and manage your notes by adding "tags" to your notes + searching notes by these "tags".

| Сommands for notes | Response |
| ------ | ------ |
| add-note | Adds new note. |
| edit-note | Changes existing note by title. |
| show-notes | Shows all notes. Optional argument: tag or title |
| remove-note | Delete a note by title. Required arguments: title |

## Muad'Dib provides

#### It can guess what the fremen wants from it based on the entered text and offer the nearest command to execute!

## License

### _Confirmed by Shai-Hulud_
![](img/shai-hulud.jpg)

**Free Software, Hell Yeah!**
