PyX

---

About

It's here. And it's got a kernel, a file system, a standard library, and a shell.

---

How-to

Run shell.py to get started

---

Technical breakdown

The lowest level API is file.py, the file system API.
Next comes kernel.py, this standardizes errors and checks permissions from...
Shell is the highest level, allowing a user to interact with the file system.
Shell calls kernel, which calls file, which works with Python's standard library.
Somewhere between kernel and shell also sits std, for now it handles non-kernel errors.

---

FAQ

Q: Kept us waiting
A: Huh?
