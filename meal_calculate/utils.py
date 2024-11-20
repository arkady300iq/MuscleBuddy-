def calculate_nutrition(weight, gender, goal, activity_level):

    if gender == 'male':
        bmr = 10 * weight + 6.25 * 175 - 5 * 30 + 5 
    else:
        bmr = 10 * weight + 6.25 * 165 - 5 * 30 - 161  

    activity_multipliers = {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'active': 1.725,
        'very_active': 1.9
    }

    activity_multiplier = activity_multipliers.get(activity_level, 1.2)

    if goal == 'gain weight':  
        caloric_intake = bmr * activity_multiplier + 400 
    elif goal == 'lose weight': 
        caloric_intake = bmr * activity_multiplier - 400  
    else: 
        caloric_intake = bmr * activity_multiplier  

    protein = weight * 2.2  
    fat = weight * 1 
    carbs = (caloric_intake - (protein * 4 + fat * 9)) / 4  

    return {
        'protein': round(protein, 1),
        'fat': round(fat, 1),
        'carbs': round(carbs, 1)
    }
