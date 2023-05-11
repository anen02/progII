from time import perf_counter as pc
from time import sleep as pause
import multiprocessing as mp

def runner():
    print("Performing a costly function")
    pause(1)
    print("Function complete")

if __name__ == "__main__":
    start = pc()
    p1 = mp.Process(target=runner)
    p2 = mp.Process(target=runner)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = pc()
    print(f"Process took {round(end - start, 2)} seconds")




