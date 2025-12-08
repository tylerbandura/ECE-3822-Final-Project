"""
linkedListTest

purpose: this file is made to test the linked list datastructure to ensure I can use it
            in other files like hashmap and inside queries if needed

"""
from DataStructures.linkedlist import LinkedList

def test_linked_list():
    ll = LinkedList()

    # Insert elements
    ll.insert("Inception", 2010)
    ll.insert("Dune", 2021)
    ll.insert("Dune", 2023)  # overwrite existing key
    ll.insert("Tenet", 2020)

    # Display all
    ll.display()

    # Lookup
    print("Lookup Dune:", ll.lookup("Dune"))
    print("Lookup Avatar:", ll.lookup("Avatar"))

    # Remove
    ll.remove("Tenet")
    print("\nAfter removal:")
    ll.display()

if __name__ == "__main__":
    test_linked_list()
