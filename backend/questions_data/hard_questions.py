"""Hard difficulty trivia questions.

This module contains hard difficulty questions for the trivia game.
Total: 257 questions

Add new hard questions here in the following format:
{
    "text": "What is the question?",
    "category": "Category Name",
    "correct": "Correct Answer",
    "wrong": ["Wrong Answer 1", "Wrong Answer 2", "Wrong Answer 3"]
}
"""

HARD_QUESTIONS = [
    {
        "text": 'What design pattern ensures a class has only one instance?',
        "category": 'Coding',
        "correct": 'Singleton',
        "wrong": ['Factory', 'Observer', 'Prototype']
    },
    {
        "text": 'Which Big O notation represents logarithmic time complexity?',
        "category": 'Coding',
        "correct": 'O(log n)',
        "wrong": ['O(n)', 'O(n²)', 'O(1)']
    },
    {
        "text": 'What does SOLID stand for in object-oriented programming?',
        "category": 'Coding',
        "correct": 'Single responsibility, Open-closed, Liskov substitution, Interface segregation, Dependency inversion',
        "wrong": ['Simple, Optimal, Logical, Integrated, Dynamic', 'Structured, Object-based, Linear, Iterative, Declarative', 'Sorted, Organized, Linked, Indexed, Distributed']
    },
    {
        "text": 'Which algorithm is used for finding the shortest path in a graph?',
        "category": 'Coding',
        "correct": "Dijkstra's Algorithm",
        "wrong": ['Bubble Sort', 'Binary Search', 'Merge Sort']
    },
    {
        "text": 'What is a closure in JavaScript?',
        "category": 'Coding',
        "correct": 'A function that has access to variables in its outer scope',
        "wrong": ['A method to close database connections', 'A way to end a program', 'A type of loop']
    },
    {
        "text": 'What does REST stand for in API design?',
        "category": 'Coding',
        "correct": 'Representational State Transfer',
        "wrong": ['Remote Execution State Transfer', 'Rapid Embedded System Technology', 'Resource Exchange System Type']
    },
    {
        "text": 'Which data structure uses LIFO (Last In First Out)?',
        "category": 'Coding',
        "correct": 'Stack',
        "wrong": ['Queue', 'Array', 'Tree']
    },
    {
        "text": 'What is the purpose of a mutex in concurrent programming?',
        "category": 'Coding',
        "correct": 'Mutual exclusion to prevent race conditions',
        "wrong": ['Multiple execution threads', 'Memory utilization tracking', 'Multi-user text interface']
    },
    {
        "text": 'Which sorting algorithm has the best average-case time complexity?',
        "category": 'Coding',
        "correct": 'Quick Sort',
        "wrong": ['Bubble Sort', 'Selection Sort', 'Insertion Sort']
    },
    {
        "text": 'What is dependency injection?',
        "category": 'Coding',
        "correct": 'Passing dependencies to a class rather than creating them internally',
        "wrong": ['Injecting malicious code into dependencies', 'Adding new packages to a project', 'Removing unused imports']
    },
    {
        "text": 'What does CAP theorem stand for in distributed systems?',
        "category": 'Coding',
        "correct": 'Consistency, Availability, Partition tolerance',
        "wrong": ['Capacity, Availability, Performance', 'Cache, API, Protocol', 'Cluster, Application, Processing']
    },
    {
        "text": 'Which HTTP method is idempotent?',
        "category": 'Coding',
        "correct": 'PUT',
        "wrong": ['POST', 'PATCH', 'CONNECT']
    },
    {
        "text": 'What is polymorphism in OOP?',
        "category": 'Coding',
        "correct": 'Objects of different types can be accessed through the same interface',
        "wrong": ['Creating multiple instances of a class', 'Having many parameters in a function', 'Using different programming languages']
    },
    {
        "text": 'What is the purpose of a hash table?',
        "category": 'Coding',
        "correct": 'Fast key-value lookups in O(1) average time',
        "wrong": ['Sorting data alphabetically', 'Storing passwords securely', 'Compressing data']
    },
    {
        "text": 'What does TDD stand for?',
        "category": 'Coding',
        "correct": 'Test-Driven Development',
        "wrong": ['Technical Design Document', 'Time-Delayed Deployment', 'Task Definition Database']
    },
    {
        "text": 'Which design pattern allows creating objects without specifying exact classes?',
        "category": 'Coding',
        "correct": 'Factory Pattern',
        "wrong": ['Observer Pattern', 'Strategy Pattern', 'Decorator Pattern']
    },
    {
        "text": 'What is a race condition?',
        "category": 'Coding',
        "correct": 'When multiple threads access shared data simultaneously',
        "wrong": ['When code runs too fast', 'When loops compete for resources', 'When functions return before completion']
    },
    {
        "text": 'What is the difference between SQL and NoSQL databases?',
        "category": 'Coding',
        "correct": 'SQL uses structured tables, NoSQL uses flexible document/key-value stores',
        "wrong": ['SQL is faster than NoSQL', "NoSQL doesn't support queries", 'SQL is only for small databases']
    },
    {
        "text": 'What is the purpose of Git rebase?',
        "category": 'Coding',
        "correct": 'Reapply commits on top of another base tip',
        "wrong": ['Delete the repository', 'Reset all changes', 'Rename branches']
    },
    {
        "text": 'What is memoization?',
        "category": 'Coding',
        "correct": 'Caching results of expensive function calls',
        "wrong": ['Writing documentation', 'Remembering variable names', 'Creating memory dumps']
    },
    {
        "text": 'What does ACID stand for in database transactions?',
        "category": 'Coding',
        "correct": 'Atomicity, Consistency, Isolation, Durability',
        "wrong": ['Application, Cache, Index, Data', 'Async, Concurrent, Independent, Distributed', 'Access, Create, Insert, Delete']
    },
    {
        "text": 'What is a deadlock in concurrent programming?',
        "category": 'Coding',
        "correct": 'Two or more processes waiting for each other to release resources',
        "wrong": ['A crashed program', 'A locked database', 'A frozen user interface']
    },
    {
        "text": 'What is the Observer design pattern used for?',
        "category": 'Coding',
        "correct": 'Notifying multiple objects when state changes',
        "wrong": ['Monitoring system performance', 'Watching for security threats', 'Tracking user behavior']
    },
    {
        "text": 'What is the purpose of Docker containers?',
        "category": 'Coding',
        "correct": 'Package applications with dependencies for consistent deployment',
        "wrong": ['Store database backups', 'Encrypt sensitive data', 'Monitor application logs']
    },
    {
        "text": 'What is a JWT?',
        "category": 'Coding',
        "correct": 'JSON Web Token for authentication',
        "wrong": ['JavaScript Web Template', 'Java Web Technology', 'Joint Web Transport']
    },
    {
        "text": 'What is the difference between undefined and null in JavaScript?',
        "category": 'Coding',
        "correct": 'undefined means not assigned, null means intentionally empty',
        "wrong": ['They are exactly the same', 'null is an error, undefined is not', 'undefined is a string, null is a number']
    },
    {
        "text": 'What is continuous integration (CI)?',
        "category": 'Coding',
        "correct": 'Automatically merging and testing code changes frequently',
        "wrong": ['Manually reviewing all code', 'Deploying once a month', 'Integrating third-party APIs']
    },
    {
        "text": 'What is the purpose of a load balancer?',
        "category": 'Coding',
        "correct": 'Distribute network traffic across multiple servers',
        "wrong": ['Balance the CPU load on a single server', 'Monitor server health', 'Compress network data']
    },
    {
        "text": 'What is GraphQL?',
        "category": 'Coding',
        "correct": 'A query language for APIs',
        "wrong": ['A graphics library', 'A database type', 'A programming language']
    },
    {
        "text": "What does 'sharding' mean in database design?",
        "category": 'Coding',
        "correct": 'Splitting data across multiple database servers',
        "wrong": ['Deleting old data', 'Encrypting database contents', 'Creating database backups']
    },
    {
        "text": 'What year did the Berlin Wall fall?',
        "category": 'General',
        "correct": '1989',
        "wrong": ['1987', '1991', '1985']
    },
    {
        "text": 'Who painted the Sistine Chapel ceiling?',
        "category": 'General',
        "correct": 'Michelangelo',
        "wrong": ['Leonardo da Vinci', 'Raphael', 'Donatello']
    },
    {
        "text": 'What is the speed of light in a vacuum?',
        "category": 'General',
        "correct": '299,792,458 m/s',
        "wrong": ['300,000,000 m/s', '250,000,000 m/s', '350,000,000 m/s']
    },
    {
        "text": 'In what year did World War II end?',
        "category": 'General',
        "correct": '1945',
        "wrong": ['1944', '1946', '1943']
    },
    {
        "text": 'What is the largest planet in our solar system?',
        "category": 'General',
        "correct": 'Jupiter',
        "wrong": ['Saturn', 'Neptune', 'Uranus']
    },
    {
        "text": 'What is the square root of 144?',
        "category": 'General',
        "correct": '12',
        "wrong": ['11', '13', '14']
    },
    {
        "text": 'What language is spoken in Brazil?',
        "category": 'General',
        "correct": 'Portuguese',
        "wrong": ['Spanish', 'French', 'Italian']
    },
    {
        "text": 'How many bones are in the human body?',
        "category": 'General',
        "correct": '206',
        "wrong": ['205', '207', '210']
    },
    {
        "text": "Who wrote 'Romeo and Juliet'?",
        "category": 'General',
        "correct": 'William Shakespeare',
        "wrong": ['Charles Dickens', 'Mark Twain', 'Jane Austen']
    },
    {
        "text": 'Who discovered penicillin?',
        "category": 'General',
        "correct": 'Alexander Fleming',
        "wrong": ['Louis Pasteur', 'Marie Curie', 'Jonas Salk']
    },
    {
        "text": 'How many planets are in our solar system?',
        "category": 'General',
        "correct": '8',
        "wrong": ['9', '7', '10']
    },
    {
        "text": 'Who directed Pulp Fiction?',
        "category": 'Pop Culture',
        "correct": 'Quentin Tarantino',
        "wrong": ['Martin Scorsese', 'Steven Spielberg', 'Christopher Nolan']
    },
    {
        "text": 'What is the best-selling album of all time?',
        "category": 'Pop Culture',
        "correct": 'Thriller by Michael Jackson',
        "wrong": ['Back in Black by AC/DC', 'The Dark Side of the Moon by Pink Floyd', 'Abbey Road by The Beatles']
    },
    {
        "text": 'Who is the main character in Breaking Bad?',
        "category": 'Pop Culture',
        "correct": 'Walter White',
        "wrong": ['Jesse Pinkman', 'Saul Goodman', 'Hank Schrader']
    },
    {
        "text": 'What year did Netflix start streaming?',
        "category": 'Pop Culture',
        "correct": '2007',
        "wrong": ['2005', '2010', '2008']
    },
    {
        "text": 'Who played Iron Man in the MCU?',
        "category": 'Pop Culture',
        "correct": 'Robert Downey Jr.',
        "wrong": ['Chris Evans', 'Chris Hemsworth', 'Tom Holland']
    },
    {
        "text": 'Who created the TV series The Office (US)?',
        "category": 'Pop Culture',
        "correct": 'Greg Daniels',
        "wrong": ['Ricky Gervais', 'Michael Schur', 'Steve Carell']
    },
    {
        "text": 'What is the name of the coffee shop in Friends?',
        "category": 'Pop Culture',
        "correct": 'Central Perk',
        "wrong": ['Central Park', 'Coffee Central', 'Perk Place']
    },
    {
        "text": "Who sang 'Bohemian Rhapsody'?",
        "category": 'Pop Culture',
        "correct": 'Queen',
        "wrong": ['The Beatles', 'Led Zeppelin', 'The Rolling Stones']
    },
    {
        "text": 'What year did Twitter launch?',
        "category": 'Pop Culture',
        "correct": '2006',
        "wrong": ['2004', '2008', '2007']
    },
    {
        "text": 'Who played Hermione in Harry Potter?',
        "category": 'Pop Culture',
        "correct": 'Emma Watson',
        "wrong": ['Emma Stone', 'Emma Roberts', 'Emily Blunt']
    },
    {
        "text": 'What band was Beyoncé part of before going solo?',
        "category": 'Pop Culture',
        "correct": "Destiny's Child",
        "wrong": ['TLC', 'Spice Girls', 'En Vogue']
    },
    {
        "text": 'What is the name of the island in Jurassic Park?',
        "category": 'Pop Culture',
        "correct": 'Isla Nublar',
        "wrong": ['Isla Sorna', 'Isla Muerta', 'Isla Paradiso']
    },
    {
        "text": 'Who directed The Shawshank Redemption?',
        "category": 'Pop Culture',
        "correct": 'Frank Darabont',
        "wrong": ['Steven Spielberg', 'Martin Scorsese', 'Francis Ford Coppola']
    },
    {
        "text": "What is the name of Han Solo's ship?",
        "category": 'Pop Culture',
        "correct": 'Millennium Falcon',
        "wrong": ['X-Wing', 'TIE Fighter', 'Star Destroyer']
    },
    {
        "text": 'Who created Game of Thrones (the TV series)?',
        "category": 'Pop Culture',
        "correct": 'D.B. Weiss and David Benioff',
        "wrong": ['George R.R. Martin', 'Vince Gilligan', 'J.J. Abrams']
    },
    {
        "text": 'What year did Instagram launch?',
        "category": 'Pop Culture',
        "correct": '2010',
        "wrong": ['2008', '2012', '2009']
    },
    {
        "text": 'Who plays Eleven in Stranger Things?',
        "category": 'Pop Culture',
        "correct": 'Millie Bobby Brown',
        "wrong": ['Sadie Sink', 'Natalia Dyer', 'Maya Hawke']
    },
    {
        "text": 'What is the name of the pub in How I Met Your Mother?',
        "category": 'Pop Culture',
        "correct": "MacLaren's",
        "wrong": ["McLaren's", 'MacLaren', 'The Pub']
    },
    {
        "text": 'Who directed Inception?',
        "category": 'Pop Culture',
        "correct": 'Christopher Nolan',
        "wrong": ['Denis Villeneuve', 'Ridley Scott', 'James Cameron']
    },
    {
        "text": 'What was the first Pixar movie?',
        "category": 'Pop Culture',
        "correct": 'Toy Story',
        "wrong": ["A Bug's Life", 'Finding Nemo', 'Monsters, Inc.']
    },
    {
        "text": "Who sang 'Rolling in the Deep'?",
        "category": 'Pop Culture',
        "correct": 'Adele',
        "wrong": ['Taylor Swift', 'Katy Perry', 'Rihanna']
    },
    {
        "text": 'What is the name of the dragon in The Hobbit?',
        "category": 'Pop Culture',
        "correct": 'Smaug',
        "wrong": ['Drogon', 'Toothless', 'Norbert']
    },
    {
        "text": 'Who created The Simpsons?',
        "category": 'Pop Culture',
        "correct": 'Matt Groening',
        "wrong": ['Seth MacFarlane', 'Trey Parker', 'Mike Judge']
    },
    {
        "text": 'What year did YouTube launch?',
        "category": 'Pop Culture',
        "correct": '2005',
        "wrong": ['2004', '2006', '2007']
    },
    {
        "text": 'Who plays Wednesday Addams in Wednesday (2022)?',
        "category": 'Pop Culture',
        "correct": 'Jenna Ortega',
        "wrong": ['Millie Bobby Brown', 'Sadie Sink', 'Zendaya']
    },
    {
        "text": 'What is the name of the kingdom in Frozen?',
        "category": 'Pop Culture',
        "correct": 'Arendelle',
        "wrong": ['Corona', 'DunBroch', 'Asgard']
    },
    {
        "text": "Who sang 'Thriller'?",
        "category": 'Pop Culture',
        "correct": 'Michael Jackson',
        "wrong": ['Prince', 'Stevie Wonder', 'James Brown']
    },
    {
        "text": "What is the name of Tony Stark's AI assistant?",
        "category": 'Pop Culture',
        "correct": 'JARVIS',
        "wrong": ['FRIDAY', 'VISION', 'ULTRON']
    },
    {
        "text": 'What year was the original Super Mario Bros. released?',
        "category": 'Gaming',
        "correct": '1985',
        "wrong": ['1983', '1987', '1986']
    },
    {
        "text": 'What is the highest level in Pac-Man?',
        "category": 'Gaming',
        "correct": '256',
        "wrong": ['255', '999', '128']
    },
    {
        "text": 'What company developed Fortnite?',
        "category": 'Gaming',
        "correct": 'Epic Games',
        "wrong": ['Activision', 'EA', 'Ubisoft']
    },
    {
        "text": 'What is the name of the protagonist in The Legend of Zelda?',
        "category": 'Gaming',
        "correct": 'Link',
        "wrong": ['Zelda', 'Ganon', 'Mario']
    },
    {
        "text": 'What year was Minecraft first released?',
        "category": 'Gaming',
        "correct": '2011',
        "wrong": ['2009', '2012', '2010']
    },
    {
        "text": 'What is the best-selling video game of all time?',
        "category": 'Gaming',
        "correct": 'Minecraft',
        "wrong": ['Grand Theft Auto V', 'Tetris', 'Wii Sports']
    },
    {
        "text": 'What is the name of the main character in Half-Life?',
        "category": 'Gaming',
        "correct": 'Gordon Freeman',
        "wrong": ['Alex Vance', 'Barney Calhoun', 'Isaac Kleiner']
    },
    {
        "text": 'What company created the Xbox?',
        "category": 'Gaming',
        "correct": 'Microsoft',
        "wrong": ['Sony', 'Nintendo', 'Sega']
    },
    {
        "text": 'What is the name of the princess in Super Mario?',
        "category": 'Gaming',
        "correct": 'Princess Peach',
        "wrong": ['Princess Daisy', 'Princess Rosalina', 'Princess Zelda']
    },
    {
        "text": 'What year was the PlayStation 1 released?',
        "category": 'Gaming',
        "correct": '1994',
        "wrong": ['1995', '1993', '1996']
    },
    {
        "text": 'What is the currency called in World of Warcraft?',
        "category": 'Gaming',
        "correct": 'Gold',
        "wrong": ['Credits', 'Coins', 'Zenny']
    },
    {
        "text": 'What is the main goal in Among Us?',
        "category": 'Gaming',
        "correct": 'Find the impostor or complete tasks',
        "wrong": ['Build a spaceship', 'Explore planets', 'Fight aliens']
    },
    {
        "text": 'What company developed League of Legends?',
        "category": 'Gaming',
        "correct": 'Riot Games',
        "wrong": ['Blizzard', 'Valve', 'Epic Games']
    },
    {
        "text": 'What is the name of the battle royale mode in Call of Duty?',
        "category": 'Gaming',
        "correct": 'Warzone',
        "wrong": ['Blackout', 'Battle Royale', 'Ground War']
    },
    {
        "text": 'What year was Tetris created?',
        "category": 'Gaming',
        "correct": '1984',
        "wrong": ['1985', '1983', '1986']
    },
    {
        "text": "What is the name of Sonic's sidekick?",
        "category": 'Gaming',
        "correct": 'Tails',
        "wrong": ['Knuckles', 'Shadow', 'Amy']
    },
    {
        "text": 'What company developed Overwatch?',
        "category": 'Gaming',
        "correct": 'Blizzard Entertainment',
        "wrong": ['Riot Games', 'Valve', 'Epic Games']
    },
    {
        "text": 'What is the maximum enchantment level in Minecraft?',
        "category": 'Gaming',
        "correct": '30',
        "wrong": ['50', '100', '25']
    },
    {
        "text": 'What year was Fortnite first released?',
        "category": 'Gaming',
        "correct": '2017',
        "wrong": ['2016', '2018', '2015']
    },
    {
        "text": 'What is the name of the final boss in Dark Souls?',
        "category": 'Gaming',
        "correct": 'Gwyn, Lord of Cinder',
        "wrong": ['Ornstein and Smough', 'Artorias', 'Manus']
    },
    {
        "text": 'What company created Pokemon?',
        "category": 'Gaming',
        "correct": 'Game Freak',
        "wrong": ['Nintendo', 'HAL Laboratory', 'Creatures Inc.']
    },
    {
        "text": 'What is the name of the protagonist in The Witcher 3?',
        "category": 'Gaming',
        "correct": 'Geralt of Rivia',
        "wrong": ['Vesemir', 'Eskel', 'Lambert']
    },
    {
        "text": 'What year was Doom first released?',
        "category": 'Gaming',
        "correct": '1993',
        "wrong": ['1992', '1994', '1995']
    },
    {
        "text": 'What is the name of the currency in Roblox?',
        "category": 'Gaming',
        "correct": 'Robux',
        "wrong": ['RoCoins', 'Tickets', 'Credits']
    },
    {
        "text": 'What company developed CS:GO?',
        "category": 'Gaming',
        "correct": 'Valve',
        "wrong": ['Riot Games', 'Blizzard', 'Epic Games']
    },
    {
        "text": 'What is the name of the block-placing mode in Minecraft?',
        "category": 'Gaming',
        "correct": 'Creative Mode',
        "wrong": ['Survival Mode', 'Adventure Mode', 'Hardcore Mode']
    },
    {
        "text": 'What year was Grand Theft Auto V released?',
        "category": 'Gaming',
        "correct": '2013',
        "wrong": ['2012', '2014', '2015']
    },
    {
        "text": 'What is the name of the main character in Halo?',
        "category": 'Gaming',
        "correct": 'Master Chief',
        "wrong": ['Arbiter', 'Cortana', 'Captain Keyes']
    },
    {
        "text": 'What company developed Apex Legends?',
        "category": 'Gaming',
        "correct": 'Respawn Entertainment',
        "wrong": ['EA', 'Activision', 'Epic Games']
    },
    {
        "text": 'What is the name of the final evolution of Charmander?',
        "category": 'Gaming',
        "correct": 'Charizard',
        "wrong": ['Charmeleon', 'Blaziken', 'Infernape']
    },
    {
        "text": "What is the name of Jon Snow's direwolf?",
        "category": 'Fandom',
        "correct": 'Ghost',
        "wrong": ['Grey Wind', 'Summer', 'Nymeria']
    },
    {
        "text": 'What house does Hermione belong to in Harry Potter?',
        "category": 'Fandom',
        "correct": 'Gryffindor',
        "wrong": ['Ravenclaw', 'Hufflepuff', 'Slytherin']
    },
    {
        "text": "What is the One Ring's inscription in Lord of the Rings?",
        "category": 'Fandom',
        "correct": 'One Ring to rule them all',
        "wrong": ['One Ring to find them', 'One Ring to bring them all', 'One Ring to bind them']
    },
    {
        "text": "What is the name of Thor's hammer?",
        "category": 'Fandom',
        "correct": 'Mjolnir',
        "wrong": ['Stormbreaker', 'Gungnir', 'Jarnbjorn']
    },
    {
        "text": "What is the name of Batman's butler?",
        "category": 'Fandom',
        "correct": 'Alfred Pennyworth',
        "wrong": ['James Gordon', 'Lucius Fox', 'Harvey Dent']
    },
    {
        "text": "What is the name of Frodo's gardener in LOTR?",
        "category": 'Fandom',
        "correct": 'Samwise Gamgee',
        "wrong": ['Meriadoc Brandybuck', 'Peregrin Took', 'Fredegar Bolger']
    },
    {
        "text": "What is Superman's weakness?",
        "category": 'Fandom',
        "correct": 'Kryptonite',
        "wrong": ['Magic', 'Red Sun', 'Lead']
    },
    {
        "text": "What is the name of Katniss's sister in The Hunger Games?",
        "category": 'Fandom',
        "correct": 'Primrose',
        "wrong": ['Rue', 'Clove', 'Glimmer']
    },
    {
        "text": 'What planet is Luke Skywalker from?',
        "category": 'Fandom',
        "correct": 'Tatooine',
        "wrong": ['Alderaan', 'Coruscant', 'Naboo']
    },
    {
        "text": "What is the name of Wonder Woman's home island?",
        "category": 'Fandom',
        "correct": 'Themyscira',
        "wrong": ['Themiscyra', 'Paradise Island', 'Amazon Island']
    },
    {
        "text": "What is the name of Darth Vader's grandson?",
        "category": 'Fandom',
        "correct": 'Kylo Ren',
        "wrong": ['Ben Solo', 'Finn', 'Poe Dameron']
    },
    {
        "text": 'What school does Percy Jackson attend?',
        "category": 'Fandom',
        "correct": 'Camp Half-Blood',
        "wrong": ['Hogwarts', 'Camp Jupiter', 'Yancy Academy']
    },
    {
        "text": "What is the name of Spider-Man's aunt?",
        "category": 'Fandom',
        "correct": 'Aunt May',
        "wrong": ['Aunt Marie', 'Aunt Martha', 'Aunt Anna']
    },
    {
        "text": 'What is the name of the school in The Vampire Diaries?',
        "category": 'Fandom',
        "correct": 'Mystic Falls High School',
        "wrong": ['Salvatore Boarding School', 'Whitmore College', 'Lockwood High']
    },
    {
        "text": "What is Captain America's real name?",
        "category": 'Fandom',
        "correct": 'Steve Rogers',
        "wrong": ['Bucky Barnes', 'Sam Wilson', 'Tony Stark']
    },
    {
        "text": 'What is the maximum ability score in D&D 5e (without magic items)?',
        "category": 'D&D',
        "correct": '20',
        "wrong": ['18', '25', '30']
    },
    {
        "text": 'What type of damage does a Red Dragon breathe?',
        "category": 'D&D',
        "correct": 'Fire',
        "wrong": ['Lightning', 'Acid', 'Cold']
    },
    {
        "text": 'What die do you roll for initiative in D&D?',
        "category": 'D&D',
        "correct": 'd20',
        "wrong": ['d12', 'd10', 'd8']
    },
    {
        "text": 'What class uses spell slots and a spellbook?',
        "category": 'D&D',
        "correct": 'Wizard',
        "wrong": ['Sorcerer', 'Warlock', 'Bard']
    },
    {
        "text": 'What is the name of the chaotic evil alignment?',
        "category": 'D&D',
        "correct": 'Chaotic Evil',
        "wrong": ['Neutral Evil', 'Lawful Evil', 'Chaotic Neutral']
    },
    {
        "text": 'What is the hit die for a Barbarian?',
        "category": 'D&D',
        "correct": 'd12',
        "wrong": ['d10', 'd8', 'd6']
    },
    {
        "text": 'What ability score does a Cleric use for spellcasting?',
        "category": 'D&D',
        "correct": 'Wisdom',
        "wrong": ['Intelligence', 'Charisma', 'Constitution']
    },
    {
        "text": 'What level spell is Fireball?',
        "category": 'D&D',
        "correct": '3rd level',
        "wrong": ['2nd level', '4th level', '5th level']
    },
    {
        "text": 'What does AC stand for in D&D?',
        "category": 'D&D',
        "correct": 'Armor Class',
        "wrong": ['Attack Chance', 'Action Count', 'Ability Check']
    },
    {
        "text": 'What is the maximum level in D&D 5e?',
        "category": 'D&D',
        "correct": '20',
        "wrong": ['30', '25', '15']
    },
    {
        "text": 'What type of damage does a White Dragon breathe?',
        "category": 'D&D',
        "correct": 'Cold',
        "wrong": ['Fire', 'Poison', 'Lightning']
    },
    {
        "text": 'What class can enter a Rage?',
        "category": 'D&D',
        "correct": 'Barbarian',
        "wrong": ['Fighter', 'Monk', 'Paladin']
    },
    {
        "text": 'What ability score do Rogues primarily use?',
        "category": 'D&D',
        "correct": 'Dexterity',
        "wrong": ['Strength', 'Intelligence', 'Wisdom']
    },
    {
        "text": 'What is the name of the goddess of magic in the Forgotten Realms?',
        "category": 'D&D',
        "correct": 'Mystra',
        "wrong": ['Tiamat', 'Shar', 'Selune']
    },
    {
        "text": 'What class uses Ki points?',
        "category": 'D&D',
        "correct": 'Monk',
        "wrong": ['Fighter', 'Rogue', 'Ranger']
    },
    {
        "text": 'In what year did the Berlin Wall fall?',
        "category": 'history',
        "correct": '1989',
        "wrong": ['1987', '1991', '1985']
    },
    {
        "text": 'Who was the first Emperor of Rome?',
        "category": 'history',
        "correct": 'Augustus',
        "wrong": ['Julius Caesar', 'Caligula', 'Nero']
    },
    {
        "text": 'What year did Christopher Columbus reach the Americas?',
        "category": 'history',
        "correct": '1492',
        "wrong": ['1500', '1488', '1476']
    },
    {
        "text": 'Who was the British Prime Minister during most of World War II?',
        "category": 'history',
        "correct": 'Winston Churchill',
        "wrong": ['Neville Chamberlain', 'Anthony Eden', 'Clement Attlee']
    },
    {
        "text": 'What ancient wonder of the world still exists today?',
        "category": 'history',
        "correct": 'Great Pyramid of Giza',
        "wrong": ['Lighthouse of Alexandria', 'Colossus of Rhodes', 'Hanging Gardens of Babylon']
    },
    {
        "text": 'Who was the first person to circumnavigate the globe?',
        "category": 'history',
        "correct": "Ferdinand Magellan's expedition",
        "wrong": ['Vasco da Gama', 'Christopher Columbus', 'James Cook']
    },
    {
        "text": 'What year did World War I begin?',
        "category": 'history',
        "correct": '1914',
        "wrong": ['1912', '1916', '1918']
    },
    {
        "text": 'Who wrote the Magna Carta?',
        "category": 'history',
        "correct": 'Archbishop Stephen Langton',
        "wrong": ['William Shakespeare', 'King John', 'Thomas Jefferson']
    },
    {
        "text": 'What was the name of the ship that brought the Pilgrims to America?',
        "category": 'history',
        "correct": 'Mayflower',
        "wrong": ['Discovery', 'Endeavour', 'Santa Maria']
    },
    {
        "text": 'Who was the youngest U.S. president ever elected?',
        "category": 'history',
        "correct": 'John F. Kennedy',
        "wrong": ['Bill Clinton', 'Theodore Roosevelt', 'Barack Obama']
    },
    {
        "text": 'What year did the French Revolution begin?',
        "category": 'history',
        "correct": '1789',
        "wrong": ['1793', '1776', '1799']
    },
    {
        "text": 'What empire was ruled by Genghis Khan?',
        "category": 'history',
        "correct": 'Mongol Empire',
        "wrong": ['Ottoman Empire', 'Persian Empire', 'Roman Empire']
    },
    {
        "text": 'In what year was the Declaration of Independence signed?',
        "category": 'history',
        "correct": '1776',
        "wrong": ['1774', '1780', '1778']
    },
    {
        "text": 'What year did the Soviet Union collapse?',
        "category": 'history',
        "correct": '1991',
        "wrong": ['1989', '1993', '1987']
    },
    {
        "text": 'Who was the first president of the United States?',
        "category": 'history',
        "correct": 'George Washington',
        "wrong": ['Thomas Jefferson', 'Benjamin Franklin', 'John Adams']
    },
    {
        "text": 'What was the name of the first atomic bomb dropped on Japan?',
        "category": 'history',
        "correct": 'Little Boy',
        "wrong": ['Fat Man', 'Big Boy', 'Trinity']
    },
    {
        "text": 'What year did the Great Depression begin?',
        "category": 'history',
        "correct": '1929',
        "wrong": ['1933', '1931', '1927']
    },
    {
        "text": 'Who was the Egyptian queen famous for her relationship with Julius Caesar and Mark Antony?',
        "category": 'history',
        "correct": 'Cleopatra',
        "wrong": ['Hatshepsut', 'Nefertiti', 'Nefertari']
    },
    {
        "text": 'What was the name of the first satellite launched into space?',
        "category": 'history',
        "correct": 'Sputnik 1',
        "wrong": ['Luna 1', 'Vostok 1', 'Explorer 1']
    },
    {
        "text": 'What year did the American Civil War begin?',
        "category": 'history',
        "correct": '1861',
        "wrong": ['1859', '1865', '1857']
    },
    {
        "text": 'What ancient civilization built Machu Picchu?',
        "category": 'history',
        "correct": 'Inca',
        "wrong": ['Aztec', 'Maya', 'Olmec']
    },
    {
        "text": "Who wrote 'The Communist Manifesto'?",
        "category": 'history',
        "correct": 'Karl Marx and Friedrich Engels',
        "wrong": ['Leon Trotsky', 'Joseph Stalin', 'Vladimir Lenin']
    },
    {
        "text": 'What year did India gain independence from Britain?',
        "category": 'history',
        "correct": '1947',
        "wrong": ['1945', '1950', '1942']
    },
    {
        "text": 'Who was the leader of Nazi Germany during World War II?',
        "category": 'history',
        "correct": 'Adolf Hitler',
        "wrong": ['Heinrich Himmler', 'Joseph Goebbels', 'Hermann Göring']
    },
    {
        "text": 'What was the name of the pandemic that killed millions in the 14th century?',
        "category": 'history',
        "correct": 'Black Death / Bubonic Plague',
        "wrong": ['Spanish Flu', 'Smallpox', 'Cholera']
    },
    {
        "text": 'What year did the Vietnam War end?',
        "category": 'history',
        "correct": '1975',
        "wrong": ['1971', '1973', '1977']
    },
    {
        "text": 'Who was the first female Prime Minister of the United Kingdom?',
        "category": 'history',
        "correct": 'Margaret Thatcher',
        "wrong": ['Indira Gandhi', 'Theresa May', 'Angela Merkel']
    },
    {
        "text": 'What empire was Constantinople the capital of?',
        "category": 'history',
        "correct": 'Byzantine Empire',
        "wrong": ['Roman Empire', 'Persian Empire', 'Ottoman Empire']
    },
    {
        "text": 'Who was assassinated in Sarajevo in 1914, sparking World War I?',
        "category": 'history',
        "correct": 'Archduke Franz Ferdinand',
        "wrong": ['Tsar Nicholas II', 'Kaiser Wilhelm II', 'King George V']
    },
    {
        "text": 'What year was the United Nations founded?',
        "category": 'history',
        "correct": '1945',
        "wrong": ['1948', '1950', '1942']
    },
    {
        "text": 'Who led the Bolshevik Revolution in Russia?',
        "category": 'history',
        "correct": 'Vladimir Lenin',
        "wrong": ['Joseph Stalin', 'Leon Trotsky', 'Mikhail Gorbachev']
    },
    {
        "text": 'What was the name of the ship that sank after hitting an iceberg in 1912?',
        "category": 'history',
        "correct": 'Titanic',
        "wrong": ['Lusitania', 'Olympic', 'Britannic']
    },
    {
        "text": 'Who was the Roman general who crossed the Rubicon River?',
        "category": 'history',
        "correct": 'Julius Caesar',
        "wrong": ['Mark Antony', 'Augustus', 'Pompey']
    },
    {
        "text": 'What year did the Korean War begin?',
        "category": 'history',
        "correct": '1950',
        "wrong": ['1946', '1948', '1952']
    },
    {
        "text": 'What was the name of the first successful English colony in America?',
        "category": 'history',
        "correct": 'Jamestown',
        "wrong": ['Roanoke', 'Plymouth', 'Boston']
    },
    {
        "text": 'Who invented the printing press?',
        "category": 'history',
        "correct": 'Johannes Gutenberg',
        "wrong": ['Aldus Manutius', 'Benjamin Franklin', 'William Caxton']
    },
    {
        "text": 'What year did Mexico gain independence from Spain?',
        "category": 'history',
        "correct": '1821',
        "wrong": ['1810', '1830', '1815']
    },
    {
        "text": 'Who was the first Holy Roman Emperor?',
        "category": 'history',
        "correct": 'Charlemagne',
        "wrong": ['Charles V', 'Frederick Barbarossa', 'Otto I']
    },
    {
        "text": 'What was the codename for the Allied invasion of Normandy?',
        "category": 'history',
        "correct": 'Operation Overlord',
        "wrong": ['Operation Barbarossa', 'Operation Torch', 'Operation Market Garden']
    },
    {
        "text": "Who wrote 'The Art of War'?",
        "category": 'history',
        "correct": 'Sun Tzu',
        "wrong": ['Lao Tzu', 'Miyamoto Musashi', 'Confucius']
    },
    {
        "text": 'What year did the Wright brothers make their first flight?',
        "category": 'history',
        "correct": '1903',
        "wrong": ['1906', '1910', '1900']
    },
    {
        "text": 'Who was the leader of the Soviet Union during the Cuban Missile Crisis?',
        "category": 'history',
        "correct": 'Nikita Khrushchev',
        "wrong": ['Mikhail Gorbachev', 'Leonid Brezhnev', 'Joseph Stalin']
    },
    {
        "text": 'What ancient library was burned down in Egypt?',
        "category": 'history',
        "correct": 'Library of Alexandria',
        "wrong": ['Library of Constantinople', 'Library of Nineveh', 'Library of Pergamum']
    },
    {
        "text": 'What is the capital of Mongolia?',
        "category": 'geography',
        "correct": 'Ulaanbaatar',
        "wrong": ['Bishkek', 'Tashkent', 'Astana']
    },
    {
        "text": 'What river runs through Baghdad?',
        "category": 'geography',
        "correct": 'Tigris',
        "wrong": ['Nile', 'Jordan', 'Euphrates']
    },
    {
        "text": 'Which African country was formerly known as Abyssinia?',
        "category": 'geography',
        "correct": 'Ethiopia',
        "wrong": ['Sudan', 'Eritrea', 'Somalia']
    },
    {
        "text": 'What is the longest river in South America?',
        "category": 'geography',
        "correct": 'Amazon',
        "wrong": ['Orinoco', 'Magdalena', 'Paraná']
    },
    {
        "text": 'Which ocean is the Mariana Trench located in?',
        "category": 'geography',
        "correct": 'Pacific Ocean',
        "wrong": ['Atlantic Ocean', 'Arctic Ocean', 'Indian Ocean']
    },
    {
        "text": 'Which country has the most islands?',
        "category": 'geography',
        "correct": 'Sweden',
        "wrong": ['Norway', 'Finland', 'Indonesia']
    },
    {
        "text": 'What mountain range separates Europe from Asia?',
        "category": 'geography',
        "correct": 'Ural Mountains',
        "wrong": ['Himalayas', 'Alps', 'Caucasus Mountains']
    },
    {
        "text": 'What is the capital of Bhutan?',
        "category": 'geography',
        "correct": 'Thimphu',
        "wrong": ['Lhasa', 'Kathmandu', 'Gangtok']
    },
    {
        "text": 'Which country is home to the ancient city of Petra?',
        "category": 'geography',
        "correct": 'Jordan',
        "wrong": ['Egypt', 'Syria', 'Lebanon']
    },
    {
        "text": 'What is the capital of Oman?',
        "category": 'geography',
        "correct": 'Muscat',
        "wrong": ['Doha', 'Riyadh', 'Dubai']
    },
    {
        "text": 'Which African country has Portuguese as its official language?',
        "category": 'geography',
        "correct": 'Angola (also Mozambique)',
        "wrong": ['Ghana', 'Kenya', 'Nigeria']
    },
    {
        "text": 'What strait separates Asia from North America?',
        "category": 'geography',
        "correct": 'Bering Strait',
        "wrong": ['Strait of Malacca', 'Strait of Gibraltar', 'Strait of Hormuz']
    },
    {
        "text": 'What is the capital of Myanmar?',
        "category": 'geography',
        "correct": 'Naypyidaw',
        "wrong": ['Mandalay', 'Bangkok', 'Yangon']
    },
    {
        "text": 'Which country has coastlines on both the Caribbean Sea and the Pacific Ocean?',
        "category": 'geography',
        "correct": 'Colombia (also Panama)',
        "wrong": ['Ecuador', 'Venezuela', 'Peru']
    },
    {
        "text": 'Which European capital city is split by the Danube River?',
        "category": 'geography',
        "correct": 'Budapest',
        "wrong": ['Bratislava', 'Belgrade', 'Vienna']
    },
    {
        "text": 'What is the capital of Estonia?',
        "category": 'geography',
        "correct": 'Tallinn',
        "wrong": ['Riga', 'Vilnius', 'Helsinki']
    },
    {
        "text": 'Which lake is the deepest in the world?',
        "category": 'geography',
        "correct": 'Lake Baikal',
        "wrong": ['Lake Tanganyika', 'Lake Superior', 'Caspian Sea']
    },
    {
        "text": 'What is the capital of Uruguay?',
        "category": 'geography',
        "correct": 'Montevideo',
        "wrong": ['Buenos Aires', 'Santiago', 'Asunción']
    },
    {
        "text": 'Which country is the Gobi Desert primarily located in?',
        "category": 'geography',
        "correct": 'Mongolia and China',
        "wrong": ['India', 'Pakistan', 'Kazakhstan']
    },
    {
        "text": 'What is the capital of Nigeria?',
        "category": 'geography',
        "correct": 'Abuja',
        "wrong": ['Ibadan', 'Lagos', 'Kano']
    },
    {
        "text": 'Which sea separates Europe from Africa?',
        "category": 'geography',
        "correct": 'Mediterranean Sea',
        "wrong": ['Aegean Sea', 'Black Sea', 'Red Sea']
    },
    {
        "text": 'What is the capital of Slovenia?',
        "category": 'geography',
        "correct": 'Ljubljana',
        "wrong": ['Bratislava', 'Zagreb', 'Sarajevo']
    },
    {
        "text": 'Which country has the most UNESCO World Heritage Sites?',
        "category": 'geography',
        "correct": 'Italy',
        "wrong": ['France', 'China', 'Spain']
    },
    {
        "text": 'What is the capital of Belarus?',
        "category": 'geography',
        "correct": 'Minsk',
        "wrong": ['Moscow', 'Warsaw', 'Kiev']
    },
    {
        "text": 'Which African lake is shared by Tanzania, Uganda, and Kenya?',
        "category": 'geography',
        "correct": 'Lake Victoria',
        "wrong": ['Lake Tanganyika', 'Lake Chad', 'Lake Malawi']
    },
    {
        "text": 'What is the capital of Qatar?',
        "category": 'geography',
        "correct": 'Doha',
        "wrong": ['Muscat', 'Manama', 'Dubai']
    },
    {
        "text": 'Which mountain is the tallest in Africa?',
        "category": 'geography',
        "correct": 'Mount Kilimanjaro',
        "wrong": ['Mount Kenya', 'Atlas Mountains', 'Mount Stanley']
    },
    {
        "text": 'What is the capital of Lithuania?',
        "category": 'geography',
        "correct": 'Vilnius',
        "wrong": ['Warsaw', 'Tallinn', 'Riga']
    },
    {
        "text": 'Which river forms part of the border between the USA and Mexico?',
        "category": 'geography',
        "correct": 'Rio Grande',
        "wrong": ['Columbia River', 'Colorado River', 'Mississippi River']
    },
    {
        "text": 'What is the capital of Azerbaijan?',
        "category": 'geography',
        "correct": 'Baku',
        "wrong": ['Tbilisi', 'Tehran', 'Yerevan']
    },
    {
        "text": 'Which island is the largest in the Mediterranean Sea?',
        "category": 'geography',
        "correct": 'Sicily',
        "wrong": ['Cyprus', 'Sardinia', 'Crete']
    },
    {
        "text": 'What is the capital of Senegal?',
        "category": 'geography',
        "correct": 'Dakar',
        "wrong": ['Bamako', 'Abidjan', 'Conakry']
    },
    {
        "text": 'What is the capital of Ecuador?',
        "category": 'geography',
        "correct": 'Quito',
        "wrong": ['Lima', 'Bogotá', 'Guayaquil']
    },
    {
        "text": 'Which volcano destroyed Pompeii in 79 AD?',
        "category": 'geography',
        "correct": 'Mount Vesuvius',
        "wrong": ['Krakatoa', 'Mount Etna', 'Stromboli']
    },
    {
        "text": 'What is the capital of Ghana?',
        "category": 'geography',
        "correct": 'Accra',
        "wrong": ['Dakar', 'Lagos', 'Abidjan']
    },
    {
        "text": 'Which strait connects the Mediterranean Sea to the Atlantic Ocean?',
        "category": 'geography',
        "correct": 'Strait of Gibraltar',
        "wrong": ['Dardanelles', 'Bosphorus', 'Strait of Messina']
    },
    {
        "text": 'What is the capital of Croatia?',
        "category": 'geography',
        "correct": 'Zagreb',
        "wrong": ['Sarajevo', 'Belgrade', 'Ljubljana']
    },
    {
        "text": 'Which country has the longest coastline in the world?',
        "category": 'geography',
        "correct": 'Canada',
        "wrong": ['Russia', 'Indonesia', 'Norway']
    },
    {
        "text": 'What is the capital of Bangladesh?',
        "category": 'geography',
        "correct": 'Dhaka',
        "wrong": ['Kathmandu', 'Kolkata', 'Islamabad']
    },
    {
        "text": 'Which sea is bordered by countries including Turkey, Ukraine, and Georgia?',
        "category": 'geography',
        "correct": 'Black Sea',
        "wrong": ['Mediterranean Sea', 'Caspian Sea', 'Adriatic Sea']
    },
    {
        "text": 'What is the capital of Tunisia?',
        "category": 'geography',
        "correct": 'Tunis',
        "wrong": ['Algiers', 'Rabat', 'Tripoli']
    },
    {
        "text": 'Which mountain range runs along the western coast of South America?',
        "category": 'geography',
        "correct": 'Andes',
        "wrong": ['Alps', 'Himalayas', 'Rockies']
    },
    {
        "text": 'What does OOP stand for in programming?',
        "category": 'Coding',
        "correct": 'Object-Oriented Programming',
        "wrong": ['Organized Output Program', 'Original Object Protocol', 'Optimal Operation Process']
    },
    {
        "text": 'What is the time complexity of binary search?',
        "category": 'Coding',
        "correct": 'O(log n)',
        "wrong": ['O(n log n)', 'O(n)', 'O(1)']
    },
    {
        "text": 'Who created the Linux kernel?',
        "category": 'Coding',
        "correct": 'Linus Torvalds',
        "wrong": ['Richard Stallman', 'Ken Thompson', 'Dennis Ritchie']
    },
    {
        "text": 'What does REST stand for in web services?',
        "category": 'Coding',
        "correct": 'Representational State Transfer',
        "wrong": ['Remote Execution Service Transfer', 'Relational Endpoint System Technology', 'Resource Execution State Transfer']
    },
    {
        "text": 'What year was the C programming language created?',
        "category": 'Coding',
        "correct": '1972',
        "wrong": ['1985', '1965', '1980']
    },
    {
        "text": 'What is the default port for HTTPS?',
        "category": 'Coding',
        "correct": '443',
        "wrong": ['8443', '8080', '80']
    },
    {
        "text": 'Who created the Ruby programming language?',
        "category": 'Coding',
        "correct": 'Yukihiro Matsumoto',
        "wrong": ['Guido van Rossum', 'Bjarne Stroustrup', 'James Gosling']
    },
    {
        "text": 'What is the maximum number of characters in a Tweet (as of 2023)?',
        "category": 'Coding',
        "correct": '280',
        "wrong": ['500', '140', '320']
    },
    {
        "text": 'What does JSON stand for?',
        "category": 'Coding',
        "correct": 'JavaScript Object Notation',
        "wrong": ['Java Serialized Object Notation', 'Java Standard Object Network', 'JavaScript Oriented Network']
    },
    {
        "text": 'Who created the Git version control system?',
        "category": 'Coding',
        "correct": 'Linus Torvalds',
        "wrong": ['Guido van Rossum', 'James Gosling', 'Ken Thompson']
    },
    {
        "text": 'What is the default port for SSH?',
        "category": 'Coding',
        "correct": '22',
        "wrong": ['21', '23', '24']
    },
    {
        "text": 'What does MVC stand for in software architecture?',
        "category": 'Coding',
        "correct": 'Model-View-Controller',
        "wrong": ['Model-Variable-Container', 'Module-View-Component', 'Main-Variable-Component']
    },
    {
        "text": 'What year was Java first released?',
        "category": 'Coding',
        "correct": '1995',
        "wrong": ['2000', '1990', '1998']
    },
    {
        "text": 'What does XML stand for?',
        "category": 'Coding',
        "correct": 'eXtensible Markup Language',
        "wrong": ['eXecutable Markup Language', 'eXtended Markup Language', 'eXternal Markup Language']
    },
    {
        "text": 'Who created the JavaScript programming language?',
        "category": 'Coding',
        "correct": 'Brendan Eich',
        "wrong": ['Tim Berners-Lee', 'James Gosling', 'Guido van Rossum']
    },
    {
        "text": 'What is the default port for MySQL database?',
        "category": 'Coding',
        "correct": '3306',
        "wrong": ['5432', '1433', '27017']
    },
    {
        "text": 'What does IDE stand for in programming?',
        "category": 'Coding',
        "correct": 'Integrated Development Environment',
        "wrong": ['Internal Development Engine', 'Intelligent Design Environment', 'Interactive Development Editor']
    },
    {
        "text": 'What is the time complexity of quicksort on average?',
        "category": 'Coding',
        "correct": 'O(n log n)',
        "wrong": ['O(n²)', 'O(log n)', 'O(n)']
    },
    {
        "text": 'What does CSS stand for?',
        "category": 'Coding',
        "correct": 'Cascading Style Sheets',
        "wrong": ['Colorful Style Sheets', 'Creative Style Sheets', 'Computer Style Sheets']
    },
    {
        "text": 'What is the rarest blood type in humans?',
        "category": 'General',
        "correct": 'AB negative',
        "wrong": ['O negative', 'B negative', 'A negative']
    },
    {
        "text": 'What is the hottest planet in our solar system?',
        "category": 'General',
        "correct": 'Venus',
        "wrong": ['Jupiter', 'Mars', 'Mercury']
    },
    {
        "text": 'What is the largest living species of lizard?',
        "category": 'General',
        "correct": 'Komodo Dragon',
        "wrong": ['Green Iguana', 'Saltwater Crocodile', 'Monitor Lizard']
    },
    {
        "text": 'How many eyes does a bee have?',
        "category": 'General',
        "correct": '5',
        "wrong": ['6', '2', '8']
    },
    {
        "text": 'What is the tallest bird in the world?',
        "category": 'General',
        "correct": 'Ostrich',
        "wrong": ['Emu', 'Crane', 'Cassowary']
    },
    {
        "text": 'How many hearts does an octopus have?',
        "category": 'General',
        "correct": '3',
        "wrong": ['2', '4', '1']
    },
    {
        "text": 'What is the fastest marine animal?',
        "category": 'General',
        "correct": 'Sailfish',
        "wrong": ['Dolphin', 'Marlin', 'Tuna']
    },
    {
        "text": 'How many bones do sharks have?',
        "category": 'General',
        "correct": '0 (cartilage)',
        "wrong": ['50', '200', '100']
    },
    {
        "text": 'What is the name of the programming language created by Microsoft for .NET?',
        "category": 'Coding',
        "correct": 'C#',
        "wrong": ['Visual Basic', 'F#', 'TypeScript']
    },
    {
        "text": 'What does YAML stand for in configuration files?',
        "category": 'Coding',
        "correct": "YAML Ain't Markup Language",
        "wrong": ['Youthful Automated Markup Language', 'Yield All Markup Language', 'Yet Another Markup Language']
    },
    {
        "text": "What is the name of Neptune's largest moon?",
        "category": 'science',
        "correct": 'Triton',
        "wrong": ['Europa', 'Titan', 'Ganymede']
    },
    {
        "text": 'What is the chemical symbol for tungsten?',
        "category": 'science',
        "correct": 'W',
        "wrong": ['Tn', 'Tu', 'T']
    },
    {
        "text": 'What is the capital of Iceland?',
        "category": 'geography',
        "correct": 'Reykjavik',
        "wrong": ['Helsinki', 'Copenhagen', 'Oslo']
    },
    {
        "text": 'What strait separates Morocco from Spain?',
        "category": 'geography',
        "correct": 'Strait of Gibraltar',
        "wrong": ['Strait of Hormuz', 'Dardanelles', 'Bosphorus']
    },
    {
        "text": 'Which US state has the longest coastline?',
        "category": 'geography',
        "correct": 'Alaska',
        "wrong": ['Hawaii', 'California', 'Florida']
    },
    {
        "text": 'What year did the Cold War end?',
        "category": 'history',
        "correct": '1991',
        "wrong": ['1993', '1985', '1989']
    },
    {
        "text": 'Who was the first Roman Emperor?',
        "category": 'history',
        "correct": 'Augustus',
        "wrong": ['Tiberius', 'Julius Caesar', 'Nero']
    },
    {
        "text": 'What year did the Battle of Waterloo take place?',
        "category": 'history',
        "correct": '1815',
        "wrong": ['1805', '1820', '1810']
    },
    {
        "text": 'What is the name of the mascot for Linux?',
        "category": 'technology',
        "correct": 'Tux (penguin)',
        "wrong": ['Wilbur', 'Gnu', 'Larry']
    },
    {
        "text": 'What is the fastest fish in the ocean?',
        "category": 'General',
        "correct": 'Sailfish',
        "wrong": ['Marlin', 'Tuna', 'Swordfish']
    },
    {
        "text": 'What year did MTV first air?',
        "category": 'music',
        "correct": '1981',
        "wrong": ['1985', '1979', '1983']
    },
    {
        "text": "Who wrote 'The Count of Monte Cristo'?",
        "category": 'literature',
        "correct": 'Alexandre Dumas',
        "wrong": ['Honoré de Balzac', 'Gustave Flaubert', 'Victor Hugo']
    },
    {
        "text": "What year was 'Nineteen Eighty-Four' published?",
        "category": 'literature',
        "correct": '1949',
        "wrong": ['1945', '1950', '1948']
    },
    {
        "text": 'What is the name of the server-side JavaScript runtime environment?',
        "category": 'technology',
        "correct": 'Node.js',
        "wrong": ['React', 'Deno', 'Bun']
    }
]
