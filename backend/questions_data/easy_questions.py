"""Easy difficulty trivia questions.

This module contains easy difficulty questions for the trivia game.
Total: 85 questions

Add new easy questions here in the following format:
{
    "text": "What is the question?",
    "category": "Category Name",
    "correct": "Correct Answer",
    "wrong": ["Wrong Answer 1", "Wrong Answer 2", "Wrong Answer 3"]
}
"""

EASY_QUESTIONS = [
    {
        "text": 'What is the capital of France?',
        "category": 'general',
        "correct": 'Paris',
        "wrong": ['London', 'Berlin', 'Madrid']
    },
    {
        "text": 'Which planet is known as the Red Planet?',
        "category": 'general',
        "correct": 'Mars',
        "wrong": ['Venus', 'Jupiter', 'Saturn']
    },
    {
        "text": 'What is the largest mammal in the world?',
        "category": 'general',
        "correct": 'Blue Whale',
        "wrong": ['African Elephant', 'Giraffe', 'Polar Bear']
    },
    {
        "text": 'How many sides does a triangle have?',
        "category": 'general',
        "correct": 'Three',
        "wrong": ['Two', 'Four', 'Five']
    },
    {
        "text": 'What color do you get when you mix red and white?',
        "category": 'general',
        "correct": 'Pink',
        "wrong": ['Purple', 'Orange', 'Yellow']
    },
    {
        "text": 'What is the main ingredient in bread?',
        "category": 'general',
        "correct": 'Flour',
        "wrong": ['Sugar', 'Salt', 'Water']
    },
    {
        "text": 'Which animal is known as the King of the Jungle?',
        "category": 'general',
        "correct": 'Lion',
        "wrong": ['Tiger', 'Elephant', 'Leopard']
    },
    {
        "text": 'How many days are in a week?',
        "category": 'general',
        "correct": 'Seven',
        "wrong": ['Six', 'Eight', 'Five']
    },
    {
        "text": 'What is the opposite of hot?',
        "category": 'general',
        "correct": 'Cold',
        "wrong": ['Warm', 'Cool', 'Lukewarm']
    },
    {
        "text": 'Which direction does the sun rise?',
        "category": 'general',
        "correct": 'East',
        "wrong": ['North', 'South', 'West']
    },
    {
        "text": 'What do bees make?',
        "category": 'general',
        "correct": 'Honey',
        "wrong": ['Milk', 'Butter', 'Cheese']
    },
    {
        "text": 'How many legs does a spider have?',
        "category": 'general',
        "correct": 'Eight',
        "wrong": ['Six', 'Ten', 'Four']
    },
    {
        "text": 'What is the first letter of the alphabet?',
        "category": 'general',
        "correct": 'A',
        "wrong": ['B', 'C', 'Z']
    },
    {
        "text": 'Which season comes after winter?',
        "category": 'general',
        "correct": 'Spring',
        "wrong": ['Summer', 'Fall', 'Autumn']
    },
    {
        "text": 'What do cows drink?',
        "category": 'general',
        "correct": 'Water',
        "wrong": ['Milk', 'Juice', 'Soda']
    },
    {
        "text": 'How many minutes are in an hour?',
        "category": 'general',
        "correct": 'Sixty',
        "wrong": ['Fifty', 'Seventy', 'Forty']
    },
    {
        "text": 'What is the largest ocean on Earth?',
        "category": 'general',
        "correct": 'Pacific',
        "wrong": ['Atlantic', 'Indian', 'Arctic']
    },
    {
        "text": 'Which fruit is known for keeping the doctor away?',
        "category": 'general',
        "correct": 'Apple',
        "wrong": ['Orange', 'Banana', 'Grape']
    },
    {
        "text": 'What is the name of our planet?',
        "category": 'general',
        "correct": 'Earth',
        "wrong": ['Mars', 'Venus', 'Jupiter']
    },
    {
        "text": 'How many wheels does a bicycle have?',
        "category": 'general',
        "correct": 'Two',
        "wrong": ['One', 'Three', 'Four']
    },
    {
        "text": 'What do plants need to make their own food?',
        "category": 'science',
        "correct": 'Sunlight, water, and carbon dioxide',
        "wrong": ['Water only', 'Soil only', 'Air only']
    },
    {
        "text": 'What is the center of an atom called?',
        "category": 'science',
        "correct": 'Nucleus',
        "wrong": ['Electron', 'Proton', 'Neutron']
    },
    {
        "text": 'Which part of the plant conducts photosynthesis?',
        "category": 'science',
        "correct": 'Leaves',
        "wrong": ['Roots', 'Stem', 'Flowers']
    },
    {
        "text": 'What is the chemical formula for water?',
        "category": 'science',
        "correct": 'H2O',
        "wrong": ['H2O2', 'HO2', 'H3O']
    },
    {
        "text": 'What force keeps us on the ground?',
        "category": 'science',
        "correct": 'Gravity',
        "wrong": ['Magnetism', 'Friction', 'Electricity']
    },
    {
        "text": 'What is the fastest land animal?',
        "category": 'science',
        "correct": 'Cheetah',
        "wrong": ['Lion', 'Leopard', 'Tiger']
    },
    {
        "text": 'How many legs does an insect have?',
        "category": 'science',
        "correct": 'Six',
        "wrong": ['Four', 'Eight', 'Ten']
    },
    {
        "text": 'What is the largest organ in the human body?',
        "category": 'science',
        "correct": 'Skin',
        "wrong": ['Brain', 'Liver', 'Heart']
    },
    {
        "text": 'What gas do we breathe in?',
        "category": 'science',
        "correct": 'Oxygen',
        "wrong": ['Carbon dioxide', 'Nitrogen', 'Hydrogen']
    },
    {
        "text": 'What is the study of weather called?',
        "category": 'science',
        "correct": 'Meteorology',
        "wrong": ['Biology', 'Geology', 'Astronomy']
    },
    {
        "text": 'What type of animal is a dolphin?',
        "category": 'science',
        "correct": 'Mammal',
        "wrong": ['Fish', 'Reptile', 'Amphibian']
    },
    {
        "text": 'How many eyes does a spider typically have?',
        "category": 'science',
        "correct": 'Eight',
        "wrong": ['Two', 'Six', 'Four']
    },
    {
        "text": 'What is the main source of energy for Earth?',
        "category": 'science',
        "correct": 'Sun',
        "wrong": ['Moon', 'Stars', 'Wind']
    },
    {
        "text": 'What do you call animals that eat only plants?',
        "category": 'science',
        "correct": 'Herbivores',
        "wrong": ['Carnivores', 'Omnivores', 'Predators']
    },
    {
        "text": 'What is the boiling point of water in Celsius?',
        "category": 'science',
        "correct": '100°C',
        "wrong": ['90°C', '110°C', '120°C']
    },
    {
        "text": 'Who was the first President of the United States?',
        "category": 'history',
        "correct": 'George Washington',
        "wrong": ['John Adams', 'Thomas Jefferson', 'Benjamin Franklin']
    },
    {
        "text": 'In which year did World War II end?',
        "category": 'history',
        "correct": '1945',
        "wrong": ['1944', '1946', '1947']
    },
    {
        "text": 'Which ancient wonder of the world was located in Egypt?',
        "category": 'history',
        "correct": 'Great Pyramid of Giza',
        "wrong": ['Hanging Gardens', 'Colossus of Rhodes', 'Lighthouse of Alexandria']
    },
    {
        "text": "Who was known as the 'Iron Lady'?",
        "category": 'history',
        "correct": 'Margaret Thatcher',
        "wrong": ['Queen Elizabeth', 'Marie Curie', 'Eleanor Roosevelt']
    },
    {
        "text": 'Which wall was torn down in 1989?',
        "category": 'history',
        "correct": 'Berlin Wall',
        "wrong": ['Great Wall of China', "Hadrian's Wall", 'Wall Street']
    },
    {
        "text": 'Who wrote the Declaration of Independence?',
        "category": 'history',
        "correct": 'Thomas Jefferson',
        "wrong": ['George Washington', 'John Adams', 'Benjamin Franklin']
    },
    {
        "text": 'In which city was President Kennedy assassinated?',
        "category": 'history',
        "correct": 'Dallas',
        "wrong": ['New York', 'Washington D.C.', 'Boston']
    },
    {
        "text": 'Which empire was ruled by Julius Caesar?',
        "category": 'history',
        "correct": 'Roman',
        "wrong": ['Greek', 'Egyptian', 'Persian']
    },
    {
        "text": 'What ship did Christopher Columbus sail on his first voyage?',
        "category": 'history',
        "correct": 'Santa Maria',
        "wrong": ['Nina', 'Pinta', 'Mayflower']
    },
    {
        "text": 'Who was the leader of Nazi Germany?',
        "category": 'history',
        "correct": 'Adolf Hitler',
        "wrong": ['Mussolini', 'Stalin', 'Franco']
    },
    {
        "text": 'What is the largest country in the world?',
        "category": 'geography',
        "correct": 'Russia',
        "wrong": ['China', 'United States', 'Canada']
    },
    {
        "text": 'Which river flows through London?',
        "category": 'geography',
        "correct": 'Thames',
        "wrong": ['Seine', 'Danube', 'Rhine']
    },
    {
        "text": 'What is the smallest continent?',
        "category": 'geography',
        "correct": 'Australia',
        "wrong": ['Europe', 'Antarctica', 'South America']
    },
    {
        "text": 'Which country has the most natural lakes?',
        "category": 'geography',
        "correct": 'Canada',
        "wrong": ['Russia', 'United States', 'Finland']
    },
    {
        "text": 'What is the tallest mountain in the world?',
        "category": 'geography',
        "correct": 'Mount Everest',
        "wrong": ['K2', 'Kangchenjunga', 'Lhotse']
    },
    {
        "text": 'Which desert is the largest in the world?',
        "category": 'geography',
        "correct": 'Sahara',
        "wrong": ['Gobi', 'Kalahari', 'Arabian']
    },
    {
        "text": 'What is the capital of Australia?',
        "category": 'geography',
        "correct": 'Canberra',
        "wrong": ['Sydney', 'Melbourne', 'Perth']
    },
    {
        "text": 'Which country is both in Europe and Asia?',
        "category": 'geography',
        "correct": 'Turkey',
        "wrong": ['Kazakhstan', 'Georgia', 'Armenia']
    },
    {
        "text": 'What is the longest river in Africa?',
        "category": 'geography',
        "correct": 'Nile',
        "wrong": ['Congo', 'Niger', 'Zambezi']
    },
    {
        "text": 'Which city is known as the Big Apple?',
        "category": 'geography',
        "correct": 'New York City',
        "wrong": ['Los Angeles', 'Chicago', 'Boston']
    },
    {
        "text": "Which movie features the song 'My Heart Will Go On'?",
        "category": 'entertainment',
        "correct": 'Titanic',
        "wrong": ['The Bodyguard', 'Ghost', 'Pretty Woman']
    },
    {
        "text": 'Who played Iron Man in the Marvel movies?',
        "category": 'entertainment',
        "correct": 'Robert Downey Jr.',
        "wrong": ['Chris Evans', 'Chris Hemsworth', 'Mark Ruffalo']
    },
    {
        "text": "Which animated movie features the song 'Let It Go'?",
        "category": 'entertainment',
        "correct": 'Frozen',
        "wrong": ['Moana', 'Tangled', 'The Little Mermaid']
    },
    {
        "text": "What is the name of Harry Potter's owl?",
        "category": 'entertainment',
        "correct": 'Hedwig',
        "wrong": ['Errol', 'Pigwidgeon', 'Archimedes']
    },
    {
        "text": "Which actress played Katniss Everdeen in 'The Hunger Games'?",
        "category": 'entertainment',
        "correct": 'Jennifer Lawrence',
        "wrong": ['Emma Stone', 'Scarlett Johansson', 'Anne Hathaway']
    },
    {
        "text": 'How many players are on a basketball team on the court?',
        "category": 'sports',
        "correct": 'Five',
        "wrong": ['Four', 'Six', 'Seven']
    },
    {
        "text": 'How many holes are there in a full round of golf?',
        "category": 'sports',
        "correct": '18',
        "wrong": ['16', '20', '22']
    },
    {
        "text": "Which sport is known as 'the beautiful game'?",
        "category": 'sports',
        "correct": 'Soccer/Football',
        "wrong": ['Basketball', 'Tennis', 'Cricket']
    },
    {
        "text": 'How many rings are there in the Olympic symbol?',
        "category": 'sports',
        "correct": 'Five',
        "wrong": ['Four', 'Six', 'Seven']
    },
    {
        "text": 'How many points is a touchdown worth in American football?',
        "category": 'sports',
        "correct": 'Six',
        "wrong": ['Five', 'Seven', 'Eight']
    },
    {
        "text": 'In which sport would you perform a slam dunk?',
        "category": 'sports',
        "correct": 'Basketball',
        "wrong": ['Volleyball', 'Tennis', 'Badminton']
    },
    {
        "text": 'How many minutes are in a soccer match?',
        "category": 'sports',
        "correct": '90',
        "wrong": ['80', '100', '120']
    },
    {
        "text": "Which sport uses terms like 'love' and 'deuce'?",
        "category": 'sports',
        "correct": 'Tennis',
        "wrong": ['Badminton', 'Squash', 'Table Tennis']
    },
    {
        "text": 'How many bases are there in baseball?',
        "category": 'sports',
        "correct": 'Four',
        "wrong": ['Three', 'Five', 'Six']
    },
    {
        "text": 'Which instrument has 88 keys?',
        "category": 'music',
        "correct": 'Piano',
        "wrong": ['Organ', 'Harpsichord', 'Accordion']
    },
    {
        "text": 'How many strings does a violin have?',
        "category": 'music',
        "correct": 'Four',
        "wrong": ['Three', 'Five', 'Six']
    },
    {
        "text": 'How many notes are in an octave?',
        "category": 'music',
        "correct": 'Eight',
        "wrong": ['Seven', 'Nine', 'Ten']
    },
    {
        "text": 'What is the first book in the Harry Potter series?',
        "category": 'literature',
        "correct": "Philosopher's Stone",
        "wrong": ['Chamber of Secrets', 'Prisoner of Azkaban', 'Goblet of Fire']
    },
    {
        "text": 'Which Shakespeare play features Romeo and Juliet?',
        "category": 'literature',
        "correct": 'Romeo and Juliet',
        "wrong": ['Hamlet', 'Macbeth', 'Othello']
    },
    {
        "text": 'Who is the founder of Facebook?',
        "category": 'technology',
        "correct": 'Mark Zuckerberg',
        "wrong": ['Bill Gates', 'Larry Page', 'Jack Dorsey']
    },
    {
        "text": "What does 'AI' stand for?",
        "category": 'technology',
        "correct": 'Artificial Intelligence',
        "wrong": ['Automatic Intelligence', 'Advanced Intelligence', 'Applied Intelligence']
    },
    {
        "text": 'What is the chemical symbol for oxygen?',
        "category": 'science',
        "correct": 'O',
        "wrong": ['O2', 'Ox', 'Oy']
    },
    {
        "text": 'Which planet is closest to the Sun?',
        "category": 'science',
        "correct": 'Mercury',
        "wrong": ['Venus', 'Earth', 'Mars']
    },
    {
        "text": 'What is the square root of 64?',
        "category": 'general',
        "correct": '8',
        "wrong": ['6', '10', '12']
    },
    {
        "text": 'Which ocean is the smallest?',
        "category": 'geography',
        "correct": 'Arctic',
        "wrong": ['Indian', 'Atlantic', 'Pacific']
    },
    {
        "text": 'Which country invented pizza?',
        "category": 'general',
        "correct": 'Italy',
        "wrong": ['France', 'Greece', 'Spain']
    },
    {
        "text": 'What is the main ingredient in guacamole?',
        "category": 'general',
        "correct": 'Avocado',
        "wrong": ['Tomato', 'Onion', 'Pepper']
    },
    {
        "text": 'How many continents are there?',
        "category": 'geography',
        "correct": '7',
        "wrong": ['5', '6', '8']
    },
    {
        "text": 'What is the capital of Canada?',
        "category": 'geography',
        "correct": 'Ottawa',
        "wrong": ['Toronto', 'Vancouver', 'Montreal']
    },
    {
        "text": 'What is the largest bird in the world?',
        "category": 'science',
        "correct": 'Ostrich',
        "wrong": ['Eagle', 'Condor', 'Albatross']
    }
]
