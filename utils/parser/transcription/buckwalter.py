from . import arabic_alphabet
__unicode_to_buckwalter_map = {
  arabic_alphabet.HAMZA: "'",  # Hamza
  arabic_alphabet.ALIF_WITH_MADDA_ABOVE: "|",  # Alif with Madda ABOVE
  arabic_alphabet.ALIF_WITH_HAMZA_ABOVE: ">",  # Alif with Hamza ABOVE
  arabic_alphabet.WAW_WITH_HAMZA_BELOW: "&",  # WAW with Hamza ABOVE
  arabic_alphabet.ALIF_WITH_HAMZA_BELOW: "<",  # Alif with Hamza BELOW
  arabic_alphabet.YA_WITH_HAMZA_ABOVE: "}",  # YEH with Hamza ABOVE
  arabic_alphabet.ALIF: "A",  # Alif
  arabic_alphabet.BA: "b",  # Ba
  arabic_alphabet.TA_MARBUTA: "p",  # Ta Marbuta
  arabic_alphabet.TA: "t",  # Ta
  arabic_alphabet.THA: "v",  # Tha
  arabic_alphabet.JEEM: "j",  # Jeem
  arabic_alphabet.HHA: "H",  # Ha
  arabic_alphabet.KHA: "x",  # Kha
  arabic_alphabet.DAL: "d",  # Dal
  arabic_alphabet.THAL: "*",  # Thal
  arabic_alphabet.RA: "r",  # Ra
  arabic_alphabet.ZAY: "z",  # Zain
  arabic_alphabet.SEEN: "s",  # Seen
  arabic_alphabet.SHEEN: "$",  # Sheen
  arabic_alphabet.SAD: "S",  # Sad
  arabic_alphabet.DAD: "D",  # DAD
  arabic_alphabet.TAH: "T",  # TAH
  arabic_alphabet.ZAH: "Z",  # ZAH
  arabic_alphabet.AIN: "E",  # AIN
  arabic_alphabet.GHAIN: "g",  # Ghain
  arabic_alphabet.TATWEEL: "_",  # Tatweel
  arabic_alphabet.FA: "f",  # FEH
  arabic_alphabet.QAF: "q",  # QAF
  arabic_alphabet.KAF: "k",  # KAF
  arabic_alphabet.LAM: "l",  # LAM
  arabic_alphabet.MEEM: "m",  # Meem
  arabic_alphabet.NOON: "n",  # Noon
  arabic_alphabet.HA: "h",  # Ha
  arabic_alphabet.WAW: "w",  # WAW
  arabic_alphabet.ALIF_MAKSURA: "Y",  # Alif Maksura
  arabic_alphabet.YA: "y",  # YEH
  arabic_alphabet.FATHATAN: "F",  # Fathatan
  arabic_alphabet.DAMMATAN: "N",  # Dammatan
  arabic_alphabet.KASRATAN: "K",  # Kasratan
  arabic_alphabet.FATHA: "a",  # Fatha
  arabic_alphabet.DAMMA: "u",  # Damma
  arabic_alphabet.KASRA: "i",  # Kasra
  arabic_alphabet.SHADDA: "~",  # Shadda
  arabic_alphabet.SUKUN: "o",  # Sukun
  arabic_alphabet.ALIF_KHANJAREEYA: "`",  # Alif Khanjareeya
  arabic_alphabet.ALIF_WITH_HAMZAT_WASL: "{",  # Alif with Hamzat Wasl
  # Commenting out non-Arabic letters for now.
  # chr(0x067E): "P",  # PEH
  # chr(0x0686): "J",  # TCHEH
  # chr(0x06A4): "V",  # VEH
  # chr(0x06AF): "G",  # GAF
  arabic_alphabet.MADDAH: '^',  # Maddah (Extended Buckwalter)
  arabic_alphabet.HAMZAABOVE: '#',  # HamzaAbove (Extended Buckwalter)
  arabic_alphabet.SMALL_HIGH_SEEN: ':',  # Small High Seen (Extended Buckwalter)
  arabic_alphabet.SMALL_HIGH_ROUNDED_ZERO: '@',  # Small High Rounded Zero (Extended Buckwalter)
  arabic_alphabet.SMALL_HIGH_UPRIGHT_RECTANGULAR_ZERO: '"',  # Small High Upright Rectangular Zero (Extended Buckwalter)
  arabic_alphabet.SMALL_HIGH_MEEM_ISOLATED_FORM: '[',  # Small High Meem Isolated Form (Extended Buckwalter)
  arabic_alphabet.SMALL_LOW_SEEN: ';',  # Small Low Seen (Extended Buckwalter)
  arabic_alphabet.SMALL_WAW: ',',  # Small Waw (Extended Buckwalter)
  arabic_alphabet.SMALL_YA: '.',  # Small Ya (Extended Buckwalter)
  arabic_alphabet.SMALL_HIGH_NOON: '!',  # Small High Noon (Extended Buckwalter)
  arabic_alphabet.SMALL_CENTRE_LOW_STOP: '-',  # Empty Centre Low Stop (Extended Buckwalter)
  arabic_alphabet.EMPTY_CENTRE_HIGH_STOP: '+',  # Empty Centre High Stop (Extended Buckwalter)
  arabic_alphabet.ROUNDED_HIGH_STOP_WITH_FILLED_CENTRE: '%',  # Rounded High Stop With Filled Centre (Extended Buckwalter)
  arabic_alphabet.SMALL_LOW_MEEM: ']',  # Small Low Meem (Extended Buckwalter)
  ' ': ' ',
}


# Inverse the map above to create inverse mapping.
__buckwalter_to_unicode_map = {}
for (key, value) in __unicode_to_buckwalter_map.iteritems():
   __buckwalter_to_unicode_map[value] = key


def buckwalter_char_to_unicode(c):
  """
  Converts the given Buckwalter character to unicode.

  :param c: the character to be converted.
  """
  return __buckwalter_to_unicode_map[c]


def unicode_char_to_buckwalter(c):
  """
  Converts the given Buckwalter character to unicode.

  :param c: the character to be converted.
  """
  return __unicode_to_buckwalter_map[c]


def buckwalter_to_unicode(string):
  """
  Converts the given Buckwalter string to unicode.

  :param string: The string to be converted.
  """
  return ''.join(map(buckwalter_char_to_unicode, string))


def unicode_to_buckwalter(string):
  """
  Converts the given unicode string to Buckwalter.

  :param string: The string to be converted.
  """
  return ''.join(map(unicode_char_to_buckwalter, string))
