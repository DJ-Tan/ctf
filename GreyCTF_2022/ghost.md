# Ghost

**Category:** Misc<br>
**Difficulty:** Easy 🍭<br>
**Points:** 50

## Challenge Description

I tried to send you a bunch of messages :)

## Analysis

First thing to do is the determine the filetype:<br>
`file ghost`<br>
`> ghost: ASCII text, with CRLF line terminators`<br>
It can be established that this is a .txt file. Hence, open it up in a text editor to take a look.

It would appear that some lines are encrypted, however these have nothing to do with the flag that we are looking for:<br>
1. "This is not it man, try harder!" - Base64 decode into Hex to Text converter
2. "This is not the flag man D:" - Base32 decode
3. "flag{notThatSimple:P}" - Caesar cipher

## Solution

The hint lies with the title of the challenge **ghost**. Indeed there appears to be whitespace between the lines of ASCII symbols and Pikachu trying hard to manage a thunderbolt. To see the spaces and tabs, open the file in Visual Studio Code and [set it to show whitespace characters](https://stackoverflow.com/questions/30140595/show-whitespace-characters-in-visual-studio-code).

By setting the spaces to 0, and the tabs to 1, we are presented with a binary sequence as follows:
`01100111011100100110010101111001011110110110011101101000001100000111001100110111010111110110001001111001011101000011001100100100010111110110111000110000011101000101111100110001011011100111011001101001011100110100100101100010011011000011001101111101`

Using a [binary to text converter](https://www.convertbinary.com/to-text/), the flag will be decrypted.

`Flag: grey{gh0s7_byt3$_n0t_1nvisIbl3}`
