
import module1
from module1 import function1,function2
from module1 import *

from packages1.sub_package1.module1 import function1

def main():
    ## Thực hiện một đoạn mã nào đó
    module1.function1()
    function1()

print("Đây là chương trình của chúng tôi")

if __name__ == "__main__":
    main()