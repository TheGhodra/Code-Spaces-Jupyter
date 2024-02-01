def greedy_activity_selection(activities):
    # Sortiere die Aktivitäten nach Endzeit
    activities.sort(key=lambda x: x[1])
    
    selected_activities = [activities[0]]
    
    # Durchlaufe die sortierten Aktivitäten und wähle diejenigen aus, die nicht mit den ausgewählten kollidieren
    for activity in activities[1:]:
        if activity[0] >= selected_activities[-1][1]:
            selected_activities.append(activity)
    
    return selected_activities

# Beispielaufruf
activities = [(1, 3), (2, 5), (3, 8), (5, 7), (8, 10), (9, 12)]
result = greedy_activity_selection(activities)

print("Ausgewählte Aktivitäten:", result)