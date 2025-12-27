import random

def select_next_word(cursor):
    cursor.execute("SELECT word_id FROM words")
    word_ids = [row[0] for row in cursor.fetchall()]
    if not word_ids:
        return (None, None)
    
    cursor.execute("""
        SELECT word_id, COUNT(*), SUM(correct)
        FROM attempts
        GROUP BY word_id
    """)           
    stats = {}
    for word_id, seen, correct_sum in cursor.fetchall():
        stats[word_id] = (seen, correct_sum or 0)

    choices = []
    weights = []
    max_weight = -1
    max_id = None
    
    for id in word_ids:
        if id not in stats:
            w =1.0
        else:
            seen, correct = stats[id]
            wrong = seen - correct
            w = wrong + 0.1
        if(w > max_weight):
            max_weight = w
            max_id = id
        choices.append(id)
        weights.append(w)
        
        
    
    return random.choices(choices, weights=weights, k=1)[0], max_id

    
