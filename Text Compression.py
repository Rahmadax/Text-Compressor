import random
import string
from fractions import Fraction

class text_compression():
    def init():
        s_probs = {}
        num_symbols = 100
        alphabet_size = 2
        random_prob = False
        
        # Initialize all letters in alphabet to have some probability.
        if not random_prob:
            for i in range(1, alphabet_size+1):
                s_probs[string.ascii_lowercase[i-1:i]] = (1, alphabet_size)
        else:
            print("stub")

        # Generate a random text
        text = []
        for i in range(num_symbols):
            num = random.randint(1, alphabet_size)
            text += string.ascii_lowercase[num-1:num]
        return text, s_probs 

    def text_comp(text, s_probs):
        high_val = 1.0
        low_val = 0.0
        num_symbols_run = 0
        clear_digits = ''
        output = ""
        
        for sym in text:
            prev_val = low_val
            divisions = [('',low_val)]
            for s in s_probs:
                p = s_probs[s]
                prev_val = round((prev_val + ((high_val - low_val) * (p[0] / p[1]))),10)
                divisions.append((s,prev_val))
                if s == sym:
                    s_probs[s] = (s_probs[s][0] + 1, s_probs[s][1] + 1)
                else:
                    s_probs[s] = (s_probs[s][0], s_probs[s][1] + 1)
            
            for i in range (1, len(divisions)):
                tup = divisions[i]
                if tup[0] == sym:
                    high_val = tup[1]
                    low_val = divisions[i-1][1]
                    break;
            
            hv_str = str(high_val)
            lv_str = str(low_val)
            clear_digits = ''
            for i in range(2, min(len(hv_str), len(lv_str))):
                if hv_str[i] == lv_str[i]:
                    clear_digits += (hv_str[i])
                else:
                    break

            if (len(clear_digits) > 1):
                for i in range (0, len(divisions)):
                    tup = divisions[i]
                    probability = str(tup[1])
                    divisions[i] = (tup[0], float(probability[:2] + probability[len(clear_digits)+2:len(probability)]))
                high_val = divisions[len(divisions)-1][1]
                low_val = divisions[1][1]
                output += (clear_digits)
        print(str("{:b}".format(int(output))))
            
text, s_probs = text_compression.init()
output = text_compression.text_comp(text, s_probs)

