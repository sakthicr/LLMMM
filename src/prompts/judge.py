"""
Prompt templates for the Q̄ Judge model (Qwen3.8-27B).

The judge scores poems on 5 dimensions: emotion alignment, imagery,
literary devices, originality, and coherence. Each rated 1-5.
Output is structured JSON for reliable parsing.
"""


def build_judge_prompt(
    poem_text: str,
    poem_type: str,
    target_emotion: str,
) -> list[dict[str, str]]:
    """
    Build the chat messages for the judge model.

    Returns a list of message dicts for the OpenAI-compatible API.
    """
    system_prompt = f"""You are an expert poetry critic. You will evaluate a {poem_type} poem.

Rate the poem on each of the following 5 dimensions using a scale of 1 to 5:

1. **Emotion Alignment**: How well does the poem convey the target emotion "{target_emotion}"? 
   (1=no connection, 5=powerfully evocative of {target_emotion})

2. **Imagery**: How vivid and concrete are the images?
   (1=abstract/generic, 5=striking sensory detail)

3. **Literary Devices**: Use of metaphor, simile, personification, alliteration, etc.
   (1=none, 5=masterful and organic use)

4. **Originality**: How fresh and surprising are the ideas and phrasing?
   (1=cliché, 5=genuinely novel)

5. **Coherence**: Does the poem read as a unified whole? Does it make sense?
   (1=disjointed/nonsensical, 5=seamlessly unified)

You MUST respond with ONLY a JSON object in this exact format, no other text:
{{"emotion_alignment": <int 1-5>, "imagery": <int 1-5>, "literary_devices": <int 1-5>, "originality": <int 1-5>, "coherence": <int 1-5>}}"""

    user_prompt = f"""Target emotion: {target_emotion}
Poem type: {poem_type}

Poem:
{poem_text}

Rate this poem. Respond with ONLY the JSON object."""

    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]


def build_calibration_judge_prompt(
    poem_text: str,
    poem_type: str,
) -> list[dict[str, str]]:
    """
    Build the chat messages for calibration-mode judging.

    Omits the emotion_alignment dimension since reference poems have no
    target emotion. Scores only: imagery, literary_devices, originality,
    coherence.
    """
    system_prompt = f"""You are an expert poetry critic. You will evaluate a {poem_type} poem.

Rate the poem on each of the following 4 dimensions using a scale of 1 to 5:

1. **Imagery**: How vivid and concrete are the images?
   (1=abstract/generic, 5=striking sensory detail)

2. **Literary Devices**: Use of metaphor, simile, personification, alliteration, etc.
   (1=none, 5=masterful and organic use)

3. **Originality**: How fresh and surprising are the ideas and phrasing?
   (1=cliché, 5=genuinely novel)

4. **Coherence**: Does the poem read as a unified whole? Does it make sense?
   (1=disjointed/nonsensical, 5=seamlessly unified)

You MUST respond with ONLY a JSON object in this exact format, no other text:
{{"imagery": <int 1-5>, "literary_devices": <int 1-5>, "originality": <int 1-5>, "coherence": <int 1-5>}}"""

    user_prompt = f"""Poem type: {poem_type}

Poem:
{poem_text}

Rate this poem. Respond with ONLY the JSON object."""

    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
