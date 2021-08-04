# sound-type
Required module: `playsound`

The numbers (1-8) correspond to the interval in the major scale, and 0 is a rest. 

Pass a string of numbers as a `-s` argument when running the script in the command line. E.g. `python soundtype.py -s 1155665044332210` will play the first four bars of Twinkle Twinkle Little Star. 

Passing multiple strings will play them in parallel. E.g. `python soundtype.py -s 1155665044332210 1000500040001000 3000800070003000 5000200010005000` will play the melody with a chord (I-V-IV-I) on the first beat of each bar.
