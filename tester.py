import subprocess
from subprocess import PIPE, STDOUT
import sys
import random
import platform

OK = 0
KO = 0

checker = "../checker_"
if platform.system() == "Linux":
    checker += "linux"
else:
    checker += "Mac"

def test_count(num):
    global OK
    global KO
    print("--- " + str(num) + " numbers ---")
    lst = []
    for x in range(0, 100):
        args = random.sample(range(-500, 500), num)
        arg_str = ' '.join(map(str, args))
        stdout = subprocess.run(['../push_swap', arg_str],
                    check=True, capture_output=True, text=True).stdout
        line_count = stdout.count('\n')
        lst.append(line_count)
        p = subprocess.Popen([checker, arg_str], stdout=PIPE, stdin=PIPE,
                    stderr=PIPE, text=True)
        checker_status = p.communicate(input=stdout)[0]
        if (checker_status == "OK\n"):
            OK += 1
        else:
            KO += 1
        print(str(line_count) + "\t" + checker_status)
    avg = sum(lst) / len(lst)
    max_count = max(lst)
    min_count = min(lst)
    print("avg: " + str(avg) + " max: " + str(max_count) + " min: " + str(min_count) + "\n")

test_count(2)
test_count(3)
test_count(4)
test_count(5)
test_count(10)
test_count(100)
test_count(187)
test_count(500)

print("OK: " + str(OK) + " KO: " + str(KO))
