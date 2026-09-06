rut = input()

rut_inv = rut[::-1]
s = 0; m = 2

for i in rut_inv:
    s += int(i)*m
    m +=1
    if m > 7:
        m = 2

resto = s % 11
res = 11 - resto

if res == 11:
    print("code verificador: " + "0")
elif res == 10:
    print("code verificador: " + "K")
else:
    print(f"code es: {res}")