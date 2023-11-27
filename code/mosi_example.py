'''
题目：easy_cryptoCrypto
来源：https://ctf.bugku.com/challenges/detail/id/50.html
0010 0100 01 110 1111011 11 11111 010 000 0 001101 1010 111 100 0 001101 01111 000 001101 00 10 1 0 010 0 000 1 01111 10 11110 101011 1111101
`http://www.hiencode.com/morse.html`
'''
def easyCryptoCrypto():
    key = "0010 0100 01 110 1111011 11 11111 010 000 0 001101 1010 111 100 0 001101 01111 000 001101 00 10 1 0 010 0 000 1 01111 10 11110 101011 1111101"
    value = key.replace("0", ".").replace("1", "-")
    print(value)
