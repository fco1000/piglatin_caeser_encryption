# Pig Latin

## What it is
Pig Latin is a simple, playful language game. It is often used for fun, wordplay, or as a light “secret” code mostly used by children.
In Kenya it is similar to sheng' by with a bit of differences.

## Basic rules (most common variant)
1. If a word begins with a vowel sound (a, e, i, o, u), add "way" or "yay" to the endbut in this project we. But in the case of this project we shall use "yay".
   - ink → inkyay
   - apple → appleway
2. If a word begins with a consonant or consonant cluster, move that initial consonant sound to the end of the word and add "ay".
   - dog → ogday
   - chair → airchay (ch moved)
   - three → eethray (thr moved)

## Consonant clusters
- Treat common consonant clusters (ch, sh, th, ph, qu, str, spl, etc.) as a single unit to move.
- Example: squeak → eaksquay (qu treated together)

## Special cases and gotchas
- The letter "y": sometimes a vowel (e.g., "my" → ymay or myay depending on variant). Treat "y" as a vowel when it forms the syllable nucleus.
- Capitalization: preserve original capitalization by capitalizing the translated word similarly.
  - London → Ondonlay
- Punctuation: keep punctuation in place. Translate only the alphabetic word and reattach punctuation.
  - "Hello!" → "Ellohay!"
- Hyphenated words: translate each component separately (e.g., well-known → ellway-ownknay).
- Contractions and possessives: usually translate the alphabetic parts and keep apostrophes in-place (e.g., don't → on'tday).

## Variants
- Some variants use "ay" for vowels (apple → appleay) instead of "way".
- Others add different suffixes ("yay", "way", "hay") depending on regional or personal preference.

## Quick algorithm (step-by-step)
1. Split text into tokens (words, punctuation).
2. For each word:
   * Identify leading consonant cluster (if any).
   * If starts with vowel sound -> append "way" (or "ay").
   * Else move cluster to end and append "ay".
   * Reapply original capitalization and punctuation.
3. Rejoin tokens.

## Examples
- dog → ogday
- smile → ilesmay
- apple → appleway (or appleay)
- quick → ickquay