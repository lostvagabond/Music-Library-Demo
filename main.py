class library:

    def __init__(self, dict):
        self.dict = dict

    def showMusic(self):

        for i in self.dict:
            print(f"{i}:\n")
            for c in self.dict[i]:
                if c == "":
                    continue
                else:
                    print(f"- {c}\t")
            print(" ")

    def addSong(self, artist, song):

        if artist.__contains__(" "):
            artist = artist.split(" ")
            artist = (x.capitalize() for x in artist)
            artist = " ".join(artist)
        else:
            artist = artist.capitalize()

        if artist.endswith(" ") or artist.startswith(" "):
            artist = artist.strip(" ")

        if song.__contains__(" "):
            song = song.split(" ")
            song = (x.capitalize() for x in song)
            song = " ".join(song)
        else:
            song = song.capitalize()

        if song.endswith(" ") or song.startswith(" "):
            song = song.strip(" ")

        if song.__contains__(","):
            song = song.split(",")
            song = (x.capitalize() for x in song)
            song = ",".join(song)

        if song.__contains__("."):
            song = song.split(".")
            for x in song:
                if not x[0].isupper():
                    x = x.capitalize()
                #song = (x.capitalize() for x in song)
            song = ".".join(song)

        if artist not in self.dict:
            print(f"{artist} Is Not In Database")
        elif song in self.dict[artist]:
            print(f"{song} Is Already In Database")
        else:
            self.dict[artist].append(song)
            file = open(filename,'r+')
            file.truncate(0)
            file.close()
            file = open(filename, "a")
            for key in self.dict:
                file.write(f"{key}:")
                for y in self.dict[key]:
                    file.write(f"-{y}")
                file.write("\n")
            print("Song Added")

    def addArtist(self,artist):

        if artist.__contains__(" "):
            artist = artist.split(" ")
            artist = (x.capitalize() for x in artist)
            artist = " ".join(artist)
        else:
            artist = artist.capitalize()

        if artist.endswith(" ") or artist.startswith(" "):
            artist = artist.strip(" ")

        if artist in self.dict:
            print(f"{artist} is Already In Database")
        else:
            self.dict.update({artist:[]})
            file = open(filename, 'r+')
            file.truncate(0)
            file.close()
            file = open(filename, "a")
            for key in self.dict:
                file.write(f"{key}:")
                for y in self.dict[key]:
                    file.write(f"-{y}")
                file.write("\n")
            print("Artist Added")

    def deleteSong(self,artist,song):

        if artist.__contains__(" "):
            artist = artist.split(" ")
            artist = (x.capitalize() for x in artist)
            artist = " ".join(artist)
        else:
            artist = artist.capitalize()

        if artist.endswith(" ") or artist.startswith(" "):
            artist = artist.strip(" ")

        if song.__contains__(" "):
            song = song.split(" ")
            song = (x.capitalize() for x in song)
            song = " ".join(song)
        else:
            song = song.capitalize()

        if song.endswith(" ") or song.startswith(" "):
            song = song.split(" ")

        if artist not in self.dict:
            print(f"{artist} Not In Database")

        elif song not in self.dict[artist]:
            print(f"{song} Not In Database")

        else:
            self.dict[artist].remove(song)
            file = open(filename, 'r+')
            file.truncate(0)
            file.close()
            file = open(filename, "a")
            for key in self.dict:
                file.write(f"{key}:")
                for y in self.dict[key]:
                    file.write(f"-{y}")
                file.write("\n")
            print("Song Deleted")


    def deleteArtist(self,artist):

        if artist.__contains__(" "):
            artist = artist.split(" ")
            artist = (x.capitalize() for x in artist)
            artist = " ".join(artist)
        else:
            artist = artist.capitalize()

        if artist.endswith(" ") or artist.startswith(" "):
            artist = artist.strip(" ")

        if artist not in self.dict:
            print(f"{artist} Not In Database")
        else:
            self.dict.pop(artist)
            file = open(filename, 'r+')
            file.truncate(0)
            file.close()
            file = open(filename, "a")
            for key in self.dict:
                file.write(f"{key}:")
                for y in self.dict[key]:
                    file.write(f"-{y}")
                file.write("\n")
            print("Artist Deleted")

def main():

    feeling = True
    print(f"Welcome To Ny Music Library Demo\n"
          f"You Can Do As Follows")

    while feeling:
        print(f""
              f"1- Show Music\n"
              f"2 - Add Song(s)\n"
              f"3 - Add Artist(s)\n"
              f"4 - Delete Song(s)\n"
              f"5 - Delete Artist(s)\n"
              f"6 - Quit")

        choice = input("What do you want to do? ")

        if choice == "1":

            Library.showMusic()

        elif choice == "2":
            while True:
                artist = input("Who is the artist? ")

                song = input("What is the song? ")

                while True:
                    if song =="":
                        print("Enter A Valid Song")
                        break
                    elif song.isspace():
                        print("Enter A Valid Song")
                        break
                    else:
                        Library.addSong(artist, song)
                        break

                question = input("Continue Adding Songs? ").upper()
                if question.__contains__("N"):
                    break

        elif choice == "3":
            while True:
                artist = input("Who is the artist? ")

                while True:
                    if artist =="":
                        print("Enter A Valid Artist")
                        break
                    elif artist.isspace():
                        print("Enter A Valid Artist")
                        break
                    else:
                        Library.addArtist(artist)
                        break

                question = input("Continue Adding Artists? ").upper()
                if question.__contains__("N"):
                    break

        elif choice == "4":
            while True:
                artist = input("Who is the artist? ")

                song = input("What is the song? ")

                while True:
                    if song =="":
                        print("Enter A Valid Song")
                        break
                    elif song.isspace():
                        print("Enter A Valid Song")
                        break
                    else:
                        Library.deleteSong(artist,song)
                        break

                question = input("Continue Deleting Songs? ").upper()
                if question.__contains__("N"):
                    break

        elif choice == "5":
            while True:
                artist = input("Who is the artist? ")
                while True:
                    if artist =="":
                        print("Enter A Valid Artist")
                        break
                    elif artist.isspace():
                        print("Enter A Valid Artist")
                        break
                    else:
                        Library.deleteArtist(artist)
                        break

                question = input("Continue Deleting Artists? ").upper()
                if question.__contains__("N"):
                    break

        elif choice == "6":
            print("Goodbye")
            feeling = False

        else:
            print("Please choose a valid option")


if __name__ == '__main__':
    
    filename = "music"
    dict = {}
    with open(filename) as f:
        for line in f:
            key, x = line.strip().split(":")
            value = x.split("-")
            if value != "":
                dict.update({key:value})

    for key in dict:
        for y in dict[key]:
            dict[key] = list(filter(None, dict[key]))
    Library = library(dict)
    main()
