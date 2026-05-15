a=10
b=3

print(f"{a}+{b}={a+b}")
print(f"{a}-{b}={a-b}")
print(f"{a}*{b}={a*b}")
print(f"{a}/{b}={a/b}")
print(f"{a}//{b}={a//b}")
print(f"{a}%{b}={a%b}")
print(f"{a} ** {b} = {a**b}")
print(f"{a} == {b} → {a == b}")


umar = 20
has_id_card = True

can_vote = umar >= 18 and has_id_card
print(f"Kya vote de sakta hai? {can_vote}")

is_minor = umar < 18 or not has_id_card
print(f"Kya minor hai? {is_minor}")