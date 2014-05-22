# Description

Diary is a little python program, written by me (**@benaryorg**).
It is a web-application, to store your personal diary in an easy way!

## Development

I currently do not have much time to develop this program, but I would like to use it by myself, so I will put most of my time in it.

Please report bugs or tell me what features you would like to see soon.

## Branches

There will be two branches.

### stable

The stable version, where **all** bugfixes directly go to.

### testing

The branch I will use for developing (because I have more than just one computer).

## Concept

It's concept is easy. You have a database where everything is stored.
There you have a table `users` with all your users and passwords (hashed).
The table `diaries` is to store your different diaries, for example you could have one diary for writing about school, one for writing about yourself, one for your boy/girlfriend and so on.
Here is also stored, if the diary is public (blog-like), private (for yourself) or protected (only chosen poeple have access).
The table `entries` stores your diary entries.

## Technical Details

Diary is written in _python2.7_ and is using _flask_ and _sqlalchemy_!

# Contribution

This project is on **GitHub**!

Just send a pull request!

# License

This program uses the **WTFPL** (Do What The Fuck You Want To Public License)!

I would appreciate it, if you would leave my name somewhere in the HTML-templates.
