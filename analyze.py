import ch1text

def count_sentences(text):
    count = 0
    terminals = '.;?!'
    for char in text:
            if char in terminals:
        # if char == '.' or char == ';' or char == '?' or char == '!':
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

def count_syllables(words):
    count = 0

    for word in words:
        word_count = count_syllables_in_word(word)
        count = word_count + 1

        return count

def count_syllables_in_word(word):
    count = 0

    return count        


compute_readibility(ch1text.text)
