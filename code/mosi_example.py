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
'''
来源：https://www.bilibili.com/video/BV1T5411g7JR/?p=22&spm_id_from=pageDriver&vd_source=5cf6ecba30bdbb5e2ad9856f540a60da
恰恰 恰恰恰 恰绑恰绑 恰 绑绑恰绑 {恰恰绑 恰恰恰 恰恰恰 恰绑绑}
最后出来的莫斯密码解密方式不是全都丢进去解密，直接丢进去的‘{}’会干扰解密结果，应该把花括号里面和外面的莫斯密码分开解密
解密之后的内容为：MOCTF{GOOD}
'''
def qiaBang():
    key = "恰恰 恰恰恰 恰绑恰绑 恰 绑绑恰绑 {恰恰绑 恰恰恰 恰恰恰 恰绑绑}"
    # value = key.translate(''.maketrans("恰绑","-."))
    value = key.replace("恰", "-").replace("绑", ".")
    print(value)