# Price number to Polish word converter

## Description
A Python program for converting numbers (including floats) to their textual equivalents in Polish, with formatting for prices in złoty and grosz. Supports numbers from 0 to 999 billion.

## Features

- Converts integers to text.
- Converts floating-point numbers to text (złoty and grosz).
- Supports numbers up to 999 billion.

## Requirements
- Python 3.x

## Installation
No special installation required. Copy the source code and run it in a Python environment:

```
python main.py
```

## Usage
Call the price_to_text function with a number as the argument.


**Example 1:** 1234 zł
```python
print(price_to_text(1234))
```
Output:
```
tysiąc dwieście trzydzieści cztery złote
```


**Example 2:** 124 234,56 zł

```python
print(price_to_text(124234.56))
```
Output:
```
sto dwadzieścia cztery tysiące dwieście trzydzieści cztery złote pięćdziesiąt sześć groszy
```

## Limitations

Designed specifically for the Polish language.

Does not support numbers larger than 999 billion.

## License

MIT License
