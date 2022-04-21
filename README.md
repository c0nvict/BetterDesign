### BetterDesign
## Purpose
BetterDesign is a simple python module to make styling command line applications easier.
## Usage
You can install BetterDesign using this command:
```
pip install BetterDesign
```
You can import BetterDesign like this:
```py
import BetterDesign as bd
```
Example code for printing a table:
```py
import BetterDesign as bd

values = {
    "GitHub": "https://github.com/c0nvict",
    "PyPi": "https://pypi.org/project/BetterDesign/1.0.0/"
    }

print(bd.table(values))
```
```
╔══════════════════════════════════════════════╦══════════════════════════════════════════════╗
║ GitHub                                       ║ https://github.com/c0nvict                   ║
║ PyPi                                         ║ https://pypi.org/project/BetterDesign/1.0.0/ ║
╚══════════════════════════════════════════════╩══════════════════════════════════════════════╝
```
## Updates and new features
If I ever update this, it will be uncommon since I only made this when I was bored. I do plan to eventually add some stuff with colors, feel free to submit a pull request if you add anything!
## Credits
This was solely developed by <a href="https://github.com/c0nvict">c0nvict</a>, this isn't supposed to be a huge project, just some things to make your application nicer
