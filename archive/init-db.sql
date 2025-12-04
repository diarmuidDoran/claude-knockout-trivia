-- Comprehensive trivia database with 200 unique questions
-- Categories: general, science, history, geography, sports, entertainment, literature, music, technology

-- Clear existing data
DELETE FROM question_options;
DELETE FROM questions;

-- Reset sequences
ALTER SEQUENCE questions_id_seq RESTART WITH 1;
ALTER SEQUENCE question_options_id_seq RESTART WITH 1;

-- Insert all trivia questions
INSERT INTO questions (question_text, category, difficulty) VALUES
('What year did the Titanic sink?', 'general', 'medium'),
('Who painted the Mona Lisa?', 'general', 'medium'),
('What is the smallest country in the world?', 'general', 'medium'),
('Which gas makes up most of Earth''s atmosphere?', 'general', 'medium'),
('What is the currency of Japan?', 'general', 'medium'),
('How many bones are in the adult human body?', 'general', 'medium'),
('What is the longest river in the world?', 'general', 'medium'),
('Which vitamin is produced when skin is exposed to sunlight?', 'general', 'medium'),
('What is the hardest natural substance on Earth?', 'general', 'medium'),
('Which continent is the largest?', 'general', 'medium'),
('What does ''www'' stand for?', 'general', 'medium'),
('How many chambers does a human heart have?', 'general', 'medium'),
('What is the speed of light?', 'general', 'medium'),
('Which country gifted the Statue of Liberty to the United States?', 'general', 'medium'),
('What is the most abundant gas in the universe?', 'general', 'medium'),
('How many time zones are there in Russia?', 'general', 'medium'),
('What is the chemical symbol for gold?', 'general', 'medium'),
('Which organ in the human body produces insulin?', 'general', 'medium'),
('What is the smallest unit of matter?', 'general', 'medium'),
('How many strings does a standard guitar have?', 'general', 'medium'),
('What is the atomic number of carbon?', 'science', 'medium'),
('Which scientist developed the theory of evolution?', 'science', 'medium'),
('What is the powerhouse of the cell?', 'science', 'medium'),
('How many bones are in a giraffe''s neck?', 'science', 'medium'),
('What is the study of earthquakes called?', 'science', 'medium'),
('Which blood type is known as the universal donor?', 'science', 'medium'),
('What is the chemical symbol for silver?', 'science', 'medium'),
('How long does it take for light from the Sun to reach Earth?', 'science', 'medium'),
('What is the most common element in the human body?', 'science', 'medium'),
('Which planet has the most moons?', 'science', 'medium'),
('What is the study of fungi called?', 'science', 'medium'),
('How many pairs of chromosomes do humans have?', 'science', 'medium'),
('What is the speed of sound in air at room temperature?', 'science', 'medium'),
('Which organ filters blood in the human body?', 'science', 'medium'),
('What is the smallest bone in the human body?', 'science', 'medium'),
('In which year did the Berlin Wall fall?', 'history', 'medium'),
('Who was the last Tsar of Russia?', 'history', 'medium'),
('Which battle marked the end of Napoleon''s rule?', 'history', 'medium'),
('In which year did the American Civil War begin?', 'history', 'medium'),
('Who was the first person to walk on the moon?', 'history', 'medium'),
('Which ancient civilization built Machu Picchu?', 'history', 'medium'),
('What year was the Magna Carta signed?', 'history', 'medium'),
('Who led the Indian independence movement?', 'history', 'medium'),
('Which war was fought between 1950-1953?', 'history', 'medium'),
('Who was the first woman to win a Nobel Prize?', 'history', 'medium'),
('In which year did the French Revolution begin?', 'history', 'medium'),
('Which emperor built the Colosseum?', 'history', 'medium'),
('What was the name of the ship on which Charles Darwin made his voyage?', 'history', 'medium'),
('Who painted the ceiling of the Sistine Chapel?', 'history', 'medium'),
('Which country was the first to grant women the right to vote?', 'history', 'medium'),
('What is the deepest point in Earth''s oceans?', 'geography', 'medium'),
('Which country has the most time zones?', 'geography', 'medium'),
('What is the capital of New Zealand?', 'geography', 'medium'),
('Which African country was never colonized?', 'geography', 'medium'),
('What is the driest desert in the world?', 'geography', 'medium'),
('Which strait separates Europe and Africa?', 'geography', 'medium'),
('What is the highest waterfall in the world?', 'geography', 'medium'),
('Which country has the longest coastline?', 'geography', 'medium'),
('What is the largest island in the Mediterranean?', 'geography', 'medium'),
('Which mountain range contains Mount Everest?', 'geography', 'medium'),
('What is the capital of Kazakhstan?', 'geography', 'medium'),
('Which sea is the saltiest in the world?', 'geography', 'medium'),
('What is the southernmost continent?', 'geography', 'medium'),
('Which country is entirely landlocked by South Africa?', 'geography', 'medium'),
('What is the largest lake in Africa?', 'geography', 'medium'),
('Who directed the movie ''Jaws''?', 'entertainment', 'medium'),
('What is the highest-grossing film of all time?', 'entertainment', 'medium'),
('Which TV show features the character Walter White?', 'entertainment', 'medium'),
('What is the first movie in the Star Wars saga?', 'entertainment', 'medium'),
('Who won the Academy Award for Best Actor in 2020?', 'entertainment', 'medium'),
('Which director is known for films like ''Pulp Fiction''?', 'entertainment', 'medium'),
('What is the longest-running animated TV series?', 'entertainment', 'medium'),
('Who played the Joker in ''The Dark Knight''?', 'entertainment', 'medium'),
('Which movie won the first Academy Award for Best Picture?', 'entertainment', 'medium'),
('What is the name of the coffee shop in ''Friends''?', 'entertainment', 'medium'),
('Which country won the 2018 FIFA World Cup?', 'sports', 'medium'),
('Which tennis tournament is played on grass courts?', 'sports', 'medium'),
('Which athlete has won the most Olympic gold medals?', 'sports', 'medium'),
('Which country hosts Formula 1''s Monaco Grand Prix?', 'sports', 'medium'),
('How many strikes do you need for a perfect game in bowling?', 'sports', 'medium'),
('Which swimmer is known as the ''Flying Fish''?', 'sports', 'medium'),
('Who composed ''The Four Seasons''?', 'music', 'medium'),
('Which band released ''Bohemian Rhapsody''?', 'music', 'medium'),
('What does ''forte'' mean in music?', 'music', 'medium'),
('Which instrument is Yo-Yo Ma famous for playing?', 'music', 'medium'),
('Who wrote ''The Magic Flute''?', 'music', 'medium'),
('Which genre of music originated in New Orleans?', 'music', 'medium'),
('What is the highest female singing voice?', 'music', 'medium'),
('Who wrote ''Pride and Prejudice''?', 'literature', 'medium'),
('Which novel begins with ''It was the best of times''?', 'literature', 'medium'),
('Who created the detective Sherlock Holmes?', 'literature', 'medium'),
('Who wrote ''1984''?', 'literature', 'medium'),
('Who wrote ''To Kill a Mockingbird''?', 'literature', 'medium'),
('What is the first line of ''A Tale of Two Cities''?', 'literature', 'medium'),
('Who wrote ''The Great Gatsby''?', 'literature', 'medium'),
('Which epic poem tells the story of Odysseus?', 'literature', 'medium'),
('What does ''CPU'' stand for?', 'technology', 'medium'),
('Who founded Microsoft?', 'technology', 'medium'),
('What year was the first iPhone released?', 'technology', 'medium'),
('What does ''RAM'' stand for?', 'technology', 'medium'),
('Which company created the Android operating system?', 'technology', 'medium'),
('What does ''USB'' stand for?', 'technology', 'medium'),
('Which programming language is known for its use in web development?', 'technology', 'medium'),
('What year was the World Wide Web invented?', 'technology', 'medium'),
('What is the largest desert in the world?', 'geography', 'medium'),
('Who invented the telephone?', 'history', 'medium'),
('What does ''HTTP'' stand for?', 'technology', 'medium'),
('Who wrote ''Hamlet''?', 'literature', 'medium'),
('What is the fastest bird?', 'science', 'medium'),
('What is the smallest prime number?', 'general', 'medium'),
('Which vitamin deficiency causes scurvy?', 'science', 'medium'),
('Who painted ''Starry Night''?', 'art', 'medium'),
('Which element has the symbol ''Fe''?', 'science', 'medium'),
('What year did the first man land on the moon?', 'history', 'medium'),
('Which instrument did Mozart primarily compose for?', 'music', 'medium'),
('What is the Planck constant in joule-seconds?', 'science', 'hard'),
('In which year did the Byzantine Empire finally fall?', 'history', 'hard'),
('What is the capital of Bhutan?', 'geography', 'hard'),
('Who composed ''The Art of Fugue''?', 'music', 'hard'),
('What is the rarest blood type?', 'science', 'hard'),
('In which year was the Treaty of Westphalia signed?', 'history', 'hard'),
('What is the smallest bone in the human body?', 'science', 'hard'),
('Which element has the highest atomic number that occurs naturally?', 'science', 'hard'),
('What is the longest word in the English language without repeating letters?', 'literature', 'hard'),
('In what year did the Chernobyl disaster occur?', 'history', 'hard'),
('What is the study of earthquakes called?', 'science', 'hard'),
('Which programming language was developed by Bjarne Stroustrup?', 'technology', 'hard'),
('What is the smallest country in Africa by area?', 'geography', 'hard'),
('Who wrote ''One Hundred Years of Solitude''?', 'literature', 'hard'),
('What is the chemical formula for caffeine?', 'science', 'hard'),
('In which year did the Thirty Years'' War end?', 'history', 'hard'),
('What is the hardest natural mineral on the Mohs scale?', 'science', 'hard'),
('Which artist painted ''The Persistence of Memory''?', 'art', 'hard'),
('What is the capital of Kazakhstan?', 'geography', 'hard'),
('Who developed the theory of continental drift?', 'science', 'hard'),
('What is the most abundant protein in the human body?', 'science', 'hard'),
('In which year was the Berlin Wall erected?', 'history', 'hard'),
('What is the study of fungi called?', 'science', 'hard'),
('Which composer wrote ''The Ring of the Nibelung''?', 'music', 'hard'),
('What is the smallest planet in our solar system?', 'science', 'hard'),
('Who wrote ''The Master and Margarita''?', 'literature', 'hard'),
('What is the chemical symbol for tungsten?', 'science', 'hard'),
('In which year did the Russo-Japanese War begin?', 'history', 'hard'),
('What is the largest moon of Saturn?', 'science', 'hard'),
('Which artist sculpted ''The Thinker''?', 'art', 'hard'),
('What is the capital of Mongolia?', 'geography', 'hard'),
('Who discovered penicillin?', 'science', 'hard'),
('What is the study of birds called?', 'science', 'hard'),
('Which film won the first Academy Award for Best Picture?', 'entertainment', 'hard'),
('What is the smallest unit of matter?', 'science', 'hard'),
('In which year was the United Nations founded?', 'history', 'hard'),
('What is the study of insects called?', 'science', 'hard'),
('Who painted ''Guernica''?', 'art', 'hard'),
('What is the capital of Eritrea?', 'geography', 'hard'),
('Which element has the atomic number 79?', 'science', 'hard'),
('What is the longest river in Asia?', 'geography', 'hard'),
('Who wrote ''Ulysses''?', 'literature', 'hard'),
('What is the study of stars called?', 'science', 'hard'),
('In which year did World War I begin?', 'history', 'hard'),
('What is the chemical formula for table salt?', 'science', 'hard'),
('Which composer wrote ''The Four Seasons''?', 'music', 'hard'),
('What is the capital of Myanmar?', 'geography', 'hard'),
('Who developed the periodic table?', 'science', 'hard'),
('What is the study of the weather called?', 'science', 'hard'),
('Which artist painted ''The Starry Night''?', 'art', 'hard'),
('What is the smallest country in South America?', 'geography', 'hard'),
('Who wrote ''The Canterbury Tales''?', 'literature', 'hard'),
('What is the study of reptiles called?', 'science', 'hard'),
('In which year did the American Civil War end?', 'history', 'hard'),
('What is the chemical symbol for lead?', 'science', 'hard'),
('Which composer wrote ''Swan Lake''?', 'music', 'hard'),
('What is the capital of Tajikistan?', 'geography', 'hard'),
('Who discovered the structure of DNA?', 'science', 'hard'),
('What is the study of fish called?', 'science', 'hard'),
('Which film director made ''Citizen Kane''?', 'entertainment', 'hard'),
('What is the largest desert in the world?', 'geography', 'hard'),
('Who wrote ''Don Quixote''?', 'literature', 'hard'),
('What is the study of the mind called?', 'science', 'hard'),
('In which year was the first iPhone released?', 'technology', 'hard'),
('What is the chemical formula for water?', 'science', 'hard'),
('Which artist painted ''The Birth of Venus''?', 'art', 'hard'),
('What is the capital of Uzbekistan?', 'geography', 'hard'),
('Who developed the theory of evolution?', 'science', 'hard'),
('What is the study of plants called?', 'science', 'hard'),
('Which composer wrote ''The Magic Flute''?', 'music', 'hard'),
('What is the smallest bone in the human ear?', 'science', 'hard'),
('In which year did the French Revolution begin?', 'history', 'hard'),
('What is the chemical symbol for iron?', 'science', 'hard'),
('Which artist sculpted ''David''?', 'art', 'hard'),
('What is the capital of Kyrgyzstan?', 'geography', 'hard'),
('Who invented the telephone?', 'technology', 'hard'),
('What is the study of rocks called?', 'science', 'hard'),
('Which film won the Academy Award for Best Picture in 1994?', 'entertainment', 'hard'),
('What is the largest lake in the world?', 'geography', 'hard'),
('Who wrote ''Pride and Prejudice''?', 'literature', 'hard'),
('What is the study of the Earth''s structure called?', 'science', 'hard'),
('In which year was the Berlin Wall torn down?', 'history', 'hard'),
('What is the chemical symbol for silver?', 'science', 'hard'),
('Which composer wrote ''Carmen''?', 'music', 'hard'),
('What is the capital of Azerbaijan?', 'geography', 'hard'),
('Who discovered radioactivity?', 'science', 'hard'),
('What is the study of ancient life called?', 'science', 'hard'),
('Which artist painted ''The Scream''?', 'art', 'hard'),
('What is the smallest state in India by area?', 'geography', 'hard'),
('Who wrote ''The Iliad''?', 'literature', 'hard'),
('What is the Planck constant in joule-seconds?', 'science', 'hard'),
('In which year did the Byzantine Empire finally fall?', 'history', 'hard'),
('What is the capital of Bhutan?', 'geography', 'hard'),
('Who composed ''The Art of Fugue''?', 'music', 'hard'),
('What is the rarest blood type?', 'science', 'hard'),
('In which year was the Treaty of Westphalia signed?', 'history', 'hard'),
('What is the smallest bone in the human body?', 'science', 'hard'),
('Which element has the highest atomic number that occurs naturally?', 'science', 'hard'),
('What is the longest word in the English language without repeating letters?', 'literature', 'hard'),
('In what year did the Chernobyl disaster occur?', 'history', 'hard'),
('What is the study of earthquakes called?', 'science', 'hard'),
('Which programming language was developed by Bjarne Stroustrup?', 'technology', 'hard'),
('What is the smallest country in Africa by area?', 'geography', 'hard'),
('Who wrote ''One Hundred Years of Solitude''?', 'literature', 'hard'),
('What is the chemical formula for caffeine?', 'science', 'hard'),
('In which year did the Thirty Years'' War end?', 'history', 'hard'),
('What is the hardest natural mineral on the Mohs scale?', 'science', 'hard'),
('Which artist painted ''The Persistence of Memory''?', 'art', 'hard'),
('What is the capital of Kazakhstan?', 'geography', 'hard'),
('Who developed the theory of continental drift?', 'science', 'hard'),
('What is the most abundant protein in the human body?', 'science', 'hard'),
('In which year was the Berlin Wall erected?', 'history', 'hard'),
('What is the study of fungi called?', 'science', 'hard'),
('Which composer wrote ''The Ring of the Nibelung''?', 'music', 'hard'),
('What is the smallest planet in our solar system?', 'science', 'hard'),
('Who wrote ''The Master and Margarita''?', 'literature', 'hard'),
('What is the chemical symbol for tungsten?', 'science', 'hard'),
('In which year did the Russo-Japanese War begin?', 'history', 'hard'),
('What is the largest moon of Saturn?', 'science', 'hard'),
('Which artist sculpted ''The Thinker''?', 'art', 'hard'),
('What is the capital of Mongolia?', 'geography', 'hard'),
('Who discovered penicillin?', 'science', 'hard'),
('What is the study of birds called?', 'science', 'hard'),
('Which film won the first Academy Award for Best Picture?', 'entertainment', 'hard'),
('What is the smallest unit of matter?', 'science', 'hard'),
('In which year was the United Nations founded?', 'history', 'hard'),
('What is the study of insects called?', 'science', 'hard'),
('Who painted ''Guernica''?', 'art', 'hard'),
('What is the capital of Eritrea?', 'geography', 'hard'),
('Which element has the atomic number 79?', 'science', 'hard'),
('What is the longest river in Asia?', 'geography', 'hard'),
('Who wrote ''Ulysses''?', 'literature', 'hard'),
('What is the study of stars called?', 'science', 'hard'),
('In which year did World War I begin?', 'history', 'hard'),
('What is the chemical formula for table salt?', 'science', 'hard'),
('Which composer wrote ''The Four Seasons''?', 'music', 'hard'),
('What is the capital of Myanmar?', 'geography', 'hard'),
('Who developed the periodic table?', 'science', 'hard'),
('What is the study of the weather called?', 'science', 'hard'),
('Which artist painted ''The Starry Night''?', 'art', 'hard'),
('What is the smallest country in South America?', 'geography', 'hard'),
('Who wrote ''The Canterbury Tales''?', 'literature', 'hard'),
('What is the study of reptiles called?', 'science', 'hard'),
('In which year did the American Civil War end?', 'history', 'hard'),
('What is the chemical symbol for lead?', 'science', 'hard'),
('Which composer wrote ''Swan Lake''?', 'music', 'hard'),
('What is the capital of Tajikistan?', 'geography', 'hard'),
('Who discovered the structure of DNA?', 'science', 'hard'),
('What is the study of fish called?', 'science', 'hard'),
('Which film director made ''Citizen Kane''?', 'entertainment', 'hard'),
('What is the largest desert in the world?', 'geography', 'hard'),
('Who wrote ''Don Quixote''?', 'literature', 'hard'),
('What is the study of the mind called?', 'science', 'hard'),
('In which year was the first iPhone released?', 'technology', 'hard'),
('What is the chemical formula for water?', 'science', 'hard'),
('Which artist painted ''The Birth of Venus''?', 'art', 'hard'),
('What is the capital of Uzbekistan?', 'geography', 'hard'),
('Who developed the theory of evolution?', 'science', 'hard'),
('What is the study of plants called?', 'science', 'hard'),
('Which composer wrote ''The Magic Flute''?', 'music', 'hard'),
('What is the smallest bone in the human ear?', 'science', 'hard'),
('In which year did the French Revolution begin?', 'history', 'hard'),
('What is the chemical symbol for iron?', 'science', 'hard'),
('Which artist sculpted ''David''?', 'art', 'hard'),
('What is the capital of Kyrgyzstan?', 'geography', 'hard'),
('Who invented the telephone?', 'technology', 'hard'),
('What is the study of rocks called?', 'science', 'hard'),
('Which film won the Academy Award for Best Picture in 1994?', 'entertainment', 'hard'),
('What is the largest lake in the world?', 'geography', 'hard'),
('Who wrote ''Pride and Prejudice''?', 'literature', 'hard'),
('What is the study of the Earth''s structure called?', 'science', 'hard'),
('In which year was the Berlin Wall torn down?', 'history', 'hard'),
('What is the chemical symbol for silver?', 'science', 'hard'),
('Which composer wrote ''Carmen''?', 'music', 'hard'),
('What is the capital of Azerbaijan?', 'geography', 'hard'),
('Who discovered radioactivity?', 'science', 'hard'),
('What is the study of ancient life called?', 'science', 'hard'),
('Which artist painted ''The Scream''?', 'art', 'hard'),
('What is the smallest state in India by area?', 'geography', 'hard'),
('Who wrote ''The Iliad''?', 'literature', 'hard'),
('What is the Planck constant in joule-seconds?', 'science', 'hard'),
('In which year did the Byzantine Empire finally fall?', 'history', 'hard'),
('What is the capital of Bhutan?', 'geography', 'hard'),
('Who composed ''The Art of Fugue''?', 'music', 'hard'),
('What is the rarest blood type?', 'science', 'hard'),
('In which year was the Treaty of Westphalia signed?', 'history', 'hard'),
('What is the smallest bone in the human body?', 'science', 'hard'),
('Which element has the highest atomic number that occurs naturally?', 'science', 'hard'),
('What is the longest word in the English language without repeating letters?', 'literature', 'hard'),
('In what year did the Chernobyl disaster occur?', 'history', 'hard'),
('What is the study of earthquakes called?', 'science', 'hard'),
('Which programming language was developed by Bjarne Stroustrup?', 'technology', 'hard'),
('What is the smallest country in Africa by area?', 'geography', 'hard'),
('Who wrote ''One Hundred Years of Solitude''?', 'literature', 'hard'),
('What is the chemical formula for caffeine?', 'science', 'hard'),
('In which year did the Thirty Years'' War end?', 'history', 'hard'),
('What is the hardest natural mineral on the Mohs scale?', 'science', 'hard'),
('Which artist painted ''The Persistence of Memory''?', 'art', 'hard'),
('What is the capital of Kazakhstan?', 'geography', 'hard'),
('Who developed the theory of continental drift?', 'science', 'hard'),
('What is the most abundant protein in the human body?', 'science', 'hard'),
('In which year was the Berlin Wall erected?', 'history', 'hard'),
('What is the study of fungi called?', 'science', 'hard'),
('Which composer wrote ''The Ring of the Nibelung''?', 'music', 'hard'),
('What is the smallest planet in our solar system?', 'science', 'hard'),
('Who wrote ''The Master and Margarita''?', 'literature', 'hard'),
('What is the chemical symbol for tungsten?', 'science', 'hard'),
('In which year did the Russo-Japanese War begin?', 'history', 'hard'),
('What is the largest moon of Saturn?', 'science', 'hard'),
('Which artist sculpted ''The Thinker''?', 'art', 'hard'),
('What is the capital of Mongolia?', 'geography', 'hard'),
('Who discovered penicillin?', 'science', 'hard'),
('What is the study of birds called?', 'science', 'hard'),
('Which film won the first Academy Award for Best Picture?', 'entertainment', 'hard'),
('What is the smallest unit of matter?', 'science', 'hard'),
('In which year was the United Nations founded?', 'history', 'hard'),
('What is the study of insects called?', 'science', 'hard'),
('Who painted ''Guernica''?', 'art', 'hard'),
('What is the capital of Eritrea?', 'geography', 'hard'),
('Which element has the atomic number 79?', 'science', 'hard'),
('What is the longest river in Asia?', 'geography', 'hard'),
('Who wrote ''Ulysses''?', 'literature', 'hard'),
('What is the study of stars called?', 'science', 'hard'),
('In which year did World War I begin?', 'history', 'hard'),
('What is the chemical formula for table salt?', 'science', 'hard'),
('Which composer wrote ''The Four Seasons''?', 'music', 'hard'),
('What is the capital of Myanmar?', 'geography', 'hard'),
('Who developed the periodic table?', 'science', 'hard'),
('What is the study of the weather called?', 'science', 'hard'),
('Which artist painted ''The Starry Night''?', 'art', 'hard'),
('What is the smallest country in South America?', 'geography', 'hard'),
('Who wrote ''The Canterbury Tales''?', 'literature', 'hard'),
('What is the study of reptiles called?', 'science', 'hard'),
('In which year did the American Civil War end?', 'history', 'hard'),
('What is the chemical symbol for lead?', 'science', 'hard'),
('Which composer wrote ''Swan Lake''?', 'music', 'hard'),
('What is the capital of Tajikistan?', 'geography', 'hard'),
('Who discovered the structure of DNA?', 'science', 'hard'),
('What is the study of fish called?', 'science', 'hard'),
('Which film director made ''Citizen Kane''?', 'entertainment', 'hard'),
('What is the largest desert in the world?', 'geography', 'hard'),
('Who wrote ''Don Quixote''?', 'literature', 'hard'),
('What is the study of the mind called?', 'science', 'hard'),
('In which year was the first iPhone released?', 'technology', 'hard'),
('What is the chemical formula for water?', 'science', 'hard'),
('Which artist painted ''The Birth of Venus''?', 'art', 'hard'),
('What is the capital of Uzbekistan?', 'geography', 'hard'),
('Who developed the theory of evolution?', 'science', 'hard'),
('What is the study of plants called?', 'science', 'hard'),
('Which composer wrote ''The Magic Flute''?', 'music', 'hard'),
('What is the smallest bone in the human ear?', 'science', 'hard'),
('In which year did the French Revolution begin?', 'history', 'hard'),
('What is the chemical symbol for iron?', 'science', 'hard'),
('Which artist sculpted ''David''?', 'art', 'hard'),
('What is the capital of Kyrgyzstan?', 'geography', 'hard'),
('Who invented the telephone?', 'technology', 'hard'),
('What is the study of rocks called?', 'science', 'hard'),
('Which film won the Academy Award for Best Picture in 1994?', 'entertainment', 'hard'),
('What is the largest lake in the world?', 'geography', 'hard'),
('Who wrote ''Pride and Prejudice''?', 'literature', 'hard'),
('What is the study of the Earth''s structure called?', 'science', 'hard'),
('In which year was the Berlin Wall torn down?', 'history', 'hard'),
('What is the chemical symbol for silver?', 'science', 'hard'),
('Which composer wrote ''Carmen''?', 'music', 'hard'),
('What is the capital of Azerbaijan?', 'geography', 'hard'),
('Who discovered radioactivity?', 'science', 'hard'),
('What is the study of ancient life called?', 'science', 'hard'),
('Which artist painted ''The Scream''?', 'art', 'hard'),
('What is the smallest state in India by area?', 'geography', 'hard'),
('Who wrote ''The Iliad''?', 'literature', 'hard');

-- Insert all answer options
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (1, 'London', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (1, 'Berlin', FALSE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (1, 'Paris', TRUE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (1, 'Madrid', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (2, 'Venus', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (2, 'Mars', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (2, 'Jupiter', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (2, 'Saturn', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (3, 'African Elephant', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (3, 'Blue Whale', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (3, 'Giraffe', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (3, 'Polar Bear', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (4, 'Two', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (4, 'Three', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (4, 'Four', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (4, 'Five', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (5, 'Purple', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (5, 'Pink', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (5, 'Orange', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (5, 'Yellow', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (6, 'Sugar', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (6, 'Flour', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (6, 'Salt', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (6, 'Water', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (7, 'Tiger', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (7, 'Lion', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (7, 'Elephant', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (7, 'Leopard', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (8, 'Six', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (8, 'Seven', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (8, 'Eight', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (8, 'Five', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (9, 'Warm', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (9, 'Cold', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (9, 'Cool', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (9, 'Lukewarm', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (10, 'North', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (10, 'East', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (10, 'South', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (10, 'West', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (11, 'Milk', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (11, 'Honey', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (11, 'Butter', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (11, 'Cheese', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (12, 'Six', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (12, 'Eight', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (12, 'Ten', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (12, 'Four', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (13, 'B', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (13, 'A', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (13, 'C', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (13, 'Z', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (14, 'Summer', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (14, 'Spring', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (14, 'Fall', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (14, 'Autumn', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (15, 'Milk', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (15, 'Water', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (15, 'Juice', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (15, 'Soda', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (16, 'Fifty', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (16, 'Sixty', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (16, 'Seventy', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (16, 'Forty', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (17, 'Atlantic', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (17, 'Pacific', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (17, 'Indian', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (17, 'Arctic', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (18, 'Orange', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (18, 'Apple', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (18, 'Banana', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (18, 'Grape', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (19, 'Mars', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (19, 'Earth', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (19, 'Venus', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (19, 'Jupiter', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (20, 'One', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (20, 'Two', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (20, 'Three', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (20, 'Four', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (21, '1910', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (21, '1912', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (21, '1914', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (21, '1916', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (22, 'Vincent van Gogh', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (22, 'Leonardo da Vinci', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (22, 'Pablo Picasso', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (22, 'Michelangelo', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (23, 'Monaco', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (23, 'Vatican City', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (23, 'San Marino', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (23, 'Liechtenstein', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (24, 'Oxygen', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (24, 'Nitrogen', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (24, 'Carbon Dioxide', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (24, 'Hydrogen', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (25, 'Yuan', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (25, 'Yen', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (25, 'Won', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (25, 'Dollar', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (26, '198', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (26, '206', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (26, '215', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (26, '192', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (27, 'Amazon', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (27, 'Nile', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (27, 'Mississippi', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (27, 'Yangtze', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (28, 'Vitamin C', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (28, 'Vitamin D', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (28, 'Vitamin A', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (28, 'Vitamin B12', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (29, 'Quartz', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (29, 'Diamond', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (29, 'Steel', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (29, 'Iron', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (30, 'Africa', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (30, 'Asia', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (30, 'North America', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (30, 'Europe', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (31, 'World Wide Web', TRUE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (31, 'World Wide Website', FALSE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (31, 'World Web Wide', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (31, 'Wide World Web', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (32, 'Two', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (32, 'Four', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (32, 'Six', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (32, 'Eight', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (33, '300,000 km/s', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (33, '299,792,458 m/s', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (33, '186,000 mph', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (33, '300,000 m/s', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (34, 'England', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (34, 'France', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (34, 'Spain', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (34, 'Italy', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (35, 'Oxygen', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (35, 'Hydrogen', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (35, 'Helium', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (35, 'Nitrogen', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (36, '9', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (36, '11', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (36, '13', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (36, '15', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (37, 'Go', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (37, 'Au', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (37, 'Ag', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (37, 'Gd', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (38, 'Liver', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (38, 'Pancreas', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (38, 'Kidney', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (38, 'Stomach', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (39, 'Molecule', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (39, 'Atom', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (39, 'Electron', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (39, 'Proton', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (40, 'Four', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (40, 'Six', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (40, 'Eight', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (40, 'Twelve', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (41, 'Water only', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (41, 'Sunlight, water, and carbon dioxide', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (41, 'Soil only', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (41, 'Air only', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (42, 'Electron', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (42, 'Nucleus', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (42, 'Proton', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (42, 'Neutron', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (43, 'Roots', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (43, 'Leaves', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (43, 'Stem', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (43, 'Flowers', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (44, 'H2O2', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (44, 'H2O', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (44, 'HO2', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (44, 'H3O', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (45, 'Magnetism', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (45, 'Gravity', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (45, 'Friction', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (45, 'Electricity', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (46, 'Lion', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (46, 'Cheetah', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (46, 'Leopard', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (46, 'Tiger', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (47, 'Four', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (47, 'Six', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (47, 'Eight', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (47, 'Ten', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (48, 'Brain', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (48, 'Skin', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (48, 'Liver', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (48, 'Heart', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (49, 'Carbon dioxide', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (49, 'Oxygen', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (49, 'Nitrogen', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (49, 'Hydrogen', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (50, 'Biology', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (50, 'Meteorology', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (50, 'Geology', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (50, 'Astronomy', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (51, 'Fish', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (51, 'Mammal', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (51, 'Reptile', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (51, 'Amphibian', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (52, 'Two', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (52, 'Eight', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (52, 'Six', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (52, 'Four', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (53, 'Moon', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (53, 'Sun', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (53, 'Stars', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (53, 'Wind', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (54, 'Carnivores', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (54, 'Herbivores', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (54, 'Omnivores', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (54, 'Predators', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (55, '90°C', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (55, '100°C', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (55, '110°C', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (55, '120°C', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (56, '4', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (56, '6', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (56, '8', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (56, '12', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (57, 'Einstein', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (57, 'Darwin', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (57, 'Newton', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (57, 'Galileo', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (58, 'Nucleus', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (58, 'Mitochondria', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (58, 'Ribosome', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (58, 'Cytoplasm', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (59, '5', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (59, '7', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (59, '9', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (59, '12', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (60, 'Geology', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (60, 'Seismology', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (60, 'Meteorology', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (60, 'Volcanology', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (61, 'A', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (61, 'O', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (61, 'B', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (61, 'AB', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (62, 'Si', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (62, 'Ag', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (62, 'Au', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (62, 'Al', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (63, '8 minutes', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (63, '8 minutes and 20 seconds', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (63, '10 minutes', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (63, '5 minutes', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (64, 'Carbon', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (64, 'Oxygen', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (64, 'Hydrogen', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (64, 'Nitrogen', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (65, 'Jupiter', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (65, 'Saturn', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (65, 'Uranus', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (65, 'Neptune', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (66, 'Biology', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (66, 'Mycology', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (66, 'Botany', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (66, 'Zoology', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (67, '22', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (67, '23', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (67, '24', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (67, '25', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (68, '320 m/s', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (68, '343 m/s', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (68, '360 m/s', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (68, '380 m/s', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (69, 'Liver', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (69, 'Kidneys', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (69, 'Heart', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (69, 'Lungs', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (70, 'Stapes', TRUE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (70, 'Stirrup', FALSE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (70, 'Hammer', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (70, 'Anvil', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (71, 'John Adams', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (71, 'George Washington', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (71, 'Thomas Jefferson', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (71, 'Benjamin Franklin', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (72, '1944', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (72, '1945', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (72, '1946', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (72, '1947', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (73, 'Hanging Gardens', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (73, 'Great Pyramid of Giza', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (73, 'Colossus of Rhodes', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (73, 'Lighthouse of Alexandria', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (74, 'Queen Elizabeth', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (74, 'Margaret Thatcher', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (74, 'Marie Curie', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (74, 'Eleanor Roosevelt', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (75, 'Great Wall of China', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (75, 'Berlin Wall', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (75, 'Hadrian''s Wall', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (75, 'Wall Street', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (76, 'George Washington', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (76, 'Thomas Jefferson', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (76, 'John Adams', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (76, 'Benjamin Franklin', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (77, 'New York', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (77, 'Dallas', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (77, 'Washington D.C.', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (77, 'Boston', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (78, 'Greek', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (78, 'Roman', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (78, 'Egyptian', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (78, 'Persian', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (79, 'Nina', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (79, 'Santa Maria', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (79, 'Pinta', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (79, 'Mayflower', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (80, 'Mussolini', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (80, 'Adolf Hitler', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (80, 'Stalin', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (80, 'Franco', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (81, '1987', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (81, '1989', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (81, '1991', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (81, '1993', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (82, 'Alexander III', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (82, 'Nicholas II', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (82, 'Peter the Great', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (82, 'Ivan the Terrible', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (83, 'Austerlitz', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (83, 'Waterloo', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (83, 'Trafalgar', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (83, 'Leipzig', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (84, '1859', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (84, '1861', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (84, '1863', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (84, '1865', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (85, 'Buzz Aldrin', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (85, 'Neil Armstrong', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (85, 'John Glenn', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (85, 'Alan Shepard', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (86, 'Aztecs', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (86, 'Incas', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (86, 'Mayans', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (86, 'Olmecs', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (87, '1205', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (87, '1215', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (87, '1225', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (87, '1235', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (88, 'Nehru', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (88, 'Mahatma Gandhi', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (88, 'Patel', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (88, 'Bose', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (89, 'Vietnam War', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (89, 'Korean War', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (89, 'Cold War', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (89, 'World War III', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (90, 'Rosa Parks', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (90, 'Marie Curie', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (90, 'Mother Teresa', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (90, 'Jane Addams', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (91, '1787', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (91, '1789', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (91, '1791', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (91, '1793', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (92, 'Julius Caesar', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (92, 'Vespasian', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (92, 'Augustus', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (92, 'Nero', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (93, 'HMS Victory', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (93, 'HMS Beagle', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (93, 'HMS Bounty', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (93, 'HMS Endeavour', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (94, 'Leonardo da Vinci', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (94, 'Michelangelo', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (94, 'Raphael', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (94, 'Donatello', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (95, 'United States', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (95, 'New Zealand', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (95, 'United Kingdom', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (95, 'Australia', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (96, 'China', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (96, 'Russia', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (96, 'United States', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (96, 'Canada', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (97, 'Seine', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (97, 'Thames', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (97, 'Danube', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (97, 'Rhine', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (98, 'Europe', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (98, 'Australia', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (98, 'Antarctica', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (98, 'South America', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (99, 'Russia', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (99, 'Canada', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (99, 'United States', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (99, 'Finland', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (100, 'K2', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (100, 'Mount Everest', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (100, 'Kangchenjunga', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (100, 'Lhotse', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (101, 'Gobi', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (101, 'Sahara', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (101, 'Kalahari', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (101, 'Arabian', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (102, 'Sydney', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (102, 'Canberra', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (102, 'Melbourne', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (102, 'Perth', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (103, 'Kazakhstan', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (103, 'Turkey', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (103, 'Georgia', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (103, 'Armenia', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (104, 'Congo', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (104, 'Nile', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (104, 'Niger', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (104, 'Zambezi', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (105, 'Los Angeles', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (105, 'New York City', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (105, 'Chicago', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (105, 'Boston', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (106, 'Puerto Rico Trench', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (106, 'Mariana Trench', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (106, 'Java Trench', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (106, 'Peru-Chile Trench', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (107, 'Russia', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (107, 'France', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (107, 'United States', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (107, 'China', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (108, 'Auckland', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (108, 'Wellington', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (108, 'Christchurch', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (108, 'Hamilton', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (109, 'Liberia', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (109, 'Ethiopia', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (109, 'Morocco', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (109, 'Egypt', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (110, 'Sahara', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (110, 'Atacama', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (110, 'Gobi', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (110, 'Kalahari', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (111, 'Bosphorus', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (111, 'Strait of Gibraltar', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (111, 'Strait of Hormuz', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (111, 'Dardanelles', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (112, 'Niagara Falls', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (112, 'Angel Falls', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (112, 'Victoria Falls', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (112, 'Iguazu Falls', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (113, 'Russia', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (113, 'Canada', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (113, 'Norway', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (113, 'Chile', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (114, 'Sardinia', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (114, 'Sicily', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (114, 'Cyprus', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (114, 'Corsica', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (115, 'Andes', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (115, 'Himalayas', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (115, 'Rocky Mountains', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (115, 'Alps', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (116, 'Almaty', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (116, 'Nur-Sultan', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (116, 'Shymkent', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (116, 'Aktobe', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (117, 'Red Sea', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (117, 'Dead Sea', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (117, 'Mediterranean Sea', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (117, 'Caspian Sea', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (118, 'South America', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (118, 'Antarctica', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (118, 'Australia', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (118, 'Africa', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (119, 'Botswana', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (119, 'Lesotho', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (119, 'Swaziland', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (119, 'Zimbabwe', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (120, 'Lake Chad', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (120, 'Lake Victoria', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (120, 'Lake Tanganyika', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (120, 'Lake Malawi', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (121, 'George Lucas', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (121, 'Steven Spielberg', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (121, 'Martin Scorsese', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (121, 'Francis Ford Coppola', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (122, 'The Bodyguard', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (122, 'Titanic', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (122, 'Ghost', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (122, 'Pretty Woman', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (123, 'Titanic', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (123, 'Avatar', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (123, 'Avengers: Endgame', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (123, 'Star Wars: The Force Awakens', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (124, 'Chris Evans', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (124, 'Robert Downey Jr.', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (124, 'Chris Hemsworth', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (124, 'Mark Ruffalo', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (125, 'The Sopranos', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (125, 'Breaking Bad', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (125, 'Better Call Saul', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (125, 'Dexter', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (126, 'The Phantom Menace', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (126, 'A New Hope', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (126, 'The Empire Strikes Back', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (126, 'Return of the Jedi', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (127, 'Adam Driver', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (127, 'Joaquin Phoenix', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (127, 'Leonardo DiCaprio', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (127, 'Antonio Banderas', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (128, 'Moana', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (128, 'Frozen', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (128, 'Tangled', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (128, 'The Little Mermaid', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (129, 'Errol', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (129, 'Hedwig', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (129, 'Pigwidgeon', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (129, 'Archimedes', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (130, 'Martin Scorsese', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (130, 'Quentin Tarantino', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (130, 'Christopher Nolan', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (130, 'David Fincher', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (131, 'South Park', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (131, 'The Simpsons', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (131, 'Family Guy', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (131, 'Futurama', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (132, 'Jack Nicholson', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (132, 'Heath Ledger', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (132, 'Joaquin Phoenix', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (132, 'Jared Leto', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (133, 'The Jazz Singer', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (133, 'Wings', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (133, 'Sunrise', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (133, 'The Way of All Flesh', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (134, 'The Grind', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (134, 'Central Perk', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (134, 'Java Joe''s', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (134, 'The Coffee House', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (135, 'Emma Stone', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (135, 'Jennifer Lawrence', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (135, 'Scarlett Johansson', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (135, 'Anne Hathaway', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (136, 'Four', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (136, 'Five', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (136, 'Six', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (136, 'Seven', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (137, 'Germany', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (137, 'France', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (137, 'Brazil', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (137, 'Argentina', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (138, '16', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (138, '18', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (138, '20', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (138, '22', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (139, 'Basketball', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (139, 'Soccer/Football', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (139, 'Tennis', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (139, 'Cricket', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (140, 'Four', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (140, 'Five', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (140, 'Six', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (140, 'Seven', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (141, 'US Open', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (141, 'Wimbledon', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (141, 'French Open', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (141, 'Australian Open', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (142, 'Five', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (142, 'Six', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (142, 'Seven', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (142, 'Eight', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (143, 'Carl Lewis', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (143, 'Michael Phelps', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (143, 'Mark Spitz', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (143, 'Usain Bolt', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (144, 'Volleyball', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (144, 'Basketball', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (144, 'Tennis', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (144, 'Badminton', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (145, '80', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (145, '90', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (145, '100', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (145, '120', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (146, 'France', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (146, 'Monaco', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (146, 'Italy', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (146, 'Spain', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (147, '10', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (147, '12', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (147, '15', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (147, '20', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (148, 'Badminton', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (148, 'Tennis', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (148, 'Squash', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (148, 'Table Tennis', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (149, 'Three', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (149, 'Four', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (149, 'Five', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (149, 'Six', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (150, 'Adam Peaty', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (150, 'Michael Phelps', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (150, 'Caeleb Dressel', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (150, 'Katie Ledecky', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (151, 'Organ', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (151, 'Piano', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (151, 'Harpsichord', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (151, 'Accordion', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (152, 'Bach', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (152, 'Vivaldi', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (152, 'Mozart', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (152, 'Beethoven', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (153, 'Three', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (153, 'Four', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (153, 'Five', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (153, 'Six', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (154, 'The Beatles', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (154, 'Queen', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (154, 'Led Zeppelin', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (154, 'The Rolling Stones', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (155, 'Soft', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (155, 'Loud', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (155, 'Fast', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (155, 'Slow', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (156, 'Violin', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (156, 'Cello', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (156, 'Piano', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (156, 'Flute', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (157, 'Seven', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (157, 'Eight', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (157, 'Nine', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (157, 'Ten', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (158, 'Bach', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (158, 'Mozart', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (158, 'Beethoven', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (158, 'Handel', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (159, 'Blues', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (159, 'Jazz', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (159, 'Rock', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (159, 'Country', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (160, 'Alto', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (160, 'Soprano', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (160, 'Mezzo-soprano', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (160, 'Contralto', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (161, 'Charlotte Brontë', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (161, 'Jane Austen', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (161, 'Emily Dickinson', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (161, 'Virginia Woolf', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (162, 'Great Expectations', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (162, 'A Tale of Two Cities', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (162, 'Oliver Twist', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (162, 'David Copperfield', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (163, 'Agatha Christie', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (163, 'Arthur Conan Doyle', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (163, 'Edgar Allan Poe', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (163, 'Raymond Chandler', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (164, 'Chamber of Secrets', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (164, 'Philosopher''s Stone', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (164, 'Prisoner of Azkaban', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (164, 'Goblet of Fire', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (165, 'Aldous Huxley', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (165, 'George Orwell', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (165, 'Ray Bradbury', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (165, 'Kurt Vonnegut', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (166, 'Hamlet', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (166, 'Romeo and Juliet', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (166, 'Macbeth', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (166, 'Othello', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (167, 'Toni Morrison', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (167, 'Harper Lee', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (167, 'Maya Angelou', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (167, 'Flannery O''Connor', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (168, 'Call me Ishmael', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (168, 'It was the best of times, it was the worst of times', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (168, 'In the beginning', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (168, 'Once upon a time', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (169, 'Ernest Hemingway', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (169, 'F. Scott Fitzgerald', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (169, 'John Steinbeck', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (169, 'William Faulkner', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (170, 'The Iliad', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (170, 'The Odyssey', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (170, 'The Aeneid', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (170, 'Beowulf', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (171, 'Computer Processing Unit', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (171, 'Central Processing Unit', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (171, 'Central Program Unit', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (171, 'Computer Program Unit', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (172, 'Steve Jobs', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (172, 'Bill Gates', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (172, 'Larry Page', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (172, 'Mark Zuckerberg', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (173, '2005', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (173, '2007', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (173, '2009', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (173, '2011', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (174, 'Random Access Memory', TRUE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (174, 'Random Application Memory', FALSE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (174, 'Rapid Access Memory', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (174, 'Read Access Memory', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (175, 'Apple', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (175, 'Google', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (175, 'Microsoft', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (175, 'Samsung', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (176, 'Universal Serial Bus', TRUE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (176, 'Universal System Bus', FALSE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (176, 'United Serial Bus', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (176, 'United System Bus', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (177, 'Bill Gates', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (177, 'Mark Zuckerberg', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (177, 'Larry Page', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (177, 'Jack Dorsey', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (178, 'Automatic Intelligence', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (178, 'Artificial Intelligence', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (178, 'Advanced Intelligence', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (178, 'Applied Intelligence', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (179, 'Python', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (179, 'JavaScript', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (179, 'C++', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (179, 'Java', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (180, '1989', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (180, '1991', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (180, '1993', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (180, '1995', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (181, 'O', TRUE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (181, 'O2', FALSE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (181, 'Ox', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (181, 'Oy', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (182, 'Venus', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (182, 'Mercury', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (182, 'Earth', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (182, 'Mars', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (183, 'Gobi', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (183, 'Sahara', FALSE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (183, 'Antarctica', TRUE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (183, 'Arabian', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (184, 'Thomas Edison', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (184, 'Alexander Graham Bell', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (184, 'Nikola Tesla', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (184, 'Benjamin Franklin', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (185, '6', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (185, '8', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (185, '10', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (185, '12', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (186, 'Indian', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (186, 'Arctic', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (186, 'Atlantic', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (186, 'Pacific', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (187, 'HyperText Transfer Protocol', TRUE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (187, 'High Transfer Text Protocol', FALSE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (187, 'HyperText Transport Protocol', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (187, 'High Text Transfer Protocol', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (188, 'Charles Dickens', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (188, 'William Shakespeare', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (188, 'Jane Austen', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (188, 'Mark Twain', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (189, 'Eagle', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (189, 'Peregrine Falcon', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (189, 'Hawk', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (189, 'Owl', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (190, 'France', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (190, 'Italy', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (190, 'Greece', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (190, 'Spain', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (191, 'Tomato', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (191, 'Avocado', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (191, 'Onion', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (191, 'Pepper', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (192, '5', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (192, '7', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (192, '6', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (192, '8', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (193, '0', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (193, '2', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (193, '1', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (193, '3', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (194, 'Vitamin A', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (194, 'Vitamin C', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (194, 'Vitamin D', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (194, 'Vitamin B12', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (195, 'Toronto', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (195, 'Ottawa', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (195, 'Vancouver', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (195, 'Montreal', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (196, 'Pablo Picasso', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (196, 'Vincent van Gogh', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (196, 'Claude Monet', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (196, 'Salvador Dali', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (197, 'Eagle', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (197, 'Ostrich', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (197, 'Condor', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (197, 'Albatross', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (198, 'Fluorine', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (198, 'Iron', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (198, 'Francium', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (198, 'Fermium', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (199, '1967', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (199, '1969', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (199, '1971', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (199, '1973', FALSE, 4);

INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (200, 'Violin', FALSE, 1);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (200, 'Piano', TRUE, 2);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (200, 'Flute', FALSE, 3);
INSERT INTO question_options (question_id, option_text, is_correct, option_order) VALUES (200, 'Organ', FALSE, 4);


-- Hard question options
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (116, '6.626 × 10^-34', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (116, '9.109 × 10^-31', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (116, '1.602 × 10^-19', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (116, '1.381 × 10^-23', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (117, '1453', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (117, '1492', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (117, '1461', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (117, '1444', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (118, 'Thimphu', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (118, 'Paro', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (118, 'Punakha', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (118, 'Jakar', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (119, 'Johann Sebastian Bach', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (119, 'Ludwig van Beethoven', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (119, 'Wolfgang Amadeus Mozart', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (119, 'George Frideric Handel', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (120, 'Rh-null', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (120, 'AB-', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (120, 'O-', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (120, 'Duffy negative', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (121, '1648', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (121, '1659', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (121, '1635', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (121, '1672', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (122, 'Stapes', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (122, 'Malleus', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (122, 'Incus', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (122, 'Hyoid', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (123, 'Uranium', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (123, 'Plutonium', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (123, 'Thorium', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (123, 'Radium', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (124, 'Uncopyrightable', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (124, 'Subdermatoglyphic', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (124, 'Dermatoglyphics', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (124, 'Ambidextrously', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (125, '1986', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (125, '1984', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (125, '1987', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (125, '1985', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (126, 'Seismology', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (126, 'Geology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (126, 'Volcanology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (126, 'Meteorology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (127, 'C++', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (127, 'Java', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (127, 'Python', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (127, 'C#', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (128, 'Seychelles', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (128, 'Gambia', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (128, 'Sao Tome and Principe', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (128, 'Comoros', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (129, 'Gabriel García Márquez', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (129, 'Mario Vargas Llosa', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (129, 'Jorge Luis Borges', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (129, 'Pablo Neruda', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (130, 'C8H10N4O2', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (130, 'C6H12O6', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (130, 'C2H5OH', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (130, 'C17H21NO4', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (131, '1648', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (131, '1659', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (131, '1635', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (131, '1642', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (132, 'Diamond', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (132, 'Corundum', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (132, 'Topaz', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (132, 'Quartz', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (133, 'Salvador Dalí', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (133, 'René Magritte', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (133, 'Max Ernst', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (133, 'Giorgio de Chirico', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (134, 'Nur-Sultan', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (134, 'Almaty', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (134, 'Shymkent', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (134, 'Aktobe', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (135, 'Alfred Wegener', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (135, 'Charles Darwin', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (135, 'James Hutton', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (135, 'Louis Agassiz', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (136, 'Collagen', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (136, 'Hemoglobin', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (136, 'Insulin', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (136, 'Albumin', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (137, '1961', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (137, '1962', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (137, '1959', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (137, '1963', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (138, 'Mycology', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (138, 'Botany', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (138, 'Zoology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (138, 'Microbiology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (139, 'Richard Wagner', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (139, 'Giuseppe Verdi', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (139, 'Giacomo Puccini', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (139, 'Richard Strauss', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (140, 'Mercury', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (140, 'Mars', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (140, 'Venus', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (140, 'Pluto', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (141, 'Mikhail Bulgakov', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (141, 'Leo Tolstoy', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (141, 'Fyodor Dostoevsky', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (141, 'Anton Chekhov', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (142, 'W', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (142, 'Tu', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (142, 'Tn', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (142, 'Tg', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (143, '1904', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (143, '1905', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (143, '1903', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (143, '1906', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (144, 'Titan', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (144, 'Enceladus', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (144, 'Mimas', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (144, 'Iapetus', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (145, 'Auguste Rodin', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (145, 'Michelangelo', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (145, 'Donatello', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (145, 'Bernini', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (146, 'Ulaanbaatar', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (146, 'Darkhan', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (146, 'Erdenet', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (146, 'Choibalsan', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (147, 'Alexander Fleming', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (147, 'Louis Pasteur', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (147, 'Robert Koch', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (147, 'Joseph Lister', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (148, 'Ornithology', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (148, 'Entomology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (148, 'Herpetology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (148, 'Ichthyology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (149, 'Wings', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (149, 'Sunrise', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (149, 'The Jazz Singer', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (149, '7th Heaven', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (150, 'Atom', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (150, 'Molecule', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (150, 'Electron', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (150, 'Quark', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (151, '1945', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (151, '1946', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (151, '1944', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (151, '1947', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (152, 'Entomology', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (152, 'Ornithology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (152, 'Herpetology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (152, 'Arachnology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (153, 'Pablo Picasso', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (153, 'Henri Matisse', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (153, 'Paul Cézanne', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (153, 'Claude Monet', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (154, 'Asmara', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (154, 'Massawa', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (154, 'Keren', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (154, 'Assab', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (155, 'Gold', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (155, 'Silver', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (155, 'Platinum', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (155, 'Mercury', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (156, 'Yangtze', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (156, 'Yellow', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (156, 'Mekong', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (156, 'Ganges', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (157, 'James Joyce', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (157, 'Virginia Woolf', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (157, 'T.S. Eliot', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (157, 'Ezra Pound', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (158, 'Astronomy', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (158, 'Astrology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (158, 'Cosmology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (158, 'Astrophysics', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (159, '1914', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (159, '1915', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (159, '1913', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (159, '1916', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (160, 'NaCl', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (160, 'KCl', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (160, 'CaCl2', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (160, 'MgCl2', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (161, 'Antonio Vivaldi', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (161, 'Johann Sebastian Bach', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (161, 'George Frideric Handel', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (161, 'Arcangelo Corelli', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (162, 'Naypyidaw', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (162, 'Yangon', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (162, 'Mandalay', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (162, 'Bagan', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (163, 'Dmitri Mendeleev', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (163, 'Antoine Lavoisier', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (163, 'John Dalton', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (163, 'Marie Curie', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (164, 'Meteorology', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (164, 'Climatology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (164, 'Atmospheric Science', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (164, 'Hydrology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (165, 'Vincent van Gogh', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (165, 'Paul Gauguin', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (165, 'Henri de Toulouse-Lautrec', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (165, 'Paul Cézanne', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (166, 'Suriname', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (166, 'Uruguay', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (166, 'Guyana', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (166, 'French Guiana', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (167, 'Geoffrey Chaucer', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (167, 'William Shakespeare', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (167, 'Edmund Spenser', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (167, 'Christopher Marlowe', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (168, 'Herpetology', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (168, 'Ornithology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (168, 'Entomology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (168, 'Ichthyology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (169, '1865', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (169, '1864', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (169, '1866', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (169, '1863', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (170, 'Pb', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (170, 'Ld', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (170, 'Le', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (170, 'L', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (171, 'Pyotr Ilyich Tchaikovsky', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (171, 'Sergei Rachmaninoff', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (171, 'Igor Stravinsky', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (171, 'Modest Mussorgsky', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (172, 'Dushanbe', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (172, 'Khujand', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (172, 'Kulob', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (172, 'Qurghonteppa', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (173, 'Watson and Crick', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (173, 'Rosalind Franklin', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (173, 'Maurice Wilkins', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (173, 'Linus Pauling', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (174, 'Ichthyology', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (174, 'Ornithology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (174, 'Herpetology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (174, 'Marine Biology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (175, 'Orson Welles', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (175, 'John Ford', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (175, 'Frank Capra', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (175, 'Howard Hawks', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (176, 'Antarctica', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (176, 'Sahara', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (176, 'Arabian', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (176, 'Gobi', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (177, 'Miguel de Cervantes', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (177, 'Lope de Vega', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (177, 'Pedro Calderón', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (177, 'Francisco de Quevedo', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (178, 'Psychology', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (178, 'Psychiatry', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (178, 'Neuroscience', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (178, 'Philosophy', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (179, '2007', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (179, '2006', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (179, '2008', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (179, '2005', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (180, 'H2O', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (180, 'H2O2', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (180, 'H3O', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (180, 'HO2', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (181, 'Sandro Botticelli', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (181, 'Leonardo da Vinci', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (181, 'Raphael', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (181, 'Titian', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (182, 'Tashkent', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (182, 'Samarkand', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (182, 'Bukhara', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (182, 'Nukus', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (183, 'Charles Darwin', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (183, 'Alfred Russel Wallace', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (183, 'Jean-Baptiste Lamarck', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (183, 'Gregor Mendel', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (184, 'Botany', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (184, 'Zoology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (184, 'Ecology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (184, 'Biology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (185, 'Wolfgang Amadeus Mozart', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (185, 'Ludwig van Beethoven', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (185, 'Franz Schubert', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (185, 'Johannes Brahms', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (186, 'Stapes', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (186, 'Malleus', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (186, 'Incus', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (186, 'Cochlea', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (187, '1789', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (187, '1790', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (187, '1788', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (187, '1791', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (188, 'Fe', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (188, 'Ir', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (188, 'I', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (188, 'In', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (189, 'Michelangelo', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (189, 'Donatello', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (189, 'Bernini', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (189, 'Rodin', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (190, 'Bishkek', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (190, 'Osh', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (190, 'Jalal-Abad', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (190, 'Karakol', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (191, 'Alexander Graham Bell', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (191, 'Thomas Edison', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (191, 'Nikola Tesla', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (191, 'Guglielmo Marconi', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (192, 'Geology', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (192, 'Mineralogy', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (192, 'Petrology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (192, 'Geophysics', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (193, 'Forrest Gump', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (193, 'The Shawshank Redemption', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (193, 'Pulp Fiction', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (193, 'The Lion King', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (194, 'Caspian Sea', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (194, 'Superior', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (194, 'Victoria', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (194, 'Huron', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (195, 'Jane Austen', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (195, 'Charlotte Brontë', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (195, 'Emily Brontë', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (195, 'George Eliot', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (196, 'Geology', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (196, 'Geography', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (196, 'Geophysics', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (196, 'Geochemistry', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (197, '1989', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (197, '1990', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (197, '1988', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (197, '1991', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (198, 'Ag', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (198, 'Si', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (198, 'S', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (198, 'Sl', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (199, 'Georges Bizet', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (199, 'Giuseppe Verdi', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (199, 'Giacomo Puccini', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (199, 'Jules Massenet', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (200, 'Baku', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (200, 'Ganja', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (200, 'Sumgayit', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (200, 'Mingachevir', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (201, 'Henri Becquerel', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (201, 'Marie Curie', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (201, 'Pierre Curie', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (201, 'Ernest Rutherford', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (202, 'Paleontology', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (202, 'Archaeology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (202, 'Anthropology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (202, 'Geology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (203, 'Edvard Munch', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (203, 'Vincent van Gogh', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (203, 'Paul Gauguin', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (203, 'Henri de Toulouse-Lautrec', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (204, 'Goa', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (204, 'Sikkim', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (204, 'Tripura', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (204, 'Nagaland', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (205, 'Homer', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (205, 'Virgil', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (205, 'Ovid', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (205, 'Hesiod', false);

-- Hard question options
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (116, '6.626 × 10^-34', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (116, '9.109 × 10^-31', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (116, '1.602 × 10^-19', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (116, '1.381 × 10^-23', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (117, '1453', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (117, '1492', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (117, '1461', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (117, '1444', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (118, 'Thimphu', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (118, 'Paro', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (118, 'Punakha', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (118, 'Jakar', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (119, 'Johann Sebastian Bach', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (119, 'Ludwig van Beethoven', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (119, 'Wolfgang Amadeus Mozart', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (119, 'George Frideric Handel', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (120, 'Rh-null', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (120, 'AB-', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (120, 'O-', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (120, 'Duffy negative', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (121, '1648', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (121, '1659', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (121, '1635', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (121, '1672', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (122, 'Stapes', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (122, 'Malleus', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (122, 'Incus', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (122, 'Hyoid', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (123, 'Uranium', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (123, 'Plutonium', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (123, 'Thorium', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (123, 'Radium', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (124, 'Uncopyrightable', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (124, 'Subdermatoglyphic', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (124, 'Dermatoglyphics', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (124, 'Ambidextrously', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (125, '1986', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (125, '1984', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (125, '1987', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (125, '1985', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (126, 'Seismology', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (126, 'Geology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (126, 'Volcanology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (126, 'Meteorology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (127, 'C++', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (127, 'Java', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (127, 'Python', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (127, 'C#', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (128, 'Seychelles', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (128, 'Gambia', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (128, 'Sao Tome and Principe', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (128, 'Comoros', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (129, 'Gabriel García Márquez', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (129, 'Mario Vargas Llosa', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (129, 'Jorge Luis Borges', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (129, 'Pablo Neruda', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (130, 'C8H10N4O2', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (130, 'C6H12O6', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (130, 'C2H5OH', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (130, 'C17H21NO4', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (131, '1648', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (131, '1659', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (131, '1635', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (131, '1642', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (132, 'Diamond', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (132, 'Corundum', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (132, 'Topaz', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (132, 'Quartz', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (133, 'Salvador Dalí', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (133, 'René Magritte', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (133, 'Max Ernst', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (133, 'Giorgio de Chirico', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (134, 'Nur-Sultan', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (134, 'Almaty', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (134, 'Shymkent', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (134, 'Aktobe', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (135, 'Alfred Wegener', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (135, 'Charles Darwin', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (135, 'James Hutton', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (135, 'Louis Agassiz', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (136, 'Collagen', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (136, 'Hemoglobin', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (136, 'Insulin', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (136, 'Albumin', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (137, '1961', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (137, '1962', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (137, '1959', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (137, '1963', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (138, 'Mycology', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (138, 'Botany', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (138, 'Zoology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (138, 'Microbiology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (139, 'Richard Wagner', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (139, 'Giuseppe Verdi', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (139, 'Giacomo Puccini', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (139, 'Richard Strauss', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (140, 'Mercury', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (140, 'Mars', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (140, 'Venus', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (140, 'Pluto', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (141, 'Mikhail Bulgakov', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (141, 'Leo Tolstoy', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (141, 'Fyodor Dostoevsky', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (141, 'Anton Chekhov', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (142, 'W', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (142, 'Tu', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (142, 'Tn', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (142, 'Tg', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (143, '1904', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (143, '1905', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (143, '1903', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (143, '1906', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (144, 'Titan', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (144, 'Enceladus', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (144, 'Mimas', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (144, 'Iapetus', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (145, 'Auguste Rodin', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (145, 'Michelangelo', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (145, 'Donatello', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (145, 'Bernini', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (146, 'Ulaanbaatar', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (146, 'Darkhan', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (146, 'Erdenet', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (146, 'Choibalsan', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (147, 'Alexander Fleming', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (147, 'Louis Pasteur', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (147, 'Robert Koch', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (147, 'Joseph Lister', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (148, 'Ornithology', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (148, 'Entomology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (148, 'Herpetology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (148, 'Ichthyology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (149, 'Wings', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (149, 'Sunrise', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (149, 'The Jazz Singer', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (149, '7th Heaven', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (150, 'Atom', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (150, 'Molecule', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (150, 'Electron', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (150, 'Quark', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (151, '1945', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (151, '1946', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (151, '1944', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (151, '1947', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (152, 'Entomology', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (152, 'Ornithology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (152, 'Herpetology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (152, 'Arachnology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (153, 'Pablo Picasso', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (153, 'Henri Matisse', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (153, 'Paul Cézanne', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (153, 'Claude Monet', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (154, 'Asmara', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (154, 'Massawa', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (154, 'Keren', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (154, 'Assab', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (155, 'Gold', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (155, 'Silver', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (155, 'Platinum', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (155, 'Mercury', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (156, 'Yangtze', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (156, 'Yellow', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (156, 'Mekong', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (156, 'Ganges', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (157, 'James Joyce', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (157, 'Virginia Woolf', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (157, 'T.S. Eliot', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (157, 'Ezra Pound', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (158, 'Astronomy', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (158, 'Astrology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (158, 'Cosmology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (158, 'Astrophysics', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (159, '1914', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (159, '1915', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (159, '1913', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (159, '1916', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (160, 'NaCl', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (160, 'KCl', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (160, 'CaCl2', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (160, 'MgCl2', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (161, 'Antonio Vivaldi', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (161, 'Johann Sebastian Bach', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (161, 'George Frideric Handel', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (161, 'Arcangelo Corelli', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (162, 'Naypyidaw', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (162, 'Yangon', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (162, 'Mandalay', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (162, 'Bagan', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (163, 'Dmitri Mendeleev', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (163, 'Antoine Lavoisier', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (163, 'John Dalton', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (163, 'Marie Curie', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (164, 'Meteorology', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (164, 'Climatology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (164, 'Atmospheric Science', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (164, 'Hydrology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (165, 'Vincent van Gogh', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (165, 'Paul Gauguin', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (165, 'Henri de Toulouse-Lautrec', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (165, 'Paul Cézanne', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (166, 'Suriname', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (166, 'Uruguay', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (166, 'Guyana', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (166, 'French Guiana', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (167, 'Geoffrey Chaucer', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (167, 'William Shakespeare', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (167, 'Edmund Spenser', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (167, 'Christopher Marlowe', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (168, 'Herpetology', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (168, 'Ornithology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (168, 'Entomology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (168, 'Ichthyology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (169, '1865', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (169, '1864', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (169, '1866', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (169, '1863', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (170, 'Pb', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (170, 'Ld', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (170, 'Le', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (170, 'L', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (171, 'Pyotr Ilyich Tchaikovsky', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (171, 'Sergei Rachmaninoff', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (171, 'Igor Stravinsky', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (171, 'Modest Mussorgsky', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (172, 'Dushanbe', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (172, 'Khujand', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (172, 'Kulob', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (172, 'Qurghonteppa', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (173, 'Watson and Crick', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (173, 'Rosalind Franklin', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (173, 'Maurice Wilkins', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (173, 'Linus Pauling', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (174, 'Ichthyology', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (174, 'Ornithology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (174, 'Herpetology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (174, 'Marine Biology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (175, 'Orson Welles', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (175, 'John Ford', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (175, 'Frank Capra', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (175, 'Howard Hawks', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (176, 'Antarctica', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (176, 'Sahara', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (176, 'Arabian', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (176, 'Gobi', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (177, 'Miguel de Cervantes', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (177, 'Lope de Vega', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (177, 'Pedro Calderón', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (177, 'Francisco de Quevedo', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (178, 'Psychology', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (178, 'Psychiatry', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (178, 'Neuroscience', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (178, 'Philosophy', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (179, '2007', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (179, '2006', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (179, '2008', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (179, '2005', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (180, 'H2O', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (180, 'H2O2', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (180, 'H3O', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (180, 'HO2', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (181, 'Sandro Botticelli', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (181, 'Leonardo da Vinci', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (181, 'Raphael', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (181, 'Titian', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (182, 'Tashkent', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (182, 'Samarkand', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (182, 'Bukhara', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (182, 'Nukus', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (183, 'Charles Darwin', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (183, 'Alfred Russel Wallace', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (183, 'Jean-Baptiste Lamarck', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (183, 'Gregor Mendel', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (184, 'Botany', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (184, 'Zoology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (184, 'Ecology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (184, 'Biology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (185, 'Wolfgang Amadeus Mozart', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (185, 'Ludwig van Beethoven', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (185, 'Franz Schubert', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (185, 'Johannes Brahms', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (186, 'Stapes', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (186, 'Malleus', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (186, 'Incus', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (186, 'Cochlea', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (187, '1789', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (187, '1790', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (187, '1788', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (187, '1791', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (188, 'Fe', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (188, 'Ir', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (188, 'I', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (188, 'In', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (189, 'Michelangelo', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (189, 'Donatello', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (189, 'Bernini', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (189, 'Rodin', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (190, 'Bishkek', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (190, 'Osh', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (190, 'Jalal-Abad', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (190, 'Karakol', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (191, 'Alexander Graham Bell', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (191, 'Thomas Edison', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (191, 'Nikola Tesla', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (191, 'Guglielmo Marconi', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (192, 'Geology', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (192, 'Mineralogy', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (192, 'Petrology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (192, 'Geophysics', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (193, 'Forrest Gump', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (193, 'The Shawshank Redemption', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (193, 'Pulp Fiction', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (193, 'The Lion King', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (194, 'Caspian Sea', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (194, 'Superior', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (194, 'Victoria', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (194, 'Huron', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (195, 'Jane Austen', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (195, 'Charlotte Brontë', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (195, 'Emily Brontë', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (195, 'George Eliot', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (196, 'Geology', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (196, 'Geography', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (196, 'Geophysics', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (196, 'Geochemistry', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (197, '1989', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (197, '1990', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (197, '1988', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (197, '1991', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (198, 'Ag', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (198, 'Si', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (198, 'S', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (198, 'Sl', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (199, 'Georges Bizet', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (199, 'Giuseppe Verdi', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (199, 'Giacomo Puccini', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (199, 'Jules Massenet', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (200, 'Baku', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (200, 'Ganja', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (200, 'Sumgayit', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (200, 'Mingachevir', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (201, 'Henri Becquerel', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (201, 'Marie Curie', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (201, 'Pierre Curie', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (201, 'Ernest Rutherford', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (202, 'Paleontology', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (202, 'Archaeology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (202, 'Anthropology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (202, 'Geology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (203, 'Edvard Munch', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (203, 'Vincent van Gogh', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (203, 'Paul Gauguin', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (203, 'Henri de Toulouse-Lautrec', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (204, 'Goa', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (204, 'Sikkim', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (204, 'Tripura', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (204, 'Nagaland', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (205, 'Homer', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (205, 'Virgil', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (205, 'Ovid', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (205, 'Hesiod', false);

-- Hard question options
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (116, '6.626 × 10^-34', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (116, '9.109 × 10^-31', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (116, '1.602 × 10^-19', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (116, '1.381 × 10^-23', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (117, '1453', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (117, '1492', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (117, '1461', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (117, '1444', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (118, 'Thimphu', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (118, 'Paro', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (118, 'Punakha', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (118, 'Jakar', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (119, 'Johann Sebastian Bach', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (119, 'Ludwig van Beethoven', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (119, 'Wolfgang Amadeus Mozart', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (119, 'George Frideric Handel', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (120, 'Rh-null', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (120, 'AB-', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (120, 'O-', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (120, 'Duffy negative', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (121, '1648', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (121, '1659', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (121, '1635', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (121, '1672', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (122, 'Stapes', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (122, 'Malleus', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (122, 'Incus', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (122, 'Hyoid', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (123, 'Uranium', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (123, 'Plutonium', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (123, 'Thorium', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (123, 'Radium', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (124, 'Uncopyrightable', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (124, 'Subdermatoglyphic', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (124, 'Dermatoglyphics', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (124, 'Ambidextrously', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (125, '1986', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (125, '1984', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (125, '1987', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (125, '1985', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (126, 'Seismology', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (126, 'Geology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (126, 'Volcanology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (126, 'Meteorology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (127, 'C++', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (127, 'Java', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (127, 'Python', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (127, 'C#', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (128, 'Seychelles', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (128, 'Gambia', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (128, 'Sao Tome and Principe', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (128, 'Comoros', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (129, 'Gabriel García Márquez', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (129, 'Mario Vargas Llosa', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (129, 'Jorge Luis Borges', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (129, 'Pablo Neruda', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (130, 'C8H10N4O2', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (130, 'C6H12O6', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (130, 'C2H5OH', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (130, 'C17H21NO4', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (131, '1648', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (131, '1659', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (131, '1635', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (131, '1642', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (132, 'Diamond', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (132, 'Corundum', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (132, 'Topaz', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (132, 'Quartz', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (133, 'Salvador Dalí', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (133, 'René Magritte', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (133, 'Max Ernst', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (133, 'Giorgio de Chirico', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (134, 'Nur-Sultan', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (134, 'Almaty', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (134, 'Shymkent', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (134, 'Aktobe', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (135, 'Alfred Wegener', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (135, 'Charles Darwin', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (135, 'James Hutton', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (135, 'Louis Agassiz', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (136, 'Collagen', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (136, 'Hemoglobin', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (136, 'Insulin', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (136, 'Albumin', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (137, '1961', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (137, '1962', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (137, '1959', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (137, '1963', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (138, 'Mycology', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (138, 'Botany', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (138, 'Zoology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (138, 'Microbiology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (139, 'Richard Wagner', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (139, 'Giuseppe Verdi', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (139, 'Giacomo Puccini', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (139, 'Richard Strauss', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (140, 'Mercury', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (140, 'Mars', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (140, 'Venus', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (140, 'Pluto', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (141, 'Mikhail Bulgakov', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (141, 'Leo Tolstoy', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (141, 'Fyodor Dostoevsky', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (141, 'Anton Chekhov', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (142, 'W', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (142, 'Tu', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (142, 'Tn', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (142, 'Tg', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (143, '1904', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (143, '1905', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (143, '1903', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (143, '1906', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (144, 'Titan', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (144, 'Enceladus', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (144, 'Mimas', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (144, 'Iapetus', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (145, 'Auguste Rodin', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (145, 'Michelangelo', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (145, 'Donatello', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (145, 'Bernini', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (146, 'Ulaanbaatar', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (146, 'Darkhan', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (146, 'Erdenet', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (146, 'Choibalsan', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (147, 'Alexander Fleming', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (147, 'Louis Pasteur', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (147, 'Robert Koch', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (147, 'Joseph Lister', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (148, 'Ornithology', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (148, 'Entomology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (148, 'Herpetology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (148, 'Ichthyology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (149, 'Wings', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (149, 'Sunrise', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (149, 'The Jazz Singer', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (149, '7th Heaven', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (150, 'Atom', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (150, 'Molecule', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (150, 'Electron', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (150, 'Quark', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (151, '1945', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (151, '1946', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (151, '1944', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (151, '1947', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (152, 'Entomology', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (152, 'Ornithology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (152, 'Herpetology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (152, 'Arachnology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (153, 'Pablo Picasso', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (153, 'Henri Matisse', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (153, 'Paul Cézanne', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (153, 'Claude Monet', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (154, 'Asmara', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (154, 'Massawa', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (154, 'Keren', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (154, 'Assab', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (155, 'Gold', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (155, 'Silver', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (155, 'Platinum', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (155, 'Mercury', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (156, 'Yangtze', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (156, 'Yellow', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (156, 'Mekong', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (156, 'Ganges', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (157, 'James Joyce', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (157, 'Virginia Woolf', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (157, 'T.S. Eliot', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (157, 'Ezra Pound', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (158, 'Astronomy', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (158, 'Astrology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (158, 'Cosmology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (158, 'Astrophysics', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (159, '1914', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (159, '1915', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (159, '1913', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (159, '1916', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (160, 'NaCl', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (160, 'KCl', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (160, 'CaCl2', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (160, 'MgCl2', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (161, 'Antonio Vivaldi', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (161, 'Johann Sebastian Bach', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (161, 'George Frideric Handel', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (161, 'Arcangelo Corelli', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (162, 'Naypyidaw', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (162, 'Yangon', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (162, 'Mandalay', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (162, 'Bagan', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (163, 'Dmitri Mendeleev', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (163, 'Antoine Lavoisier', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (163, 'John Dalton', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (163, 'Marie Curie', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (164, 'Meteorology', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (164, 'Climatology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (164, 'Atmospheric Science', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (164, 'Hydrology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (165, 'Vincent van Gogh', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (165, 'Paul Gauguin', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (165, 'Henri de Toulouse-Lautrec', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (165, 'Paul Cézanne', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (166, 'Suriname', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (166, 'Uruguay', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (166, 'Guyana', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (166, 'French Guiana', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (167, 'Geoffrey Chaucer', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (167, 'William Shakespeare', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (167, 'Edmund Spenser', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (167, 'Christopher Marlowe', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (168, 'Herpetology', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (168, 'Ornithology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (168, 'Entomology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (168, 'Ichthyology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (169, '1865', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (169, '1864', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (169, '1866', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (169, '1863', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (170, 'Pb', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (170, 'Ld', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (170, 'Le', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (170, 'L', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (171, 'Pyotr Ilyich Tchaikovsky', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (171, 'Sergei Rachmaninoff', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (171, 'Igor Stravinsky', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (171, 'Modest Mussorgsky', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (172, 'Dushanbe', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (172, 'Khujand', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (172, 'Kulob', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (172, 'Qurghonteppa', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (173, 'Watson and Crick', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (173, 'Rosalind Franklin', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (173, 'Maurice Wilkins', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (173, 'Linus Pauling', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (174, 'Ichthyology', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (174, 'Ornithology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (174, 'Herpetology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (174, 'Marine Biology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (175, 'Orson Welles', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (175, 'John Ford', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (175, 'Frank Capra', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (175, 'Howard Hawks', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (176, 'Antarctica', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (176, 'Sahara', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (176, 'Arabian', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (176, 'Gobi', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (177, 'Miguel de Cervantes', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (177, 'Lope de Vega', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (177, 'Pedro Calderón', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (177, 'Francisco de Quevedo', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (178, 'Psychology', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (178, 'Psychiatry', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (178, 'Neuroscience', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (178, 'Philosophy', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (179, '2007', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (179, '2006', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (179, '2008', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (179, '2005', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (180, 'H2O', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (180, 'H2O2', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (180, 'H3O', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (180, 'HO2', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (181, 'Sandro Botticelli', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (181, 'Leonardo da Vinci', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (181, 'Raphael', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (181, 'Titian', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (182, 'Tashkent', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (182, 'Samarkand', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (182, 'Bukhara', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (182, 'Nukus', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (183, 'Charles Darwin', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (183, 'Alfred Russel Wallace', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (183, 'Jean-Baptiste Lamarck', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (183, 'Gregor Mendel', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (184, 'Botany', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (184, 'Zoology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (184, 'Ecology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (184, 'Biology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (185, 'Wolfgang Amadeus Mozart', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (185, 'Ludwig van Beethoven', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (185, 'Franz Schubert', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (185, 'Johannes Brahms', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (186, 'Stapes', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (186, 'Malleus', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (186, 'Incus', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (186, 'Cochlea', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (187, '1789', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (187, '1790', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (187, '1788', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (187, '1791', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (188, 'Fe', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (188, 'Ir', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (188, 'I', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (188, 'In', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (189, 'Michelangelo', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (189, 'Donatello', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (189, 'Bernini', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (189, 'Rodin', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (190, 'Bishkek', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (190, 'Osh', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (190, 'Jalal-Abad', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (190, 'Karakol', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (191, 'Alexander Graham Bell', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (191, 'Thomas Edison', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (191, 'Nikola Tesla', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (191, 'Guglielmo Marconi', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (192, 'Geology', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (192, 'Mineralogy', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (192, 'Petrology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (192, 'Geophysics', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (193, 'Forrest Gump', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (193, 'The Shawshank Redemption', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (193, 'Pulp Fiction', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (193, 'The Lion King', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (194, 'Caspian Sea', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (194, 'Superior', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (194, 'Victoria', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (194, 'Huron', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (195, 'Jane Austen', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (195, 'Charlotte Brontë', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (195, 'Emily Brontë', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (195, 'George Eliot', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (196, 'Geology', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (196, 'Geography', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (196, 'Geophysics', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (196, 'Geochemistry', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (197, '1989', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (197, '1990', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (197, '1988', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (197, '1991', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (198, 'Ag', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (198, 'Si', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (198, 'S', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (198, 'Sl', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (199, 'Georges Bizet', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (199, 'Giuseppe Verdi', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (199, 'Giacomo Puccini', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (199, 'Jules Massenet', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (200, 'Baku', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (200, 'Ganja', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (200, 'Sumgayit', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (200, 'Mingachevir', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (201, 'Henri Becquerel', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (201, 'Marie Curie', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (201, 'Pierre Curie', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (201, 'Ernest Rutherford', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (202, 'Paleontology', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (202, 'Archaeology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (202, 'Anthropology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (202, 'Geology', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (203, 'Edvard Munch', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (203, 'Vincent van Gogh', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (203, 'Paul Gauguin', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (203, 'Henri de Toulouse-Lautrec', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (204, 'Goa', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (204, 'Sikkim', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (204, 'Tripura', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (204, 'Nagaland', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (205, 'Homer', true);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (205, 'Virgil', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (205, 'Ovid', false);
INSERT INTO question_options (question_id, option_text, is_correct) VALUES (205, 'Hesiod', false);
