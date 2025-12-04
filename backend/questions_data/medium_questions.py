"""Medium difficulty trivia questions.

This module contains medium difficulty questions for the trivia game.
Total: 169 questions

Add new medium questions here in the following format:
{
    "text": "What is the question?",
    "category": "Category Name",
    "correct": "Correct Answer",
    "wrong": ["Wrong Answer 1", "Wrong Answer 2", "Wrong Answer 3"]
}
"""

MEDIUM_QUESTIONS = [
    {
        "text": 'What year did the Titanic sink?',
        "category": 'general',
        "correct": '1912',
        "wrong": ['1910', '1914', '1916']
    },
    {
        "text": 'Who painted the Mona Lisa?',
        "category": 'general',
        "correct": 'Leonardo da Vinci',
        "wrong": ['Vincent van Gogh', 'Pablo Picasso', 'Michelangelo']
    },
    {
        "text": 'What is the smallest country in the world?',
        "category": 'general',
        "correct": 'Vatican City',
        "wrong": ['Monaco', 'San Marino', 'Liechtenstein']
    },
    {
        "text": "Which gas makes up most of Earth's atmosphere?",
        "category": 'general',
        "correct": 'Nitrogen',
        "wrong": ['Oxygen', 'Carbon Dioxide', 'Hydrogen']
    },
    {
        "text": 'What is the currency of Japan?',
        "category": 'general',
        "correct": 'Yen',
        "wrong": ['Yuan', 'Won', 'Dollar']
    },
    {
        "text": 'How many bones are in the adult human body?',
        "category": 'general',
        "correct": '206',
        "wrong": ['198', '215', '192']
    },
    {
        "text": 'What is the longest river in the world?',
        "category": 'general',
        "correct": 'Nile',
        "wrong": ['Amazon', 'Mississippi', 'Yangtze']
    },
    {
        "text": 'Which vitamin is produced when skin is exposed to sunlight?',
        "category": 'general',
        "correct": 'Vitamin D',
        "wrong": ['Vitamin C', 'Vitamin A', 'Vitamin B12']
    },
    {
        "text": 'What is the hardest natural substance on Earth?',
        "category": 'general',
        "correct": 'Diamond',
        "wrong": ['Quartz', 'Steel', 'Iron']
    },
    {
        "text": 'Which continent is the largest?',
        "category": 'general',
        "correct": 'Asia',
        "wrong": ['Africa', 'North America', 'Europe']
    },
    {
        "text": "What does 'www' stand for?",
        "category": 'general',
        "correct": 'World Wide Web',
        "wrong": ['World Wide Website', 'World Web Wide', 'Wide World Web']
    },
    {
        "text": 'How many chambers does a human heart have?',
        "category": 'general',
        "correct": 'Four',
        "wrong": ['Two', 'Six', 'Eight']
    },
    {
        "text": 'What is the speed of light?',
        "category": 'general',
        "correct": '299,792,458 m/s',
        "wrong": ['300,000 km/s', '186,000 mph', '300,000 m/s']
    },
    {
        "text": 'Which country gifted the Statue of Liberty to the United States?',
        "category": 'general',
        "correct": 'France',
        "wrong": ['England', 'Spain', 'Italy']
    },
    {
        "text": 'What is the most abundant gas in the universe?',
        "category": 'general',
        "correct": 'Hydrogen',
        "wrong": ['Oxygen', 'Helium', 'Nitrogen']
    },
    {
        "text": 'How many time zones are there in Russia?',
        "category": 'general',
        "correct": '11',
        "wrong": ['9', '13', '15']
    },
    {
        "text": 'What is the chemical symbol for gold?',
        "category": 'general',
        "correct": 'Au',
        "wrong": ['Go', 'Ag', 'Gd']
    },
    {
        "text": 'Which organ in the human body produces insulin?',
        "category": 'general',
        "correct": 'Pancreas',
        "wrong": ['Liver', 'Kidney', 'Stomach']
    },
    {
        "text": 'What is the smallest unit of matter?',
        "category": 'general',
        "correct": 'Atom',
        "wrong": ['Molecule', 'Electron', 'Proton']
    },
    {
        "text": 'How many strings does a standard guitar have?',
        "category": 'general',
        "correct": 'Six',
        "wrong": ['Four', 'Eight', 'Twelve']
    },
    {
        "text": 'What is the atomic number of carbon?',
        "category": 'science',
        "correct": '6',
        "wrong": ['4', '8', '12']
    },
    {
        "text": 'Which scientist developed the theory of evolution?',
        "category": 'science',
        "correct": 'Darwin',
        "wrong": ['Einstein', 'Newton', 'Galileo']
    },
    {
        "text": 'What is the powerhouse of the cell?',
        "category": 'science',
        "correct": 'Mitochondria',
        "wrong": ['Nucleus', 'Ribosome', 'Cytoplasm']
    },
    {
        "text": "How many bones are in a giraffe's neck?",
        "category": 'science',
        "correct": '7',
        "wrong": ['5', '9', '12']
    },
    {
        "text": 'What is the study of earthquakes called?',
        "category": 'science',
        "correct": 'Seismology',
        "wrong": ['Geology', 'Meteorology', 'Volcanology']
    },
    {
        "text": 'Which blood type is known as the universal donor?',
        "category": 'science',
        "correct": 'O',
        "wrong": ['A', 'B', 'AB']
    },
    {
        "text": 'What is the chemical symbol for silver?',
        "category": 'science',
        "correct": 'Ag',
        "wrong": ['Si', 'Au', 'Al']
    },
    {
        "text": 'How long does it take for light from the Sun to reach Earth?',
        "category": 'science',
        "correct": '8 minutes and 20 seconds',
        "wrong": ['8 minutes', '10 minutes', '5 minutes']
    },
    {
        "text": 'What is the most common element in the human body?',
        "category": 'science',
        "correct": 'Oxygen',
        "wrong": ['Carbon', 'Hydrogen', 'Nitrogen']
    },
    {
        "text": 'Which planet has the most moons?',
        "category": 'science',
        "correct": 'Saturn',
        "wrong": ['Jupiter', 'Uranus', 'Neptune']
    },
    {
        "text": 'What is the study of fungi called?',
        "category": 'science',
        "correct": 'Mycology',
        "wrong": ['Biology', 'Botany', 'Zoology']
    },
    {
        "text": 'How many pairs of chromosomes do humans have?',
        "category": 'science',
        "correct": '23',
        "wrong": ['22', '24', '25']
    },
    {
        "text": 'What is the speed of sound in air at room temperature?',
        "category": 'science',
        "correct": '343 m/s',
        "wrong": ['320 m/s', '360 m/s', '380 m/s']
    },
    {
        "text": 'Which organ filters blood in the human body?',
        "category": 'science',
        "correct": 'Kidneys',
        "wrong": ['Liver', 'Heart', 'Lungs']
    },
    {
        "text": 'What is the smallest bone in the human body?',
        "category": 'science',
        "correct": 'Stapes',
        "wrong": ['Stirrup', 'Hammer', 'Anvil']
    },
    {
        "text": 'In which year did the Berlin Wall fall?',
        "category": 'history',
        "correct": '1989',
        "wrong": ['1987', '1991', '1993']
    },
    {
        "text": 'Who was the last Tsar of Russia?',
        "category": 'history',
        "correct": 'Nicholas II',
        "wrong": ['Alexander III', 'Peter the Great', 'Ivan the Terrible']
    },
    {
        "text": "Which battle marked the end of Napoleon's rule?",
        "category": 'history',
        "correct": 'Waterloo',
        "wrong": ['Austerlitz', 'Trafalgar', 'Leipzig']
    },
    {
        "text": 'In which year did the American Civil War begin?',
        "category": 'history',
        "correct": '1861',
        "wrong": ['1859', '1863', '1865']
    },
    {
        "text": 'Who was the first person to walk on the moon?',
        "category": 'history',
        "correct": 'Neil Armstrong',
        "wrong": ['Buzz Aldrin', 'John Glenn', 'Alan Shepard']
    },
    {
        "text": 'Which ancient civilization built Machu Picchu?',
        "category": 'history',
        "correct": 'Incas',
        "wrong": ['Aztecs', 'Mayans', 'Olmecs']
    },
    {
        "text": 'What year was the Magna Carta signed?',
        "category": 'history',
        "correct": '1215',
        "wrong": ['1205', '1225', '1235']
    },
    {
        "text": 'Who led the Indian independence movement?',
        "category": 'history',
        "correct": 'Mahatma Gandhi',
        "wrong": ['Nehru', 'Patel', 'Bose']
    },
    {
        "text": 'Which war was fought between 1950-1953?',
        "category": 'history',
        "correct": 'Korean War',
        "wrong": ['Vietnam War', 'Cold War', 'World War III']
    },
    {
        "text": 'Who was the first woman to win a Nobel Prize?',
        "category": 'history',
        "correct": 'Marie Curie',
        "wrong": ['Rosa Parks', 'Mother Teresa', 'Jane Addams']
    },
    {
        "text": 'In which year did the French Revolution begin?',
        "category": 'history',
        "correct": '1789',
        "wrong": ['1787', '1791', '1793']
    },
    {
        "text": 'Which emperor built the Colosseum?',
        "category": 'history',
        "correct": 'Vespasian',
        "wrong": ['Julius Caesar', 'Augustus', 'Nero']
    },
    {
        "text": 'What was the name of the ship on which Charles Darwin made his voyage?',
        "category": 'history',
        "correct": 'HMS Beagle',
        "wrong": ['HMS Victory', 'HMS Bounty', 'HMS Endeavour']
    },
    {
        "text": 'Who painted the ceiling of the Sistine Chapel?',
        "category": 'history',
        "correct": 'Michelangelo',
        "wrong": ['Leonardo da Vinci', 'Raphael', 'Donatello']
    },
    {
        "text": 'Which country was the first to grant women the right to vote?',
        "category": 'history',
        "correct": 'New Zealand',
        "wrong": ['United States', 'United Kingdom', 'Australia']
    },
    {
        "text": "What is the deepest point in Earth's oceans?",
        "category": 'geography',
        "correct": 'Mariana Trench',
        "wrong": ['Puerto Rico Trench', 'Java Trench', 'Peru-Chile Trench']
    },
    {
        "text": 'Which country has the most time zones?',
        "category": 'geography',
        "correct": 'France',
        "wrong": ['Russia', 'United States', 'China']
    },
    {
        "text": 'What is the capital of New Zealand?',
        "category": 'geography',
        "correct": 'Wellington',
        "wrong": ['Auckland', 'Christchurch', 'Hamilton']
    },
    {
        "text": 'Which African country was never colonized?',
        "category": 'geography',
        "correct": 'Ethiopia',
        "wrong": ['Liberia', 'Morocco', 'Egypt']
    },
    {
        "text": 'What is the driest desert in the world?',
        "category": 'geography',
        "correct": 'Atacama',
        "wrong": ['Sahara', 'Gobi', 'Kalahari']
    },
    {
        "text": 'Which strait separates Europe and Africa?',
        "category": 'geography',
        "correct": 'Strait of Gibraltar',
        "wrong": ['Bosphorus', 'Strait of Hormuz', 'Dardanelles']
    },
    {
        "text": 'What is the highest waterfall in the world?',
        "category": 'geography',
        "correct": 'Angel Falls',
        "wrong": ['Niagara Falls', 'Victoria Falls', 'Iguazu Falls']
    },
    {
        "text": 'Which country has the longest coastline?',
        "category": 'geography',
        "correct": 'Canada',
        "wrong": ['Russia', 'Norway', 'Chile']
    },
    {
        "text": 'What is the largest island in the Mediterranean?',
        "category": 'geography',
        "correct": 'Sicily',
        "wrong": ['Sardinia', 'Cyprus', 'Corsica']
    },
    {
        "text": 'Which mountain range contains Mount Everest?',
        "category": 'geography',
        "correct": 'Himalayas',
        "wrong": ['Andes', 'Rocky Mountains', 'Alps']
    },
    {
        "text": 'What is the capital of Kazakhstan?',
        "category": 'geography',
        "correct": 'Nur-Sultan',
        "wrong": ['Almaty', 'Shymkent', 'Aktobe']
    },
    {
        "text": 'Which sea is the saltiest in the world?',
        "category": 'geography',
        "correct": 'Dead Sea',
        "wrong": ['Red Sea', 'Mediterranean Sea', 'Caspian Sea']
    },
    {
        "text": 'What is the southernmost continent?',
        "category": 'geography',
        "correct": 'Antarctica',
        "wrong": ['South America', 'Australia', 'Africa']
    },
    {
        "text": 'Which country is entirely landlocked by South Africa?',
        "category": 'geography',
        "correct": 'Lesotho',
        "wrong": ['Botswana', 'Swaziland', 'Zimbabwe']
    },
    {
        "text": 'What is the largest lake in Africa?',
        "category": 'geography',
        "correct": 'Lake Victoria',
        "wrong": ['Lake Chad', 'Lake Tanganyika', 'Lake Malawi']
    },
    {
        "text": "Who directed the movie 'Jaws'?",
        "category": 'entertainment',
        "correct": 'Steven Spielberg',
        "wrong": ['George Lucas', 'Martin Scorsese', 'Francis Ford Coppola']
    },
    {
        "text": 'What is the highest-grossing film of all time?',
        "category": 'entertainment',
        "correct": 'Avatar',
        "wrong": ['Titanic', 'Avengers: Endgame', 'Star Wars: The Force Awakens']
    },
    {
        "text": 'Which TV show features the character Walter White?',
        "category": 'entertainment',
        "correct": 'Breaking Bad',
        "wrong": ['The Sopranos', 'Better Call Saul', 'Dexter']
    },
    {
        "text": 'What is the first movie in the Star Wars saga?',
        "category": 'entertainment',
        "correct": 'A New Hope',
        "wrong": ['The Phantom Menace', 'The Empire Strikes Back', 'Return of the Jedi']
    },
    {
        "text": 'Who won the Academy Award for Best Actor in 2020?',
        "category": 'entertainment',
        "correct": 'Joaquin Phoenix',
        "wrong": ['Adam Driver', 'Leonardo DiCaprio', 'Antonio Banderas']
    },
    {
        "text": "Which director is known for films like 'Pulp Fiction'?",
        "category": 'entertainment',
        "correct": 'Quentin Tarantino',
        "wrong": ['Martin Scorsese', 'Christopher Nolan', 'David Fincher']
    },
    {
        "text": 'What is the longest-running animated TV series?',
        "category": 'entertainment',
        "correct": 'The Simpsons',
        "wrong": ['South Park', 'Family Guy', 'Futurama']
    },
    {
        "text": "Who played the Joker in 'The Dark Knight'?",
        "category": 'entertainment',
        "correct": 'Heath Ledger',
        "wrong": ['Jack Nicholson', 'Joaquin Phoenix', 'Jared Leto']
    },
    {
        "text": 'Which movie won the first Academy Award for Best Picture?',
        "category": 'entertainment',
        "correct": 'Wings',
        "wrong": ['The Jazz Singer', 'Sunrise', 'The Way of All Flesh']
    },
    {
        "text": "What is the name of the coffee shop in 'Friends'?",
        "category": 'entertainment',
        "correct": 'Central Perk',
        "wrong": ['The Grind', "Java Joe's", 'The Coffee House']
    },
    {
        "text": 'Which country won the 2018 FIFA World Cup?',
        "category": 'sports',
        "correct": 'France',
        "wrong": ['Germany', 'Brazil', 'Argentina']
    },
    {
        "text": 'Which tennis tournament is played on grass courts?',
        "category": 'sports',
        "correct": 'Wimbledon',
        "wrong": ['US Open', 'French Open', 'Australian Open']
    },
    {
        "text": 'Which athlete has won the most Olympic gold medals?',
        "category": 'sports',
        "correct": 'Michael Phelps',
        "wrong": ['Carl Lewis', 'Mark Spitz', 'Usain Bolt']
    },
    {
        "text": "Which country hosts Formula 1's Monaco Grand Prix?",
        "category": 'sports',
        "correct": 'Monaco',
        "wrong": ['France', 'Italy', 'Spain']
    },
    {
        "text": 'How many strikes do you need for a perfect game in bowling?',
        "category": 'sports',
        "correct": '12',
        "wrong": ['10', '15', '20']
    },
    {
        "text": "Which swimmer is known as the 'Flying Fish'?",
        "category": 'sports',
        "correct": 'Michael Phelps',
        "wrong": ['Adam Peaty', 'Caeleb Dressel', 'Katie Ledecky']
    },
    {
        "text": "Who composed 'The Four Seasons'?",
        "category": 'music',
        "correct": 'Vivaldi',
        "wrong": ['Bach', 'Mozart', 'Beethoven']
    },
    {
        "text": "Which band released 'Bohemian Rhapsody'?",
        "category": 'music',
        "correct": 'Queen',
        "wrong": ['The Beatles', 'Led Zeppelin', 'The Rolling Stones']
    },
    {
        "text": "What does 'forte' mean in music?",
        "category": 'music',
        "correct": 'Loud',
        "wrong": ['Soft', 'Fast', 'Slow']
    },
    {
        "text": 'Which instrument is Yo-Yo Ma famous for playing?',
        "category": 'music',
        "correct": 'Cello',
        "wrong": ['Violin', 'Piano', 'Flute']
    },
    {
        "text": "Who wrote 'The Magic Flute'?",
        "category": 'music',
        "correct": 'Mozart',
        "wrong": ['Bach', 'Beethoven', 'Handel']
    },
    {
        "text": 'Which genre of music originated in New Orleans?',
        "category": 'music',
        "correct": 'Jazz',
        "wrong": ['Blues', 'Rock', 'Country']
    },
    {
        "text": 'What is the highest female singing voice?',
        "category": 'music',
        "correct": 'Soprano',
        "wrong": ['Alto', 'Mezzo-soprano', 'Contralto']
    },
    {
        "text": "Who wrote 'Pride and Prejudice'?",
        "category": 'literature',
        "correct": 'Jane Austen',
        "wrong": ['Charlotte Brontë', 'Emily Dickinson', 'Virginia Woolf']
    },
    {
        "text": "Which novel begins with 'It was the best of times'?",
        "category": 'literature',
        "correct": 'A Tale of Two Cities',
        "wrong": ['Great Expectations', 'Oliver Twist', 'David Copperfield']
    },
    {
        "text": 'Who created the detective Sherlock Holmes?',
        "category": 'literature',
        "correct": 'Arthur Conan Doyle',
        "wrong": ['Agatha Christie', 'Edgar Allan Poe', 'Raymond Chandler']
    },
    {
        "text": "Who wrote '1984'?",
        "category": 'literature',
        "correct": 'George Orwell',
        "wrong": ['Aldous Huxley', 'Ray Bradbury', 'Kurt Vonnegut']
    },
    {
        "text": "Who wrote 'To Kill a Mockingbird'?",
        "category": 'literature',
        "correct": 'Harper Lee',
        "wrong": ['Toni Morrison', 'Maya Angelou', "Flannery O'Connor"]
    },
    {
        "text": "What is the first line of 'A Tale of Two Cities'?",
        "category": 'literature',
        "correct": 'It was the best of times, it was the worst of times',
        "wrong": ['Call me Ishmael', 'In the beginning', 'Once upon a time']
    },
    {
        "text": "Who wrote 'The Great Gatsby'?",
        "category": 'literature',
        "correct": 'F. Scott Fitzgerald',
        "wrong": ['Ernest Hemingway', 'John Steinbeck', 'William Faulkner']
    },
    {
        "text": 'Which epic poem tells the story of Odysseus?',
        "category": 'literature',
        "correct": 'The Odyssey',
        "wrong": ['The Iliad', 'The Aeneid', 'Beowulf']
    },
    {
        "text": "What does 'CPU' stand for?",
        "category": 'technology',
        "correct": 'Central Processing Unit',
        "wrong": ['Computer Processing Unit', 'Central Program Unit', 'Computer Program Unit']
    },
    {
        "text": 'Who founded Microsoft?',
        "category": 'technology',
        "correct": 'Bill Gates',
        "wrong": ['Steve Jobs', 'Larry Page', 'Mark Zuckerberg']
    },
    {
        "text": 'What year was the first iPhone released?',
        "category": 'technology',
        "correct": '2007',
        "wrong": ['2005', '2009', '2011']
    },
    {
        "text": "What does 'RAM' stand for?",
        "category": 'technology',
        "correct": 'Random Access Memory',
        "wrong": ['Random Application Memory', 'Rapid Access Memory', 'Read Access Memory']
    },
    {
        "text": 'Which company created the Android operating system?',
        "category": 'technology',
        "correct": 'Google',
        "wrong": ['Apple', 'Microsoft', 'Samsung']
    },
    {
        "text": "What does 'USB' stand for?",
        "category": 'technology',
        "correct": 'Universal Serial Bus',
        "wrong": ['Universal System Bus', 'United Serial Bus', 'United System Bus']
    },
    {
        "text": 'Which programming language is known for its use in web development?',
        "category": 'technology',
        "correct": 'JavaScript',
        "wrong": ['Python', 'C++', 'Java']
    },
    {
        "text": 'What year was the World Wide Web invented?',
        "category": 'technology',
        "correct": '1991',
        "wrong": ['1989', '1993', '1995']
    },
    {
        "text": 'What is the largest desert in the world?',
        "category": 'geography',
        "correct": 'Antarctica',
        "wrong": ['Gobi', 'Sahara', 'Arabian']
    },
    {
        "text": 'Who invented the telephone?',
        "category": 'history',
        "correct": 'Alexander Graham Bell',
        "wrong": ['Thomas Edison', 'Nikola Tesla', 'Benjamin Franklin']
    },
    {
        "text": "What does 'HTTP' stand for?",
        "category": 'technology',
        "correct": 'HyperText Transfer Protocol',
        "wrong": ['High Transfer Text Protocol', 'HyperText Transport Protocol', 'High Text Transfer Protocol']
    },
    {
        "text": "Who wrote 'Hamlet'?",
        "category": 'literature',
        "correct": 'William Shakespeare',
        "wrong": ['Charles Dickens', 'Jane Austen', 'Mark Twain']
    },
    {
        "text": 'What is the fastest bird?',
        "category": 'science',
        "correct": 'Peregrine Falcon',
        "wrong": ['Eagle', 'Hawk', 'Owl']
    },
    {
        "text": 'What is the smallest prime number?',
        "category": 'general',
        "correct": '2',
        "wrong": ['0', '1', '3']
    },
    {
        "text": 'Which vitamin deficiency causes scurvy?',
        "category": 'science',
        "correct": 'Vitamin C',
        "wrong": ['Vitamin A', 'Vitamin D', 'Vitamin B12']
    },
    {
        "text": "Who painted 'Starry Night'?",
        "category": 'art',
        "correct": 'Vincent van Gogh',
        "wrong": ['Pablo Picasso', 'Claude Monet', 'Salvador Dali']
    },
    {
        "text": "Which element has the symbol 'Fe'?",
        "category": 'science',
        "correct": 'Iron',
        "wrong": ['Fluorine', 'Francium', 'Fermium']
    },
    {
        "text": 'What year did the first man land on the moon?',
        "category": 'history',
        "correct": '1969',
        "wrong": ['1967', '1971', '1973']
    },
    {
        "text": 'Which instrument did Mozart primarily compose for?',
        "category": 'music',
        "correct": 'Piano',
        "wrong": ['Violin', 'Flute', 'Organ']
    },
    {
        "text": "What is the most abundant gas in Earth's atmosphere?",
        "category": 'science',
        "correct": 'Nitrogen',
        "wrong": ['Argon', 'Oxygen', 'Carbon Dioxide']
    },
    {
        "text": 'What blood type is the universal donor?',
        "category": 'science',
        "correct": 'O negative',
        "wrong": ['A positive', 'AB positive', 'O positive']
    },
    {
        "text": 'What planet has the most moons?',
        "category": 'science',
        "correct": 'Saturn',
        "wrong": ['Neptune', 'Uranus', 'Jupiter']
    },
    {
        "text": 'What is the smallest unit of life?',
        "category": 'science',
        "correct": 'Cell',
        "wrong": ['Tissue', 'Atom', 'Molecule']
    },
    {
        "text": 'What gas do plants absorb from the atmosphere?',
        "category": 'science',
        "correct": 'Carbon Dioxide',
        "wrong": ['Oxygen', 'Nitrogen', 'Helium']
    },
    {
        "text": 'What is the process by which plants make food?',
        "category": 'science',
        "correct": 'Photosynthesis',
        "wrong": ['Osmosis', 'Respiration', 'Diffusion']
    },
    {
        "text": 'What type of rock is formed from cooling lava?',
        "category": 'science',
        "correct": 'Igneous',
        "wrong": ['Limestone', 'Sedimentary', 'Metamorphic']
    },
    {
        "text": 'What is the pH level of pure water?',
        "category": 'science',
        "correct": '7',
        "wrong": ['14', '10', '0']
    },
    {
        "text": 'What force keeps planets in orbit around the sun?',
        "category": 'science',
        "correct": 'Gravity',
        "wrong": ['Magnetism', 'Inertia', 'Friction']
    },
    {
        "text": 'What is the boiling point of water at sea level in Celsius?',
        "category": 'science',
        "correct": '100°C',
        "wrong": ['212°C', '0°C', '50°C']
    },
    {
        "text": 'What element has the atomic number 1?',
        "category": 'science',
        "correct": 'Hydrogen',
        "wrong": ['Oxygen', 'Helium', 'Carbon']
    },
    {
        "text": 'What is the chemical symbol for sodium?',
        "category": 'science',
        "correct": 'Na',
        "wrong": ['Sd', 'S', 'So']
    },
    {
        "text": 'What is the most common element in the universe?',
        "category": 'science',
        "correct": 'Hydrogen',
        "wrong": ['Oxygen', 'Helium', 'Carbon']
    },
    {
        "text": 'What particle in an atom has a negative charge?',
        "category": 'science',
        "correct": 'Electron',
        "wrong": ['Proton', 'Nucleus', 'Neutron']
    },
    {
        "text": 'What is the freezing point of water in Fahrenheit?',
        "category": 'science',
        "correct": '32°F',
        "wrong": ['0°F', '100°F', '212°F']
    },
    {
        "text": 'What gas makes up most of the Sun?',
        "category": 'science',
        "correct": 'Hydrogen',
        "wrong": ['Helium', 'Nitrogen', 'Oxygen']
    },
    {
        "text": 'What is the largest internal organ in the human body?',
        "category": 'science',
        "correct": 'Liver',
        "wrong": ['Heart', 'Stomach', 'Lungs']
    },
    {
        "text": 'What planet is closest to the Sun?',
        "category": 'science',
        "correct": 'Mercury',
        "wrong": ['Venus', 'Mars', 'Earth']
    },
    {
        "text": 'What is the scientific name for the kneecap?',
        "category": 'science',
        "correct": 'Patella',
        "wrong": ['Tibia', 'Fibula', 'Femur']
    },
    {
        "text": 'What is the process of liquid turning into gas called?',
        "category": 'science',
        "correct": 'Evaporation',
        "wrong": ['Precipitation', 'Condensation', 'Sublimation']
    },
    {
        "text": 'What metal is liquid at room temperature?',
        "category": 'science',
        "correct": 'Mercury',
        "wrong": ['Gold', 'Silver', 'Iron']
    },
    {
        "text": 'How many teeth does an adult human typically have?',
        "category": 'science',
        "correct": '32',
        "wrong": ['36', '28', '24']
    },
    {
        "text": 'What is the largest bone in the human body?',
        "category": 'science',
        "correct": 'Femur',
        "wrong": ['Humerus', 'Tibia', 'Radius']
    },
    {
        "text": 'What vitamin is produced when skin is exposed to sunlight?',
        "category": 'science',
        "correct": 'Vitamin D',
        "wrong": ['Vitamin B12', 'Vitamin C', 'Vitamin A']
    },
    {
        "text": 'What is the main gas in the air we breathe out?',
        "category": 'science',
        "correct": 'Carbon Dioxide',
        "wrong": ['Hydrogen', 'Nitrogen', 'Oxygen']
    },
    {
        "text": 'What is the term for animals that eat both plants and meat?',
        "category": 'science',
        "correct": 'Omnivore',
        "wrong": ['Herbivore', 'Carnivore', 'Insectivore']
    },
    {
        "text": 'What is the colored part of the human eye called?',
        "category": 'science',
        "correct": 'Iris',
        "wrong": ['Pupil', 'Cornea', 'Retina']
    },
    {
        "text": 'What is the name of the galaxy that contains our solar system?',
        "category": 'science',
        "correct": 'Milky Way',
        "wrong": ['Whirlpool', 'Andromeda', 'Triangulum']
    },
    {
        "text": 'What is the chemical symbol for iron?',
        "category": 'science',
        "correct": 'Fe',
        "wrong": ['In', 'Ir', 'I']
    },
    {
        "text": 'What is the main component of natural gas?',
        "category": 'science',
        "correct": 'Methane',
        "wrong": ['Propane', 'Ethane', 'Butane']
    },
    {
        "text": 'What is the term for a scientist who studies rocks?',
        "category": 'science',
        "correct": 'Geologist',
        "wrong": ['Physicist', 'Biologist', 'Chemist']
    },
    {
        "text": 'What is the approximate age of the Earth?',
        "category": 'science',
        "correct": '4.5 billion years',
        "wrong": ['1 billion years', '10 billion years', '100 million years']
    },
    {
        "text": 'What is the name of the process where a caterpillar becomes a butterfly?',
        "category": 'science',
        "correct": 'Metamorphosis',
        "wrong": ['Mitosis', 'Evolution', 'Photosynthesis']
    },
    {
        "text": 'What is the chemical formula for table salt?',
        "category": 'science',
        "correct": 'NaCl',
        "wrong": ['KCl', 'MgCl2', 'CaCl2']
    },
    {
        "text": 'What particle has no electrical charge?',
        "category": 'science',
        "correct": 'Neutron',
        "wrong": ['Electron', 'Positron', 'Proton']
    },
    {
        "text": 'How many continents are there on Earth?',
        "category": 'General',
        "correct": '7',
        "wrong": ['6', '5', '8']
    },
    {
        "text": 'How many sides does a hexagon have?',
        "category": 'General',
        "correct": '6',
        "wrong": ['8', '5', '7']
    },
    {
        "text": 'How many teeth does an adult human have?',
        "category": 'General',
        "correct": '32',
        "wrong": ['36', '30', '28']
    },
    {
        "text": 'What is the largest land animal?',
        "category": 'General',
        "correct": 'African Elephant',
        "wrong": ['Giraffe', 'White Rhinoceros', 'Hippopotamus']
    },
    {
        "text": 'What is the largest type of bear?',
        "category": 'General',
        "correct": 'Polar Bear',
        "wrong": ['Brown Bear', 'Kodiak Bear', 'Grizzly Bear']
    },
    {
        "text": 'What is the freezing point of water in Celsius?',
        "category": 'General',
        "correct": '0°C',
        "wrong": ['100°C', '-32°C', '32°C']
    },
    {
        "text": 'How many stripes are on the American flag?',
        "category": 'General',
        "correct": '13',
        "wrong": ['50', '11', '15']
    },
    {
        "text": 'What is the smallest planet in our solar system?',
        "category": 'General',
        "correct": 'Mercury',
        "wrong": ['Pluto', 'Mars', 'Venus']
    },
    {
        "text": 'What is the largest country by area?',
        "category": 'General',
        "correct": 'Russia',
        "wrong": ['Canada', 'USA', 'China']
    },
    {
        "text": 'What type of bond involves the sharing of electron pairs?',
        "category": 'science',
        "correct": 'Covalent bond',
        "wrong": ['Hydrogen bond', 'Metallic bond', 'Ionic bond']
    },
    {
        "text": 'What is the SI unit of electric current?',
        "category": 'science',
        "correct": 'Ampere',
        "wrong": ['Volt', 'Ohm', 'Watt']
    },
    {
        "text": 'What is the capital of Vietnam?',
        "category": 'geography',
        "correct": 'Hanoi',
        "wrong": ['Hue', 'Ho Chi Minh City', 'Da Nang']
    },
    {
        "text": 'What year was Wikipedia founded?',
        "category": 'technology',
        "correct": '2001',
        "wrong": ['2003', '2005', '1999']
    },
    {
        "text": 'What does NFC stand for in mobile technology?',
        "category": 'technology',
        "correct": 'Near Field Communication',
        "wrong": ['New Frequency Channel', 'Network File Control', 'Next-Gen File Communication']
    },
    {
        "text": 'Who composed the theme music for Star Wars?',
        "category": 'entertainment',
        "correct": 'John Williams',
        "wrong": ['Howard Shore', 'Danny Elfman', 'Hans Zimmer']
    },
    {
        "text": 'What is the largest species of shark?',
        "category": 'General',
        "correct": 'Whale Shark',
        "wrong": ['Great White Shark', 'Megalodon', 'Tiger Shark']
    },
    {
        "text": 'What country won the 2014 FIFA World Cup?',
        "category": 'sports',
        "correct": 'Germany',
        "wrong": ['Brazil', 'Spain', 'Argentina']
    },
    {
        "text": 'How many Grand Slam tournaments are there in tennis per year?',
        "category": 'sports',
        "correct": '4',
        "wrong": ['3', '5', '6']
    },
    {
        "text": "Who wrote 'The Iliad'?",
        "category": 'literature',
        "correct": 'Homer',
        "wrong": ['Virgil', 'Euripides', 'Sophocles']
    }
]
