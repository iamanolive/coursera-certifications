text = "X-DSPAM-Confidence:    0.8475"
position = text.find(" ")
number_str = text[position:]
number_str = number_str.strip()
number_flt = float(number_str)
print(number_flt)