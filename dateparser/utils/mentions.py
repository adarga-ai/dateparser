

def combine(s, sep=" "):
    x = {
        "text": sep.join(map(lambda x: x["text"], s)),
        "char_start": max([token["char_start"] for token in s if token["char_start"] is not None]),
        "char_end": max([token["char_end"] for token in s if token["char_end"] is not None])
    }
    return x


def split_mention(mention, splitter):
    splits = []
    start = mention["char_start"]
    for split in mention["text"].split(splitter):
        nchar = len(split)
        splits.append({"text": split, "char_start": start, "char_end": start + nchar})
        start += len(split) + 1
    splits = [split for split in splits if split["char_end"] > split["char_start"]]
    return splits
