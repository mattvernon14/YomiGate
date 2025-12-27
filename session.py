import sqlite3
import random
import os 
from llm import generate_sentence
from llm import llm_available
from adaptive_selection import select_next_word

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "Japanese Words.db")

def get_words(cursor, word_id):
    cursor.execute("""
        SELECT word_id, kanji, hiragana, english
        FROM words 
        WHERE word_id = ?
        LIMIT 1
""", (word_id,))
    return cursor.fetchone()

def calculate_attempt(cursor, connection, word_id, is_correct):
    cursor.execute(
        "INSERT INTO attempts (word_id, correct) VALUES (?, ?)",
        (word_id, 1 if is_correct else 0)
    )
    #Save changes to DB.
    connection.commit()

def practice_vocab(cursor, connection, level, word_id, llm_running, session):
    word = get_words(cursor, word_id)
    if not word:
        return
    kanji = word[1]
    hiragana = word[2]
    english = word[3]
    print("Kanji:", word[1])
    if llm_running:
        sentence = generate_sentence(level, kanji, hiragana, english)
        if sentence: 
            print("Example Sentence:", sentence) 

    user_input = input("Input Hiragana: ").strip()
    is_correct = (user_input == word[2])
    if is_correct:
        session["attempts"]+=1
        session["correct"]+=1
        print("Correct!")
    else: 
        
        session["attempts"]+=1
        print("Wrong:", word[2])
    print("Meaning:", word[3])
    print()
    calculate_attempt(cursor, connection, word_id, is_correct)

def start_session(level):
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        session = {
            "attempts": 0, 
            "correct": 0,
            
        }
        llm_running = llm_available()

        #program works with or without LLM
        for quiz in range(5):
            word_id, most_missed_id = select_next_word(cursor)
            if word_id is None:
                break
            practice_vocab(cursor, connection, level, word_id, llm_running, session)
        cursor.execute(
            "SELECT KANJI FROM words WHERE word_id = ?",
            (most_missed_id,)           
        )
        word = cursor.fetchone()
        results(session)
        print("\nMost missed word:", word[0])
        
def results(session):
    if session["attempts"] != 0:
        print("Total Attempts: ", session["attempts"])
        print("Total Correct", session["correct"])
        accuracy = (session["correct"]/ session["attempts"]) * 100
        print(f"Accuracy: {accuracy:.1f}%")
    else: 
        print("No attempts recorded.")
    
    

