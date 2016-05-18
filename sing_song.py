class Song():
    def __init__(self,lyrics):
        self.lyrics = lyrics


    def sing(self):
        return self.lyrics


Birthday = Song("\nHappy B'day To you\nMay god bless u,\nHappy b'day to you....\n")
Star_poem = Song("\nTwinkle Twinkle little star\nHow I wonder what you are\nUp above the world so high,\nlike a diamond in the sky\n")
Christmas = Song("""\nJigle bells jingle bells,\nJingle all the way.\nSantaclaus is coming along riding on a sleigh.\n""")
Sargam = Song("\nSa Re Ga Ma Pa Dha Ni Saa,\n Sa Ni Dha Pa Ma Ga Re Saa\n")

def singer(user):
    if user == 0:
        return 0
    elif user == 1:
        return 1
    elif user == 2:
        return 2
    elif user == 3:
        return 3
    elif user == 4:
        return 4
    else:
        return 5


if __name__ == "__main__":
    print("Select the song")
    print("1. Birthday")
    print("2. Star Poem")
    print("3. Chrismas song")
    print("4. Sargam")
    Flag = True
    while Flag:
        user = int(input("Which song you want? "))
        result = singer(user) 
        if result == 0:
            print("\nYou are out of the game.\n")
            Flag = False

        if result not in [0,1,2,3,4]:
            print("\nEnter a valid choice.\n")
            continue

        if result == 1:
            print Birthday.sing()

        if result == 2:
            print Star_poem.sing()

        if result == 3:
            print Christmas.sing()

        if result == 4:
            print Sargam.sing()





