#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？

i = int(input('净利润:'))


def calculate(profit):
    if profit > 1000000:
        return (profit - 1000000) * 0.01 + calculate(1000000)
    elif profit > 60 * 10000:
        return (profit - 60 * 10000) * 0.015 + calculate(60 * 10000)
    elif profit > 40 * 10000:
        return (profit - 40 * 10000) * 0.03 + calculate(40 * 10000)
    elif profit > 20 * 10000:
        return (profit - 20 * 10000) * 0.05 + calculate(20 * 10000)
    elif profit > 10 * 10000:
        return (profit - 10 * 10000) * 0.075 + calculate(10 * 10000)
    else:
        return profit * 0.1

print(calculate(i))
