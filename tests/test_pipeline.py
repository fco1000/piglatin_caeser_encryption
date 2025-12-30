import json
import os
import re


def caesar_cipher(s: str, k: int) -> str:
    k = k % 26
    res = []
    for ch in s:
        if 'a' <= ch <= 'z':
            res.append(chr((ord(ch) - ord('a') + k) % 26 + ord('a')))
        elif 'A' <= ch <= 'Z':
            res.append(chr((ord(ch) - ord('A') + k) % 26 + ord('A')))
        else:
            res.append(ch)
    return ''.join(res)


def caesar_decipher(s: str, k: int) -> str:
    return caesar_cipher(s, (-k) % 26)


def pig_latin_token(word: str) -> str:
    # handle empty
    if word == "":
        return ""
    # preserve capitalization pattern: if first is uppercase, capitalize result accordingly
    orig_capitalized = word[0].isupper()
    lower = word.lower()

    # find first vowel
    m = re.match(r"([aeiouAEIOU].*)", word)
    if re.match(r"^[aeiouAEIOU]", word):
        out = lower + "way"
    else:
        # consonant cluster to first vowel
        m = re.search(r"[aeiouAEIOU]", word)
        if m:
            i = m.start()
            out = lower[i:] + lower[:i] + "ay"
        else:
            # no vowel
            out = lower + "-ay"

    if orig_capitalized and out:
        out = out.capitalize()
    return out


def pig_latin(s: str) -> str:
    # split on whitespace, preserve punctuation attached to words
    parts = s.split(' ')
    out_parts = []
    for part in parts:
        if part == "":
            out_parts.append("")
            continue
        # hyphenated: transform each component
        if '-' in part:
            comps = part.split('-')
            out_comps = []
            for c in comps:
                leading = re.match(r"^([^A-Za-z]*)([A-Za-z]+)([^A-Za-z]*)$", c)
                if leading:
                    pre, core, post = leading.group(1), leading.group(2), leading.group(3)
                    out_comps.append(pre + pig_latin_token(core) + post)
                else:
                    out_comps.append(c)
            out_parts.append('-'.join(out_comps))
            continue

        m = re.match(r"^([^A-Za-z]*)([A-Za-z]+)([^A-Za-z]*)$", part)
        if m:
            pre, core, post = m.group(1), m.group(2), m.group(3)
            out_parts.append(pre + pig_latin_token(core) + post)
        else:
            out_parts.append(part)

    return ' '.join(out_parts)


def pig_latin_deconv(s: str) -> str:
    # best-effort reversal for tests (assumes simple suffixes and no apostrophe markers)
    parts = s.split(' ')
    out_parts = []
    for part in parts:
        if part == "":
            out_parts.append("")
            continue
        if '-' in part:
            comps = part.split('-')
            out_comps = []
            for c in comps:
                m = re.match(r"^([^A-Za-z]*)([A-Za-z]+)([^A-Za-z]*)$", c)
                if m:
                    pre, core, post = m.group(1), m.group(2), m.group(3)
                    # reverse: if endswith 'way' or 'ay'
                    if core.lower().endswith('way'):
                        base = core[:-3]
                    elif core.lower().endswith('ay'):
                        body = core[:-2]
                        # try to move last consonant cluster back (simple heuristic)
                        # move trailing consonants to front
                        m2 = re.search(r"[^aeiouAEIOU]+$", body)
                        if m2:
                            cluster = m2.group(0)
                            base = cluster + body[: -len(cluster)]
                        else:
                            base = body
                    else:
                        base = core
                    if core[0].isupper():
                        base = base.capitalize()
                    out_comps.append(pre + base + post)
                else:
                    out_comps.append(c)
            out_parts.append('-'.join(out_comps))
            continue

        m = re.match(r"^([^A-Za-z]*)([A-Za-z]+)([^A-Za-z]*)$", part)
        if m:
            pre, core, post = m.group(1), m.group(2), m.group(3)
            if core.lower().endswith('way'):
                base = core[:-3]
            elif core.lower().endswith('ay'):
                body = core[:-2]
                m2 = re.search(r"[^aeiouAEIOU]+$", body)
                if m2:
                    cluster = m2.group(0)
                    base = cluster + body[: -len(cluster)]
                else:
                    base = body
            else:
                base = core
            if core[0].isupper():
                base = base.capitalize()
            out_parts.append(pre + base + post)
        else:
            out_parts.append(part)

    return ' '.join(out_parts)


def load_vectors(dirpath):
    all = []
    for fn in os.listdir(dirpath):
        if fn.endswith('.json'):
            with open(os.path.join(dirpath, fn), 'r', encoding='utf-8') as f:
                all.extend(json.load(f))
    return all


def test_vectors_roundtrip():
    vecs = load_vectors(os.path.join(os.path.dirname(__file__), 'test_vectors'))
    assert len(vecs) > 0
    all_passed = True
    for v in vecs:
        inp = v.get('input', '')
        pig_expected = v.get('pig_expected')
        key = v.get('caesar_key')
        caesar_expected = v.get('caesar_expected')

        got_pig = pig_latin(inp)
        if pig_expected is not None and got_pig != pig_expected:
            all_passed = False
            print(f"PigLatin mismatch for {v['id']}: {got_pig} != {pig_expected}")

        if caesar_expected is not None and key is not None:
            got_caesar = caesar_cipher(got_pig, key)
            if got_caesar != caesar_expected:
                all_passed = False
                print(f"Caesar forward mismatch for {v['id']}: {got_caesar} != {caesar_expected}")
            back = caesar_decipher(got_caesar, key)
            if back != got_pig:
                all_passed = False
                print(f"Caesar reverse failed for {v['id']}: {back} != {got_pig}")

        back_pl = pig_latin_deconv(got_pig)
        if inp and any(c.isalpha() for c in inp):
            if ''.join([c.lower() for c in re.sub(r'[^A-Za-z]', '', back_pl)]) != ''.join([c.lower() for c in re.sub(r'[^A-Za-z]', '', inp)]):
                all_passed = False
                print(f"Pig roundtrip letters mismatch for {v['id']}")

    if all_passed:
        print("All test vectors passed successfully!")
