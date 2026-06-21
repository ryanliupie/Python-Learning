def badge_analyzer(employee_ids): 
    count = {}

    for id in employee_ids: 
        count[id] = count.get(id, 0) + 1

    unique_count = len(count)
    
    most_common = max(count, key=lambda k: count[k]) # count=dict, lambda k=for each key k, count[k] grabs value and uses it for comparison

    freq_sorted = sorted(count, key=lambda k: count[k], reverse=True)

    new_dict = {
        "unique_count": unique_count, 
        "most_common": most_common, 
        "sorted_by_frequency": freq_sorted
    }

    return new_dict

print(badge_analyzer(["A123", "B456", "A123", "C789", "B456", "A123"]))