# Оценки кампаний по различным критериям
campaigns = {
    'A': {'profit': 1000, 'cost': 200, 'success_potential': 7},
    'B': {'profit': 1200, 'cost': 250, 'success_potential': 8}
}

# Веса критериев
weights = {'profit': 0.5, 'cost': 0.3, 'success_potential': 0.2}

# Выбор лучшей кампании
best_campaign = None
best_score = -float('inf')

for campaign, data in campaigns.items():
    # Рассчитываем оценку кампании на основе весов критериев
    score = sum(data[feature] * weight for feature, weight in weights.items())
    if score > best_score:
        best_campaign = campaign
        best_score = score

# Выводим результаты
print("Лучшая кампания:", best_campaign)
print("Оценка кампании:", best_score)
