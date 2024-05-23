import threading

ex1data = "aaa"
ex2data = "abababaab"

thread1 = False
thread2 = False
thread3 = False

# List thats keeps track of thread results
boolList = [thread1, thread2, thread3]


# Generate tests
def example1(index: int, char: str) -> None:
    # do the threading for a FA
    if char == 'a':
        boolList[index] = True


def example2A(index: int, char: str) -> None:
    # do the threading for a FA
    if char == 'a':
        boolList[index] = True


def example2B(index: int, char: str) -> None:
    # do the threading for a FA
    if char == 'b':
        boolList[index] = True


if __name__ == "__main__":
    # L1(aaa), this requires us to use three threads
    # this is a simple NFA test
    threads = list()
    for index in range(3):
        i = ex1data[index]
        x = threading.Thread(target=example1, args=(index, i,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        thread.join()

    if thread1 and thread2 and thread3:
        print("example 1 accepted")

    for i in range(0, len(boolList) - 1):
        boolList[i] = False

    # L2((a,b)*aba(a,b)*),
    # this requires us to use three threads to check for aba
    threads = list()
    for outIndex in range(len(ex2data)):
        if ex2data[outIndex] is None:
            print("rejected")
            break
        i = ""
        for index in range(3):
            i = ex2data[index]

            if index == 2:
                x = threading.Thread(target=example2B, args=(index, i,))
            else:
                x = threading.Thread(target=example2A, args=(index, i,))

            threads.append(x)
            x.start()

        for index, thread in enumerate(threads):
            thread.join()

        if thread1 and thread2 and thread3:
            print("example 2 accepted")
        elif i == 'a' or i == 'b':
            continue
        else:
            print("rejected")
            break
