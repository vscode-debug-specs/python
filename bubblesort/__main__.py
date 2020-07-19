from typing import List
import argparse
import bubblesort
import ptvsd
import time


def main():
    """sort"""

    parser = argparse.ArgumentParser()
    parser.add_argument("--remote", type=bool, default=False)
    parser.add_argument("--sleep", type=int, default=0)
    parser.add_argument("intengers", metavar="N", type=int, nargs="+")
    args = parser.parse_args()

    if args.remote:
        ptvsd.enable_attach(address=("0.0.0.0", 3333))
        ptvsd.wait_for_attach()

    if args.sleep > 0:
        time.sleep(args.sleep)

    nums: List[int] = args.intengers
    nums = bubblesort.bubblesort(nums)
    print(nums)


if __name__ == "__main__":
    main()
