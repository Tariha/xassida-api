from dataclasses import dataclass
from typing import List

@dataclass
class TranslatedName:
    lang: str
    transcription: str
    translation: str

@dataclass
class VerseTiming:
    verse_number: int
    timestamp_from: str
    timestamp_to: str
    duration: str

@dataclass
class Audio:
    file: str
    duration: str
    reciter: str
    verse_timings: List[VerseTiming]

@dataclass
class Reciter:
    name: str
    picture: str
    #audios: List[Audio] = None

@dataclass
class Word:
    position: int
    text: str
    transcription: str

@dataclass
class VerseTranslation:
    lang: str
    text: str
    author: str

@dataclass
class Verse:
    number: int
    key: str
    text: str
    words: List[Word] = None
    translations: List[VerseTranslation] = None

@dataclass
class Chapter:
    name: str
    number: int
    verses: List[Verse]
    start_page: int = None
    end_page: int = None
    translated_names: List[TranslatedName] = None

@dataclass
class Xassida:
    name: str
    chapters: List[Chapter]
    translated_names: List[TranslatedName] = None
    audios: List[Audio] = None

@dataclass
class AuthorInfo:
    lang: str
    text: str

@dataclass
class Author:
    name: str
    tariha: str
    xassidas: List[Xassida]
    infos: List[AuthorInfo] = None 
    picture: str = ""
