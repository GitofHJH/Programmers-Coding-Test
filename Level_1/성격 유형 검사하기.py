def solution(survey, choices):
    mbti = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    length = len(survey)
    for i in range(length):
        choice = choices[i] - 4
        if choice < 0:
            mbti[survey[i][0]] += abs(choice)
        elif choice > 0:
            mbti[survey[i][1]] += abs(choice)
        else:
            continue
    
    answer = ''
    if mbti["R"] >= mbti["T"]:
        answer += "R"
    else:
        answer += "T"
    
    if mbti["C"] >= mbti["F"]:
        answer += "C"
    else:
        answer += "F"

    if mbti["J"] >= mbti["M"]:
        answer += "J"
    else:
        answer += "M"

    if mbti["A"] >= mbti["N"]:
        answer += "A"
    else:
        answer += "N"
    
    return answer