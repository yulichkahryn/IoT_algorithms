
# q is prime number
# d is the number of characters in the input alphabet

def do_rabin_karp(pat, txt, q=101, d=256):
    pat_length = len(pat)
    txt_length = len(txt)
    pat_hash = 0
    txt_hash = 0
    i = 0
    j = 0
    hash_value = 1
    positions = list()

    for i in range(pat_length - 1):
        hash_value = (hash_value * d) % q

    for i in range(pat_length):
        pat_hash = (d * pat_hash + ord(pat[i])) % q
        txt_hash = (d * txt_hash + ord(txt[i])) % q

    for i in range(txt_length - pat_length + 1):
        if pat_hash == txt_hash:
            for j in range(pat_length):
                if txt[i + j] != pat[j]:
                    break

            j += 1
            if j == pat_length:
                positions.append(i)

        if i < txt_length - pat_length:
            txt_hash = (d * (txt_hash - ord(txt[i]) * hash_value) + ord(txt[i + pat_length])) % q

            if txt_hash < 0:
                txt_hash = txt_hash + q

    return positions


def main():
    txt = "Have you got colour in your cheeks?" \
          "Do you ever get that fear that you can't shift the tide" \
          "That sticks around like summat in your teeth?" \
          "Are there some aces up your sleeve?" \
          "Have you no idea that you're in deep?" \
          "I've dreamt about you nearly every night this week" \
          "How many secrets can you keep?" \
          "'Cause there's this tune I found" \
          "That makes me think of you somehow an' I play it on repeat" \
          "Until I fall asleep, spillin' drinks on my settee"
    pat = "secrets"
    result = do_rabin_karp(pat, txt)
    print(result)


if __name__ == '__main__':
    main()

