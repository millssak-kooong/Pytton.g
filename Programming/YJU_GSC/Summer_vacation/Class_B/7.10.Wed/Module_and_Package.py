# script는 interpriter로 번역이 된다.

# 한 개의 파일은 스크립트 파일을 의미하고 또한 모듈을 의미한다.


from bar import file_name as b_name
import foo

foo.print_name(b_name)

# ----------------------------------------
# Current working directory의 위치 확인

import os

print(os.getcwd())

# ----------------------------------------
# 현재 모듈의 위치 확인

import sys

for path in sys.path:
    print(path)