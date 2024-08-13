import sqlite3
def add_daily_word(word, meaning, example):
    conn = sqlite3.connect('daily_word.db')
    c = conn.cursor()
    c.execute('INSERT INTO daily_words (word, meaning, example) VALUES (?, ?, ?)',
              (word, meaning, example))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    add_daily_word("euphoria", "a feeling or state of intense excitement and happiness",
                   "After winning the championship, the team was in a state of euphoria.")
    add_daily_word("solitude", "the state of being alone",
                   "He sought solitude in the mountains, away from the city's noise.")
    add_daily_word("ineffable", "too great or extreme to be expressed in words",
                   "The beauty of the Grand Canyon is truly ineffable.")
    add_daily_word("luminous", "full of or shedding light; bright or shining",
                   "The luminous stars lit up the night sky.")
    add_daily_word("epiphany", "a moment of sudden revelation or insight",
                   "She had an epiphany about her career path during the conference.")
    add_daily_word("ubiquitous", "present, appearing, or found everywhere",
                   "Smartphones have become ubiquitous in today's society.")
    add_daily_word("ethereal", "extremely delicate and light in a way that seems too perfect for this world",
                   "The dancer moved with an ethereal grace.")
    add_daily_word("paradigm", "a typical example or pattern of something; a model",
                   "The company is seen as a paradigm of successful business practice.")
    add_daily_word("eloquent", "fluent or persuasive in speaking or writing",
                   "Her eloquent speech captivated the audience.")
    add_daily_word("tranquility", "the quality or state of being tranquil; calm",
                   "They enjoyed the tranquility of the lakeside cabin.")
    add_daily_word("vivacious", "attractively lively and animated",
                   "Her vivacious personality made her the life of the party.")
    add_daily_word("benevolent", "well-meaning and kindly",
                   "The benevolent stranger helped the lost child find his way home.")
    add_daily_word("melancholy", "a feeling of pensive sadness, typically with no obvious cause",
                   "He felt a deep melancholy after the end of the movie.")
    add_daily_word("plethora", "a large or excessive amount of something",
                   "There was a plethora of options at the buffet.")
    add_daily_word("catharsis",
                   "the process of releasing, and thereby providing relief from, strong or repressed emotions",
                   "Crying can be a catharsis for releasing stress.")
    add_daily_word("nostalgia", "a sentimental longing or wistful affection for the past",
                   "He was filled with nostalgia as he looked through the old photos.")
    add_daily_word("evanescent", "soon passing out of sight, memory, or existence; quickly fading or disappearing",
                   "The evanescent rainbow was gone within minutes.")
    add_daily_word("resilient", "able to withstand or recover quickly from difficult conditions",
                   "The resilient community rebuilt their homes after the flood.")
    add_daily_word("lucid", "expressed clearly; easy to understand",
                   "His explanation was so lucid that everyone understood the concept.")
    add_daily_word("zenith", "the time at which something is most powerful or successful",
                   "At the zenith of her career, she was the most sought-after actress in Hollywood.")
    add_daily_word("aesthetic", "concerned with beauty or the appreciation of beauty",
                   "The aesthetic appeal of the garden was undeniable.")
    add_daily_word("serene", "calm, peaceful, and untroubled; tranquil",
                   "The lake was serene, with not a ripple disturbing its surface.")
    add_daily_word("tenacity", "the quality or fact of being very determined; determination",
                   "Her tenacity in overcoming obstacles was inspiring.")
    add_daily_word("elation", "great happiness and exhilaration", "The team felt elation after winning the match.")
    add_daily_word("idyllic", "like an idyll; extremely happy, peaceful, or picturesque",
                   "The cottage is situated in an idyllic setting.")
    add_daily_word("altruistic", "showing a disinterested and selfless concern for the well-being of others",
                   "Her altruistic nature led her to volunteer at the shelter.")
    add_daily_word("buoyant",
                   "able or apt to stay afloat or rise to the top of a liquid or gas; cheerful and optimistic",
                   "Her buoyant spirit lifted everyone's mood.")
