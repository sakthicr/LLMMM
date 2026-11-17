"""
Prompt templates for poem generation and mutation.

Generation prompts create initial population candidates.
Mutation prompts create variations of existing poems,
preserving core theme/imagery while revising rhyme/emotion/word choice.
"""

import logging
import re

logger = logging.getLogger(__name__)


def build_generation_prompt(
    poem_type: str,
    emotion: str,
    description: str,
    count: int = 1,
) -> list[dict[str, str]]:
    """
    Build the chat messages for generating initial poem candidates.

    Args:
        poem_type: 'haiku' or 'limerick'
        emotion: target emotion (e.g. 'joy', 'sorrow')
        description: user-provided or fixed scenario description
        count: how many poems to generate in one call

    Returns:
        List of message dicts for the OpenAI-compatible API.
    """
    if poem_type == "haiku":
        structure_guide = (
            "A haiku has exactly 3 lines with syllable counts of 5-7-5.\n"
            "Example structure:\n"
            "Line 1: 5 syllables\n"
            "Line 2: 7 syllables\n"
            "Line 3: 5 syllables"
        )
    elif poem_type == "limerick":
        structure_guide = (
            "A limerick has exactly 5 lines with rhyme scheme AABBA.\n"
            "Lines 1, 2, and 5 rhyme with each other and have 3 strong beats.\n"
            "Lines 3 and 4 rhyme with each other and have 2 strong beats.\n"
            "The rhythm should be anapestic (da-da-DUM)."
        )
    else:
        raise ValueError(f"Unknown poem type: {poem_type}")

    system_prompt = f"""You are a skilled poet. Generate {count} {poem_type}(s) that:
1. Convey the emotion: {emotion}
2. Are inspired by this description: "{description}"
3. Follow this structure precisely:

{structure_guide}

IMPORTANT RULES:
- Output ONLY the poem text, nothing else.
- Each line of the poem on its own line.
- If generating multiple poems, separate them with a blank line containing only "---".
- Do NOT include titles, labels, syllable counts, or explanations.
- Count syllables carefully before writing each line."""

    user_prompt = (
        f"Write {count} {poem_type}(s) about: {description}\n"
        f"Emotion to convey: {emotion}"
    )

    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]


def build_mutation_prompt(
    poem_text: str,
    poem_type: str,
    emotion: str,
    description: str,
    count: int = 5,
) -> list[dict[str, str]]:
    """
    Build the chat messages for mutating an existing poem.

    Generates `count` variations that preserve the core theme/imagery
    while revising rhyme, emotion, word choice, or phrasing.
    """
    if poem_type == "haiku":
        structure_guide = (
            "Each variant must be exactly 3 lines with syllable counts 5-7-5."
        )
    elif poem_type == "limerick":
        structure_guide = (
            "Each variant must be exactly 5 lines with AABBA rhyme scheme, "
            "anapestic rhythm (3-3-2-2-3 strong beats)."
        )
    else:
        raise ValueError(f"Unknown poem type: {poem_type}")

    system_prompt = f"""You are a skilled poet revising poems. Given an existing {poem_type}, 
create {count} varied revisions.

Each revision should:
- PRESERVE the core theme and imagery of the original
- VARY the word choice, phrasing, rhyme, or emotional intensity
- STILL convey the emotion: {emotion}
- STILL be inspired by: "{description}"
- FOLLOW the structural rules: {structure_guide}

IMPORTANT RULES:
- Output ONLY the poem texts, nothing else.
- Each line of a poem on its own line.
- Separate poems with a blank line containing only "---".
- Do NOT include titles, labels, syllable counts, or explanations.
- Make each variant meaningfully different from the others.
- Count syllables carefully before writing each line."""

    user_prompt = f"""Original {poem_type}:
{poem_text}

Create {count} revised variants. Emotion: {emotion}. Description: {description}."""

    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]


def parse_multiple_poems(
    raw_output: str,
    poem_type: str,
    expected_count: int = 1,
) -> list[str]:
    """
    Parse multiple poems from a single API response.

    Hierarchical parsing strategy:
      1. Split on '---' delimiters.
      2. If that yields fewer poems than requested, fallback to blank lines
         (double newlines).
      3. Clean non-poem lines (labels, numbers, and standalone '---').
      4. If any candidate has more lines than target_lines (5 for limerick, 3 for haiku),
         chunk into exact target_lines. Keep ONLY chunks with exactly target_lines;
         discard incomplete remainders and log discarded line count.
      5. Log every parsed candidate's line count at INFO level.
    """
    target_lines = 3 if poem_type == "haiku" else 5

    # Strip common markdown wrappers
    text = raw_output.strip()
    if text.startswith("```"):
        lines = text.split("\n")
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        text = "\n".join(lines).strip()

    def _clean_lines(block: str) -> list[str]:
        """Extract non-label, non-empty poem lines and drop standalone '---'."""
        cleaned_lines = []
        for line in block.split("\n"):
            stripped = line.strip()
            if not stripped:
                continue
            # Drop standalone '---' (or markdown horizontal rules)
            if stripped == "---" or stripped == "--" or set(stripped) == {"-"}:
                continue
            # Skip obvious labels like "Haiku 1:", "Variant 2:", etc.
            if (stripped.endswith(":") and len(stripped) < 30 and
                any(kw in stripped.lower() for kw in
                    ["haiku", "limerick", "poem", "variant", "version", "revision"])):
                continue
            # Skip pure numbers like "1.", "2.", etc.
            if stripped.rstrip(".").isdigit():
                continue
            # Strip trailing rhyme-scheme labels (e.g. ', A', ': B', '- C')
            if re.search(r"\s*[,:\-—–]\s*[A-E]\s*$", stripped):
                cleaned_line = re.sub(r"\s*[,:\-—–]\s*[A-E]\s*$", "", stripped).rstrip()
                logger.info(
                    f"Parser stripped trailing rhyme-scheme label: "
                    f"{repr(stripped)} -> {repr(cleaned_line)}"
                )
                stripped = cleaned_line

            # Warn if line still ends with a standalone capital letter or bracketed letter like (A) or [B]
            if re.search(r"(\s+[A-Z]|\s*[\(\[][A-Z][\)\]])\s*$", stripped):
                logger.warning(
                    f"Parser detected possible trailing label in line: {repr(stripped)}"
                )
            cleaned_lines.append(stripped)
        return cleaned_lines

    # Step 1: Split on '---'
    raw_parts = [p.strip() for p in text.split("---") if p.strip()]

    # Step 2: Fallback to blank lines ONLY IF fewer than expected were produced by '---'
    if len(raw_parts) < expected_count:
        stanzas = [s.strip() for s in re.split(r"\n\s*\n+", text) if s.strip() and s.strip() != "---"]
        if len(stanzas) > len(raw_parts):
            raw_parts = stanzas

    # Step 3: Clean and enforce exact target_lines (chunking when > target_lines)
    final_poems: list[str] = []
    discarded_count = 0

    for part in raw_parts:
        lines = _clean_lines(part)
        if not lines:
            continue

        if len(lines) == target_lines:
            final_poems.append("\n".join(lines))
        elif len(lines) > target_lines:
            for i in range(0, len(lines), target_lines):
                chunk = lines[i : i + target_lines]
                if len(chunk) == target_lines:
                    final_poems.append("\n".join(chunk))
                else:
                    discarded_count += len(chunk)
        else:
            # len(lines) < target_lines
            discarded_count += len(lines)

    if discarded_count > 0:
        logger.info(
            f"Parser discarded {discarded_count} incomplete line(s) "
            f"that did not meet exact target of {target_lines} lines for {poem_type}"
        )

    # Step 4: Log line count of every candidate at INFO level
    for idx, p in enumerate(final_poems, 1):
        p_lines = [l for l in p.split("\n") if l.strip()]
        first_line = p_lines[0] if p_lines else ""
        logger.info(
            f"Parsed candidate poem #{idx} | lines={len(p_lines)} "
            f"(target={target_lines}) | first_line='{first_line[:40]}'"
        )

    return final_poems
