### BetterDesign
## Purpose
BetterDesign is a simple python module to make styling command line applications easier.
## Usage
You can install this module using:
```
pip install BetterDesign
```
You can import this module using:
```py
import BetterDesign as bd
```
Printing a table code example:
```py
import BetterDesign as bd

values = {
    "GitHub": "https://github.com/c0nvict/BetterDesign",
    "PyPi": "https://pypi.org/project/BetterDesign"
}

table = bd.table(values)

print(table)
```
![Screenshot](https://media.discordapp.net/attachments/965371411180945439/966692517762465852/unknown.png)

Centering a string code example:
```py
import BetterDesign as bd

string = "Hello world!"

print(bd.center(string)) # this works for multiple line strings and allows you to use the "end" keyword unlike python's native center.
```
![Screenshot](https://media.discordapp.net/attachments/965371411180945439/966693268182143036/unknown.png)

Using colors with a table code example:
```py
import BetterDesign as bd

values = {
    "GitHub": "https://github.com/c0nvict/BetterDesign",
    "PyPi": "https://pypi.org/project/BetterDesign"
}

table = bd.table(values, value_color="green", key_color="green", border_color="red")

print(table)
```
![Screenshot](https://media.discordapp.net/attachments/965371411180945439/966693835793129522/unknown.png)

There is some other stuff that I have not shown examples for yet, just feel free to read the code or message me on discord at convict#0001!
## Updates and new features
If I ever update this, it will be uncommon since I only made this when I was bored. I do plan to eventually add some stuff with colors, feel free to submit a pull request if you add anything!
## Credits
This was solely developed by <a href="https://github.com/c0nvict">c0nvict</a>, this isn't supposed to be a huge project, just some things to make your application better
