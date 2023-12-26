from collections import defaultdict

def solution(survey, choices):
    answer = ''
    survey_dict = defaultdict(int)
    for i, s in enumerate(survey):
        choice = choices[i]
        if choice == 4: continue
        elif choice < 4: survey_dict[s[0]] += 4 - choice
        elif choice > 4: survey_dict[s[1]] += choice - 4
        
    if survey_dict['R'] >= survey_dict['T']: answer += 'R'
    else: answer += 'T'
    if survey_dict['C'] >= survey_dict['F']: answer += 'C'
    else: answer += 'F'
    if survey_dict['J'] >= survey_dict['M']: answer += 'J'
    else: answer += 'M'
    if survey_dict['A'] >= survey_dict['N']: answer += 'A'
    else: answer += 'N'
    return answer