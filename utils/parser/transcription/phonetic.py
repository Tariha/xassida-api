# The following letters have different rules depending on the context in the
# ALA-LC transcription:
# Hamza
# Ta' Marbuta

from io import StringIO
from .arabic_text import ArabicText
from . import arabic_alphabet

__unicode_to_phonetic_map = {
    arabic_alphabet.HAMZA: u'\'',
    arabic_alphabet.ALIF_WITH_MADDA_ABOVE: chr(0x0100),
    arabic_alphabet.ALIF_WITH_HAMZA_ABOVE: u'\'a',
    arabic_alphabet.WAW_WITH_HAMZA_ABOVE: u'\'u',
    arabic_alphabet.ALIF_WITH_HAMZA_BELOW: u'\'i',
    arabic_alphabet.YA_WITH_HAMZA_ABOVE: u'i\'',  # Ya with Hamza ABOVE
    # NOTE: Alif doesn't seem to have transcription in ALA-LC, so I am using the
    # same one for Alif with Madda.
    arabic_alphabet.ALIF: chr(0x0101),
    arabic_alphabet.BA: u'b',  # Ba
    arabic_alphabet.TA_MARBUTA: chr(0x1e97),
    arabic_alphabet.TA: u't',
    arabic_alphabet.THA: chr(0x1e6f),
    arabic_alphabet.JEEM: chr(0x01e7),
    arabic_alphabet.HHA: chr(0x1e25),
    arabic_alphabet.KHA: chr(0x1e96),
    arabic_alphabet.DAL: u'd',
    arabic_alphabet.THAL: chr(0x1e0f),
    arabic_alphabet.RA: u'r',
    arabic_alphabet.ZAY: u'z',
    arabic_alphabet.SEEN: u's',
    arabic_alphabet.SHEEN: chr(0x0161),
    arabic_alphabet.SAD: chr(0x1e63),
    arabic_alphabet.DAD: chr(0x1e0d),
    arabic_alphabet.TAH: chr(0x1e6d),
    arabic_alphabet.ZAH: chr(0x1e93),
    arabic_alphabet.AIN: chr(0x02bf),
    arabic_alphabet.GHAIN: chr(0x0121),
    # Removing Tatweel in the transcription
    arabic_alphabet.TATWEEL: u'',
    arabic_alphabet.FA: u'f',
    arabic_alphabet.QAF: u'q',
    arabic_alphabet.KAF: u'k',
    arabic_alphabet.LAM: u'l',
    arabic_alphabet.MEEM: u'm',
    arabic_alphabet.NOON: u'n',
    arabic_alphabet.HA: u'h',
    arabic_alphabet.WAW: u'w',
    arabic_alphabet.ALIF_MAKSURA: chr(0x1ef3),
    arabic_alphabet.YA: chr(0x012b),
    arabic_alphabet.FATHATAN: u'an',   # Rafid
    arabic_alphabet.DAMMATAN: u'un',   # Rafid
    arabic_alphabet.KASRATAN: u'in',   # Rafid
    arabic_alphabet.FATHA: u'a',
    arabic_alphabet.DAMMA: u'u',
    arabic_alphabet.KASRA: u'i',
    # Shadda in ALA-LC is represented by doubling the letter.
    #arabic_alphabet.SHADDA: chr(),  # Shadda
    # Sukon in ALA-LC doesn't have a representation in ALA-LC.
    arabic_alphabet.SUKUN: u'',  # Sukun
    # Alif Khanjariya
    chr(0x0670): chr(0x0101),  # Alif Khanjariya
    # TODO: Implement the transcription of Hamzat Al-Wasl
    #chr(0x0671): chr(),  # Alif with Hamzat Wasl
    # The following letters don't have a representation in ALA-LC.
    arabic_alphabet.HAMZAABOVE: u'',
    arabic_alphabet.SMALL_HIGH_SEEN: u'',
    arabic_alphabet.SMALL_HIGH_ROUNDED_ZERO: u'',
    arabic_alphabet.SMALL_HIGH_UPRIGHT_RECTANGULAR_ZERO_: u'',
    arabic_alphabet.SMALL_HIGH_MEEM_ISOLATED_FORM: u'',
    arabic_alphabet.SMALL_LOW_SEEN: u'',
    arabic_alphabet.SMALL_WAW: u'',
    arabic_alphabet.SMALL_YA: u'',
    arabic_alphabet.SMALL_HIGH_NOON: u'',
    arabic_alphabet.EMPTY_CENTRE_LOW_STOP: u'',
    arabic_alphabet.EMPTY_CENTRE_HIGH_STOP: u'',
    arabic_alphabet.ROUNDED_HIGH_STOP_WITH_FILLED_CENTRE: u'',
    arabic_alphabet.SMALL_LOW_MEEM: u''
}

def get_char(key):
    return __unicode_to_phonetic_map.get(key, '')


def unicode_to_phonetic(string):
    """
    Converts the given unicode string to Buckwalter.
    :param string: The string to be converted.
    :return The phonetic representation of the string.
    """
    string_buffer = StringIO()

    arabic_text = iter(ArabicText(string))
    for caracter in arabic_text:
        # Whitespace
        if caracter.is_blank():
            string_buffer.write(u' ')
            continue

        # Handle Hamza
        if caracter.is_hamza() and caracter.is_word_start():
            # Hamza at the beginning of a word is not encoded in ALA-LC.
            continue

        # Handle Ta Marbuta
        if caracter.is_ta_marbuta():
            # Ta Marbuta is transcribed as either 't' or 'h' depending on the
            # context.
            string_buffer.write(u't')
            continue

        # Handle Al
        if caracter.is_al():
            if caracter.is_word_start():
                string_buffer.write(u'al-')
            else:
                if c:=caracter.is_followed_by_sun():
                    string_buffer.write(u''+'-'.join(get_char(c)*2))
                    next(arabic_text)
                else:
                    string_buffer.write(u'l-')

            # Skip the next letter (Lam) because we already processed it.
            next(arabic_text)
            continue

        # Handle Alif with Madda
        if caracter.is_alif_with_madda_above():
            if caracter.is_word_start():
                # Alif with Madda at the beginning of a word is replaced with
                # ā
                string_buffer.write(chr(0x0101))
            else:
                # Alif with Madda not at the beginning of a word is replaced with
                # `ā
                string_buffer.write('\'' + chr(0x0101))
            continue

        if caracter.is_fatha_followed_by_alif():
            # Treat like an Alif.
            string_buffer.write(__unicode_to_phonetic_map[arabic_alphabet.ALIF])
            next(arabic_text)
            continue

        if caracter.is_kasra_followed_by_ya():
            # Treat like a Ya
            string_buffer.write(__unicode_to_phonetic_map[arabic_alphabet.YA])
            next(arabic_text)
            continue

        if caracter.is_damma_followed_by_waw():
            # Treat like a Waw
            string_buffer.write(__unicode_to_phonetic_map[arabic_alphabet.WAW])
            next(arabic_text)
            continue

        # Handle the rest
        if caracter.char() in __unicode_to_phonetic_map:
            count = 1
            if caracter.is_followed_by_shadda():
                count = 2
            string_buffer.write(__unicode_to_phonetic_map[caracter.char()]*count)

    phonetic = string_buffer.getvalue()
    # TODO: Need to ensure we close the string buffer if an exception happens
    # before we reach this statement.
    string_buffer.close()
    return phonetic
