
from typing import Any, Optional, Tuple

class SimpleLinkedListNode:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> str:
        s = str(self.data)
        if self.next:
            s += ' -> ' + str(self.next)
            # s = s + ' -> ' + str(self.next)
            # s += f" -> {self.next}"

        return s
    
    def get_element_at_position_if_exists(
            self, 
            pos: int
    ) -> Optional['SimpleLinkedListNode']:
        current = self
        cnt = 0
        while cnt < pos and current.next:
            current = current.next
            cnt += 1

        # if cnt != pos:
        #     # if the element does not exist
        #     return None
        # return current
        
        return None if cnt != pos else current # expression ternaire

    def add_at_position_if_possible(
            self, 
            position: int, # after which we are going to cut
            data: Any
    ) -> 'SimpleLinkedListNode':
        # regarder si c'est possible de l'inserer
        # si oui, prendre l'element en question sur la position

        # if base := self.get_element_at_position_if_exists(position):

        current = self.get_element_at_position_if_exists(position)
        if current:
            # mettre l'ancien resultat de cote, afin de ne pas le perdre.
            tmp = current.next

            # creer le nouveau element a inserer
            node = SimpleLinkedListNode(data)

            # faire pointer l'element "current" vers le nouveau element cree
            current.next = node

            # faire pointer le nouveau element vers ancien "next"
            node.next = tmp

            # faire pointer l'element "current" vers le nouveau element cree
            current.next = node

        return self

    def remove_at_position_if_possible(
            self, 
            position: int
    ) -> Tuple['SimpleLinkedListNode', Optional['SimpleLinkedListNode']]:
        # regarder si c'est possible de l'supprimer 
        # si oui, prendre l'element en question sur la position
        removed_node = None

        current = self.get_element_at_position_if_exists(position)
        if current and current.next:
            removed_node = current.next
            current.next = current.next.next
            removed_node.next = None
            
        return self, removed_node

    def get_tail(self) -> 'SimpleLinkedListNode':
        current = self
        while current.next:
            current = current.next

        return current
    
    def add_to_tail(self, data: Any) -> 'SimpleLinkedListNode':
        tail = self.get_tail()
        tail.next = SimpleLinkedListNode(data)
        return self
    
class DoubleLinkedListNode:
    def __init__(self):
        ...
    
    def __str__(self):
        ...
    
    def get_element_at_position_if_exists(self):
        ...
    
    def add_at_position_if_possible(self):
        ...
        
    def remove_at_position_if_possible(self):
        ...

    def get_tail(self):
        ...

    def add_to_tail(self):
        ...
