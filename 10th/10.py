class Song:
    
    def spell_title_author(self):
        if self.author != "" and self.title != "":
            print(f"{self.author} wrote {self.title}")
        elif self.author != "" and self.title == "":
            print(f"{self.author} is the author")
        elif self.author == "" and self.title != "":
            print(f"{self.title} is the title")
        else:
            print("No title or author here!")

    def __init__(self, title="", author="", lyrics=()):
        self.title = title
        self.author = author
        self.lyrics = lyrics

        print(f"New Song made!")
        self.spell_title_author()


    def sing(self, max_value=-1):
        self.max_value = max_value
        self.spell_title_author()

        if self.max_value == -1:
            print(*self.lyrics, sep=f"\n")
        else:
            print(*self.lyrics[:max_value], sep=f"\n")

        return self

    def yell(self, max_value=-1):
        self.max_value = max_value
        self.spell_title_author()

        lyrics_list = list(self.lyrics[:max_value])
        full_lyrics_list = list(self.lyrics)
        converted_lyrics = [c.upper() for c in lyrics_list]
        full_converted_lyrics = [c.upper() for c in full_lyrics_list]

        if self.max_value == -1:
            print(*full_converted_lyrics, sep=f"\n")
        else:
            print(*converted_lyrics, sep=f"\n")

        return self

new_song = Song(title="virsraksts", lyrics=("rinda 1","rinda 2","rinda 3"))
# new_song.sing(1).yell()


class Rap(Song):

    def __init__(self, title="", author="", lyrics=(), master_c = ""):
       super().__init__(title="", author="", lyrics=())
       self.master_c = master_c

    def break_it(self, max_lines = -1, drop = "yeah"):
        self.max_lines = max_lines
        self.drop = drop

        self.spell_title_author()

#this is where the breaking goes

        return self


