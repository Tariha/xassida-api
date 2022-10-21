from . import arabic_alphabet
from .types import LinkedQueue

# TODO: Considering implementing ArabicTextIter and ArabicTextChar for easier
# and neater enumeration of ArabicText objects.

class ArabicText(LinkedQueue):

  class ArabicTextChar:  
      def __init__(self, parent, node):
          self._node = node 
          self._parent = parent

      def __eq__(self, other):
          return self.char() == other

      def char(self):
          return self._node._ele

      def is_blank(self):
        return self == ' '

      def is_hamza(self):
        return self == arabic_alphabet.HAMZA

      def is_ta_marbuta(self):
        return self == arabic_alphabet.TA_MARBUTA

      def is_word_start(self):
        return self._node is self._parent._head 

      def is_alif(self):
        # NOTE: Alif with Wasla is pronounced differently based on whether
        # it is connected with the previous word or not; if it is connected
        # it is pronounced like an Lam, otherwise it is pronounced like
        # an Alif with Hamza above.
        return self == arabic_alphabet.ALIF or \
               self == arabic_alphabet.ALIF_WITH_WASLA_ABOVE or \
               self == arabic_alphabet.ALIF_KHANJAREEYA

      def is_al(self):
        """
        Determines whether there is an Alif followed by Lam at the given position.
        """
        return self.is_alif() and self._parent.after(self) == arabic_alphabet.LAM

      def is_fatha_followed_by_alif(self):
        try:
            return self == arabic_alphabet.FATHA and self._parent.after(self).is_alif()
        except:
            return False

      def is_followed_by_sun(self):
          next_node = self._parent.after(self)
          if self._parent.after(next_node).is_followed_by_shadda():
              return self._parent.after(next_node).char()
          return False

      def is_followed_by_shadda(self):
          return self._parent.after(self) == arabic_alphabet.SHADDA

      def is_kasra_followed_by_ya(self):
        return self == arabic_alphabet.KASRA and self._parent.after(self) == arabic_alphabet.YA

      def is_damma_followed_by_waw(self):
        return self == arabic_alphabet.DAMMA and self._parent.after(self) == arabic_alphabet.WAW

      def is_alif_with_madda_above(self):
        return self == arabic_alphabet.ALIF_WITH_MADDA_ABOVE

      def is_alif_with_madda_above(self):
        return self == arabic_alphabet.ALIF_WITH_MADDA_ABOVE

      def is_alif_with_wasla_above(self):
        return self == arabic_alphabet.ALIF_WITH_WASLA_ABOVE


  def __init__(self, text):
    super().__init__()
    for c in text:
        self.enqueue(c)

  def _make_position(self, node):
      if node is None:
          return None
      return self.ArabicTextChar(self, node)

  def first(self):
      return self._make_position(self._head)

  def after(self, p):
      return self._make_position(p._node._next)

  def __iter__(self):
      cursor = self.first()
      while cursor is not None:
          self.cursor = cursor
          yield cursor
          cursor = self.after(cursor)
