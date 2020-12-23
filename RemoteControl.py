
class RemoteControl:

    def __init__(self):

        self.channels = ['CN','espn','cnn','power HD','BBc', 'Music','Netflix']
        self.index = 0

    def __iter__(self):

        return self

    def __next__(self):

        self.index += 1

        if self.index == len(self.channels):

            raise  StopIteration

        return self.channels[self.index]


if __name__ == '__main__':

    rc = RemoteControl()

    itr = iter(rc)

    print(next(itr))
    print(next(itr))
    print(next(itr))
    print(next(itr))
    print(next(itr))