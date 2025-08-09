import hashlib


def simhash(text: str, shingle_size: int = 4) -> int:
    if not text:
        return 0
    shingles = [text[i : i + shingle_size] for i in range(max(len(text) - shingle_size + 1, 1))]
    bits = [0] * 64
    for sh in shingles:
        h = int(hashlib.md5(sh.encode("utf-8")).hexdigest(), 16)
        for i in range(64):
            bits[i] += 1 if h & (1 << i) else -1
    result = 0
    for i, b in enumerate(bits):
        if b > 0:
            result |= 1 << i
    return result
