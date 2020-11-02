# 수학문제 규칙 찾기 : 가로+세로-gcd
import math


def solution(w, h):
    ret = math.gcd(w, h)
    return w*h - (w+h-ret)
