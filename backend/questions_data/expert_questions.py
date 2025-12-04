"""Expert difficulty trivia questions.

This module contains expert difficulty questions for the trivia game.
Total: 489 questions

Add new expert questions here in the following format:
{
    "text": "What is the question?",
    "category": "Category Name",
    "correct": "Correct Answer",
    "wrong": ["Wrong Answer 1", "Wrong Answer 2", "Wrong Answer 3"]
}
"""

EXPERT_QUESTIONS = [
    {
        "text": 'In distributed systems, what does the CAP theorem state you must sacrifice?',
        "category": 'Coding',
        "correct": 'One of: Consistency, Availability, or Partition tolerance',
        "wrong": ['Performance for reliability', 'Security for speed', 'Scalability for simplicity']
    },
    {
        "text": 'What is the time complexity of the Bellman-Ford algorithm?',
        "category": 'Coding',
        "correct": 'O(V*E)',
        "wrong": ['O(E log V)', 'O(V^2)', 'O(V + E)']
    },
    {
        "text": 'What is the main purpose of a semaphore in concurrent programming?',
        "category": 'Coding',
        "correct": 'Control access to shared resources',
        "wrong": ['Increase processing speed', 'Manage memory allocation', 'Handle exceptions']
    },
    {
        "text": 'In the actor model of concurrency, what is the primary unit of computation?',
        "category": 'Coding',
        "correct": 'Actor',
        "wrong": ['Thread', 'Process', 'Coroutine']
    },
    {
        "text": 'What does CQRS stand for in software architecture?',
        "category": 'Coding',
        "correct": 'Command Query Responsibility Segregation',
        "wrong": ['Centralized Query Response System', 'Command Queue Request Service', 'Concurrent Query Resource Sharing']
    },
    {
        "text": 'Which consensus algorithm is used by Bitcoin?',
        "category": 'Coding',
        "correct": 'Proof of Work',
        "wrong": ['Paxos', 'Raft', 'Byzantine Fault Tolerance']
    },
    {
        "text": 'What is the chromatic number of a planar graph according to the four color theorem?',
        "category": 'Coding',
        "correct": 'At most 4',
        "wrong": ['At most 3', 'At most 5', 'Exactly 4']
    },
    {
        "text": 'In functional programming, what is a monad?',
        "category": 'Coding',
        "correct": 'A design pattern for composing computations',
        "wrong": ['A type of data structure', 'A concurrency primitive', 'A memory management technique']
    },
    {
        "text": 'What is the space complexity of merge sort?',
        "category": 'Coding',
        "correct": 'O(n)',
        "wrong": ['O(log n)', 'O(1)', 'O(n log n)']
    },
    {
        "text": 'Which data structure provides O(1) amortized time for both push and pop operations?',
        "category": 'Coding',
        "correct": 'Dynamic array (ArrayList)',
        "wrong": ['Binary heap', 'Red-black tree', 'Skip list']
    },
    {
        "text": 'What is the Byzantine Generals Problem in distributed computing?',
        "category": 'Coding',
        "correct": 'Achieving consensus with faulty or malicious nodes',
        "wrong": ['Load balancing across servers', 'Deadlock prevention', 'Memory synchronization']
    },
    {
        "text": 'In type theory, what is a dependent type?',
        "category": 'Coding',
        "correct": 'A type that depends on a value',
        "wrong": ['A type that inherits from another', 'A nullable reference type', 'A generic type parameter']
    },
    {
        "text": 'What is the halting problem in computer science?',
        "category": 'Coding',
        "correct": 'Determining if a program will terminate',
        "wrong": ['Optimizing program execution time', 'Preventing infinite loops', 'Managing program crashes']
    },
    {
        "text": 'Which algorithm is used to find strongly connected components in a graph?',
        "category": 'Coding',
        "correct": "Tarjan's algorithm",
        "wrong": ["Dijkstra's algorithm", "Kruskal's algorithm", 'Floyd-Warshall']
    },
    {
        "text": 'What is the Cook-Levin theorem about?',
        "category": 'Coding',
        "correct": 'SAT is NP-complete',
        "wrong": ['P equals NP', 'Graph coloring complexity', 'Sorting lower bounds']
    },
    {
        "text": 'In compiler design, what is SSA form?',
        "category": 'Coding',
        "correct": 'Static Single Assignment',
        "wrong": ['Synchronized Stack Allocation', 'Shared State Architecture', 'Sequential Sequence Analysis']
    },
    {
        "text": 'What is the difference between a mutex and a spinlock?',
        "category": 'Coding',
        "correct": 'Spinlock busy-waits, mutex sleeps',
        "wrong": ['Mutex is faster than spinlock', 'Spinlock allows multiple owners', 'Mutex works across processes']
    },
    {
        "text": 'What is the pigeonhole principle used for in algorithm analysis?',
        "category": 'Coding',
        "correct": 'Proving lower bounds and impossibility',
        "wrong": ['Optimizing hash functions', 'Improving sorting algorithms', 'Memory management']
    },
    {
        "text": 'In graph theory, what is a chromatic polynomial?',
        "category": 'Coding',
        "correct": 'Counts valid k-colorings of a graph',
        "wrong": ['Finds shortest paths', 'Detects cycles', 'Computes maximum flow']
    },
    {
        "text": 'What is the lambda calculus?',
        "category": 'Coding',
        "correct": 'A formal system for expressing computation',
        "wrong": ['A calculus for optimization', 'A method for parallel computing', 'A database query language']
    },
    {
        "text": 'What does the Y combinator do in functional programming?',
        "category": 'Coding',
        "correct": 'Enables recursion without named functions',
        "wrong": ['Parallelizes computations', 'Manages state', 'Optimizes tail calls']
    },
    {
        "text": 'What is the amortized time complexity of union-find with path compression?',
        "category": 'Coding',
        "correct": 'O(α(n)) - inverse Ackermann',
        "wrong": ['O(log n)', 'O(1)', 'O(log* n)']
    },
    {
        "text": 'In cryptography, what property does a rainbow table attack exploit?',
        "category": 'Coding',
        "correct": 'Precomputed hash chains',
        "wrong": ['Weak encryption keys', 'Buffer overflows', 'SQL injection']
    },
    {
        "text": 'What is the purpose of Bloom filters?',
        "category": 'Coding',
        "correct": 'Probabilistic set membership testing',
        "wrong": ['Exact string matching', 'Sorting algorithms', 'Memory compression']
    },
    {
        "text": 'What is the difference between optimistic and pessimistic locking?',
        "category": 'Coding',
        "correct": 'When conflicts are checked: before vs after',
        "wrong": ['Performance characteristics only', 'Thread vs process level', 'Database vs file system']
    },
    {
        "text": 'In information theory, what does Shannon entropy measure?',
        "category": 'Coding',
        "correct": 'Average information content',
        "wrong": ['Computational complexity', 'Network bandwidth', 'Encryption strength']
    },
    {
        "text": 'What is the two-phase commit protocol used for?',
        "category": 'Coding',
        "correct": 'Distributed transaction coordination',
        "wrong": ['Memory management', 'Load balancing', 'Cache invalidation']
    },
    {
        "text": 'What problem does the Dining Philosophers problem illustrate?',
        "category": 'Coding',
        "correct": 'Deadlock and resource contention',
        "wrong": ['Race conditions', 'Memory leaks', 'Stack overflow']
    },
    {
        "text": 'In graph algorithms, what is the cut property used for?',
        "category": 'Coding',
        "correct": 'Finding minimum spanning trees',
        "wrong": ['Detecting cycles', 'Topological sorting', 'Graph coloring']
    },
    {
        "text": 'What is the purpose of write-ahead logging (WAL) in databases?',
        "category": 'Coding',
        "correct": 'Ensuring durability and atomicity',
        "wrong": ['Improving query performance', 'Data compression', 'Access control']
    },
    {
        "text": 'What is the only mammal capable of true flight?',
        "category": 'General',
        "correct": 'Bat',
        "wrong": ['Flying squirrel', 'Sugar glider', 'Flying lemur']
    },
    {
        "text": 'Which element has the highest melting point?',
        "category": 'General',
        "correct": 'Tungsten',
        "wrong": ['Carbon', 'Osmium', 'Rhenium']
    },
    {
        "text": 'What is the Planck length?',
        "category": 'General',
        "correct": 'The smallest measurable length in physics',
        "wrong": ['The distance light travels in one second', 'The radius of an atom', 'The wavelength of visible light']
    },
    {
        "text": 'Who proved that the set of real numbers is uncountable?',
        "category": 'General',
        "correct": 'Georg Cantor',
        "wrong": ['David Hilbert', 'Bertrand Russell', 'Kurt Gödel']
    },
    {
        "text": 'What is the Riemann Hypothesis about?',
        "category": 'General',
        "correct": 'Distribution of prime numbers',
        "wrong": ['Geometry of curved spaces', 'Quantum mechanics', 'Set theory paradoxes']
    },
    {
        "text": 'Which civilization invented the concept of zero?',
        "category": 'General',
        "correct": 'Ancient India',
        "wrong": ['Ancient Egypt', 'Ancient Greece', 'Ancient China']
    },
    {
        "text": 'What is the name of the closest star system to our solar system?',
        "category": 'General',
        "correct": 'Alpha Centauri',
        "wrong": ["Barnard's Star", 'Sirius', 'Proxima']
    },
    {
        "text": 'What does the Heisenberg Uncertainty Principle state?',
        "category": 'General',
        "correct": 'Position and momentum cannot both be precisely known',
        "wrong": ['Time travel is impossible', 'Energy cannot be created or destroyed', 'Matter and energy are equivalent']
    },
    {
        "text": 'What is the Mohs hardness of diamond?',
        "category": 'General',
        "correct": '10',
        "wrong": ['9', '8', '12']
    },
    {
        "text": 'Who formulated the Three Laws of Thermodynamics?',
        "category": 'General',
        "correct": 'Rudolf Clausius',
        "wrong": ['Lord Kelvin', 'James Joule', 'Sadi Carnot']
    },
    {
        "text": 'What is the half-life of Carbon-14?',
        "category": 'General',
        "correct": '5,730 years',
        "wrong": ['10,000 years', '2,500 years', '50,000 years']
    },
    {
        "text": "What is Schrödinger's wave equation used for?",
        "category": 'General',
        "correct": 'Describing quantum mechanical systems',
        "wrong": ['Calculating gravitational waves', 'Modeling chemical reactions', 'Predicting weather patterns']
    },
    {
        "text": 'What is the Drake Equation used to estimate?',
        "category": 'General',
        "correct": 'Number of communicative alien civilizations',
        "wrong": ['Age of the universe', 'Number of galaxies', 'Probability of asteroid impact']
    },
    {
        "text": "What is Fermat's Last Theorem?",
        "category": 'General',
        "correct": 'No three positive integers satisfy a^n + b^n = c^n for n > 2',
        "wrong": ['Every even number is the sum of two primes', 'There are infinitely many prime numbers', 'Pi is transcendental']
    },
    {
        "text": 'What is the name of the supercontinent that existed 300 million years ago?',
        "category": 'General',
        "correct": 'Pangaea',
        "wrong": ['Gondwana', 'Laurasia', 'Rodinia']
    },
    {
        "text": 'What phenomenon causes the Northern Lights (Aurora Borealis)?',
        "category": 'General',
        "correct": "Solar wind interacting with Earth's magnetosphere",
        "wrong": ['Ice crystals in the upper atmosphere', 'Volcanic ash reflecting sunlight', 'Meteor showers']
    },
    {
        "text": 'What is the Schwarzschild radius?',
        "category": 'General',
        "correct": "The radius of a black hole's event horizon",
        "wrong": ['The distance to the nearest galaxy', 'The size of an atom', 'The orbital radius of Mercury']
    },
    {
        "text": 'What is the strongest known material by tensile strength?',
        "category": 'General',
        "correct": 'Graphene',
        "wrong": ['Diamond', 'Carbon nanotubes', 'Kevlar']
    },
    {
        "text": 'What is the SI unit of radioactivity?',
        "category": 'General',
        "correct": 'Becquerel',
        "wrong": ['Sievert', 'Gray', 'Roentgen']
    },
    {
        "text": 'What is the Fibonacci sequence recursion relation?',
        "category": 'General',
        "correct": 'F(n) = F(n-1) + F(n-2)',
        "wrong": ['F(n) = F(n-1) * F(n-2)', 'F(n) = 2*F(n-1)', 'F(n) = F(n-1)^2']
    },
    {
        "text": "What is Avogadro's number?",
        "category": 'General',
        "correct": '6.022 × 10^23',
        "wrong": ['3.14159', '2.71828', '9.81']
    },
    {
        "text": 'What causes the Coriolis effect?',
        "category": 'General',
        "correct": "Earth's rotation",
        "wrong": ["Moon's gravity", 'Solar radiation', 'Ocean currents']
    },
    {
        "text": 'What is the name of the first artificial satellite?',
        "category": 'General',
        "correct": 'Sputnik 1',
        "wrong": ['Explorer 1', 'Vanguard 1', 'Telstar']
    },
    {
        "text": 'What is the event horizon of a black hole?',
        "category": 'General',
        "correct": 'The boundary beyond which nothing can escape',
        "wrong": ['The point where matter is compressed', 'The outer edge of the galaxy', 'The gravitational center']
    },
    {
        "text": 'What is the principle of superposition in quantum mechanics?',
        "category": 'General',
        "correct": 'A particle can exist in multiple states simultaneously',
        "wrong": ['Energy levels are discrete', 'Particles have wave properties', 'Observation affects the system']
    },
    {
        "text": "What is the cosmological constant in Einstein's field equations?",
        "category": 'General',
        "correct": 'Lambda (Λ), related to dark energy',
        "wrong": ['Hubble constant', 'Speed of light', 'Gravitational constant']
    },
    {
        "text": "Who proved Gödel's Incompleteness Theorems?",
        "category": 'General',
        "correct": 'Kurt Gödel',
        "wrong": ['Alan Turing', 'Bertrand Russell', 'David Hilbert']
    },
    {
        "text": 'What is the P versus NP problem?',
        "category": 'General',
        "correct": 'Whether problems verifiable in polynomial time are also solvable in polynomial time',
        "wrong": ['The relationship between primes and composite numbers', 'A question about parallel processing', 'A network topology problem']
    },
    {
        "text": "Who directed the film 'Citizen Kane'?",
        "category": 'Pop Culture',
        "correct": 'Orson Welles',
        "wrong": ['Alfred Hitchcock', 'Stanley Kubrick', 'Frank Capra']
    },
    {
        "text": "What is the name of the fictional language spoken by the Na'vi in Avatar?",
        "category": 'Pop Culture',
        "correct": "Na'vi",
        "wrong": ['Pandoran', 'Eywa', 'Toruk']
    },
    {
        "text": "Who composed the soundtrack for 'The Lord of the Rings' trilogy?",
        "category": 'Pop Culture',
        "correct": 'Howard Shore',
        "wrong": ['Hans Zimmer', 'John Williams', 'James Horner']
    },
    {
        "text": "What is the name of the fictional metal in the Marvel Universe that makes up Captain America's shield?",
        "category": 'Pop Culture',
        "correct": 'Vibranium',
        "wrong": ['Adamantium', 'Carbonadium', 'Uru']
    },
    {
        "text": "Who wrote the novel 'Neuromancer', which popularized the concept of cyberspace?",
        "category": 'Pop Culture',
        "correct": 'William Gibson',
        "wrong": ['Philip K. Dick', 'Isaac Asimov', 'Neal Stephenson']
    },
    {
        "text": 'What is the name of the AI in the Portal video game series?',
        "category": 'Pop Culture',
        "correct": 'GLaDOS',
        "wrong": ['Cortana', 'SHODAN', 'HAL 9000']
    },
    {
        "text": "In what year was the first episode of 'Doctor Who' broadcast?",
        "category": 'Pop Culture',
        "correct": '1963',
        "wrong": ['1965', '1960', '1958']
    },
    {
        "text": "Who created the animated series 'Cowboy Bebop'?",
        "category": 'Pop Culture',
        "correct": 'Shinichirō Watanabe',
        "wrong": ['Hayao Miyazaki', 'Satoshi Kon', 'Mamoru Oshii']
    },
    {
        "text": 'What is the name of the fictional city in Batman comics?',
        "category": 'Pop Culture',
        "correct": 'Gotham City',
        "wrong": ['Metropolis', 'Central City', 'Star City']
    },
    {
        "text": "Who painted 'The Persistence of Memory' featuring melting clocks?",
        "category": 'Pop Culture',
        "correct": 'Salvador Dalí',
        "wrong": ['Pablo Picasso', 'René Magritte', 'Joan Miró']
    },
    {
        "text": "What is the name of the fictional language created for Star Trek's Klingon species?",
        "category": 'Pop Culture',
        "correct": 'Klingon (tlhIngan Hol)',
        "wrong": ['Vulcan', 'Romulan', 'Cardassian']
    },
    {
        "text": "Who directed 'Blade Runner'?",
        "category": 'Pop Culture',
        "correct": 'Ridley Scott',
        "wrong": ['Stanley Kubrick', 'Steven Spielberg', 'James Cameron']
    },
    {
        "text": 'What is the name of the fictional wizarding school in Harry Potter?',
        "category": 'Pop Culture',
        "correct": 'Hogwarts',
        "wrong": ['Beauxbatons', 'Durmstrang', 'Ilvermorny']
    },
    {
        "text": "Who wrote 'Dune'?",
        "category": 'Pop Culture',
        "correct": 'Frank Herbert',
        "wrong": ['Isaac Asimov', 'Arthur C. Clarke', 'Robert Heinlein']
    },
    {
        "text": "What is the name of the fictional company in the 'Alien' franchise?",
        "category": 'Pop Culture',
        "correct": 'Weyland-Yutani Corporation',
        "wrong": ['Tyrell Corporation', 'Cyberdyne Systems', 'Umbrella Corporation']
    },
    {
        "text": "Who composed the score for 'Star Wars'?",
        "category": 'Pop Culture',
        "correct": 'John Williams',
        "wrong": ['Hans Zimmer', 'Ennio Morricone', 'Jerry Goldsmith']
    },
    {
        "text": "What year did 'The Matrix' first release in theaters?",
        "category": 'Pop Culture',
        "correct": '1999',
        "wrong": ['1998', '2000', '1997']
    },
    {
        "text": "Who created the comic book series 'Watchmen'?",
        "category": 'Pop Culture',
        "correct": 'Alan Moore',
        "wrong": ['Frank Miller', 'Neil Gaiman', 'Grant Morrison']
    },
    {
        "text": "What is the name of the fictional planet in 'Dune'?",
        "category": 'Pop Culture',
        "correct": 'Arrakis',
        "wrong": ['Caladan', 'Giedi Prime', 'Kaitain']
    },
    {
        "text": "Who directed 'Pulp Fiction'?",
        "category": 'Pop Culture',
        "correct": 'Quentin Tarantino',
        "wrong": ['Martin Scorsese', 'Coen Brothers', 'Paul Thomas Anderson']
    },
    {
        "text": "What is the name of the AI in '2001: A Space Odyssey'?",
        "category": 'Pop Culture',
        "correct": 'HAL 9000',
        "wrong": ['GERTY', 'TARS', 'Mother']
    },
    {
        "text": "Who created the TV series 'The Wire'?",
        "category": 'Pop Culture',
        "correct": 'David Simon',
        "wrong": ['Vince Gilligan', 'David Chase', 'Matthew Weiner']
    },
    {
        "text": "What is the name of the fictional corporation in 'Blade Runner'?",
        "category": 'Pop Culture',
        "correct": 'Tyrell Corporation',
        "wrong": ['Weyland-Yutani', 'Cyberdyne Systems', 'Omni Consumer Products']
    },
    {
        "text": "Who wrote the novel 'Fahrenheit 451'?",
        "category": 'Pop Culture',
        "correct": 'Ray Bradbury',
        "wrong": ['George Orwell', 'Aldous Huxley', 'Kurt Vonnegut']
    },
    {
        "text": "What is the name of the ship in 'Firefly'?",
        "category": 'Pop Culture',
        "correct": 'Serenity',
        "wrong": ['Millennium Falcon', 'Enterprise', 'Galactica']
    },
    {
        "text": "Who directed 'Inception'?",
        "category": 'Pop Culture',
        "correct": 'Christopher Nolan',
        "wrong": ['Denis Villeneuve', 'Darren Aronofsky', 'David Fincher']
    },
    {
        "text": "What is the name of the fictional metal that Wolverine's claws are made of?",
        "category": 'Pop Culture',
        "correct": 'Adamantium',
        "wrong": ['Vibranium', 'Carbonadium', 'Uru']
    },
    {
        "text": "Who created 'Rick and Morty'?",
        "category": 'Pop Culture',
        "correct": 'Justin Roiland and Dan Harmon',
        "wrong": ['Seth MacFarlane', 'Matt Groening', 'Trey Parker and Matt Stone']
    },
    {
        "text": "What is the name of the fictional spice in 'Dune'?",
        "category": 'Pop Culture',
        "correct": 'Melange',
        "wrong": ['Spice', 'Saffron', 'Arrakeen']
    },
    {
        "text": "Who directed 'The Shawshank Redemption'?",
        "category": 'Pop Culture',
        "correct": 'Frank Darabont',
        "wrong": ['Rob Reiner', 'Steven Spielberg', 'Clint Eastwood']
    },
    {
        "text": 'What year was the original Pong arcade game released?',
        "category": 'Gaming',
        "correct": '1972',
        "wrong": ['1974', '1970', '1976']
    },
    {
        "text": 'What is the name of the first commercially successful video game?',
        "category": 'Gaming',
        "correct": 'Pong',
        "wrong": ['Space Invaders', 'Pac-Man', 'Computer Space']
    },
    {
        "text": 'Who is credited with creating Minecraft?',
        "category": 'Gaming',
        "correct": "Markus 'Notch' Persson",
        "wrong": ['Jens Bergensten', 'Gabe Newell', 'John Carmack']
    },
    {
        "text": 'What is the maximum level cap in the original Diablo?',
        "category": 'Gaming',
        "correct": '50',
        "wrong": ['60', '99', '100']
    },
    {
        "text": 'What game engine does Half-Life 2 use?',
        "category": 'Gaming',
        "correct": 'Source Engine',
        "wrong": ['Unreal Engine', 'id Tech', 'CryEngine']
    },
    {
        "text": "What was the first game to feature a 'battle royale' mode?",
        "category": 'Gaming',
        "correct": 'DayZ: Battle Royale mod',
        "wrong": ['PUBG', 'Fortnite', 'H1Z1']
    },
    {
        "text": 'What is the name of the planet where Halo takes place?',
        "category": 'Gaming',
        "correct": 'Installation 04 (Halo ring)',
        "wrong": ['Reach', 'Earth', 'Sanghelios']
    },
    {
        "text": 'What year did World of Warcraft launch?',
        "category": 'Gaming',
        "correct": '2004',
        "wrong": ['2003', '2005', '2006']
    },
    {
        "text": 'Who developed the Souls series (Dark Souls, Bloodborne, Elden Ring)?',
        "category": 'Gaming',
        "correct": 'FromSoftware',
        "wrong": ['Capcom', 'Platinum Games', 'Team Ninja']
    },
    {
        "text": 'What is the name of the fictional virus in Resident Evil?',
        "category": 'Gaming',
        "correct": 'T-Virus',
        "wrong": ['G-Virus', 'C-Virus', 'Uroboros']
    },
    {
        "text": 'What was the first 3D platformer game?',
        "category": 'Gaming',
        "correct": 'Super Mario 64',
        "wrong": ['Crash Bandicoot', 'Spyro the Dragon', 'Banjo-Kazooie']
    },
    {
        "text": 'What is the name of the protagonist in the Metal Gear Solid series?',
        "category": 'Gaming',
        "correct": 'Solid Snake',
        "wrong": ['Liquid Snake', 'Big Boss', 'Raiden']
    },
    {
        "text": 'What company developed the Fallout series?',
        "category": 'Gaming',
        "correct": 'Interplay (original), Bethesda (modern)',
        "wrong": ['BioWare', 'Obsidian Entertainment', 'inXile Entertainment']
    },
    {
        "text": 'What is the name of the fictional city in Grand Theft Auto V?',
        "category": 'Gaming',
        "correct": 'Los Santos',
        "wrong": ['Liberty City', 'Vice City', 'San Fierro']
    },
    {
        "text": 'What year was the Nintendo Entertainment System (NES) released in North America?',
        "category": 'Gaming',
        "correct": '1985',
        "wrong": ['1983', '1987', '1984']
    },
    {
        "text": 'What is the name of the AI companion in Portal?',
        "category": 'Gaming',
        "correct": 'GLaDOS',
        "wrong": ['Wheatley', 'Cortana', 'EDI']
    },
    {
        "text": 'Who created the Zelda series?',
        "category": 'Gaming',
        "correct": 'Shigeru Miyamoto',
        "wrong": ['Koji Kondo', 'Eiji Aonuma', 'Satoru Iwata']
    },
    {
        "text": 'What is the maximum number of players in a single Fortnite Battle Royale match?',
        "category": 'Gaming',
        "correct": '100',
        "wrong": ['64', '150', '200']
    },
    {
        "text": 'What is the name of the main character in The Witcher series?',
        "category": 'Gaming',
        "correct": 'Geralt of Rivia',
        "wrong": ['Vesemir', 'Ciri', 'Dandelion']
    },
    {
        "text": "What game popularized the 'loot box' monetization model?",
        "category": 'Gaming',
        "correct": 'Team Fortress 2',
        "wrong": ['Overwatch', 'FIFA', 'Counter-Strike']
    },
    {
        "text": 'What is the name of the currency in League of Legends used to purchase champions?',
        "category": 'Gaming',
        "correct": 'Blue Essence (formerly IP)',
        "wrong": ['Riot Points', 'Gold', 'Tokens']
    },
    {
        "text": 'What company developed StarCraft?',
        "category": 'Gaming',
        "correct": 'Blizzard Entertainment',
        "wrong": ['Westwood Studios', 'Ensemble Studios', 'Relic Entertainment']
    },
    {
        "text": 'What is the name of the final boss in the original Dark Souls?',
        "category": 'Gaming',
        "correct": 'Gwyn, Lord of Cinder',
        "wrong": ['Ornstein and Smough', 'Seath the Scaleless', 'Nito']
    },
    {
        "text": 'What year was Steam launched by Valve?',
        "category": 'Gaming',
        "correct": '2003',
        "wrong": ['2004', '2002', '2005']
    },
    {
        "text": "What is the name of the fictional organization in Assassin's Creed?",
        "category": 'Gaming',
        "correct": 'Assassin Brotherhood',
        "wrong": ['Templars', 'Abstergo', 'The Order']
    },
    {
        "text": 'What is the name of the protagonist in the BioShock series?',
        "category": 'Gaming',
        "correct": 'Jack (BioShock 1)',
        "wrong": ['Andrew Ryan', 'Booker DeWitt', 'Atlas']
    },
    {
        "text": 'What game engine does Unreal Tournament use?',
        "category": 'Gaming',
        "correct": 'Unreal Engine',
        "wrong": ['id Tech', 'Source Engine', 'CryEngine']
    },
    {
        "text": 'What is the name of the fictional disease in The Last of Us?',
        "category": 'Gaming',
        "correct": 'Cordyceps Brain Infection',
        "wrong": ['T-Virus', 'Green Flu', 'Harran Virus']
    },
    {
        "text": "Who is the creator of Five Nights at Freddy's?",
        "category": 'Gaming',
        "correct": 'Scott Cawthon',
        "wrong": ['Toby Fox', 'Daisuke Amaya', 'Edmund McMillen']
    },
    {
        "text": 'What is the name of the spacesuit in Dead Space?',
        "category": 'Gaming',
        "correct": 'RIG (Resource Integration Gear)',
        "wrong": ['EVA Suit', 'Power Armor', 'Hazard Suit']
    },
    {
        "text": 'What are the three Deathly Hallows in Harry Potter?',
        "category": 'Fandom',
        "correct": 'Elder Wand, Resurrection Stone, Invisibility Cloak',
        "wrong": ['Sword of Gryffindor, Time-Turner, Phoenix', "Philosopher's Stone, Marauder's Map, Cloak", 'Wand, Ring, Mirror']
    },
    {
        "text": "What is the name of Thor's hammer in Marvel comics?",
        "category": 'Fandom',
        "correct": 'Mjolnir',
        "wrong": ['Stormbreaker', 'Gungnir', 'Jarnbjorn']
    },
    {
        "text": 'What is the name of the rebel base in Star Wars: A New Hope?',
        "category": 'Fandom',
        "correct": 'Yavin 4',
        "wrong": ['Hoth', 'Endor', 'Dantooine']
    },
    {
        "text": "What is the name of Frodo's sword in Lord of the Rings?",
        "category": 'Fandom',
        "correct": 'Sting',
        "wrong": ['Glamdring', 'Orcrist', 'Andúril']
    },
    {
        "text": 'What are the four Hogwarts houses in Harry Potter?',
        "category": 'Fandom',
        "correct": 'Gryffindor, Slytherin, Ravenclaw, Hufflepuff',
        "wrong": ['Gryffindor, Slytherin, Beauxbatons, Durmstrang', 'Gryffindor, Ravenclaw, Merlin, Morgana', 'Lions, Snakes, Eagles, Badgers']
    },
    {
        "text": "What is the name of Captain America's shield material?",
        "category": 'Fandom',
        "correct": 'Vibranium',
        "wrong": ['Adamantium', 'Carbonadium', 'Uru']
    },
    {
        "text": 'What is the name of the school of magic Geralt belongs to in The Witcher?',
        "category": 'Fandom',
        "correct": 'School of the Wolf',
        "wrong": ['School of the Cat', 'School of the Griffin', 'School of the Bear']
    },
    {
        "text": "What is the name of Jon Snow's direwolf in Game of Thrones?",
        "category": 'Fandom',
        "correct": 'Ghost',
        "wrong": ['Grey Wind', 'Summer', 'Nymeria']
    },
    {
        "text": 'What is the name of the fictional language spoken by elves in Lord of the Rings?',
        "category": 'Fandom',
        "correct": 'Sindarin/Quenya',
        "wrong": ['Elvish', 'Valyrian', 'Common Tongue']
    },
    {
        "text": "What is the name of the main character's patronus in Harry Potter?",
        "category": 'Fandom',
        "correct": 'Stag',
        "wrong": ['Doe', 'Phoenix', 'Otter']
    },
    {
        "text": 'What is the name of the evil organization in Agents of SHIELD?',
        "category": 'Fandom',
        "correct": 'Hydra',
        "wrong": ['AIM', 'The Hand', 'Ten Rings']
    },
    {
        "text": "What is the name of Katniss's home district in The Hunger Games?",
        "category": 'Fandom',
        "correct": 'District 12',
        "wrong": ['District 13', 'District 1', 'District 4']
    },
    {
        "text": 'What is the name of the spice-producing planet in Dune?',
        "category": 'Fandom',
        "correct": 'Arrakis',
        "wrong": ['Caladan', 'Giedi Prime', 'Kaitain']
    },
    {
        "text": 'What is the maximum ability score in D&D 5e without magic items?',
        "category": 'D&D',
        "correct": '20',
        "wrong": ['18', '24', '30']
    },
    {
        "text": 'What dice do you roll for initiative in D&D?',
        "category": 'D&D',
        "correct": 'd20',
        "wrong": ['d10', 'd12', '2d6']
    },
    {
        "text": "What is the name of the Nine Hells' ruler in D&D lore?",
        "category": 'D&D',
        "correct": 'Asmodeus',
        "wrong": ['Baal', 'Mephistopheles', 'Zariel']
    },
    {
        "text": 'What is the name of the multiverse cosmology in D&D?',
        "category": 'D&D',
        "correct": 'The Great Wheel',
        "wrong": ['The Astral Sea', 'The Feywild', 'The Material Plane']
    },
    {
        "text": 'What level do most D&D 5e classes get their first subclass feature?',
        "category": 'D&D',
        "correct": 'Level 3 (except Cleric/Warlock at 1)',
        "wrong": ['Level 2', 'Level 1', 'Level 5']
    },
    {
        "text": 'What is the name of the iconic D&D dungeon adventure?',
        "category": 'D&D',
        "correct": 'Tomb of Horrors',
        "wrong": ['Curse of Strahd', 'Lost Mine of Phandelver', 'Waterdeep: Dragon Heist']
    },
    {
        "text": 'What is the highest level spell slot in D&D 5e?',
        "category": 'D&D',
        "correct": '9th level',
        "wrong": ['10th level', '8th level', '12th level']
    },
    {
        "text": "What is the name of the dragon goddess Tiamat's counterpart?",
        "category": 'D&D',
        "correct": 'Bahamut',
        "wrong": ['Io', 'Sardior', 'Chronepsis']
    },
    {
        "text": 'What is the Armor Class of a creature with no armor or Dex bonus?',
        "category": 'D&D',
        "correct": '10',
        "wrong": ['0', '12', '8']
    },
    {
        "text": 'What is the name of the iconic D&D vampire lord in Ravenloft?',
        "category": 'D&D',
        "correct": 'Strahd von Zarovich',
        "wrong": ['Vecna', 'Acererak', 'Demogorgon']
    },
    {
        "text": 'What damage type does a fireball spell deal?',
        "category": 'D&D',
        "correct": 'Fire',
        "wrong": ['Force', 'Radiant', 'Lightning']
    },
    {
        "text": 'What is the most common creature type in D&D bestiaries?',
        "category": 'D&D',
        "correct": 'Humanoid',
        "wrong": ['Beast', 'Monstrosity', 'Aberration']
    },
    {
        "text": 'What is the name of the iconic D&D lich?',
        "category": 'D&D',
        "correct": 'Vecna',
        "wrong": ['Acererak', 'Larloch', 'Szass Tam']
    },
    {
        "text": 'What ability score modifier applies to melee weapon attack rolls?',
        "category": 'D&D',
        "correct": 'Strength (or Dex for finesse)',
        "wrong": ['Dexterity only', 'Constitution', 'Intelligence']
    },
    {
        "text": 'What is the name of the D&D god of death?',
        "category": 'D&D',
        "correct": 'Kelemvor (Forgotten Realms)',
        "wrong": ['Myrkul', 'Nerull', 'Orcus']
    },
    {
        "text": "Who composed the '1812 Overture'?",
        "category": 'music',
        "correct": 'Pyotr Ilyich Tchaikovsky',
        "wrong": ['Sergei Rachmaninoff', 'Johannes Brahms', 'Franz Liszt']
    },
    {
        "text": 'What does CPU stand for in computing?',
        "category": 'technology',
        "correct": 'Central Processing Unit',
        "wrong": ['Computer Processing Unit', 'Core Processing Unit', 'Central Program Unit']
    },
    {
        "text": 'Who is credited with inventing the World Wide Web?',
        "category": 'technology',
        "correct": 'Tim Berners-Lee',
        "wrong": ['Bill Gates', 'Steve Jobs', 'Mark Zuckerberg']
    },
    {
        "text": 'What does HTML stand for?',
        "category": 'technology',
        "correct": 'HyperText Markup Language',
        "wrong": ['Home Tool Markup Language', 'High Tech Modern Language', 'Hyperlinks and Text Markup Language']
    },
    {
        "text": 'What was the first social media platform to reach 1 billion users?',
        "category": 'technology',
        "correct": 'Facebook',
        "wrong": ['Twitter', 'Instagram', 'YouTube']
    },
    {
        "text": 'What does USB stand for?',
        "category": 'technology',
        "correct": 'Universal Serial Bus',
        "wrong": ['Universal System Bus', 'Uniform Serial Bus', 'United Serial Bus']
    },
    {
        "text": "What is the name of Apple's virtual assistant?",
        "category": 'technology',
        "correct": 'Siri',
        "wrong": ['Google Assistant', 'Cortana', 'Alexa']
    },
    {
        "text": 'What does RAM stand for in computing?',
        "category": 'technology',
        "correct": 'Random Access Memory',
        "wrong": ['Remote Access Memory', 'Rapid Access Memory', 'Read Access Memory']
    },
    {
        "text": 'What programming language is known for its use in artificial intelligence?',
        "category": 'technology',
        "correct": 'Python',
        "wrong": ['C++', 'Java', 'Ruby']
    },
    {
        "text": 'What was the first commercially successful personal computer?',
        "category": 'technology',
        "correct": 'Apple II',
        "wrong": ['Commodore 64', 'IBM PC', 'Atari 800']
    },
    {
        "text": 'What does GPU stand for?',
        "category": 'technology',
        "correct": 'Graphics Processing Unit',
        "wrong": ['General Processing Unit', 'Graphical Program Unit', 'Game Processing Unit']
    },
    {
        "text": 'Who is the founder of Tesla and SpaceX?',
        "category": 'technology',
        "correct": 'Elon Musk',
        "wrong": ['Jeff Bezos', 'Richard Branson', 'Larry Page']
    },
    {
        "text": 'What year was Google founded?',
        "category": 'technology',
        "correct": '1998',
        "wrong": ['2000', '2002', '1995']
    },
    {
        "text": 'What does VPN stand for?',
        "category": 'technology',
        "correct": 'Virtual Private Network',
        "wrong": ['Verified Private Network', 'Virtual Protected Network', 'Virtual Public Network']
    },
    {
        "text": 'What is the most popular programming language for web development?',
        "category": 'technology',
        "correct": 'JavaScript',
        "wrong": ['C#', 'Python', 'Java']
    },
    {
        "text": 'What does SSD stand for in computer storage?',
        "category": 'technology',
        "correct": 'Solid State Drive',
        "wrong": ['Secure State Drive', 'System Storage Drive', 'Super Speed Drive']
    },
    {
        "text": 'Who founded Amazon?',
        "category": 'technology',
        "correct": 'Jeff Bezos',
        "wrong": ['Larry Ellison', 'Bill Gates', 'Elon Musk']
    },
    {
        "text": 'What is the name of the first electronic computer?',
        "category": 'technology',
        "correct": 'ENIAC',
        "wrong": ['IBM 701', 'UNIVAC', 'EDSAC']
    },
    {
        "text": 'What does AI stand for?',
        "category": 'technology',
        "correct": 'Artificial Intelligence',
        "wrong": ['Advanced Intelligence', 'Applied Intelligence', 'Automated Intelligence']
    },
    {
        "text": 'What year was Twitter founded?',
        "category": 'technology',
        "correct": '2006',
        "wrong": ['2010', '2004', '2008']
    },
    {
        "text": 'What is the binary system based on?',
        "category": 'technology',
        "correct": 'Base-2 (0s and 1s)',
        "wrong": ['Base-8', 'Base-16', 'Base-10']
    },
    {
        "text": 'Who co-founded Apple with Steve Jobs?',
        "category": 'technology',
        "correct": 'Steve Wozniak',
        "wrong": ['Ronald Wayne', 'Tim Cook', 'Bill Gates']
    },
    {
        "text": 'What does IoT stand for?',
        "category": 'technology',
        "correct": 'Internet of Things',
        "wrong": ['Integration of Technology', 'Interface of Technology', 'Internet of Transmission']
    },
    {
        "text": 'What is the most used operating system for smartphones?',
        "category": 'technology',
        "correct": 'Android',
        "wrong": ['iOS', 'BlackBerry OS', 'Windows Phone']
    },
    {
        "text": 'What does CAPTCHA stand for?',
        "category": 'technology',
        "correct": 'Completely Automated Public Turing test',
        "wrong": ['Controlled Access Public Test', 'Computer Automated Private Test', 'Cyber Authentication Protocol']
    },
    {
        "text": 'What year was YouTube founded?',
        "category": 'technology',
        "correct": '2005',
        "wrong": ['2007', '2009', '2003']
    },
    {
        "text": "What is the name of Amazon's voice assistant?",
        "category": 'technology',
        "correct": 'Alexa',
        "wrong": ['Cortana', 'Siri', 'Google Assistant']
    },
    {
        "text": 'What does SQL stand for in databases?',
        "category": 'technology',
        "correct": 'Structured Query Language',
        "wrong": ['Sequential Query Language', 'Standard Query Language', 'System Query Language']
    },
    {
        "text": 'Who founded Facebook?',
        "category": 'technology',
        "correct": 'Mark Zuckerberg',
        "wrong": ['Sergey Brin', 'Jack Dorsey', 'Larry Page']
    },
    {
        "text": 'What is the maximum speed of USB 3.0?',
        "category": 'technology',
        "correct": '5 Gbps',
        "wrong": ['480 Mbps', '2.5 Gbps', '10 Gbps']
    },
    {
        "text": 'What does API stand for in programming?',
        "category": 'technology',
        "correct": 'Application Programming Interface',
        "wrong": ['Automated Program Interface', 'Application Program Integration', 'Advanced Programming Interface']
    },
    {
        "text": 'What year was Linux first released?',
        "category": 'technology',
        "correct": '1991',
        "wrong": ['1987', '1999', '1995']
    },
    {
        "text": "What is the name of Google's mobile operating system?",
        "category": 'technology',
        "correct": 'Android',
        "wrong": ['Chrome OS', 'Windows', 'iOS']
    },
    {
        "text": 'What does HTTP stand for?',
        "category": 'technology',
        "correct": 'HyperText Transfer Protocol',
        "wrong": ['Home Transfer Protocol', 'Hyperlink Text Protocol', 'High Tech Transfer Protocol']
    },
    {
        "text": 'Who invented the transistor?',
        "category": 'technology',
        "correct": 'John Bardeen, Walter Brattain, William Shockley',
        "wrong": ['Alan Turing', 'Nikola Tesla', 'Thomas Edison']
    },
    {
        "text": 'What does BIOS stand for in computing?',
        "category": 'technology',
        "correct": 'Basic Input/Output System',
        "wrong": ['Boot Input/Output System', 'Base Integrated Operating System', 'Binary Input/Output System']
    },
    {
        "text": 'What year was the first text message sent?',
        "category": 'technology',
        "correct": '1992',
        "wrong": ['1998', '2000', '1985']
    },
    {
        "text": "What is the name of Microsoft's cloud computing platform?",
        "category": 'technology',
        "correct": 'Azure',
        "wrong": ['iCloud', 'Google Cloud', 'AWS']
    },
    {
        "text": 'What does DNS stand for in networking?',
        "category": 'technology',
        "correct": 'Domain Name System',
        "wrong": ['Domain Network Server', 'Data Name System', 'Digital Network System']
    },
    {
        "text": 'Who created the Python programming language?',
        "category": 'technology',
        "correct": 'Guido van Rossum',
        "wrong": ['Dennis Ritchie', 'James Gosling', 'Bjarne Stroustrup']
    },
    {
        "text": 'What is the smallest unit of data in computing?',
        "category": 'technology',
        "correct": 'Bit',
        "wrong": ['Nibble', 'Word', 'Byte']
    },
    {
        "text": 'What does 4G stand for in mobile networks?',
        "category": 'technology',
        "correct": 'Fourth Generation',
        "wrong": ['Frequency Generation', 'Four Gigabytes', 'Fast Generation']
    },
    {
        "text": 'What year was Instagram launched?',
        "category": 'technology',
        "correct": '2010',
        "wrong": ['2014', '2012', '2008']
    },
    {
        "text": "What is Moore's Law about?",
        "category": 'technology',
        "correct": 'Transistor density doubling every two years',
        "wrong": ['Computer size halving', 'Storage capacity tripling', 'Internet speed doubling']
    },
    {
        "text": 'What does HDMI stand for?',
        "category": 'technology',
        "correct": 'High-Definition Multimedia Interface',
        "wrong": ['High-Definition Media Input', 'Home Digital Media Interface', 'High Data Media Interface']
    },
    {
        "text": 'Who is known as the father of the computer?',
        "category": 'technology',
        "correct": 'Charles Babbage',
        "wrong": ['Ada Lovelace', 'Alan Turing', 'John von Neumann']
    },
    {
        "text": 'What does PDF stand for?',
        "category": 'technology',
        "correct": 'Portable Document Format',
        "wrong": ['Printed Document File', 'Protected Document Format', 'Public Document Format']
    },
    {
        "text": 'What is the name of the first web browser?',
        "category": 'technology',
        "correct": 'WorldWideWeb (later Nexus)',
        "wrong": ['Netscape Navigator', 'Internet Explorer', 'Mosaic']
    },
    {
        "text": 'What year was Bitcoin created?',
        "category": 'technology',
        "correct": '2009',
        "wrong": ['2007', '2011', '2013']
    },
    {
        "text": "Who directed the movie 'Pulp Fiction'?",
        "category": 'entertainment',
        "correct": 'Quentin Tarantino',
        "wrong": ['Steven Spielberg', 'Christopher Nolan', 'Martin Scorsese']
    },
    {
        "text": 'What year was the first Star Wars movie released?',
        "category": 'entertainment',
        "correct": '1977',
        "wrong": ['1980', '1983', '1975']
    },
    {
        "text": "Who played Jack in the movie 'Titanic'?",
        "category": 'entertainment',
        "correct": 'Leonardo DiCaprio',
        "wrong": ['Tom Cruise', 'Johnny Depp', 'Brad Pitt']
    },
    {
        "text": 'What TV show featured the characters Ross, Rachel, Monica, Chandler, Joey, and Phoebe?',
        "category": 'entertainment',
        "correct": 'Friends',
        "wrong": ['Seinfeld', 'The Big Bang Theory', 'How I Met Your Mother']
    },
    {
        "text": "Who directed 'The Godfather'?",
        "category": 'entertainment',
        "correct": 'Francis Ford Coppola',
        "wrong": ['Steven Spielberg', 'Brian De Palma', 'Martin Scorsese']
    },
    {
        "text": "What animated film features the song 'Let It Go'?",
        "category": 'entertainment',
        "correct": 'Frozen',
        "wrong": ['Moana', 'Tangled', 'The Lion King']
    },
    {
        "text": 'Who played Iron Man in the Marvel Cinematic Universe?',
        "category": 'entertainment',
        "correct": 'Robert Downey Jr.',
        "wrong": ['Chris Evans', 'Mark Ruffalo', 'Chris Hemsworth']
    },
    {
        "text": "What year did the TV show 'Breaking Bad' first air?",
        "category": 'entertainment',
        "correct": '2008',
        "wrong": ['2012', '2010', '2006']
    },
    {
        "text": "What is the name of the kingdom in Disney's 'Frozen'?",
        "category": 'entertainment',
        "correct": 'Arendelle',
        "wrong": ['Atlantica', 'DunBroch', 'Corona']
    },
    {
        "text": 'What year was Netflix founded?',
        "category": 'entertainment',
        "correct": '1997',
        "wrong": ['1995', '2002', '2000']
    },
    {
        "text": "Who directed 'Jurassic Park'?",
        "category": 'entertainment',
        "correct": 'Steven Spielberg',
        "wrong": ['George Lucas', 'James Cameron', 'Ridley Scott']
    },
    {
        "text": 'Who won the first season of American Idol?',
        "category": 'entertainment',
        "correct": 'Kelly Clarkson',
        "wrong": ['Carrie Underwood', 'Fantasia Barrino', 'Jennifer Hudson']
    },
    {
        "text": "What year did the final episode of 'Game of Thrones' air?",
        "category": 'entertainment',
        "correct": '2019',
        "wrong": ['2020', '2018', '2017']
    },
    {
        "text": "Who directed 'Schindler's List'?",
        "category": 'entertainment',
        "correct": 'Steven Spielberg',
        "wrong": ['Martin Scorsese', 'Ridley Scott', 'Francis Ford Coppola']
    },
    {
        "text": "What is the name of the dragon in 'The Hobbit'?",
        "category": 'entertainment',
        "correct": 'Smaug',
        "wrong": ['Drogon', 'Toothless', 'Falkor']
    },
    {
        "text": 'Who played Hermione Granger in the Harry Potter films?',
        "category": 'entertainment',
        "correct": 'Emma Watson',
        "wrong": ['Emily Blunt', 'Emma Roberts', 'Emma Stone']
    },
    {
        "text": "What year was the movie 'The Matrix' released?",
        "category": 'entertainment',
        "correct": '1999',
        "wrong": ['1997', '2001', '2003']
    },
    {
        "text": "What is the name of the fictional African country in 'Black Panther'?",
        "category": 'entertainment',
        "correct": 'Wakanda',
        "wrong": ['Sokovia', 'Zamunda', 'Genovia']
    },
    {
        "text": 'Who played Forrest Gump?',
        "category": 'entertainment',
        "correct": 'Tom Hanks',
        "wrong": ['Leonardo DiCaprio', 'Brad Pitt', 'Tom Cruise']
    },
    {
        "text": "What year did 'The Simpsons' first air?",
        "category": 'entertainment',
        "correct": '1989',
        "wrong": ['1985', '1987', '1991']
    },
    {
        "text": "Who directed 'E.T. the Extra-Terrestrial'?",
        "category": 'entertainment',
        "correct": 'Steven Spielberg',
        "wrong": ['Robert Zemeckis', 'George Lucas', 'James Cameron']
    },
    {
        "text": 'Who played Wolverine in the X-Men films?',
        "category": 'entertainment',
        "correct": 'Hugh Jackman',
        "wrong": ['Russell Crowe', 'Ryan Reynolds', 'Christian Bale']
    },
    {
        "text": "What year was 'The Lion King' released?",
        "category": 'entertainment',
        "correct": '1994',
        "wrong": ['1996', '1998', '1992']
    },
    {
        "text": "Who directed 'Fight Club'?",
        "category": 'entertainment',
        "correct": 'David Fincher',
        "wrong": ['Guy Ritchie', 'Quentin Tarantino', 'Christopher Nolan']
    },
    {
        "text": "What is the name of the island in 'Jurassic Park'?",
        "category": 'entertainment',
        "correct": 'Isla Nublar',
        "wrong": ['Monster Island', 'Skull Island', 'Isla Sorna']
    },
    {
        "text": "Who played the lead role in 'Mad Max: Fury Road'?",
        "category": 'entertainment',
        "correct": 'Tom Hardy',
        "wrong": ['Mel Gibson', 'Jason Statham', 'Chris Pratt']
    },
    {
        "text": "What year was the first 'Lord of the Rings' movie released?",
        "category": 'entertainment',
        "correct": '2001',
        "wrong": ['2003', '1999', '2005']
    },
    {
        "text": "Who directed 'The Grand Budapest Hotel'?",
        "category": 'entertainment',
        "correct": 'Wes Anderson',
        "wrong": ['Edgar Wright', 'Coen Brothers', 'Quentin Tarantino']
    },
    {
        "text": "Who played Katniss Everdeen in 'The Hunger Games'?",
        "category": 'entertainment',
        "correct": 'Jennifer Lawrence',
        "wrong": ['Emma Stone', 'Kristen Stewart', 'Shailene Woodley']
    },
    {
        "text": "What year did 'Stranger Things' first air?",
        "category": 'entertainment',
        "correct": '2016',
        "wrong": ['2018', '2015', '2014']
    },
    {
        "text": "Who directed 'Goodfellas'?",
        "category": 'entertainment',
        "correct": 'Martin Scorsese',
        "wrong": ['Quentin Tarantino', 'Francis Ford Coppola', 'Brian De Palma']
    },
    {
        "text": "What is the name of the spaceship in 'Alien'?",
        "category": 'entertainment',
        "correct": 'Nostromo',
        "wrong": ['Covenant', 'Prometheus', 'Sulaco']
    },
    {
        "text": "Who played James Bond in 'Casino Royale' (2006)?",
        "category": 'entertainment',
        "correct": 'Daniel Craig',
        "wrong": ['Sean Connery', 'Timothy Dalton', 'Pierce Brosnan']
    },
    {
        "text": "What year was 'Toy Story' released?",
        "category": 'entertainment',
        "correct": '1995',
        "wrong": ['1997', '1993', '1999']
    },
    {
        "text": "Who directed 'The Silence of the Lambs'?",
        "category": 'entertainment',
        "correct": 'Jonathan Demme',
        "wrong": ['David Fincher', 'Ridley Scott', 'Michael Mann']
    },
    {
        "text": "What is the name of the prison in 'The Shawshank Redemption'?",
        "category": 'entertainment',
        "correct": 'Shawshank State Penitentiary',
        "wrong": ['San Quentin', 'Sing Sing', 'Alcatraz']
    },
    {
        "text": "Who played Gandalf in 'The Lord of the Rings'?",
        "category": 'entertainment',
        "correct": 'Ian McKellen',
        "wrong": ['Patrick Stewart', 'Michael Gambon', 'Christopher Lee']
    },
    {
        "text": "What year was 'Back to the Future' released?",
        "category": 'entertainment',
        "correct": '1985',
        "wrong": ['1983', '1989', '1987']
    },
    {
        "text": "Who directed 'Gladiator'?",
        "category": 'entertainment',
        "correct": 'Ridley Scott',
        "wrong": ['Peter Jackson', 'James Cameron', 'Steven Spielberg']
    },
    {
        "text": "What is the name of the main character in 'The Matrix'?",
        "category": 'entertainment',
        "correct": 'Neo (Thomas Anderson)',
        "wrong": ['Trinity', 'Smith', 'Morpheus']
    },
    {
        "text": 'Who played Captain Jack Sparrow?',
        "category": 'entertainment',
        "correct": 'Johnny Depp',
        "wrong": ['Geoffrey Rush', 'Javier Bardem', 'Orlando Bloom']
    },
    {
        "text": "What year was 'The Wizard of Oz' released?",
        "category": 'entertainment',
        "correct": '1939',
        "wrong": ['1941', '1945', '1937']
    },
    {
        "text": 'Who holds the record for the most home runs in a single MLB season?',
        "category": 'sports',
        "correct": 'Barry Bonds (73)',
        "wrong": ['Sammy Sosa', 'Babe Ruth', 'Mark McGwire']
    },
    {
        "text": 'What country won the first FIFA World Cup in 1930?',
        "category": 'sports',
        "correct": 'Uruguay',
        "wrong": ['Argentina', 'Brazil', 'Italy']
    },
    {
        "text": "Who has won the most Grand Slam titles in men's tennis?",
        "category": 'sports',
        "correct": 'Novak Djokovic (24)',
        "wrong": ['Pete Sampras', 'Roger Federer', 'Rafael Nadal']
    },
    {
        "text": 'What year were the first modern Olympic Games held?',
        "category": 'sports',
        "correct": '1896',
        "wrong": ['1888', '1900', '1892']
    },
    {
        "text": 'Who is the all-time leading scorer in NBA history?',
        "category": 'sports',
        "correct": 'LeBron James',
        "wrong": ['Michael Jordan', 'Kareem Abdul-Jabbar', 'Kobe Bryant']
    },
    {
        "text": "What boxer was known as 'The Greatest'?",
        "category": 'sports',
        "correct": 'Muhammad Ali',
        "wrong": ['Mike Tyson', 'Sugar Ray Robinson', 'Floyd Mayweather']
    },
    {
        "text": 'How many Super Bowl rings does Tom Brady have?',
        "category": 'sports',
        "correct": '7',
        "wrong": ['6', '5', '8']
    },
    {
        "text": 'What country hosted the 2016 Summer Olympics?',
        "category": 'sports',
        "correct": 'Brazil',
        "wrong": ['UK', 'Greece', 'China']
    },
    {
        "text": 'Who won the FIFA World Cup in 2018?',
        "category": 'sports',
        "correct": 'France',
        "wrong": ['Germany', 'Brazil', 'Croatia']
    },
    {
        "text": 'What is the maximum break in snooker?',
        "category": 'sports',
        "correct": '147',
        "wrong": ['180', '150', '200']
    },
    {
        "text": 'Who holds the record for most goals in a calendar year?',
        "category": 'sports',
        "correct": 'Lionel Messi (91 in 2012)',
        "wrong": ['Pele', 'Cristiano Ronaldo', 'Gerd Müller']
    },
    {
        "text": 'What year did Michael Jordan retire for the final time?',
        "category": 'sports',
        "correct": '2003',
        "wrong": ['1999', '2005', '2001']
    },
    {
        "text": 'Who has won the most Tour de France titles?',
        "category": 'sports',
        "correct": 'Lance Armstrong (titles stripped), Jacques Anquetil, Eddy Merckx, Bernard Hinault, Miguel Indurain (5 each)',
        "wrong": ['Alberto Contador', 'Greg LeMond', 'Chris Froome']
    },
    {
        "text": 'What is the national sport of Canada?',
        "category": 'sports',
        "correct": 'Lacrosse and Ice Hockey',
        "wrong": ['Baseball', 'Basketball', 'Football']
    },
    {
        "text": 'Who was the youngest heavyweight boxing champion?',
        "category": 'sports',
        "correct": 'Mike Tyson',
        "wrong": ['Evander Holyfield', 'Muhammad Ali', 'Floyd Patterson']
    },
    {
        "text": 'What year did Usain Bolt set the 100m world record?',
        "category": 'sports',
        "correct": '2009',
        "wrong": ['2012', '2008', '2016']
    },
    {
        "text": 'How many players are on a rugby union team?',
        "category": 'sports',
        "correct": '15',
        "wrong": ['13', '7', '11']
    },
    {
        "text": 'Who won the first UFC championship?',
        "category": 'sports',
        "correct": 'Royce Gracie',
        "wrong": ['Ken Shamrock', 'Dan Severn', 'Randy Couture']
    },
    {
        "text": 'What is the diameter of a basketball hoop in inches?',
        "category": 'sports',
        "correct": '18 inches',
        "wrong": ['20 inches', '22 inches', '16 inches']
    },
    {
        "text": 'Who has won the most Formula 1 World Championships?',
        "category": 'sports',
        "correct": 'Lewis Hamilton and Michael Schumacher (7 each)',
        "wrong": ['Ayrton Senna', 'Sebastian Vettel', 'Juan Manuel Fangio']
    },
    {
        "text": 'What year did Roger Federer win his first Wimbledon?',
        "category": 'sports',
        "correct": '2003',
        "wrong": ['2001', '2005', '2000']
    },
    {
        "text": 'Who holds the record for most career strikeouts in MLB?',
        "category": 'sports',
        "correct": 'Nolan Ryan',
        "wrong": ['Roger Clemens', 'Randy Johnson', 'Steve Carlton']
    },
    {
        "text": 'What country has won the most Rugby World Cups?',
        "category": 'sports',
        "correct": 'New Zealand (3) and South Africa (3)',
        "wrong": ['France', 'Australia', 'England']
    },
    {
        "text": 'Who was the first athlete to run a sub-4-minute mile?',
        "category": 'sports',
        "correct": 'Roger Bannister',
        "wrong": ['Jesse Owens', 'Paavo Nurmi', 'Emil Zátopek']
    },
    {
        "text": 'What is the maximum score in a single frame of bowling?',
        "category": 'sports',
        "correct": '30',
        "wrong": ['10', '20', '300']
    },
    {
        "text": 'Who won the NBA MVP award in 2023?',
        "category": 'sports',
        "correct": 'Joel Embiid',
        "wrong": ['Luka Doncic', 'Giannis Antetokounmpo', 'Nikola Jokic']
    },
    {
        "text": 'What year was the first Super Bowl played?',
        "category": 'sports',
        "correct": '1967',
        "wrong": ['1969', '1970', '1965']
    },
    {
        "text": 'Who has won the most Olympic gold medals?',
        "category": 'sports',
        "correct": 'Michael Phelps (23)',
        "wrong": ['Simone Biles', 'Carl Lewis', 'Usain Bolt']
    },
    {
        "text": 'What is the length of a marathon in kilometers?',
        "category": 'sports',
        "correct": '42.195 km',
        "wrong": ['40 km', '50 km', '45 km']
    },
    {
        "text": 'Who holds the record for most goals in World Cup history?',
        "category": 'sports',
        "correct": 'Miroslav Klose (16)',
        "wrong": ['Gerd Müller', 'Ronaldo', 'Pele']
    },
    {
        "text": 'What year did Tiger Woods win his first Masters?',
        "category": 'sports',
        "correct": '1997',
        "wrong": ['1999', '1995', '2000']
    },
    {
        "text": 'How many games are in a standard NBA season (pre-2023)?',
        "category": 'sports',
        "correct": '82',
        "wrong": ['90', '72', '76']
    },
    {
        "text": 'Who was the first overall pick in the 2003 NBA Draft?',
        "category": 'sports',
        "correct": 'LeBron James',
        "wrong": ['Dwyane Wade', 'Chris Bosh', 'Carmelo Anthony']
    },
    {
        "text": 'What is the term for three strikes in a row in bowling?',
        "category": 'sports',
        "correct": 'Turkey',
        "wrong": ['Eagle', 'Triple', 'Hat Trick']
    },
    {
        "text": "Who won the FIFA Women's World Cup in 2023?",
        "category": 'sports',
        "correct": 'Spain',
        "wrong": ['Sweden', 'USA', 'England']
    },
    {
        "text": 'What year did the NBA introduce the three-point line?',
        "category": 'sports',
        "correct": '1979',
        "wrong": ['1983', '1975', '1987']
    },
    {
        "text": 'Who holds the record for most career assists in the NBA?',
        "category": 'sports',
        "correct": 'John Stockton',
        "wrong": ['Chris Paul', 'Steve Nash', 'Magic Johnson']
    },
    {
        "text": 'What is the oldest tennis tournament in the world?',
        "category": 'sports',
        "correct": 'Wimbledon',
        "wrong": ['Australian Open', 'French Open', 'US Open']
    },
    {
        "text": 'Who was the first African-American to play in Major League Baseball?',
        "category": 'sports',
        "correct": 'Jackie Robinson',
        "wrong": ['Satchel Paige', 'Hank Aaron', 'Willie Mays']
    },
    {
        "text": 'What year did the Chicago Bulls win their first NBA championship?',
        "category": 'sports',
        "correct": '1991',
        "wrong": ['1989', '1993', '1987']
    },
    {
        "text": 'How many players are on a baseball field for each team?',
        "category": 'sports',
        "correct": '9',
        "wrong": ['11', '8', '10']
    },
    {
        "text": 'Who holds the record for most career home runs in MLB?',
        "category": 'sports',
        "correct": 'Barry Bonds (762)',
        "wrong": ['Babe Ruth', 'Hank Aaron', 'Alex Rodriguez']
    },
    {
        "text": 'What country won the first ever Cricket World Cup in 1975?',
        "category": 'sports',
        "correct": 'West Indies',
        "wrong": ['India', 'England', 'Australia']
    },
    {
        "text": 'Who was the first woman to win an IndyCar race?',
        "category": 'sports',
        "correct": 'Danica Patrick',
        "wrong": ['Simona de Silvestro', 'Janet Guthrie', 'Sarah Fisher']
    },
    {
        "text": 'What is the regulation height of a basketball hoop in feet?',
        "category": 'sports',
        "correct": '10 feet',
        "wrong": ['12 feet', '9 feet', '11 feet']
    },
    {
        "text": 'Who holds the record for most consecutive games played in MLB?',
        "category": 'sports',
        "correct": 'Cal Ripken Jr. (2,632)',
        "wrong": ['Derek Jeter', 'Pete Rose', 'Lou Gehrig']
    },
    {
        "text": 'What year was the first Wimbledon Championships held?',
        "category": 'sports',
        "correct": '1877',
        "wrong": ['1920', '1850', '1900']
    },
    {
        "text": 'Who has won the most PGA Tour events?',
        "category": 'sports',
        "correct": 'Sam Snead (82)',
        "wrong": ['Tiger Woods', 'Jack Nicklaus', 'Arnold Palmer']
    },
    {
        "text": 'What is the name of the trophy awarded to the NHL champions?',
        "category": 'sports',
        "correct": 'Stanley Cup',
        "wrong": ["Larry O'Brien Trophy", "Commissioner's Trophy", 'Vince Lombardi Trophy']
    },
    {
        "text": "Who is known as the 'King of Pop'?",
        "category": 'music',
        "correct": 'Michael Jackson',
        "wrong": ['Prince', 'Elvis Presley', 'Justin Timberlake']
    },
    {
        "text": 'What band was Freddie Mercury the lead singer of?',
        "category": 'music',
        "correct": 'Queen',
        "wrong": ['Led Zeppelin', 'The Rolling Stones', 'The Beatles']
    },
    {
        "text": "What year was The Beatles' 'Sgt. Pepper's Lonely Hearts Club Band' released?",
        "category": 'music',
        "correct": '1967',
        "wrong": ['1970', '1969', '1965']
    },
    {
        "text": 'Who composed the Four Seasons?',
        "category": 'music',
        "correct": 'Antonio Vivaldi',
        "wrong": ['Ludwig van Beethoven', 'Wolfgang Amadeus Mozart', 'Johann Sebastian Bach']
    },
    {
        "text": 'Who won the first Grammy Award for Album of the Year?',
        "category": 'music',
        "correct": 'Henry Mancini (The Music from Peter Gunn)',
        "wrong": ['Nat King Cole', 'Elvis Presley', 'Frank Sinatra']
    },
    {
        "text": 'What is the real name of rapper Eminem?',
        "category": 'music',
        "correct": 'Marshall Bruce Mathers III',
        "wrong": ['Andre Romelle Young', 'Curtis James Jackson III', 'Calvin Cordozar Broadus Jr.']
    },
    {
        "text": "Who wrote the opera 'The Magic Flute'?",
        "category": 'music',
        "correct": 'Wolfgang Amadeus Mozart',
        "wrong": ['Richard Wagner', 'Giuseppe Verdi', 'Ludwig van Beethoven']
    },
    {
        "text": 'What year did Elvis Presley die?',
        "category": 'music',
        "correct": '1977',
        "wrong": ['1980', '1975', '1979']
    },
    {
        "text": 'Who holds the record for most Grammy Awards won?',
        "category": 'music',
        "correct": 'Beyoncé (32)',
        "wrong": ['Alison Krauss', 'Quincy Jones', 'Georg Solti']
    },
    {
        "text": "What is the name of Taylor Swift's first album?",
        "category": 'music',
        "correct": 'Taylor Swift',
        "wrong": ['Fearless', 'Red', 'Speak Now']
    },
    {
        "text": 'Who was the original drummer for The Beatles?',
        "category": 'music',
        "correct": 'Pete Best',
        "wrong": ['Stuart Sutcliffe', 'George Harrison', 'Ringo Starr']
    },
    {
        "text": "What year was 'Bohemian Rhapsody' released?",
        "category": 'music',
        "correct": '1975',
        "wrong": ['1979', '1977', '1973']
    },
    {
        "text": 'What is the best-selling single of all time?',
        "category": 'music',
        "correct": 'White Christmas by Bing Crosby',
        "wrong": ['Thriller by Michael Jackson', 'I Will Always Love You by Whitney Houston', 'Candle in the Wind by Elton John']
    },
    {
        "text": 'Who was the lead singer of Nirvana?',
        "category": 'music',
        "correct": 'Kurt Cobain',
        "wrong": ['Dave Grohl', 'Eddie Vedder', 'Chris Cornell']
    },
    {
        "text": 'What year did Woodstock music festival take place?',
        "category": 'music',
        "correct": '1969',
        "wrong": ['1973', '1971', '1967']
    },
    {
        "text": "Who wrote 'Für Elise'?",
        "category": 'music',
        "correct": 'Ludwig van Beethoven',
        "wrong": ['Franz Schubert', 'Johann Sebastian Bach', 'Wolfgang Amadeus Mozart']
    },
    {
        "text": 'What is the real name of Lady Gaga?',
        "category": 'music',
        "correct": 'Stefani Joanne Angelina Germanotta',
        "wrong": ['Robyn Rihanna Fenty', 'Madonna Louise Ciccone', 'Beyoncé Giselle Knowles']
    },
    {
        "text": "Who is known as the 'Queen of Soul'?",
        "category": 'music',
        "correct": 'Aretha Franklin',
        "wrong": ['Tina Turner', 'Diana Ross', 'Whitney Houston']
    },
    {
        "text": 'What year was MTV launched?',
        "category": 'music',
        "correct": '1981',
        "wrong": ['1979', '1985', '1983']
    },
    {
        "text": "Who composed 'The Nutcracker'?",
        "category": 'music',
        "correct": 'Pyotr Ilyich Tchaikovsky',
        "wrong": ['Sergei Prokofiev', 'Dmitri Shostakovich', 'Igor Stravinsky']
    },
    {
        "text": 'What is the best-selling album by a female artist?',
        "category": 'music',
        "correct": 'The Bodyguard soundtrack by Whitney Houston',
        "wrong": ['Come On Over by Shania Twain', 'Thriller by Michael Jackson', '21 by Adele']
    },
    {
        "text": 'Who was the first artist to have a Billboard Hot 100 number-one single, album, and film simultaneously?',
        "category": 'music',
        "correct": 'Dolly Parton',
        "wrong": ['Whitney Houston', 'Madonna', 'Cher']
    },
    {
        "text": 'What year did The Beatles break up?',
        "category": 'music',
        "correct": '1970',
        "wrong": ['1968', '1969', '1972']
    },
    {
        "text": "Who wrote 'Rhapsody in Blue'?",
        "category": 'music',
        "correct": 'George Gershwin',
        "wrong": ['Aaron Copland', 'Leonard Bernstein', 'Duke Ellington']
    },
    {
        "text": 'What is the real name of Bono from U2?',
        "category": 'music',
        "correct": 'Paul David Hewson',
        "wrong": ['Adam Clayton', 'David Evans', 'Larry Mullen Jr.']
    },
    {
        "text": 'Who holds the record for most number-one singles on the Billboard Hot 100?',
        "category": 'music',
        "correct": 'The Beatles (20)',
        "wrong": ['Madonna', 'Mariah Carey', 'Elvis Presley']
    },
    {
        "text": 'What year did Johnny Cash perform at Folsom Prison?',
        "category": 'music',
        "correct": '1968',
        "wrong": ['1970', '1972', '1965']
    },
    {
        "text": "Who composed 'The Planets' suite?",
        "category": 'music',
        "correct": 'Gustav Holst',
        "wrong": ['Maurice Ravel', 'Ralph Vaughan Williams', 'Claude Debussy']
    },
    {
        "text": "What is the name of Beyoncé's visual album released in 2016?",
        "category": 'music',
        "correct": 'Lemonade',
        "wrong": ['Beyoncé', '4', 'Renaissance']
    },
    {
        "text": 'Who was the first rapper to win a Pulitzer Prize?',
        "category": 'music',
        "correct": 'Kendrick Lamar',
        "wrong": ['Jay-Z', 'Kanye West', 'Nas']
    },
    {
        "text": 'What year did Jimi Hendrix die?',
        "category": 'music',
        "correct": '1970',
        "wrong": ['1968', '1969', '1972']
    },
    {
        "text": "Who wrote 'Canon in D'?",
        "category": 'music',
        "correct": 'Johann Pachelbel',
        "wrong": ['George Frideric Handel', 'Johann Sebastian Bach', 'Antonio Vivaldi']
    },
    {
        "text": 'What is the best-selling rap album of all time?',
        "category": 'music',
        "correct": 'Speakerboxxx/The Love Below by OutKast',
        "wrong": ['The Marshall Mathers LP by Eminem', 'The Chronic by Dr. Dre', 'All Eyez on Me by 2Pac']
    },
    {
        "text": 'Who was the lead guitarist of Led Zeppelin?',
        "category": 'music',
        "correct": 'Jimmy Page',
        "wrong": ['Jimi Hendrix', 'Eddie Van Halen', 'Eric Clapton']
    },
    {
        "text": 'What year was Live Aid held?',
        "category": 'music',
        "correct": '1985',
        "wrong": ['1989', '1987', '1983']
    },
    {
        "text": "Who composed 'Bolero'?",
        "category": 'music',
        "correct": 'Maurice Ravel',
        "wrong": ['Igor Stravinsky', 'Erik Satie', 'Claude Debussy']
    },
    {
        "text": 'What is the real name of rapper Snoop Dogg?',
        "category": 'music',
        "correct": 'Calvin Cordozar Broadus Jr.',
        "wrong": ['Andre Romelle Young', 'Marshall Bruce Mathers III', 'Curtis James Jackson III']
    },
    {
        "text": 'Who was the first woman inducted into the Rock and Roll Hall of Fame?',
        "category": 'music',
        "correct": 'Aretha Franklin',
        "wrong": ['Janis Joplin', 'Tina Turner', 'Diana Ross']
    },
    {
        "text": "What year did David Bowie release 'Space Oddity'?",
        "category": 'music',
        "correct": '1969',
        "wrong": ['1967', '1973', '1971']
    },
    {
        "text": "Who wrote the opera 'Carmen'?",
        "category": 'music',
        "correct": 'Georges Bizet',
        "wrong": ['Giuseppe Verdi', 'Richard Wagner', 'Giacomo Puccini']
    },
    {
        "text": "What is the name of Adele's first album?",
        "category": 'music',
        "correct": '19',
        "wrong": ['21', '30', '25']
    },
    {
        "text": 'Who holds the record for longest-running number one song on Billboard Hot 100?',
        "category": 'music',
        "correct": "Lil Nas X ('Old Town Road' - 19 weeks)",
        "wrong": ['Mariah Carey', 'Boyz II Men', 'The Beatles']
    },
    {
        "text": 'What year did Bob Marley die?',
        "category": 'music',
        "correct": '1981',
        "wrong": ['1977', '1983', '1979']
    },
    {
        "text": "Who composed 'The Ride of the Valkyries'?",
        "category": 'music',
        "correct": 'Richard Wagner',
        "wrong": ['Giuseppe Verdi', 'Johannes Brahms', 'Franz Liszt']
    },
    {
        "text": "What is the name of Pink Floyd's best-selling album?",
        "category": 'music',
        "correct": 'The Dark Side of the Moon',
        "wrong": ['Animals', 'Wish You Were Here', 'The Wall']
    },
    {
        "text": 'Who was the original lead singer of Van Halen?',
        "category": 'music',
        "correct": 'David Lee Roth',
        "wrong": ['Eddie Van Halen', 'Sammy Hagar', 'Gary Cherone']
    },
    {
        "text": "What year was 'Thriller' released?",
        "category": 'music',
        "correct": '1982',
        "wrong": ['1980', '1986', '1984']
    },
    {
        "text": "Who wrote 'The Messiah' oratorio?",
        "category": 'music',
        "correct": 'George Frideric Handel',
        "wrong": ['Johann Sebastian Bach', 'Antonio Vivaldi', 'Joseph Haydn']
    },
    {
        "text": "What year was 'Pride and Prejudice' published?",
        "category": 'literature',
        "correct": '1813',
        "wrong": ['1825', '1805', '1820']
    },
    {
        "text": 'What is the longest novel ever written?',
        "category": 'literature',
        "correct": 'In Search of Lost Time by Marcel Proust',
        "wrong": ['Les Misérables by Victor Hugo', 'Atlas Shrugged by Ayn Rand', 'War and Peace by Leo Tolstoy']
    },
    {
        "text": "Who wrote 'The Catcher in the Rye'?",
        "category": 'literature',
        "correct": 'J.D. Salinger',
        "wrong": ['Jack Kerouac', 'Ken Kesey', 'Ernest Hemingway']
    },
    {
        "text": "Who wrote 'The Odyssey'?",
        "category": 'literature',
        "correct": 'Homer',
        "wrong": ['Sophocles', 'Euripides', 'Virgil']
    },
    {
        "text": 'What year did William Shakespeare die?',
        "category": 'literature',
        "correct": '1616',
        "wrong": ['1610', '1625', '1620']
    },
    {
        "text": "Who wrote 'Moby-Dick'?",
        "category": 'literature',
        "correct": 'Herman Melville',
        "wrong": ['Edgar Allan Poe', 'Nathaniel Hawthorne', 'Mark Twain']
    },
    {
        "text": 'What is the best-selling fiction book of all time?',
        "category": 'literature',
        "correct": 'Don Quixote by Miguel de Cervantes',
        "wrong": ['A Tale of Two Cities by Charles Dickens', 'The Lord of the Rings by J.R.R. Tolkien', 'Harry Potter series by J.K. Rowling']
    },
    {
        "text": "Who wrote 'The Brothers Karamazov'?",
        "category": 'literature',
        "correct": 'Fyodor Dostoevsky',
        "wrong": ['Leo Tolstoy', 'Anton Chekhov', 'Ivan Turgenev']
    },
    {
        "text": "What year was 'Frankenstein' published?",
        "category": 'literature',
        "correct": '1818',
        "wrong": ['1815', '1825', '1820']
    },
    {
        "text": "Who wrote 'The Divine Comedy'?",
        "category": 'literature',
        "correct": 'Dante Alighieri',
        "wrong": ['Virgil', 'Petrarch', 'Boccaccio']
    },
    {
        "text": 'What is the pen name of Samuel Clemens?',
        "category": 'literature',
        "correct": 'Mark Twain',
        "wrong": ['George Eliot', 'Lewis Carroll', 'O. Henry']
    },
    {
        "text": "Who wrote 'One Hundred Years of Solitude'?",
        "category": 'literature',
        "correct": 'Gabriel García Márquez',
        "wrong": ['Pablo Neruda', 'Jorge Luis Borges', 'Isabel Allende']
    },
    {
        "text": "What year did Jane Austen publish 'Emma'?",
        "category": 'literature',
        "correct": '1815',
        "wrong": ['1810', '1813', '1820']
    },
    {
        "text": "Who wrote 'The Picture of Dorian Gray'?",
        "category": 'literature',
        "correct": 'Oscar Wilde',
        "wrong": ['Thomas Hardy', 'Charles Dickens', 'H.G. Wells']
    },
    {
        "text": 'What is the real name of George Orwell?',
        "category": 'literature',
        "correct": 'Eric Arthur Blair',
        "wrong": ['Eric George Blair', 'Arthur Eric Blair', 'George Arthur Blair']
    },
    {
        "text": "Who wrote 'Brave New World'?",
        "category": 'literature',
        "correct": 'Aldous Huxley',
        "wrong": ['H.G. Wells', 'Ray Bradbury', 'George Orwell']
    },
    {
        "text": "What year was 'The Lord of the Rings: The Fellowship of the Ring' published?",
        "category": 'literature',
        "correct": '1954',
        "wrong": ['1958', '1960', '1950']
    },
    {
        "text": "Who wrote 'Crime and Punishment'?",
        "category": 'literature',
        "correct": 'Fyodor Dostoevsky',
        "wrong": ['Anton Chekhov', 'Leo Tolstoy', 'Nikolai Gogol']
    },
    {
        "text": "What is the first line of 'The Metamorphosis' by Franz Kafka?",
        "category": 'literature',
        "correct": 'As Gregor Samsa awoke one morning from uneasy dreams he found himself transformed in his bed into a gigantic insect',
        "wrong": ['It was the best of times', 'Call me Ishmael', 'All happy families are alike']
    },
    {
        "text": "Who wrote 'Wuthering Heights'?",
        "category": 'literature',
        "correct": 'Emily Brontë',
        "wrong": ['Jane Austen', 'Charlotte Brontë', 'George Eliot']
    },
    {
        "text": 'What year did Ernest Hemingway win the Nobel Prize in Literature?',
        "category": 'literature',
        "correct": '1954',
        "wrong": ['1950', '1958', '1960']
    },
    {
        "text": "Who wrote 'Ulysses'?",
        "category": 'literature',
        "correct": 'James Joyce',
        "wrong": ['Ezra Pound', 'T.S. Eliot', 'Virginia Woolf']
    },
    {
        "text": 'What is the real name of Lewis Carroll?',
        "category": 'literature',
        "correct": 'Charles Lutwidge Dodgson',
        "wrong": ['Lewis Charles Dodgson', 'Charles Dodgson Lewis', 'Lutwidge Charles Dodgson']
    },
    {
        "text": "Who wrote 'The Grapes of Wrath'?",
        "category": 'literature',
        "correct": 'John Steinbeck',
        "wrong": ['Ernest Hemingway', 'F. Scott Fitzgerald', 'William Faulkner']
    },
    {
        "text": "What year was 'The Hobbit' first published?",
        "category": 'literature',
        "correct": '1937',
        "wrong": ['1940', '1945', '1935']
    },
    {
        "text": "Who wrote 'Les Misérables'?",
        "category": 'literature',
        "correct": 'Victor Hugo',
        "wrong": ['Honoré de Balzac', 'Alexandre Dumas', 'Gustave Flaubert']
    },
    {
        "text": "What is the first book in 'The Chronicles of Narnia' series (publication order)?",
        "category": 'literature',
        "correct": 'The Lion, the Witch and the Wardrobe',
        "wrong": ['Prince Caspian', "The Magician's Nephew", 'The Voyage of the Dawn Treader']
    },
    {
        "text": "Who wrote 'A Clockwork Orange'?",
        "category": 'literature',
        "correct": 'Anthony Burgess',
        "wrong": ['Ray Bradbury', 'George Orwell', 'Aldous Huxley']
    },
    {
        "text": "What year did Charles Dickens publish 'A Christmas Carol'?",
        "category": 'literature',
        "correct": '1843',
        "wrong": ['1845', '1840', '1850']
    },
    {
        "text": "Who wrote 'The Canterbury Tales'?",
        "category": 'literature',
        "correct": 'Geoffrey Chaucer',
        "wrong": ['Edmund Spenser', 'William Shakespeare', 'John Milton']
    },
    {
        "text": 'What is the pen name of Mary Ann Evans?',
        "category": 'literature',
        "correct": 'George Eliot',
        "wrong": ['Emily Brontë', 'Charlotte Brontë', 'George Sand']
    },
    {
        "text": "Who wrote 'Slaughterhouse-Five'?",
        "category": 'literature',
        "correct": 'Kurt Vonnegut',
        "wrong": ['Joseph Heller', 'Philip K. Dick', 'Ken Kesey']
    },
    {
        "text": "What year was 'Dracula' published?",
        "category": 'literature',
        "correct": '1897',
        "wrong": ['1905', '1900', '1890']
    },
    {
        "text": "Who wrote 'The Sound and the Fury'?",
        "category": 'literature',
        "correct": 'William Faulkner',
        "wrong": ['John Steinbeck', 'F. Scott Fitzgerald', 'Ernest Hemingway']
    },
    {
        "text": "What is the first line of 'Moby-Dick'?",
        "category": 'literature',
        "correct": 'Call me Ishmael',
        "wrong": ['All happy families are alike', 'It is a truth universally acknowledged', 'It was the best of times']
    },
    {
        "text": "Who wrote 'The Handmaid's Tale'?",
        "category": 'literature',
        "correct": 'Margaret Atwood',
        "wrong": ['Doris Lessing', 'Octavia Butler', 'Ursula K. Le Guin']
    },
    {
        "text": 'What year did J.R.R. Tolkien die?',
        "category": 'literature',
        "correct": '1973',
        "wrong": ['1975', '1978', '1970']
    },
    {
        "text": "Who wrote 'The Old Man and the Sea'?",
        "category": 'literature',
        "correct": 'Ernest Hemingway',
        "wrong": ['John Steinbeck', 'F. Scott Fitzgerald', 'William Faulkner']
    },
    {
        "text": 'What is the pen name of Theodor Seuss Geisel?',
        "category": 'literature',
        "correct": 'Dr. Seuss',
        "wrong": ['Maurice Sendak', 'Shel Silverstein', 'Roald Dahl']
    },
    {
        "text": "Who wrote 'The Stranger' (L'Étranger)?",
        "category": 'literature',
        "correct": 'Albert Camus',
        "wrong": ['André Gide', 'Jean-Paul Sartre', 'Simone de Beauvoir']
    },
    {
        "text": "What year was 'Alice's Adventures in Wonderland' published?",
        "category": 'literature',
        "correct": '1865',
        "wrong": ['1875', '1860', '1870']
    },
    {
        "text": "Who wrote 'Invisible Man'?",
        "category": 'literature',
        "correct": 'Ralph Ellison',
        "wrong": ['Richard Wright', 'Toni Morrison', 'James Baldwin']
    },
    {
        "text": "What is the first line of 'Anna Karenina'?",
        "category": 'literature',
        "correct": 'All happy families are alike; each unhappy family is unhappy in its own way',
        "wrong": ['It was the best of times', 'Call me Ishmael', 'It is a truth universally acknowledged']
    },
    {
        "text": "Who wrote 'The Sun Also Rises'?",
        "category": 'literature',
        "correct": 'Ernest Hemingway',
        "wrong": ['William Faulkner', 'F. Scott Fitzgerald', 'John Steinbeck']
    },
    {
        "text": "What year did Virginia Woolf publish 'Mrs Dalloway'?",
        "category": 'literature',
        "correct": '1925',
        "wrong": ['1920', '1935', '1930']
    },
    {
        "text": 'What year was the Mona Lisa painted?',
        "category": 'art',
        "correct": '1503-1519',
        "wrong": ['1480-1485', '1520-1525', '1490-1495']
    },
    {
        "text": "Who sculpted 'David'?",
        "category": 'art',
        "correct": 'Michelangelo',
        "wrong": ['Donatello', 'Leonardo da Vinci', 'Raphael']
    },
    {
        "text": 'What art movement was Pablo Picasso associated with?',
        "category": 'art',
        "correct": 'Cubism',
        "wrong": ['Surrealism', 'Abstract Expressionism', 'Impressionism']
    },
    {
        "text": 'What year did the Dutch Golden Age of painting begin?',
        "category": 'art',
        "correct": '1588',
        "wrong": ['1600', '1550', '1650']
    },
    {
        "text": "Who painted 'The Birth of Venus'?",
        "category": 'art',
        "correct": 'Sandro Botticelli',
        "wrong": ['Raphael', 'Leonardo da Vinci', 'Titian']
    },
    {
        "text": 'What art movement did Claude Monet help found?',
        "category": 'art',
        "correct": 'Impressionism',
        "wrong": ['Romanticism', 'Post-Impressionism', 'Realism']
    },
    {
        "text": "Who painted 'Guernica'?",
        "category": 'art',
        "correct": 'Pablo Picasso',
        "wrong": ['Joan Miró', 'Diego Rivera', 'Salvador Dalí']
    },
    {
        "text": "What year was 'The Scream' painted?",
        "category": 'art',
        "correct": '1893',
        "wrong": ['1900', '1910', '1885']
    },
    {
        "text": "Who sculpted 'The Thinker'?",
        "category": 'art',
        "correct": 'Auguste Rodin',
        "wrong": ['Bernini', 'Michelangelo', 'Donatello']
    },
    {
        "text": 'What museum houses the Mona Lisa?',
        "category": 'art',
        "correct": 'Louvre Museum',
        "wrong": ['Prado Museum', 'Uffizi Gallery', 'National Gallery']
    },
    {
        "text": "Who painted 'Girl with a Pearl Earring'?",
        "category": 'art',
        "correct": 'Johannes Vermeer',
        "wrong": ['Rembrandt', 'Jan van Eyck', 'Frans Hals']
    },
    {
        "text": 'What art movement was Andy Warhol part of?',
        "category": 'art',
        "correct": 'Pop Art',
        "wrong": ['Conceptual Art', 'Minimalism', 'Abstract Expressionism']
    },
    {
        "text": "Who painted the ceiling of the Sistine Chapel's Cappella Sistina?",
        "category": 'art',
        "correct": 'Michelangelo',
        "wrong": ['Botticelli', 'Leonardo da Vinci', 'Raphael']
    },
    {
        "text": 'What year did Vincent van Gogh cut off his ear?',
        "category": 'art',
        "correct": '1888',
        "wrong": ['1886', '1890', '1885']
    },
    {
        "text": "Who painted 'The Garden of Earthly Delights'?",
        "category": 'art',
        "correct": 'Hieronymus Bosch',
        "wrong": ['Jan van Eyck', 'Albrecht Dürer', 'Pieter Bruegel']
    },
    {
        "text": 'What is the most expensive painting ever sold at auction?',
        "category": 'art',
        "correct": 'Salvator Mundi by Leonardo da Vinci',
        "wrong": ['Nude, Green Leaves and Bust by Picasso', 'Shot Sage Blue Marilyn by Warhol', "Les Femmes d'Alger by Picasso"]
    },
    {
        "text": "Who painted 'American Gothic'?",
        "category": 'art',
        "correct": 'Grant Wood',
        "wrong": ['Norman Rockwell', 'Edward Hopper', "Georgia O'Keeffe"]
    },
    {
        "text": 'What year did the Renaissance period begin in Italy?',
        "category": 'art',
        "correct": '14th century (1300s)',
        "wrong": ['12th century', '15th century', '16th century']
    },
    {
        "text": "Who created the sculpture 'The Kiss'?",
        "category": 'art',
        "correct": 'Auguste Rodin',
        "wrong": ['Constantin Brâncuși', 'Camille Claudel', 'Antonio Canova']
    },
    {
        "text": 'What art movement did Jackson Pollock pioneer?',
        "category": 'art',
        "correct": 'Abstract Expressionism',
        "wrong": ['Surrealism', 'Pop Art', 'Cubism']
    },
    {
        "text": "Who painted 'The Last Supper'?",
        "category": 'art',
        "correct": 'Leonardo da Vinci',
        "wrong": ['Michelangelo', 'Raphael', 'Caravaggio']
    },
    {
        "text": 'What year did Leonardo da Vinci die?',
        "category": 'art',
        "correct": '1519',
        "wrong": ['1510', '1530', '1525']
    },
    {
        "text": "Who painted 'The Night Watch'?",
        "category": 'art',
        "correct": 'Rembrandt van Rijn',
        "wrong": ['Johannes Vermeer', 'Frans Hals', 'Peter Paul Rubens']
    },
    {
        "text": "What museum houses 'Starry Night'?",
        "category": 'art',
        "correct": 'Museum of Modern Art (MoMA)',
        "wrong": ['Metropolitan Museum of Art', 'Van Gogh Museum', 'Louvre Museum']
    },
    {
        "text": "Who painted 'The Creation of Adam'?",
        "category": 'art',
        "correct": 'Michelangelo',
        "wrong": ['Titian', 'Leonardo da Vinci', 'Raphael']
    },
    {
        "text": 'What art movement emphasized dreams and the unconscious mind?',
        "category": 'art',
        "correct": 'Surrealism',
        "wrong": ['Expressionism', 'Dadaism', 'Symbolism']
    },
    {
        "text": "Who painted 'Les Demoiselles d'Avignon'?",
        "category": 'art',
        "correct": 'Pablo Picasso',
        "wrong": ['Georges Braque', 'André Derain', 'Henri Matisse']
    },
    {
        "text": 'What year was the Guggenheim Museum in New York designed by Frank Lloyd Wright opened?',
        "category": 'art',
        "correct": '1959',
        "wrong": ['1967', '1963', '1955']
    },
    {
        "text": "Who painted 'Water Lilies' series?",
        "category": 'art',
        "correct": 'Claude Monet',
        "wrong": ['Camille Pissarro', 'Edgar Degas', 'Pierre-Auguste Renoir']
    },
    {
        "text": 'What is the term for a painting done on wet plaster?',
        "category": 'art',
        "correct": 'Fresco',
        "wrong": ['Oil painting', 'Tempera', 'Encaustic']
    },
    {
        "text": "Who painted 'The School of Athens'?",
        "category": 'art',
        "correct": 'Raphael',
        "wrong": ['Leonardo da Vinci', 'Botticelli', 'Michelangelo']
    },
    {
        "text": 'What year did Pablo Picasso die?',
        "category": 'art',
        "correct": '1973',
        "wrong": ['1970', '1976', '1980']
    },
    {
        "text": "Who created the sculpture 'The Gates of Hell'?",
        "category": 'art',
        "correct": 'Auguste Rodin',
        "wrong": ['Donatello', 'Bernini', 'Michelangelo']
    },
    {
        "text": 'What art movement was characterized by geometric shapes and primary colors?',
        "category": 'art',
        "correct": 'De Stijl / Neo-Plasticism',
        "wrong": ['Constructivism', 'Suprematism', 'Bauhaus']
    },
    {
        "text": "Who painted 'The Kiss' (1907-1908)?",
        "category": 'art',
        "correct": 'Gustav Klimt',
        "wrong": ['Edvard Munch', 'Egon Schiele', 'Henri de Toulouse-Lautrec']
    },
    {
        "text": "What museum houses 'The Scream'?",
        "category": 'art',
        "correct": 'National Museum of Norway',
        "wrong": ['Munch Museum', 'Tate Modern', 'MoMA']
    },
    {
        "text": "Who painted 'No. 5, 1948', one of the most expensive paintings ever sold?",
        "category": 'art',
        "correct": 'Jackson Pollock',
        "wrong": ['Franz Kline', 'Willem de Kooning', 'Mark Rothko']
    },
    {
        "text": 'What year was the Impressionist movement founded?',
        "category": 'art',
        "correct": '1874',
        "wrong": ['1860', '1880', '1890']
    },
    {
        "text": "Who created the sculpture 'Bird in Space'?",
        "category": 'art',
        "correct": 'Constantin Brâncuși',
        "wrong": ['Auguste Rodin', 'Henry Moore', 'Alberto Giacometti']
    },
    {
        "text": 'What art movement did Kazimir Malevich found?',
        "category": 'art',
        "correct": 'Suprematism',
        "wrong": ['De Stijl', 'Constructivism', 'Futurism']
    },
    {
        "text": "Who painted 'Olympia' (1863)?",
        "category": 'art',
        "correct": 'Édouard Manet',
        "wrong": ['Gustave Courbet', 'Claude Monet', 'Pierre-Auguste Renoir']
    },
    {
        "text": 'What year did Frida Kahlo die?',
        "category": 'art',
        "correct": '1954',
        "wrong": ['1960', '1958', '1950']
    },
    {
        "text": "Who created the readymade artwork 'Fountain' (a urinal)?",
        "category": 'art',
        "correct": 'Marcel Duchamp',
        "wrong": ['Kurt Schwitters', 'Francis Picabia', 'Man Ray']
    },
    {
        "text": 'What art movement emphasized spontaneity and automatism?',
        "category": 'art',
        "correct": 'Surrealism',
        "wrong": ['Dadaism', 'Fluxus', 'Abstract Expressionism']
    },
    {
        "text": "Who painted 'The Arnolfini Portrait'?",
        "category": 'art',
        "correct": 'Jan van Eyck',
        "wrong": ['Rogier van der Weyden', 'Robert Campin', 'Petrus Christus']
    },
    {
        "text": 'What museum is home to the largest collection of Impressionist art?',
        "category": 'art',
        "correct": "Musée d'Orsay",
        "wrong": ['Louvre Museum', 'Metropolitan Museum of Art', 'National Gallery']
    },
    {
        "text": "Who painted 'Nighthawks'?",
        "category": 'art',
        "correct": 'Edward Hopper',
        "wrong": ['Thomas Hart Benton', 'Andrew Wyeth', 'Grant Wood']
    },
    {
        "text": "What year was Andy Warhol's 'Campbell's Soup Cans' first exhibited?",
        "category": 'art',
        "correct": '1962',
        "wrong": ['1968', '1960', '1965']
    },
    {
        "text": 'What year was the first Super Mario Bros game released?',
        "category": 'Gaming',
        "correct": '1985',
        "wrong": ['1990', '1983', '1987']
    },
    {
        "text": 'Who is the main character in The Legend of Zelda series?',
        "category": 'Gaming',
        "correct": 'Link',
        "wrong": ['Zelda', 'Ganondorf', 'Epona']
    },
    {
        "text": 'What company created the PlayStation?',
        "category": 'Gaming',
        "correct": 'Sony',
        "wrong": ['Microsoft', 'Nintendo', 'Sega']
    },
    {
        "text": 'What year was Pac-Man first released?',
        "category": 'Gaming',
        "correct": '1980',
        "wrong": ['1978', '1985', '1982']
    },
    {
        "text": 'What is the name of the protagonist in Half-Life?',
        "category": 'Gaming',
        "correct": 'Gordon Freeman',
        "wrong": ['Adrian Shephard', 'Barney Calhoun', 'John Freeman']
    },
    {
        "text": 'What is the maximum level in Pokémon games?',
        "category": 'Gaming',
        "correct": '100',
        "wrong": ['255', '150', '99']
    },
    {
        "text": 'Who is the creator of Minecraft?',
        "category": 'Gaming',
        "correct": 'Markus Persson (Notch)',
        "wrong": ['Hideo Kojima', 'Gabe Newell', 'Shigeru Miyamoto']
    },
    {
        "text": 'What year was the Xbox 360 released?',
        "category": 'Gaming',
        "correct": '2005',
        "wrong": ['2003', '2010', '2007']
    },
    {
        "text": 'What is the name of the main character in the Metal Gear Solid series?',
        "category": 'Gaming',
        "correct": 'Solid Snake',
        "wrong": ['Liquid Snake', 'Big Boss', 'Naked Snake']
    },
    {
        "text": 'What company developed the game Portal?',
        "category": 'Gaming',
        "correct": 'Valve',
        "wrong": ['BioWare', 'Bethesda', 'Rockstar']
    },
    {
        "text": 'What year was The Elder Scrolls V: Skyrim released?',
        "category": 'Gaming',
        "correct": '2011',
        "wrong": ['2013', '2015', '2009']
    },
    {
        "text": 'What is the name of the currency in Fortnite?',
        "category": 'Gaming',
        "correct": 'V-Bucks',
        "wrong": ['Coins', 'Credits', 'Crowns']
    },
    {
        "text": 'Who is the mascot of Sega?',
        "category": 'Gaming',
        "correct": 'Sonic the Hedgehog',
        "wrong": ['Shadow', 'Tails', 'Knuckles']
    },
    {
        "text": 'What company created World of Warcraft?',
        "category": 'Gaming',
        "correct": 'Blizzard Entertainment',
        "wrong": ['Bethesda', 'Electronic Arts', 'BioWare']
    },
    {
        "text": 'What year was League of Legends released?',
        "category": 'Gaming',
        "correct": '2009',
        "wrong": ['2013', '2007', '2011']
    },
    {
        "text": 'What is the name of the main character in BioShock?',
        "category": 'Gaming',
        "correct": 'Jack',
        "wrong": ['Frank Fontaine', 'Atlas', 'Andrew Ryan']
    },
    {
        "text": 'What year did the iPhone first release?',
        "category": 'Pop Culture',
        "correct": '2007',
        "wrong": ['2010', '2009', '2005']
    },
    {
        "text": 'Who is the highest-paid actress in Hollywood (2023)?',
        "category": 'Pop Culture',
        "correct": 'Margot Robbie',
        "wrong": ['Jennifer Lawrence', 'Angelina Jolie', 'Scarlett Johansson']
    },
    {
        "text": 'What year did TikTok launch internationally?',
        "category": 'Pop Culture',
        "correct": '2018',
        "wrong": ['2019', '2016', '2020']
    },
    {
        "text": 'Who is the most followed person on Instagram (2024)?',
        "category": 'Pop Culture',
        "correct": 'Cristiano Ronaldo',
        "wrong": ['Selena Gomez', 'Lionel Messi', 'Kylie Jenner']
    },
    {
        "text": 'What year did Spotify launch?',
        "category": 'Pop Culture',
        "correct": '2008',
        "wrong": ['2010', '2006', '2012']
    },
    {
        "text": 'Who won the first season of The Voice?',
        "category": 'Pop Culture',
        "correct": 'Javier Colon',
        "wrong": ['Danielle Bradbery', 'Cassadee Pope', 'Jordan Smith']
    },
    {
        "text": 'What year was the first Amazon Echo released?',
        "category": 'Pop Culture',
        "correct": '2014',
        "wrong": ['2016', '2012', '2018']
    },
    {
        "text": "Who is the creator of Grey's Anatomy?",
        "category": 'Pop Culture',
        "correct": 'Shonda Rhimes',
        "wrong": ['J.J. Abrams', 'Ryan Murphy', 'Chuck Lorre']
    },
    {
        "text": 'What year did Vine shut down?',
        "category": 'Pop Culture',
        "correct": '2017',
        "wrong": ['2018', '2015', '2019']
    },
    {
        "text": 'Who was the first Bachelorette on the reality show?',
        "category": 'Pop Culture',
        "correct": 'Trista Rehn',
        "wrong": ['JoJo Fletcher', 'Kaitlyn Bristowe', 'Becca Kufrin']
    },
    {
        "text": 'What year was Snapchat founded?',
        "category": 'Pop Culture',
        "correct": '2011',
        "wrong": ['2013', '2009', '2015']
    },
    {
        "text": 'Who is the highest-earning YouTuber (2023)?',
        "category": 'Pop Culture',
        "correct": 'MrBeast',
        "wrong": ['PewDiePie', 'Dude Perfect', 'Ryan Kaji']
    },
    {
        "text": 'What year did Myspace launch?',
        "category": 'Pop Culture',
        "correct": '2003',
        "wrong": ['2005', '2007', '2001']
    },
    {
        "text": 'Who created the TV show The Office (US version)?',
        "category": 'Pop Culture',
        "correct": 'Greg Daniels',
        "wrong": ['Steve Carell', 'Ricky Gervais', 'Michael Schur']
    },
    {
        "text": 'What year was the first iPad released?',
        "category": 'Pop Culture',
        "correct": '2010',
        "wrong": ['2012', '2007', '2008']
    },
    {
        "text": 'Who is the most streamed artist on Spotify of all time?',
        "category": 'Pop Culture',
        "correct": 'Drake',
        "wrong": ['Taylor Swift', 'The Weeknd', 'Ed Sheeran']
    },
    {
        "text": 'What year did Clubhouse app launch?',
        "category": 'Pop Culture',
        "correct": '2020',
        "wrong": ['2021', '2018', '2019']
    },
    {
        "text": "Who won the first season of RuPaul's Drag Race?",
        "category": 'Pop Culture',
        "correct": 'BeBe Zahara Benet',
        "wrong": ['Nina Flowers', 'Shannel', 'Ongina']
    },
    {
        "text": 'What year was Reddit founded?',
        "category": 'Pop Culture',
        "correct": '2005',
        "wrong": ['2007', '2003', '2010']
    },
    {
        "text": 'Who is the creator of Stranger Things?',
        "category": 'Pop Culture',
        "correct": 'The Duffer Brothers',
        "wrong": ['J.J. Abrams', 'Vince Gilligan', 'Ryan Murphy']
    },
    {
        "text": 'What is the maximum level in D&D 5th edition?',
        "category": 'D&D',
        "correct": '20',
        "wrong": ['100', '25', '30']
    },
    {
        "text": 'Who created Dungeons & Dragons?',
        "category": 'D&D',
        "correct": 'Gary Gygax and Dave Arneson',
        "wrong": ['Ed Greenwood', 'Mike Mearls', 'Chris Perkins']
    },
    {
        "text": 'What year was the first edition of D&D released?',
        "category": 'D&D',
        "correct": '1974',
        "wrong": ['1970', '1980', '1978']
    },
    {
        "text": 'What is the name of the Forgotten Realms city known as the City of Splendors?',
        "category": 'D&D',
        "correct": 'Waterdeep',
        "wrong": ['Neverwinter', "Baldur's Gate", 'Luskan']
    },
    {
        "text": 'What is the highest damage die in standard D&D?',
        "category": 'D&D',
        "correct": 'd20',
        "wrong": ['d10', 'd12', 'd100']
    },
    {
        "text": 'Who is the god of death in the Forgotten Realms?',
        "category": 'D&D',
        "correct": 'Kelemvor',
        "wrong": ['Bhaal', 'Bane', 'Myrkul']
    },
    {
        "text": 'What is the name of the demon lord of undeath?',
        "category": 'D&D',
        "correct": 'Orcus',
        "wrong": ['Baphomet', "Graz'zt", 'Demogorgon']
    },
    {
        "text": "What ability score determines a wizard's spellcasting?",
        "category": 'D&D',
        "correct": 'Intelligence',
        "wrong": ['Constitution', 'Charisma', 'Wisdom']
    },
    {
        "text": "What is the name of the dragon goddess Tiamat's rival?",
        "category": 'D&D',
        "correct": 'Bahamut',
        "wrong": ['Chronepsis', 'Io', 'Sardior']
    },
    {
        "text": 'What year was D&D 5th edition released?',
        "category": 'D&D',
        "correct": '2014',
        "wrong": ['2016', '2010', '2012']
    },
    {
        "text": 'What is the name of the city in the Nine Hells ruled by Asmodeus?',
        "category": 'D&D',
        "correct": 'Nessus',
        "wrong": ['Dis', 'Malbolge', 'Avernus']
    },
    {
        "text": 'What is the standard AC (Armor Class) for an unarmored humanoid?',
        "category": 'D&D',
        "correct": '10',
        "wrong": ['8', '12', '15']
    },
    {
        "text": 'Who is the goddess of magic in the Forgotten Realms?',
        "category": 'D&D',
        "correct": 'Mystra',
        "wrong": ['Selûne', 'Azuth', 'Shar']
    },
    {
        "text": 'What is the name of the demon lord known as the Prince of Demons?',
        "category": 'D&D',
        "correct": 'Demogorgon',
        "wrong": ['Baphomet', 'Orcus', "Graz'zt"]
    },
    {
        "text": 'What ability score determines initiative in combat?',
        "category": 'D&D',
        "correct": 'Dexterity',
        "wrong": ['Intelligence', 'Wisdom', 'Strength']
    },
    {
        "text": 'What is the name of the drow city in the Underdark?',
        "category": 'D&D',
        "correct": 'Menzoberranzan',
        "wrong": ['Dark Haven', 'Shadowdeep', "Lloth's Reach"]
    },
    {
        "text": 'Who is the creator of the Forgotten Realms setting?',
        "category": 'D&D',
        "correct": 'Ed Greenwood',
        "wrong": ['Tracy Hickman', 'Gary Gygax', 'R.A. Salvatore']
    },
    {
        "text": "What is the name of Drizzt Do'Urden's scimitars?",
        "category": 'D&D',
        "correct": 'Icingdeath and Twinkle',
        "wrong": ['Winterbite and Glimmer', 'Frostbrand and Starshine', 'Coldfire and Moonbeam']
    },
    {
        "text": 'What plane of existence is known as the plane of pure chaos?',
        "category": 'D&D',
        "correct": 'Limbo',
        "wrong": ['Carceri', 'The Abyss', 'Pandemonium']
    },
    {
        "text": 'Who created the Rust programming language?',
        "category": 'Coding',
        "correct": 'Graydon Hoare',
        "wrong": ['Guido van Rossum', 'Brendan Eich', 'Anders Hejlsberg']
    },
    {
        "text": 'Who was the first female pharaoh of ancient Egypt?',
        "category": 'history',
        "correct": 'Hatshepsut',
        "wrong": ['Nefertiti', 'Nefertari', 'Cleopatra']
    },
    {
        "text": "Who directed the movie 'Parasite' that won Best Picture in 2020?",
        "category": 'entertainment',
        "correct": 'Bong Joon-ho',
        "wrong": ['Kim Ki-duk', 'Park Chan-wook', 'Lee Chang-dong']
    },
    {
        "text": 'What is the name of the fictional town in Twin Peaks?',
        "category": 'entertainment',
        "correct": 'Twin Peaks, Washington',
        "wrong": ['Twin Rivers', 'Twin Falls', 'Twin Oaks']
    },
    {
        "text": 'Who holds the record for most goals in a single NHL season?',
        "category": 'sports',
        "correct": 'Wayne Gretzky (92)',
        "wrong": ['Alexander Ovechkin', 'Brett Hull', 'Mario Lemieux']
    },
    {
        "text": "Who composed 'The Marriage of Figaro'?",
        "category": 'music',
        "correct": 'Wolfgang Amadeus Mozart',
        "wrong": ['Ludwig van Beethoven', 'Gioachino Rossini', 'Giuseppe Verdi']
    },
    {
        "text": "Who is known as the 'Father of the Symphony'?",
        "category": 'music',
        "correct": 'Joseph Haydn',
        "wrong": ['Wolfgang Amadeus Mozart', 'Ludwig van Beethoven', 'Johann Sebastian Bach']
    }
]
