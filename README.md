# Roman Numerals

Simple [roman numeral][rom-num] parser function in Python.

I had to do one of these in pseudo-code as an interview exercise and decided to write it up in Python and throw it on here.

It has some limitations:

  * It only supports the characters `I`, `V`, `X`, `L`, `C`, `D` and `M`.
  * Instances of [subtractive notation][sub-not] only support a single prefix character.
  * However, subtractive pairs can contain any two characters so long as the first is less than the first. So `roman_value('IM') == 999`, which I don't think is typical.

[rom-num]: //en.wikipedia.org/wiki/Roman_numerals
[sub-not]: //en.wikipedia.org/wiki/Subtractive_notation
