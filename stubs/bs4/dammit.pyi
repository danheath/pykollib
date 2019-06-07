# Stubs for bs4.dammit (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

__license__: str
chardet_type: Any

def chardet_dammit(s: Any): ...

xml_encoding_re: Any
html_meta_re: Any

class EntitySubstitution:
    CHARACTER_TO_HTML_ENTITY: Any = ...
    HTML_ENTITY_TO_CHARACTER: Any = ...
    CHARACTER_TO_HTML_ENTITY_RE: Any = ...
    CHARACTER_TO_XML_ENTITY: Any = ...
    BARE_AMPERSAND_OR_BRACKET: Any = ...
    AMPERSAND_OR_BRACKET: Any = ...
    @classmethod
    def quoted_attribute_value(self, value: Any): ...
    @classmethod
    def substitute_xml(cls, value: Any, make_quoted_attribute: bool = ...): ...
    @classmethod
    def substitute_xml_containing_entities(cls, value: Any, make_quoted_attribute: bool = ...): ...
    @classmethod
    def substitute_html(cls, s: Any): ...

class EncodingDetector:
    override_encodings: Any = ...
    exclude_encodings: Any = ...
    chardet_encoding: Any = ...
    is_html: Any = ...
    declared_encoding: Any = ...
    def __init__(self, markup: Any, override_encodings: Optional[Any] = ..., is_html: bool = ..., exclude_encodings: Optional[Any] = ...) -> None: ...
    @property
    def encodings(self) -> None: ...
    @classmethod
    def strip_byte_order_mark(cls, data: Any): ...
    @classmethod
    def find_declared_encoding(cls, markup: Any, is_html: bool = ..., search_entire_document: bool = ...): ...

class UnicodeDammit:
    CHARSET_ALIASES: Any = ...
    ENCODINGS_WITH_SMART_QUOTES: Any = ...
    smart_quotes_to: Any = ...
    tried_encodings: Any = ...
    contains_replacement_characters: bool = ...
    is_html: Any = ...
    log: Any = ...
    detector: Any = ...
    markup: Any = ...
    unicode_markup: Any = ...
    original_encoding: Any = ...
    def __init__(self, markup: Any, override_encodings: Any = ..., smart_quotes_to: Optional[Any] = ..., is_html: bool = ..., exclude_encodings: Any = ...) -> None: ...
    @property
    def declared_html_encoding(self): ...
    def find_codec(self, charset: Any): ...
    MS_CHARS: Any = ...
    MS_CHARS_TO_ASCII: Any = ...
    WINDOWS_1252_TO_UTF8: Any = ...
    MULTIBYTE_MARKERS_AND_SIZES: Any = ...
    FIRST_MULTIBYTE_MARKER: Any = ...
    LAST_MULTIBYTE_MARKER: Any = ...
    @classmethod
    def detwingle(cls, in_bytes: Any, main_encoding: str = ..., embedded_encoding: str = ...): ...
