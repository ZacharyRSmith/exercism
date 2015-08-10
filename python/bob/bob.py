def hey(what):
    cleaned = what.strip()

    # If you address him without actually saying anything:
    if not cleaned:
        return "Fine. Be that way!"

    # If you yell at him:
    if cleaned.isupper():
        return "Whoa, chill out!"

    # If you ask him a question.
    if cleaned.endswith("?"):
        return "Sure."

    return "Whatever."
