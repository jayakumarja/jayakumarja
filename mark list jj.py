a="subject"
b="mark"
t="tamil"
tm="55"
e="english"
em="45"
m="maths"
mm="48"
sci="science"
sm="38"
so="social"
som="47"

print(f"╔{'═'*10}╦{'═'*10}╗")
print(f"║{' '*10}║{' '*10}║")
print(f"╠{'═'*10}╬{'═'*10}╣")
print(f"║{t}{' '*(10-len(t))}║{tm}{' '*(10-len(tm))}║")
print(f"║{e}{' '*(10-len(e))}║{em}{' '*(10-len(em))}║")
print(f"║{m}{' '*(10-len(m))}║{mm}{' '*(10-len(mm))}║")
print(f"║{sci}{' '*(10-len(sci))}║{sm}{' '*(10-len(sm))}║")
print(f"║{so}{' '*(10-len(so))}║{som}{' '*(10-len(som))}║")
print(f"║{' '*10}║{' '*10}║")

print(f"╠{'═'*10}╬{'═'*10}╣")
print(f"╚{'═'*10}╩{'═'*10}╝")


