

import datastructlib.linkedlists as linkedlists
# from datastructlib import linkedlists



if __name__ == '__main__':
    
    head = linkedlists.SimpleLinkedListNode("Sergey")

    head = head.add_to_tail("Conrad")
    head = head.add_to_tail("Fabrice")

    print(head) # Sergey -> Conrad -> Fabrice

    print(head.get_element_at_position_if_exists(1)) # Conrad -> Fabrice

    head = head.add_at_position_if_possible(
        position=1,
        data="Monica"
    ) 
    head = head.add_at_position_if_possible(
        position=1,
        data="Arnaud"
    ) 
    print(head)

    head, removed_node = head.remove_at_position_if_possible(
        position=1
    )
    print(head, removed_node)

    head = head.switch_nodes_positions_if_possible(1, 2)
    print(head)


