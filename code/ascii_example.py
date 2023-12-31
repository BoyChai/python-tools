'''
连接：https://ctf.bugku.com/challenges/detail/id/59.html
题目：这不是md5
666c61677b616537333538376261353662616566357d
'''
import base64


def notMd5():
    key = '666c61677b616537333538376261353662616566357d'
    for i in range(0, len(key) + 1, 2):
        if i == 0:
            continue
        print(chr(int(key[i - 2:i], 16)), end="")
'''
蓝盾杯-ASCII
来源：https://www.bilibili.com/video/BV1T5411g7JR?p=12&vd_source=5cf6ecba30bdbb5e2ad9856f540a60da
d4e8e5a0f1f5e9e3eba0e2f2eff7eea0e6eff8a0eaf5edf0a0eff6e5f2a0f4e8e5a0ece1faf9a0e4efe7a1a0d4e8e5a0e6ece1e7a0e9f3baa0c2c4c3d4c6fbd9b0f5dfe1f2e5dff3ede1f2b7fd
hint:需要将每一组二进制数最高位的1去掉，也就是转换成十进制之后再减去128
'''
def lanDunASCII():
    key = "d4e8e5a0f1f5e9e3eba0e2f2eff7eea0e6eff8a0eaf5edf0a0eff6e5f2a0f4e8e5a0ece1faf9a0e4efe7a1a0d4e8e5a0e6ece1e7a0e9f3baa0c2c4c3d4c6fbd9b0f5dfe1f2e5dff3ede1f2b7fd"
    for i in range(0, len(key) + 1, 2):
        if i == 0:
            continue
        print(chr(int(key[i - 2:i], 16) - 128), end="")

'''
ISCC-隐秘的信息
来源：https://blog.csdn.net/qq_43759478/article/details/90488283
这是一个被混淆的文件，但是我忘记了这个文件的密码。你能够帮助我还原明文吗?
附件内容：
0126 062 0126 0163 0142 0103 0102 0153 0142 062 065 0154 0111 0121 0157 0113 0111 0105 0132 0163 0131 0127 0143 066 0111 0105 0154 0124 0121 060 0116 067 0124 0152 0102 0146 0115 0107 065 0154 0130 062 0116 0150 0142 0154 071 0172 0144 0104 0102 0167 0130 063 0153 0167 0144 0130 060 0113
'''
def ISCCYinCang():
    key = "0126 062 0126 0163 0142 0103 0102 0153 0142 062 065 0154 0111 0121 0157 0113 0111 0105 0132 0163 0131 0127 0143 066 0111 0105 0154 0124 0121 060 0116 067 0124 0152 0102 0146 0115 0107 065 0154 0130 062 0116 0150 0142 0154 071 0172 0144 0104 0102 0167 0130 063 0153 0167 0144 0130 060 0113"
    key2 = key.split(" ")
    value = ""
    # 没有大于7的数字，判断8进制
    for e in key2:
        value += chr(int(e, 8))
        print(chr(int(e, 8)), end="")
    print()
    # base64解密
    print(base64.b64decode(value).decode())

'''
科来杯 进制转换
附件中内容
d87 x65 x6c x63 o157 d109 o145 b100000 d116 b1101111 o40 x6b b1100101 b1101100 o141 d105 x62 d101 b1101001 d46 o40 d71 x69 d118 x65 x20 b1111001 o157 b1110101 d32 o141 d32 d102 o154 x61 x67 b100000 o141 d115 b100000 b1100001 d32 x67 o151 x66 d116 b101110 b100000 d32 d102 d108 d97 o147 d123 x31 b1100101 b110100 d98 d102 b111000 d49 b1100001 d54 b110011 x39 o64 o144 o145 d53 x61 b1100010 b1100011 o60 d48 o65 b1100001 x63 b110110 d101 o63 b111001 d97 d51 o70 d55 b1100010 d125 x20 b101110 x20 b1001000 d97 d118 o145 x20 d97 o40 d103 d111 d111 x64 d32 o164 b1101001 x6d o145 x7e
解题思路是这样的，d是10进制 x是16进制 o是8进制 b是2进制
这个解题思路是常识，应该牢记。
'''
def keLaiJinZhi():
    key = "d87 x65 x6c x63 o157 d109 o145 b100000 d116 b1101111 o40 x6b b1100101 b1101100 o141 d105 x62 d101 b1101001 d46 o40 d71 x69 d118 x65 x20 b1111001 o157 b1110101 d32 o141 d32 d102 o154 x61 x67 b100000 o141 d115 b100000 b1100001 d32 x67 o151 x66 d116 b101110 b100000 d32 d102 d108 d97 o147 d123 x31 b1100101 b110100 d98 d102 b111000 d49 b1100001 d54 b110011 x39 o64 o144 o145 d53 x61 b1100010 b1100011 o60 d48 o65 b1100001 x63 b110110 d101 o63 b111001 d97 d51 o70 d55 b1100010 d125 x20 b101110 x20 b1001000 d97 d118 o145 x20 d97 o40 d103 d111 d111 x64 d32 o164 b1101001 x6d o145 x7e"
    key2 = key.split(" ")
    for e in key2:
        if (e[0:1] == "d"):
            print(chr(int(e[1:], 10)), end="")
        if (e[0:1] == "x"):
            print(chr(int(e[1:], 16)), end="")
        if (e[0:1] == "o"):
            print(chr(int(e[1:], 8)), end="")
        if (e[0:1] == "b"):
            print(chr(int(e[1:], 2)), end="")

'''
i春秋-MISC-对错
来源：https://blog.csdn.net/weixin_51830687/article/details/116118380
附件内容：011001100110110001100001011001110111101101111010011010000100010101100011001110010011000000110011001101000110101001101111011001000111001101101010011001100110111101110011011010110110111101111101
提醒：如果说1代表对，0代表错，那么-1代表？
思路：一看就是二进制的，而ASCII是八位二进制，分割之后尝试ASCII
'''
def iChunQiuDuiCuo():
    key = "011001100110110001100001011001110111101101111010011010000100010101100011001110010011000000110011001101000110101001101111011001000111001101101010011001100110111101110011011010110110111101111101"
    for e in range(0, len(key) + 1, 8):
        if e == 0:
            continue
        print(chr(int(key[e - 8:e], 2)), end="")


'''
zero和one
来源：https://blog.csdn.net/weixin_45871855/article/details/120005161
ZEROONEZEROZEROZEROZEROONEZEROZEROONEZEROZEROONEZEROZEROONEZEROONEZEROONEZEROONEZEROZEROZEROONEZEROONEZEROZEROONEONEZEROONEZEROZEROZEROZEROONEONEZEROONEZEROONEZEROONEZEROZEROZEROONEZEROZEROZEROONEONEZEROZEROONEONEONEONEZEROONEONEZEROONEONEZEROONEZEROZEROZEROZEROZEROONEONEZEROZEROZEROONEZEROONEONEZEROZEROONEZEROZEROZEROZEROONEONEZEROZEROONEONEZEROONEZEROONEONEONEONEONEZEROZEROONEONEZEROZEROZEROONEZEROONEONEZEROONEONEONEZEROZEROONEZEROONEONEONEONEONEZEROONEONEONEZEROZEROZEROZEROZEROONEONEZEROONEONEZEROZEROZEROZEROONEONEZEROONEZEROZEROZEROZEROONEONEZEROZEROZEROONEZEROONEONEZEROONEONEONEZEROZEROONEZEROONEONEONEONEONEZEROZEROONEONEZEROONEZEROONEZEROZEROONEONEZEROZEROZEROONEZEROZEROONEONEZEROONEONEONEZEROZEROONEONEZEROZEROONEONEZEROONEONEONEONEONEZEROONE
'''
key = "ZEROONEZEROZEROZEROZEROONEZEROZEROONEZEROZEROONEZEROZEROONEZEROONEZEROONEZEROONEZEROZEROZEROONEZEROONEZEROZEROONEONEZEROONEZEROZEROZEROZEROONEONEZEROONEZEROONEZEROONEZEROZEROZEROONEZEROZEROZEROONEONEZEROZEROONEONEONEONEZEROONEONEZEROONEONEZEROONEZEROZEROZEROZEROZEROONEONEZEROZEROZEROONEZEROONEONEZEROZEROONEZEROZEROZEROZEROONEONEZEROZEROONEONEZEROONEZEROONEONEONEONEONEZEROZEROONEONEZEROZEROZEROONEZEROONEONEZEROONEONEONEZEROZEROONEZEROONEONEONEONEONEZEROONEONEONEZEROZEROZEROZEROZEROONEONEZEROONEONEZEROZEROZEROZEROONEONEZEROONEZEROZEROZEROZEROONEONEZEROZEROZEROONEZEROONEONEZEROONEONEONEZEROZEROONEZEROONEONEONEONEONEZEROZEROONEONEZEROONEZEROONEZEROZEROONEONEZEROZEROZEROONEZEROZEROONEONEZEROONEONEONEZEROZEROONEONEZEROZEROONEONEZEROONEONEONEONEONEZEROONE"
value = key.replace("ZERO",'0').replace("ONE",'1')
for e in range(0,len(value)+1,8):
    if e==0 :
        continue
    print(chr(int(value[e-8:e],2)),end="")
    