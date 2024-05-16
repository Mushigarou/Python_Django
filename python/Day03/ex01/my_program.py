from local_lib.path import Path
import os

def test():
    dir = Path('./test')
    dir.mkdir(mode=755)
    dir.
    dir.joinpath("text.txt").touch()

if __name__ == "__main__":
    test()