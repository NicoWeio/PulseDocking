import subprocess
import sys

import react

# def watcher(fooo):
#     print(f"Hello World {fooo}")

def monitor(index):
    zeroCount = 0
    isPlaying = None

    # print("TEST")

    proc = subprocess.Popen(['parec', f"--monitor-stream={index}"],stdout=subprocess.PIPE)
    # proc = subprocess.Popen(['echo', '"Foo"'],stdout=subprocess.PIPE)
    while True:
        data = proc.stdout.read(1)
        isZero = ord(data) == 0
        newIsPlaying = isPlaying
        if (isZero):
            zeroCount += 1
        else:
            zeroCount = 0
            newIsPlaying = True
        if (zeroCount > 100):
            newIsPlaying = False

        if (newIsPlaying != isPlaying):
            # print("playing" if newIsPlaying else "not playing")
            isPlaying = newIsPlaying
            react.onPlayStateChange(newIsPlaying)

if __name__ == '__main__':
    print("I am… main.")
    monitor(513)
