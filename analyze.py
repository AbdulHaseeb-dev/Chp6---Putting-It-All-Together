import ch1text

def count_sentences(text):
    count = 0

    for char in text:
        if char == '.' or char == ';' or char == '?' or char == '!':
            count = count + 1
    return count

def compute_readibility(text):
    total_text = 0
    total_sentences = 0
    total_syylables = 0
    score = 0

    words = text.split()
    total_text = len(words)
    total_sentences = count_sentences(text)
    print(total_text,'words')
    print(total_sentences,'sentences')


compute_readibility(ch1text.text)
