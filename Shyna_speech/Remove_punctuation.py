import re

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''


def remove_punctuation(my_str):
    no_punct = ""
    for char in my_str:
        if char not in punctuations:
            no_punct = no_punct + char
    data = (str(no_punct).lower()).translate(str.maketrans({"'": None}))

    if len(str(data).split())>1:
        print(data)
        return data
    else:
        data = regex_shyna(data)
        print("punctuation section", data)
        return data


def regex_shyna(str):
    regex = r"((ha){2,3}^[t]|(hi){2}^[t])"

    subst = ""
    # You can manually specify the number of replacements by changing the 4th argument
    result = re.sub(regex, subst, str, 0, re.MULTILINE)
    if result.__contains__('ha'):
        # print("result section", result)
        return "ha"
    elif result.__contains__('hi'):
        return "hi"
    else:
        # print(str)
        return str

# def check_for_palidrome():
# regex_shyna("how about that")


# remove_punctuation("he")