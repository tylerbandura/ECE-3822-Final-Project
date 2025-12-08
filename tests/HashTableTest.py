from DataStructures.hashTable import HashTable


def test_hashmap():
    hm = HashTable(size=10)

    # Insert data
    hm.insert("Inception", {"year": 2010, "rating": 8.8})
    hm.insert("Interstellar", {"year": 2014, "rating": 8.6})
    hm.insert("Tenet", {"year": 2020, "rating": 7.4})
    hm.insert("Inception", {"year": 2010, "rating": 9.0})  # overwrite test

    print("\n--- HASHMAP CONTENTS ---")
    hm.display()

    # Lookup existing keys
    print("\nLookup Inception:", hm.lookup("Inception"))
    print("Lookup Tenet:", hm.lookup("Tenet"))

    # Lookup missing key
    print("Lookup Avatar:", hm.lookup("Avatar"))

    # Remove an item
    print("\nRemoving Tenet...")
    hm.remove("Tenet")

    # Display after removal
    print("\n--- AFTER REMOVAL ---")
    hm.display()


if __name__ == "__main__":
    test_hashmap()
