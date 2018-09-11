import ex40_mystuff as mystuff

try:
    print(mystuff.mystuff['apple'])
    # print(mystuff['apple])  # this is wrong!!!
except TypeError as e:
    print(e)

mystuff.apple()
print(mystuff.pen)


class MyStuff(object):  # can remove (object), i.e. including ()
    def __init__(self):
        self.pen = "I have an pen-n-apple"

    def apple(self):
        print("I am a fuji apple." + self.pen)


thing = MyStuff()  # instantiate
print(thing.pen)
thing.apple()


class Song(object):
    def __init__(self, lyrics):  # like C# constructor
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["Happy birthday to you",
                   "This is your moment",
                   "I will always sing for you"])

an_jing_le = Song(["Only piano is left here",
                   "together with the wedding from my dream",
                   "how may I give everything I have to you."])

happy_bday.sing_me_a_song()
an_jing_le.sing_me_a_song()
