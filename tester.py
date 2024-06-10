import subprocess
import sys
import random

def test_count(num):
    print("--- " + str(num) + " numbers ---")
    lst = []
    for x in range(0, 10):
        args = random.sample(range(800), num)
        arg_str = ' '.join(map(str, args))
        stdout = subprocess.run(['./push_swap', arg_str], check=True, capture_output=True, text=True).stdout
        line_count = stdout.count('\n')
        print(line_count)
        lst.append(line_count)
    print("--- average: " + str(sum(lst) / len(lst)))

test_count(2)
test_count(3)
test_count(4)
test_count(5)
test_count(10)
test_count(100)
test_count(180)
test_count(500)
