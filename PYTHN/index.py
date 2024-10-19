name='BHARAT bharat INDIA india'
finaloutput=''
for s in name:
    if s==s.lower():
        finaloutput+=s.upper()
    elif s==s.upper():
        finaloutput+=s.lower()
print(f'Final Output:{finaloutput}')

# --------------------------------
input ='PawansingRandansingPadavi'
output=''
# --------------------------------
for c in input:
    if c.isupper():
        output+=' '+c
    else:
        output+=c
print(output.strip())

# -----------------------------
# -----------------------------