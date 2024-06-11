import subprocess
from subprocess import PIPE, STDOUT
import sys
import random
import platform

checker = "./checker_"
if platform.system() == "Linux":
    checker += "linux"
else:
    checker += "Mac"

def test_count(num):
    print("--- " + str(num) + " numbers ---")
    lst = []
    for x in range(0, 10):
        args = random.sample(range(-500, 500), num)
        arg_str = ' '.join(map(str, args))
        stdout = subprocess.run(['./push_swap', arg_str],
                    check=True, capture_output=True, text=True).stdout
        line_count = stdout.count('\n')
        lst.append(line_count)
        p = subprocess.Popen([checker, arg_str], stdout=PIPE, stdin=PIPE,
                    stderr=PIPE, text=True)
        checker_status = p.communicate(input=stdout)[0]
        print(str(line_count) + "\t" + checker_status)
    avg = sum(lst) / len(lst)
    print("--- average: " + str(avg) + "\n")

test_count(2)
test_count(3)
test_count(4)
test_count(5)
test_count(10)
test_count(100)
test_count(187)
test_count(500)
