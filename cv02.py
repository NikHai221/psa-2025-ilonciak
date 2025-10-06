#!/usr/bin/env python3

class LP():
    def __init__(self, name, year, artist, duration):
        self._name = name
        self._year = year
        self._artist = artist
        self._duration = duration

    def to_string(self):
        out = "| {0:^20} | {1:4} | {2:^20} | {3:^8} |".format(self._name, self._year, self._artist, self._duration)
        return out
    
class Library():
    def __init__(self):
        self._library = list()

    def insert_LP(self, lp):
        self._library.append(lp)

    def delete_LP(self, lp):
        self._library.remove(lp)

    def delete_LP_index(self, index):
        self._library.pop(index)
    
    def clean_library(self):
        self._library.clear()

    def seed_library(self):
        self.insert_LP(LP( "Paradise City", 1987, "Guns & Roses", 100))
        self.insert_LP(LP( "Swimming", 2018, "Mac Miller", 120))
        self.insert_LP(LP( "Banditi de Prague", 2010, "Kabat", 90))
    
    def to_string(self):
        out =  "|{}|\n".format("-"*68)
        out += "| ID | {:^20} | Year | {:^20} | Duration |\n".format("Title", "Artists")
        out += "|{}|\n".format("-"*68)
        i = 0
        for lp in self._library:
            out += "|{:2} {}\n".format(i, lp.to_string())
            i += 1
        out += "|{}|\n".format("-"*68)
        return out
    


def main():
    library = Library()

    while True:
        print("|----------------|")
        print("|     Menu       |")
        print("|----------------|")
        print(" 1 - Add new LP.")
        print(" 2 - Remove LP.")
        print(" 3 - Clear Library.")
        print(" 4 - Print Library.")
        print(" 5 - Seed Library.")
        print(" q - Exit program.")
        choice = input("Select choice: ")

        if choice[0] == "1":
            name = input("Enter title: ")
            year = input("Enter year: ")
            artist = input("Enter artist: ")
            duration = input("Enter duration in min: ")
            lp = LP(name, int(year), artist, int(duration))
            library.insert_LP(lp)
            continue
        elif choice[0] == "2":
            print(library.to_string())
            index = input("Enter index of LP to delete: ")
            try:
                index = int(index)
                library.delete_LP_index(index)
            except ValueError:
                print("ERROR: Selected value is not an index")
            except IndexError:
                print("ERROR: Selected index does not exist. ")
            continue
        elif choice[0] == "3":
            library.clean_library()
            continue
        elif choice[0] == "4":
            print(library.to_string())
            input("Press any key to continue.")
            continue
        elif choice[0] == "5":
            library.seed_library()
            continue
        elif choice[0] == "q":
            exit()
        


if __name__ == "__main__":
    main()