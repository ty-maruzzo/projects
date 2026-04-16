import nltk
from nltk.corpus import wordnet
from nltk.metrics import edit_distance

# Download required NLTK data
nltk.download('wordnet')
nltk.download('omw-1.4')

def similar_answer(user_input, correct_answer, threshold=.81):
    """
    Returns True if user_input is similar to correct_answer using:
    - direct match
    - partial match (substring)
    - WordNet synonyms
    - edit distance similarity
    """
    if user_input == "":
        return False
    user_input = user_input.lower().strip()
    correct_answer_lower = correct_answer.lower().strip()
    # Direct match
    if user_input == correct_answer_lower:
        return True
    
    # Partial match (input contained in correct answer)
    if user_input in correct_answer_lower or correct_answer_lower in user_input:
        return True
    
    
    # Edit distance similarity
    ratio = 1 - edit_distance(user_input, correct_answer_lower) / max(len(user_input), len(correct_answer_lower))
    if ratio >= threshold:
        return True
    
    # Check WordNet synonyms (works best for single words)
    synonyms = set()
    for syn in wordnet.synsets(correct_answer_lower):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name().lower().replace('_', ' '))
    if user_input in synonyms:
        return True
    
    return False

def quiz():
    questions = {
        "What is the year Christopher Columbus discovered America?": "1492",
          "What year was the French Revolution?": "1789", 
          "Where did the Gunpowder Plot take place?": "England", 
          "What caused the Protestant Reformation?": "Martin Luther's 95 Theses",
            "Why did the Persian Empire fall?" : "Alexander the Great's conquest",
              "What was the main cause of World War I?": "Assassination of Archduke Franz Ferdinand",
                "Who gained control of the Roman Republic and established the Roman Empire?": "Julius Caesar", 
                "Who became the first emperor of the Roman Empire?": "Augustus", 
                "Who invented the printing press?": "Johannes Gutenberg",
                  "What african country was never colonized?": "Ethiopia"
        
    }
    
    score = 0
    for question, answer in questions.items():
        user_answer = input(question + " ")
        if similar_answer(user_answer, answer):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {answer}.")
    
    print(f"Your final score is {score}/{len(questions)}.")

quiz()