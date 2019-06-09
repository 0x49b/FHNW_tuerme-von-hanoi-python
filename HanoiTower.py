# Implementation of Towers of Hanoi
import datetime


class HanoiTower:
    steps = 0
    silent = False

    def move(self, n, source, helper, target):

        #  print("move( ", n, source, helper, target, " called")
        if n > 0:

            # move tower of size n - 1 to helper:
            self.move(n - 1, source, target, helper)

            # move disk from source peg to target peg
            if source[0]:
                self.steps = self.steps + 1
                disk = source[0].pop()

                if not self.silent:
                    print("moving " + str(disk) + " from " + source[1] + " to " + target[1])

                target[0].append(disk)

            # move tower of size n-1 from helper to target
            self.move(n - 1, helper, source, target)


if __name__ == '__main__':
    ht = HanoiTower()

    source = ([3, 2, 1], "source")
    target = ([], "target")
    helper = ([], "helper")
    ht.silent = True
    ht.move(len(source[0]), source, helper, target)
    print("steps needed: {}".format(ht.steps))
    print("time needed: {} by 1 disc/second".format(str(datetime.timedelta(seconds=ht.steps))))
