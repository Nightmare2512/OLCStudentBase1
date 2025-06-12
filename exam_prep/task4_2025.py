
def shift(char):
    alphas = 'abcdefghijklmnopqrstuvwxyz' 
    if char in alphas:
        unshifted = alphas.find(char)
        shifted = (unshifted + 1) % 26
