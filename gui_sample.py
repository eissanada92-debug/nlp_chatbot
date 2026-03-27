import sys
sys.stdout.reconfigure(encoding='utf-8')

import tkinter as tk
import random

# ==============================
# الردود (عربي + English)
# ==============================
responses = {
    "greeting": [
        "اهلا وسهلا! اخبارك ايه؟",
        "Hello! How are you?",
        "مرحبا! نورت الشات"
    ],
    "how_are_you": [
        "انا تمام الحمد لله، وانت؟",
        "I'm good! What about you?",
        "الدنيا كويسة معايا 😄 وانت؟"
        "very good "
        "فل ,ميه ميه  , بخير"
    ],
    "thanks": [
         "العفو "
        "You are welcome!",
        "تحت امرك في اي وقت"
        " الشكر لله"
        "مفيش شكر بينا ياباشا"
        "حبيبي علي ايه"
    ],
    "name": [
        "انا Chatbot بسيط معمول بدون AI",
        "I am a simple chatbot made without AI"
    ],
    "study": [
        "ابدأ بأصعب مادة الاول",
        "Start with your hardest subject first",
        "راجع محاضراتك القديمة"
        "لا تقلق ذاكر وهتتحل"
    ],
    "bye": [
        "مع السلامة!",
        "Goodbye!",
        "اشوفك قريب"
        "هتوحشني ياباشا"
    ]
}

# ==============================
# فهم الجمل (IMPORTANT 🔥)
# ==============================
def match_intent(user_input):
    text = user_input.lower()

    # greetings
    if any(word in text for word in ["مرحبا", "السلام", "اهلا", "hello", "hi"]):
        return "greeting"

    # how are you
    if any(word in text for word in [
        "عامل ايه", "اخبارك", "الدنيا معاك", "كيفك"", حبيبي و انت ","تسلم"
        "how are you", "how are u"
    ]):
        return "how_are_you"

    # thanks
    if any(word in text for word in ["شكرا", "thanks", "thank you"]):
        return "thanks"

    # name
    if any(word in text for word in ["اسمك", "who are you", "your name"]):
        return "name"

    # study
    if any(word in text for word in ["اذاكر", "مذاكرة", "study"]):
        return "study"

    # bye
    if any(word in text for word in ["باي", "bye", "exit"]):
        return "bye"
    #old
    
    if any(word in text for word in["oh,wow,that's a mazing, so cute,  تحفهه , واو يعني ,العمر كله يارب, جميل "]):
        return"old"

    return "unknown"

# ==============================
# الرد
# ==============================
def get_response(user_input):
    intent = match_intent(user_input)

    if intent in responses:
        return random.choice(responses[intent])

    return "مش فاهم قصدك، حاول تقولها بطريقة تانية | I don't understand, try again"

# ==============================
# ارسال الرسالة
# ==============================
def send_message(event=None):
    user_input = entry.get()

    if user_input.strip() == "":
        return

    chat_area.config(state=tk.NORMAL)

    chat_area.insert(tk.END, "You: " + user_input + "\n")

    response = get_response(user_input)
    chat_area.insert(tk.END, "Bot: " + response + "\n\n")

    chat_area.config(state=tk.DISABLED)
    chat_area.see(tk.END)

    entry.delete(0, tk.END)

# ==============================
# الواجهة (شكل ChatGPT بسيط)
# ==============================
window = tk.Tk()
window.title("Smart Chatbot")
window.geometry("450x550")
window.config(bg="#ffc0cb")

chat_area = tk.Text(
    window,
    state=tk.NORMAL,
    bg="white",
    fg="black",
    font=("Arial", 12)
)
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# رسالة ترحيب
chat_area.insert(tk.END, "Bot: اهلا بيك! تقدر تكلمني عربي او English\n\n")
chat_area.config(state=tk.DISABLED)

entry = tk.Entry(window, font=("Arial", 12))
entry.pack(padx=10, pady=5, fill=tk.X)

send_button = tk.Button(
    window,
    text="Send",
    bg="#ff69b4",
    fg="white",
    font=("Arial", 12),
    command=send_message
)
send_button.pack(pady=5)

entry.bind("<Return>", send_message)

window.mainloop()