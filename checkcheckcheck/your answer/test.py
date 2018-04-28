import re



def checkio(text):
    text.strip()

    pattern=re.compile(r'[a-zA-Z]',re.I)
    m=pattern.search(text)


checkio('Hello World!')
