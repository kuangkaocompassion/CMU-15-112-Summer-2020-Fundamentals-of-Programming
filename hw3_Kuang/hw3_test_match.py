sym = """
    *     *     *
   ***   ***   ***
  ***** ***** *****
   ***   ***   ***
    *     *     *
"""


sol = """
    T     h     r
   eeD   iam   ond
  s!Thr eeDia monds
   !Th   ree   Dia
    m     o     n
"""

ans = ""

for i in sym:
    ans += i

print(ans)
print(sym.strip("\n"))
print(sol.strip("\n"))

if ans == sym :
    print("yes")

