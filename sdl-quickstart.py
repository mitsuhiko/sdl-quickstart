#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

  -- SDL Quickstart

  This git repository provides the source for a Python script
  that bootstraps a SDL project with CMake and SDL 1.3.  It
  also adds a bunch of useful helpers that make it easy to
  compile the project on OS X and Windows and adds a skelleton
  for a game class.

  You can get the latest version of the script at the following
  URL:

    http://bit.ly/sdl-quickstart


"""

import re
import os
from subprocess import Popen


MERCURIAL_URL = 'http://hg.libsdl.org/SDL'
template_re = re.compile(r'%([a-zA-Z]+)%')


def get_input(prompt, default=None):
    if default:
        prompt = '%s [%s]' % (prompt, default)
    while 1:
        rv = raw_input('%s: ' % prompt)
        if not rv:
            rv = default
        if rv:
            return rv


def apply_template(string, context):
    def handle_match(match):
        key = match.group(1)
        if key in context:
            return context[key]
        return match.group(0)
    return template_re.sub(handle_match, string)


def main():
    project_name = get_input('Project name')
    namespace = get_input('Namespace', project_name.lower())
    context = {
        'namespace':        namespace,
        'NAMESPACE':        namespace.upper(),
        'projectname':      project_name,
        'PROJECTNAME':      project_name.upper()
    }

    print 'Extracting starter template'
    target_folder = project_name
    for fn, value in PACKAGED_FILES.iteritems():
        value = value.decode('base64').decode('zlib')
        fn = os.path.join(target_folder, apply_template(fn, context))
        dirname = os.path.dirname(fn)
        if dirname and not os.path.isdir(dirname):
            os.makedirs(dirname)
        f = open(fn, 'w')
        f.write(apply_template(value, context))
        f.close()
    print 'Cloning SDL 1.3'
    try:
        Popen(['hg', 'clone', MERCURIAL_URL, 'libs/sdl-1.3']).wait()
    except OSError:
        print 'Could not pull SDL because hg is not installed.'
        print 'Please pull on your own into libs/sdl-1.3 from '
        print MERCURIAL_URL
    print 'All done'
    print
    print 'Now build SDL 1.3 in the libs folder for your platform'
    print 'On OS X and Linux build it like this:'
    print
    print '  $ cd libs/sdl-1.3'
    print '  $ ./configure --prefix=`pwd`/local'
    print '  $ make && make install'
    print
    print 'On windows open the VisualC folder and build the SDL and SDLmain'
    print 'solutions.'


PACKAGED_FILES = {
'./include/%namespace%/%namespace%.hpp': """
eJyFkFFrgzAQx9/zKQ6CUEuZsL2OglRhgqaCA/cWgjnbgCZi5mTQD7802tI+7SUcv/tz+d1R1WqJ
LWTswAMWF2lVxoc0eKo/ypJQF1Ia/82RaAuZbrpJIsxKSzPblzMMoxlw7H7BaKgXCtuIUNXCMldu
6oy9vYZwudwJdyg51lVIKKwQfIrnacx4zBJeuOKhy45Fxor464rUKvF+t9gTilqq1jtWSb4Y3GIO
+Mgj4M5anzrP1y8CLXq0g2gw4L1QGvwTRSB+jJLQdMKe0e483oSgLAhoTN+7xWczSkInf+5r23tM
Ftupg+ozh0Fhg/bZyn6PSp/25Kb+B0pDhRU=
""",
'./scripts/.gitignore': """
eJwDAAAAAAE=
""",
'./libs/.gitignore': """
eJwDAAAAAAE=
""",
'./generate-vs.bat': """
eJxzSE3OyFfIT0vj4spMU8jLL1FIrcgsLlEoK47JK81RyM1OySwCcriSU0AkV3JuYnaqgp4eiA8k
AZIPE5I=
""",
'./.gitignore': """
eJzT0kssKODyTcxOTcvMSeVKzgWy4jPziksSc3L0wDwuLb1EIE6pzMlM4tLT4nIGKXYDKi6GMJ0T
kzNS9UoqSrjKirkAFOUZ1Q==
""",
'scripts/frameworkify.py': """
eJydV99v2zYQfvdfcU1XSNpkuenTYMzD0ixDCzRt0HRPaSDQEh1zlUiBpOL4ZX/77kjql123xfRi
i7w7fnf33fH0/NmiNXqxFnLB5SM0e7tVEua3s+cw/3kOhSqFfFhCazfzX2llps/OzmaAz0azmu+U
/iI2e7fw7+iZuZULMDWrKrRS10yWUAnJwSpVgd0yCwWToPlOC4urWw4Ns1uD+1DuJatF4WxUipWc
VNeaacENCAlZucd32IgK343y1tDCHs1tuOay4KDwXTsLzmwG8HoPJd+wtrIgLOwEAjs8vTeGAo0S
0hIcZ4Qk1q0sKx4Z+Ktz3cBGVSXXaP3TVhjn0ZpMCY2YdwItMri8Zl+4R6KMRSuiKoEVVmCg0dka
d6HRquE6nGCcpmotbNkjhr/DoDkGskGn0ShKFltQG3ChcFEbfCewfXoyn4u/DXvgy6V/oeenSQaz
Zg/X+4umqUTBCFrGmmZxqaTlGIXFNSs+3C4mAvC5N/U7LCh6C6sWNcHx+fFHLQvV7LV42NolxEUC
r16en8N6Dxe6xkx+VJIVmKjMy6JtLg1fwuvbP1MwnMO7t5dX72+vMM4aaqU5ptAyUZlsRjwUdaO0
BWW6f2ZvZhutalCNbZg2HMLGh4Yw39CSns1mSASkjyxzH/GYP/GitWxd8WTpoAwLsEL7GfmXsbWh
37G0ExYbkMr2YsIQM49tuhwygaA+ttKKml9prXQcXQ1nlQqzT7b4kzA28uY9x1LClGNhjBEZTIc9
wlP4tOUkkgb1IyW/3DsQpJ6tIHLJjn4YM8GtFJICKS+kEWXgJ9VKEohrWy0nsCY5wAooc0/k46i5
dJp2jSVScGO6hN5gwcgUbt7eXHmf0UG3Ft9FinpMlEI0fxelo1TeI6dsiYW1IjWPjXqSQd0ioy7V
SmI3j5O7l/c+Tm4/nvhx95QZq0UTJyGUEcQRaTiWPlGHclp358v7+7GjNbPFFgva+xp7j1NYM8Mp
r8HhqntHVN3frFI7ruOOD9qXPZ3kjQzJwlR2ee6U/UFJZwNWq+GMQXHkYChfBzy0yPyA+CkgX1KQ
fPcDaXICXXKQIhYvBcfkvE9UsWXygUeD2UnekmzHMM5JwEQtBVXzvoHFnm4d4bH6yHoKlukHbvNR
cD3MbWtF1UEka6+mV5ozNKqYf/AumJ4RDXdAdKIJlELHU4ujPoBi9ZevSIT6RUTx4MYExlRh6mMX
ILxLkCR13iWPLhfXtOOwYsbhTWHiGp2++qTbPmRIN8xK2MXUhH+OJT5Sor/IR0z8FnMOjCVj+tL5
U1p+J98DkHSidvwcVUYPoIvc+E6cgO6KVSpCk8Ionx4M0uXEjeKFRk2uFz3R+PzNSXBymg7yDqUv
5DGdQ8ho86uVPGHOOFrOxuxAOvpjAOEOXGTZYiD6IoJfRuqz2SjL5NPd/ffb06A+Kq+DRnUgTCK+
dXZxO+ij4zB+3T+xObaF49p7JQ8boLvqrp4K7uaFOPKOnL0wZ6RABd6PWSWNMbQTwQuIj5g34Dhm
5RDmyVaSHBaPoTGMyzKOD/Gn3+BGCEISiPT/ukHqvPV076qjZkijQD03XtFYMR6twg3l9zJWlniY
D+S8cX1+TljxX8mNXUXhpcaZ7pHpVXRz8elNdKqIt7xqVhGrLNcS4T+Gkd19L6C30emjL/3R3pf+
8P7Vz+KryFgcMHOLne87GEolP0f+4ghMRxB95wijVBSijygwvtikqUQCOveT01rcXx7Y7GNaSeA3
eDWwMmhwP3a9p9FQqvZhSxbbmobz5XhYpc8shuMHfmj0HwcdEhoNEIyrOSfo7ita8aE4degNyeN0
hB+J3VeNc73nUVcapm3oRuVld6LVI6OT1kqe4sTkA0ODUjpGkg5AkzCOU0UOhYmEPYEWJ7OYjwoJ
vwgyHKZtfE4kxhDkfvLIaQyK8pwonedh2vX8nv0H/bDazQ==
""",
'./include/%namespace%/game.hpp': """
eJx1UN9rwjAQfs9fcVAqdYztvY6BdOIGTgQf9lhictVAvJQ0rYK4v31pu3bVaV5y+X7k7r5AZSQx
g49lkobL6edsvZomszCd+zJ9X61Y4FlFeF/AAkVClxLhJSS+xyLnAsPnQf20y/NXxliPwICEE2Pg
T2WUBGGVU4LrFK01NhKGCgeFk3FcOKtoCyOnnMbHxnHr3HLg0Y0nbROheVHA1jf3bWsgLzdaibj/
r6Yir+7e3x3QI+u3RfqlSJoDPByaOxrDCSy60hLsU49N4Hwhny8SQ/UYsNXCHS/1DTR0bIzRYEsi
P72XthsNDL9Ubek9TXh7rkgbkw/nb4gyl9xhlGnDHUh3Te84SY0pVkguqued1RWMsPonlZYfupmu
qMK1ndtYrap8y/hmam1GdxLqArmM42/rBj9PmF8+QJIqYz+rYMzV
""",
'./CMakeLists.txt': """
eJytVl1zozYUfV5+xZ00mTgzCe7uzvSd2NjL1AYXcDZ9YmQQRrUsUQTx0oz/e68E/spm24c2Dwn6
Ojr33HOvkm7JhiZbJti22SYV/bNhFc0GT24YeYEPn+xf7qyykn/QtB7c9B+CbOnNnWX9BA5wpmqQ
ORSUZLQCIjJQsqlSCjnjVEGjaAarFlqcBFKWnKWkZlLYlqL1IAqW4ciNLMAfVaXDLWHCTsvS+qBH
a7zHjO7M5i+uM0Za1gcmUt5kdHijiaiSpPTm/NsuNMB7mwxgYQCRfFwgScm53DGxhlRmmrPIFETj
GXy0PwMTHe20oOlGNhingCCC53uYMdF8QwiiYEc513+/4lG5UzZAIA4D8IBsgZO/WiOMFLwFLuUG
r62gLigiVJRToii80EqhLFpKvP4ecko55BWlUEvQOcL9TAHhSp4gMrpq1giyRe4KRyUVmY4FcRAd
UnNu1TCeQU2qNa171cezZBLMUEy4fh3NnV/dZLQMQ9ePky4hydgL90POVmqoMv6AWpgMjZzRFxei
OPT8KVwtSF1ocr1aVzAJ8OidpTVM8GxFqtZcNfMeQyf83UD4ztyN9BENav+sv8z8wom/RMjmRG1/
nE+i5WTiPeM5LlPCNS94YqohfDTE/cOwk7DDD5KxO3GWszjRR63v6cwdz3+fkjbffyWjMf6FEOZr
R7tECorFgRJqjiZjqlU13d4qCDCV09nBFV0Q6OENWdNBvxa6vy290B0bxN6ZR+SCvBjnkCyD24e8
QuPvZLWBkUwludV+7SVBv8baWExpO6c1BoImJbBipqyJQKh0gyaqgdVIDANrgQrZrAvjafQvIytO
O2e5z3HoaHUjuLq6s1gOA2exmKErTIVf7rh+PQ32cPWWJZ7Xds4HXYBYh3InoC9rXbiHfqOF0yaU
AoOvqI6Z6RZDeL9LF6lWnYhaa2K00aWGkCWa2LZ60CTD3pfWsmJUDQzjfyqP/lC/78wrxxVD3Jc7
nZWMYg4p7ApSm3JW5nr6jaZNbfQDmLAKeymWOVYwZkSHpXvXPYJ89fzPn/SkdkznmbOeoNsNLk+X
3nmHvYe5Mwqi5+Rx6Y9nbpde9kJqvHvViIxT0zeO1jlIyYlmsZMdE2Uk1Vy7tq5hcGPf7rseb1ic
QsFWKhQ+CxhibluYjeS01sl68ZCYGROg+bok3YvbPRP7ftg/BPtO4BnyRcuixgfTcyY2JpS+Ujqr
Y1LvjU8OgabaZQhw8h2efftMgXkmOKlrDBfDND28wB1UdJ0WAYx8cvXCZKN4a1tdr000jeR4948i
v34NFq4/PbRJ7xTmWe88mzrvX4fpszrSmmDNGD1PVfcUJcEyXixjbd3vXP3o+QjWufq4Npkmnh/r
uQ5G5zFtVC23SSq3WxRxEDvh1I0vY4JFECHi0puNzTHzbgTzueOPT/d24z08uJiEsk1YjqWX57Si
oj6euqypdxq+/rYzfH2vXy/i2x8WTg0Ef73pQ52/+tDP7vyxMhdh2uiA4UiKGhmr4ZykQTR88+/R
/yRa2dYFlqhKK1biVUezsry1yxYZX0SyfyPfwSgnKf4G0DoeoA==
""",
'./src/main.cpp': """
eJyNU9tKAzEQfd+vGCmV3VKslzdbBVEogje84GOJyaQb3E2WSdYi6r872barLbWYh2Uz55yZk0mm
Y6wsaoUw6lpRoq+ExO5gyr97eVWdJklibIBf2KQUxqYxKGgq+yBzQdDr8eYtSz4S4DUYgLMwM1a5
mYcZQmUshBwhSgvnKgiOGRwnJ9F7R8AERwopIuLNGbVMFGUVknZUCisRchPAaZCiKIydso4FkRNM
Gfe6tjIYZz1ocuUyiTJaIyF7bit6EFa11cBxDlomISxEQBXJLwWWfi/pGA0KtbGo0ufLm6PDDD4/
28iEQxe3zw9ZU+/p6vZmPLl7vAehGTfhnVvmX4dr4MLJZCvJv/uA5TqnIbGjdGeM4W6e52xBuWZG
yuHzmuKBF2ia9RvRtrW70dE/dJtMZlmrIww12YVrvgyqbXwe8dK0IR9AOsIGXMkAJ5C2jcgOYDSC
/WF78lXq7uZu/nh4wPCYEwr1R5vmIHdp1UM2TDpo+fXMzf+aguPjOCIQP3NTzcQs33fKwq/kG5/J
Dvo=
""",
'./src/game.cpp': """
eJyNVltz2jgUfudXnE2mHXuWENJ2Mt3cZhJwEu8CplzKzL54FFsGTYXE2nKAbbK/fY9kG+ykIfBg
7KNP5/Kdi3TIRMDTkMLFB0HmNFmQgH44nuJrY7ZYXNUON+tMJiqmZH5VqyWKKBZAIEWigAkFSyZC
ufSXLFQzuISvzeb5m6AZZdOZQtTpK1TEJVGQsHnKUSqFH2pcs9E8ic5rtdqjZCGU3Dw7C2KGuwn3
aRzL2Mq0JCo8O0NfmZjCR8UUp/UavP/71Wa6UnbtJ5IQQUgjJmhoTdze5082PD1tJD6K2t5kaBsr
XZokZEpv5OraatZBq2gEPmq0bPzS3mw+N151b3zvL3jS/0NndOsNnLuBN+61M5Hb8nrDkde3z2uH
lCfUbDN+BjJVcHEBB62cBzA8nMGBlhpj+sVgqQi5kaJDFaHWKkIWGbV0xZR1gpaea7UK07oisqel
GdFYJMUatju+K3CPeem5I/+723Y8Gy6gaW/i25Wzg5ZMeQhC6iLBFcLZvxRQ3UFdP/07qhwDtNEr
o9FIO/6QqmuFiXpIFbVyWXfcGbnD626/49yMb2+dwbAOOpr9t+XPOnx5f1vbG98Uhvay03b6o3t/
6P7t1OHTHgYGTjtHf30ffDdwnN7+8JvO2Nkffd3p31+X4AY/x4YX2KAa08LRoOjEtLh1cE85l1kS
N0WgUVmn9L2h33J6Iwfj23+9PGPq1WHyKyW+13d6dx1soZJseO9Nenm0unx/MyHsWahjQR6woZSE
wAQLMfYNjXNX3izXuT/lgVrlPN0VVLWk0K1oZR68TMBwSRYuAuJHwk0/mvUp7xJMzKorQ2ohsD/w
/nRaI9crYpryjiShG1KBzb+2NlIvVjNp4SCN6jt5hAxydGL+9PMt012v7XS+u85kG2acCqHH5iWo
OKVvjZD/KjOkaAzKaZkSw1iJlDbFiSnXeXm9pOxbigMom1mvj4jM6pwwwaVcVAw7j8gT0EeVqUrx
kDr94iuQPPQx8z8Sffhka9nJRIIgNWeTjLNzKcqDX84YVoa14cCGn5ua2qgVclkUAVV9GkcynhMR
YNipznSRra05c/pZetvR1icbjsEy6/ZrVbcx/SelIliXlZXDQWW5y/p3fAxqxhIsafkDlmStX4BL
MW0ATCgsYvmAJb+GGQmBQJImC13xIRRslhVZIX1Ip1MaFzUFc/mIWKqCxrbBdNNhWFdI3km0Feuf
ibZy9pc8zQnWEfcl5yZz1kdMnV1VMiN4olGfmnW9XI0W04MR05IZ0GmFiK3Q1ahgr7HZU87475cQ
qvOXLpURVy8CKJeBKYVFiJ1vVTHnFUhZ3dErPgrU8zaqMCbLcraLGYID5EW7lIlYEqbj5kzpO8ID
fiQSmUEyZBrjzWGOc21GEqBCptMZVgINWKLpYobAiioZ470pIAnSGlBBYiaxfEa6rghHrWtGeahr
DCTujHVVBXhHokmj4jOOALK2ikP0eVcz5zQWTaJbege6UhLbtjfFU7rJ4GdDrRcULrMe/TZ2R9va
SpSeHTtHTJaI7BqZ653yFqckbkmOB0Kz8TnSA/bUPP/YztcSUk/WltfxBn52q/Bv0ImdVjPHcnvl
GRwh+WYI/w9fQI8T
"""}


if __name__ == '__main__':
    main()
