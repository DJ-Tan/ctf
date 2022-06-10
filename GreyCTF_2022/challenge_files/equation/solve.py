from Crypto.Util.number import bytes_to_long

FLAG = bytes("grey{solving_equation_aint_that_hard_rite_gum0pX6XzA5PJuro}",'utf-8')

n = len(FLAG) # 58 / 59
m1 = bytes_to_long(FLAG[:n//2])
m2 = bytes_to_long(FLAG[n//2:])

x = 6561821624691895712873377320063570390939946639950635657527777521426768466359662578427758969698096016398495828220393137128357364447572051249538433588995498109880402036738005670285022506692856341252251274655224436746803335217986355992318039808507702082316654369455481303417210113572142828110728548334885189082445291316883426955606971188107523623884530298462454231862166009036435034774889739219596825015869438262395817426235839741851623674273735589636463917543863676226839118150365571855933
y = 168725889275386139859700168943249101327257707329805276301218500736697949839905039567802183739628415354469703740912207864678244970740311284556651190183619972501596417428866492657881943832362353527907371181900970981198570814739390259973631366272137756472209930619950549930165174231791691947733834860756308354192163106517240627845889335379340460495043

'''
Equations: 
13 * m2 ** 2 + m1 * m2 + 5 * m1 ** 7 = x    -> (1)
7 * m2 ** 3 + m1 ** 5 = y                   -> (2)

Since m1 is the highest power in both equations, we utilise the bit length of x and y to determine the length of m1
since exponentiation approximately multiplies the number of bits
Bit length of x is 1618 -> Closest multiple of 56 = 1624
Bit length of y is 1154 -> Closest multiple of 40 = 1160
=> m1 length = 1624/56 = 29
=> Flag length = 58 or 59

Since m1 is the highest power in both equations, using Equation 1, we can slowly adjust each character of the flag 
until we match x as closely as possible, giving us m1

Assuming that the flag length is 58, we found that changing the first character of m2 did not improve the match with x,
leading us to conclude that the flag length was 59 instead.

Since we already determined m1, using Equation 2, we can eliminate m1 to get a result f, that is purely dependent on m2.
We repeat what we did with m1 and Equation 1 with m2 and Equation 2 until m2 ** 3 exactly matched f

Putting m1 and m2 together, we got back the flag.
'''

# Checking digits of 7 * m2 ** 3 against f
# print(str(5 * m1**7)[:400])
# print(str(x)[:400])

f = (y - m1 ** 5) // 7
check = x - 5 * m1**7
# Checking digits of m2 ** 3 against f
# print(str(m2**3)[:100])
# print(str(f)[:100])

