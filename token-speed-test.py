import time
import sys

def generate_tokens(tokens_per_second, stream):
    with open('lipsum.txt', 'r') as file:
        words = file.read().split()

    words_per_token = 0.75

    num_tokens = int(len(words) / words_per_token)

    sleep_time = 1.0 / tokens_per_second

    tokens = []
    for i in range(num_tokens):
        token = ' '.join(words[int(i*words_per_token):int((i+1)*words_per_token)])

        tokens.append(token)

        if stream:
            print(token, end=' ', flush=True)

        time.sleep(sleep_time)

    return tokens

tokens_per_second = int(sys.argv[1]) if len(sys.argv) > 1 else 500

stream = sys.argv[2].lower() == 'true' if len(sys.argv) > 2 else True

start_time = time.time()

tokens = generate_tokens(tokens_per_second, stream)

end_time = time.time()

elapsed_time = end_time - start_time

actual_tokens_per_second = len(tokens) / elapsed_time

print(f"\nGenerated {len(tokens)} tokens in {elapsed_time:.2f} seconds ({actual_tokens_per_second:.2f} tokens/second)")

if not stream:
    print(' '.join(tokens))