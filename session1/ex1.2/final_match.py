def final_match():
    country_names = [('Iran', 'Spain'),
                     ('Iran', 'Portugal'),
                     ('Iran', 'Morocco'),
                     ('Spain', 'Portugal'),
                     ('Spain', 'Morocco'),
                     ('Portugal', 'Morocco'),
                     ]
    scores = {'Spain': {'win': 0, 'score': 0, 'loses': 0, 'goal difference': 0, 'draws': 0},
              'Iran': {'win': 0, 'score': 0, 'loses': 0, 'goal difference': 0, 'draws': 0},
              'Portugal': {'win': 0, 'score': 0, 'loses': 0, 'goal difference': 0, 'draws': 0},
              'Morocco': {'win': 0, 'score': 0, 'loses': 0, 'goal difference': 0, 'draws': 0}
              }
    score_input = [list(map(int, input().split("-"))) for i in range(len(country_names))]
    for i in range(len(country_names)):
        first_score = score_input[i][0]
        second_score = score_input[i][1]
        if first_score > second_score:
            diff = first_score - second_score
            scores[country_names[i][0]]['win'] = scores[country_names[i][0]]['win'] + 1
            scores[country_names[i][0]]['score'] = scores[country_names[i][0]]['score'] + 3
            scores[country_names[i][1]]['loses'] = scores[country_names[i][1]]['loses'] + 1
            scores[country_names[i][1]]['goal difference'] = scores[country_names[i][1]]['goal difference'] - diff
            scores[country_names[i][0]]['goal difference'] = scores[country_names[i][0]]['goal difference'] + diff
        elif first_score < second_score:
            diff = second_score - first_score
            scores[country_names[i][1]]['win'] = scores[country_names[i][1]]['win'] + 1
            scores[country_names[i][1]]['score'] = scores[country_names[i][1]]['score'] + 3
            scores[country_names[i][0]]['loses'] = scores[country_names[i][0]]['loses'] + 1
            scores[country_names[i][1]]['goal difference'] = scores[country_names[i][1]]['goal difference'] + diff
            scores[country_names[i][0]]['goal difference'] = scores[country_names[i][0]]['goal difference'] - diff
        else:
            scores[country_names[i][1]]['draws'] = scores[country_names[i][1]]['draws'] + 1
            scores[country_names[i][1]]['score'] = scores[country_names[i][1]]['score'] + 1
            scores[country_names[i][0]]['score'] = scores[country_names[i][0]]['score'] + 1
            scores[country_names[i][0]]['draws'] = scores[country_names[i][0]]['draws'] + 1
    sorted_scores = dict(sorted(scores.items(), key=lambda x: (-x[1]['score'], -x[1]['win'], x[0])))
    for key, value in sorted_scores.items():
        print(
            f"{key} wins:{value['win']} , loses:{value.get('loses')} , draws:{value.get('draws')} , goal difference:{value.get('goal difference')} , points:{value.get('score')} ")


final_match()
