# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Network import Network
from Node import Node


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    myNet = Network()

    node_to_Delete = Node(key=6,capacity=0)
    myNet.add_node_network(Node(key=1,capacity=2))
    myNet.add_node_network(Node(key=2,capacity=0))
    myNet.add_node_network(Node(key=3,capacity=0))
    myNet.add_node_network(Node(key=4,capacity=2))
    myNet.add_node_network(Node(key=5,capacity=1))
    myNet.add_node_network(node_to_Delete)
    myNet.add_node_network(Node(key=7,capacity=4))
    myNet.add_node_network(Node(key=8,capacity=1))

    #myNet.reorder_tree([Node(capacity=2), Node(capacity=1),
    #                    Node(capacity=4),
    #                   Node(capacity=1)])

    print('NETWORK',myNet.myNetwork)

    myNet.remove_node_network(node_to_Delete)


    for node in myNet.myNetwork:
        print('Node : ',node )
        print('Key : ',node.key )

        print('capacity : ',node.capacity )
        print('avaliability : ', node.availability)
        print('parent : ',node.parent)
        print('children : ',node.children)
        print('Next')

    #print('CAMBIOO')
    #print('NEW NET',myNewNet.myNetwork)
#
    #for node in myNewNet.myNetwork:
    #    print('Node : ',node )
    #    print('capacity : ',node.capacity )
    #    print('avaliability : ',node.avaliability )
    #    print('parent : ',node.parent)
    #    print('children : ',node.children)
    #    print('Next')
#



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
