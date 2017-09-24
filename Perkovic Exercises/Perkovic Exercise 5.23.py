def pay(PerUur, uren):
    if uren <= 40:
        loon = PerUur * uren
    elif uren <= 60:
        loon = 40 * PerUur + (uren - 40) * 1.5 * PerUur
    else:
        loon = 40 * PerUur + 20 * 1.5 * PerUur + (uren - 60) * 2 * PerUur
    return loon

print(pay(10, 65))





