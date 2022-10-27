def myFunction(inputData, spLetter):
    txt = inputData.lower().split(spLetter)
    # print(txt)
    sumTxt = ""
    for text in txt:
        sumTxt += text.capitalize()+" "

    sumTxt = sumTxt.strip()
    return sumTxt
