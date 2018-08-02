
fractions = {
    0x2189: 0.0,  # ; ; 0 # No       VULGAR FRACTION ZERO THIRDS
    0x2152: 0.1,  # ; ; 1/10 # No       VULGAR FRACTION ONE TENTH
    0x2151: 0.11111111,  # ; ; 1/9 # No       VULGAR FRACTION ONE NINTH
    0x215B: 0.125,  # ; ; 1/8 # No       VULGAR FRACTION ONE EIGHTH
    0x2150: 0.14285714,  # ; ; 1/7 # No       VULGAR FRACTION ONE SEVENTH
    0x2159: 0.16666667,  # ; ; 1/6 # No       VULGAR FRACTION ONE SIXTH
    0x2155: 0.2,  # ; ; 1/5 # No       VULGAR FRACTION ONE FIFTH
    0x00BC: 0.25,  # ; ; 1/4 # No       VULGAR FRACTION ONE QUARTER
    0x2153: 0.33333333,  # ; ; 1/3 # No       VULGAR FRACTION ONE THIRD
    0x215C: 0.375,  # ; ; 3/8 # No       VULGAR FRACTION THREE EIGHTHS
    0x2156: 0.4,  # ; ; 2/5 # No       VULGAR FRACTION TWO FIFTHS
    0x00BD: 0.5,  # ; ; 1/2 # No       VULGAR FRACTION ONE HALF
    0x2157: 0.6,  # ; ; 3/5 # No       VULGAR FRACTION THREE FIFTHS
    0x215D: 0.625,  # ; ; 5/8 # No       VULGAR FRACTION FIVE EIGHTHS
    0x2154: 0.66666667,  # ; ; 2/3 # No       VULGAR FRACTION TWO THIRDS
    0x00BE: 0.75,  # ; ; 3/4 # No       VULGAR FRACTION THREE QUARTERS
    0x2158: 0.8,  # ; ; 4/5 # No       VULGAR FRACTION FOUR FIFTHS
    0x215A: 0.83333333,  # ; ; 5/6 # No       VULGAR FRACTION FIVE SIXTHS
    0x215E: 0.875,  # ; ; 7/8 # No       VULGAR FRACTION SEVEN EIGHTHS
}
fractions_string = {
    0x2189: '.0',  # ; ; 0 # No       VULGAR FRACTION ZERO THIRDS
    0x2152: '.1',  # ; ; 1/10 # No       VULGAR FRACTION ONE TENTH
    0x2151: '.11111111',  # ; ; 1/9 # No       VULGAR FRACTION ONE NINTH
    0x215B: '.125',  # ; ; 1/8 # No       VULGAR FRACTION ONE EIGHTH
    0x2150: '.14285714',  # ; ; 1/7 # No       VULGAR FRACTION ONE SEVENTH
    0x2159: '.16666667',  # ; ; 1/6 # No       VULGAR FRACTION ONE SIXTH
    0x2155: '.2',  # ; ; 1/5 # No       VULGAR FRACTION ONE FIFTH
    0x00BC: '.25',  # ; ; 1/4 # No       VULGAR FRACTION ONE QUARTER
    0x2153: '.33333333',  # ; ; 1/3 # No       VULGAR FRACTION ONE THIRD
    0x215C: '.375',  # ; ; 3/8 # No       VULGAR FRACTION THREE EIGHTHS
    0x2156: '.4',  # ; ; 2/5 # No       VULGAR FRACTION TWO FIFTHS
    0x00BD: '.5',  # ; ; 1/2 # No       VULGAR FRACTION ONE HALF
    0x2157: '.6',  # ; ; 3/5 # No       VULGAR FRACTION THREE FIFTHS
    0x215D: '.625',  # ; ; 5/8 # No       VULGAR FRACTION FIVE EIGHTHS
    0x2154: '.66666667',  # ; ; 2/3 # No       VULGAR FRACTION TWO THIRDS
    0x00BE: '.75',  # ; ; 3/4 # No       VULGAR FRACTION THREE QUARTERS
    0x2158: '.8',  # ; ; 4/5 # No       VULGAR FRACTION FOUR FIFTHS
    0x215A: '.83333333',  # ; ; 5/6 # No       VULGAR FRACTION FIVE SIXTHS
    0x215E: '.875',  # ; ; 7/8 # No       VULGAR FRACTION SEVEN EIGHTHS
}

frac_code=[0x2189,
    0x2152,
    0x2151,
    0x215B,
    0x2150,
    0x2159,
    0x2155,
    0x00BC,
    0x2153,
    0x215C,
    0x2156,
    0x00BD,
    0x2157,
    0x215D,
    0x2154,
    0x00BE,
    0x2158,
    0x215A,
    0x215E]
def rid_uni_frac(string):
    for code in frac_code:
        string = string.replace(chr(code),fractions_string[code])
    return string
