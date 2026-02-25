# model.py

def calculate_travel_emission(travel):
    mapping = {
        "Car": 40,
        "Bus": 20,
        "Bike": 10,
        "Walk": 2
    }
    return mapping.get(travel, 10)


def calculate_diet_emission(diet):
    mapping = {
        "Vegetarian": 5,
        "Mixed": 12,
        "Non-Vegetarian": 20
    }
    return mapping.get(diet, 10)


def electricity_emission(electricity):
    return electricity * 0.35


def aqi_health_factor(aqi):
    if aqi < 80:
        return 1
    elif aqi < 120:
        return 2
    elif aqi < 160:
        return 3
    else:
        return 4


def exercise_exposure(exercise):
    mapping = {
        "Low": 1,
        "Medium": 2,
        "High": 3
    }
    return mapping.get(exercise, 2)


def normalize_eco_score(carbon):
    score = 100 - int(carbon / 2)
    return max(0, min(100, score))


def predict_impact(travel, electricity, diet, exercise, aqi):

    travel_c = calculate_travel_emission(travel)
    diet_c = calculate_diet_emission(diet)
    electric_c = electricity_emission(electricity)
    aqi_factor = aqi_health_factor(aqi)
    exercise_factor = exercise_exposure(exercise)

    total_carbon = travel_c + diet_c + electric_c + (aqi * 0.05)

    health_risk = (total_carbon / 25) + aqi_factor + exercise_factor

    eco_score = normalize_eco_score(total_carbon)

    return round(total_carbon,2), round(health_risk,2), eco_score
