"""
Text normalisation applied before rule-based scoring (Phase 2 only).

The syllable counter and the rhyme end-word picker split words with the
pattern [a-zA-Z']+, which knows only the straight apostrophe ('). The
generator often writes the typographic apostrophe (\u2019), so a word such
as "Memory\u2019s" was split into "Memory" + "s" and the lone "s" was counted
as an extra syllable (and could be taken as a line's end word for rhyme).

normalize_for_scoring() maps the typographic apostrophe variants to the
straight one. It is applied only to the copy of the text that is scored;
the poem itself is stored and displayed exactly as generated.

Controlled by config.NORMALIZE_APOSTROPHES (off in Phase 1, on in Phase 2).
"""

from src.config import NORMALIZE_APOSTROPHES

_APOSTROPHE_VARIANTS = (
    "\u2019",  # right single quotation mark (the usual curly apostrophe)
    "\u2018",  # left single quotation mark
    "\u02bc",  # modifier letter apostrophe
    "\u02b9",  # modifier letter prime
    "\u2032",  # prime
    "\uff07",  # fullwidth apostrophe
)


def normalize_for_scoring(text: str) -> str:
    """Return text with apostrophe variants replaced by a straight apostrophe."""
    if not NORMALIZE_APOSTROPHES:
        return text
    for ch in _APOSTROPHE_VARIANTS:
        text = text.replace(ch, "'")
    return text
