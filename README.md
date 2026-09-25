# About this project

This is my first python project. It is a CLI program that can calculate expressions and convert various units.

## Prerequisites

* typer
* editable mode in uv


## How to use it

Program can recognize following commands:

   `python3 -m toolkit calc "Expression"`

   `python3 -m toolkit convert Value Unit1 Unit2`
   
   `python3 -m toolkit --help`


### Examples

   `python3 -m toolkit calc "(6-5.3)*-17"`

   `python3 -m toolkit convert 36.6 c f`


### Converter limits

Converter can operate with length, mass and temperature units. Specifically with:

   + Length: mm, cm, m, km

   + Mass: g, kg

   + Temp:


### Few words about calculation and tokenization

Computations within the calculator are performed using the shunting-yard algorithm. The calculator supports parentheses, unary signs, and other mathematical operators.
   
