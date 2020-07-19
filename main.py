from typing import List
import argparse
import bubblesort
import ptvsd
import time


def main():
    """sort"""

    parser = argparse.ArgumentParser()
    parser.add_argument("--remote", type=bool, default=False)
    parser.add_argument("intengers", metavar="N", type=int, nargs="+")
    args = parser.parse_args()

    if args.remote:
        ptvsd.enable_attach(address=("0.0.0.0", 3333))
        ptvsd.wait_for_attach()

    nums: List[int] = args.intengers
    nums = bubblesort.bubblesort(nums)
    print(nums)


if __name__ == "__main__":
    main()
