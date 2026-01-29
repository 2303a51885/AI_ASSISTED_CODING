#Write a code to check whether a given message is spam or not based on the presence of certain keywords.
def is_spam(message):
    spam_keywords = ["win", "prize", "free", "money", "urgent", "click here", "subscribe", "buy now","limited time offer","act now","winner","congratulations"]
    message_lower = message.lower()
    
    for keyword in spam_keywords:
        if keyword in message_lower:
            return "Spam"
    return "Not Spam"
# Test the function
test_message_1 = "Congratulations! You have won a free prize."
test_message_2 = "Hello, how are you doing today?"
print(is_spam(test_message_1))  # Output: True
print(is_spam(test_message_2))  # Output: False



"""
Emotions: ['happy', 'sad', 'angry', 'excited', 'nervous', 'neutral']
"""
def detect_emotion(message):
    emotion_keywords = {
        "happy": ["joy", "pleased", "delighted", "cheerful", "content"],
        "sad": ["unhappy", "sorrowful", "dejected", "downcast", "mournful"],
        "angry": ["mad", "furious", "irate", "livid", "outraged"],
        "excited": ["thrilled", "elated", "eager", "enthusiastic", "overjoyed"],
        "nervous": ["anxious", "worried", "uneasy", "apprehensive", "tense"]
    }
    
    message_lower = message.lower()
    
    for emotion, keywords in emotion_keywords.items():
        for keyword in keywords:
            if keyword in message_lower:
                return emotion
    return "neutral"
# Test the function
test_message_3 = "I am so thrilled about the upcoming event!"
test_message_4 = "I feel very sad today."
print(detect_emotion(test_message_3))  # Output: excited
print(detect_emotion(test_message_4))  # Output: sad

"""
March → Mesha
April → Vrishabha
May → Mithuna
June → Karka
July → Simha
August → Kanya
September → Tula
October → Vrischika
November → Dhanu
December → Makara
January → Kumbha
February → Meena
"""
def gregorian_to_hindu_month(month):
    month_mapping = {
        "March": "Mesha",
        "April": "Vrishabha",
        "May": "Mithuna",
        "June": "Karka",
        "July": "Simha",
        "August": "Kanya",
        "September": "Tula",
        "October": "Vrischika",
        "November": "Dhanu",
        "December": "Makara",
        "January": "Kumbha",
        "February": "Meena"
    }
    
    return month_mapping.get(month, "Invalid month")
# Test the function
test_month_1 = "March"
test_month_2 = "November"
print(gregorian_to_hindu_month(test_month_1))  # Output: Mesha
print(gregorian_to_hindu_month(test_month_2))  # Output: Dhanu


"""
90–100 → A
80–89 → B
70–79 → C
60–69 → D
Below 60 → F
"""
def grade_from_score(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    elif score < 60:
        return "F"
    else:
        return "Invalid score"  
# Test the function
test_score_1 = 85
test_score_2 = 55
test_message_3 = 105
print(grade_from_score(test_score_1))  # Output: B
print(grade_from_score(test_score_2))  # Output: F
print(grade_from_score(test_message_3))  # Output: Invalid score


"""
1.List of marks
2.We will check marks and assign grades accordingly
3.we will store the whether pass or fail in a list and return the list
"""
def assign_grades(marks_list):
    results = []
    for marks in marks_list:
        if marks >= 50:
            results.append("Pass")
        else:
            results.append("Fail")
    return results
# Test the function
test_marks_list = [45, 67, 89, 34, 56]
print(assign_grades(test_marks_list))  # Output: ['Fail', 'Pass', 'Pass', 'Fail', 'Pass']
print(assign_grades([90, 40, 55, 70, 30]))  # Output: ['Pass', 'Fail', 'Pass', 'Pass', 'Fail']

"""
1.We will give a age of function
2.Basesd on the age we will decide he can vote or not
3.Return the result
"""
def can_vote(age):
    if age >= 18:
        return "Eligible to vote"
    else:
        return "Not eligible to vote"
# Test the function
test_age_1 = 20
test_age_2 = 16
print(can_vote(test_age_1))  # Output: Eligible to vote
print(can_vote(test_age_2))  # Output: Not eligible to vote

"""
1.Take a stri
"""