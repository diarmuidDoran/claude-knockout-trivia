#!/usr/bin/env python3
"""
Generate 500 factual haunting race questions for the trivia game.
Each question has a topic and 3 true/false statements.
"""

import json

def create_questions():
    """Generate 500 diverse factual questions."""
    questions = []

    # Programming Questions (100)
    programming_questions = [
        # Python
        ("Python Built-in Functions", "Programming", [
            ("enumerate()", True), ("flatten()", False), ("zip()", True)
        ]),
        ("Python Standard Library Modules", "Programming", [
            ("os", True), ("requests", False), ("datetime", True)
        ]),
        ("Python Data Types", "Programming", [
            ("list", True), ("tuple", True), ("array", False)
        ]),
        ("Python String Methods", "Programming", [
            ("split()", True), ("divide()", False), ("replace()", True)
        ]),
        ("Python Exception Types", "Programming", [
            ("ValueError", True), ("TypeError", True), ("ParseError", False)
        ]),

        # JavaScript
        ("JavaScript Array Methods", "Programming", [
            ("map()", True), ("extract()", False), ("filter()", True)
        ]),
        ("JavaScript Keywords", "Programming", [
            ("const", True), ("var", True), ("int", False)
        ]),
        ("JavaScript Promise Methods", "Programming", [
            ("then()", True), ("catch()", True), ("throw()", False)
        ]),
        ("JavaScript DOM Methods", "Programming", [
            ("getElementById()", True), ("getElementByName()", False), ("querySelector()", True)
        ]),
        ("JavaScript Object Methods", "Programming", [
            ("Object.keys()", True), ("Object.props()", False), ("Object.values()", True)
        ]),

        # Frameworks & Libraries
        ("React Hooks", "Programming", [
            ("useState", True), ("useRender", False), ("useEffect", True)
        ]),
        ("React Lifecycle Methods", "Programming", [
            ("componentDidMount", True), ("componentWillLoad", False), ("componentWillUnmount", True)
        ]),
        ("Vue.js Lifecycle Hooks", "Programming", [
            ("mounted", True), ("created", True), ("loaded", False)
        ]),
        ("Angular Decorators", "Programming", [
            ("@Component", True), ("@View", False), ("@Injectable", True)
        ]),
        ("Express.js Methods", "Programming", [
            ("app.get()", True), ("app.fetch()", False), ("app.post()", True)
        ]),

        # Databases & SQL
        ("SQL Keywords", "Programming", [
            ("SELECT", True), ("RETRIEVE", False), ("WHERE", True)
        ]),
        ("SQL JOIN Types", "Programming", [
            ("INNER JOIN", True), ("OUTER JOIN", True), ("CROSS MERGE", False)
        ]),
        ("SQL Aggregate Functions", "Programming", [
            ("COUNT()", True), ("SUM()", True), ("TOTAL()", False)
        ]),
        ("PostgreSQL Data Types", "Programming", [
            ("VARCHAR", True), ("TEXT", True), ("STRING", False)
        ]),
        ("MongoDB Query Operators", "Programming", [
            ("$gt", True), ("$gte", True), ("$greater", False)
        ]),

        # Git & Version Control
        ("Git Commands", "Programming", [
            ("commit", True), ("upload", False), ("push", True)
        ]),
        ("Git Branch Commands", "Programming", [
            ("checkout", True), ("switch", True), ("change", False)
        ]),
        ("Git Remote Commands", "Programming", [
            ("fetch", True), ("download", False), ("pull", True)
        ]),
        ("Git Configuration Commands", "Programming", [
            ("config", True), ("setup", False), ("init", True)
        ]),
        ("Git Stash Commands", "Programming", [
            ("stash", True), ("stash pop", True), ("stash save", False)
        ]),

        # Unix/Linux
        ("Unix/Linux Commands", "Programming", [
            ("grep", True), ("search", False), ("find", True)
        ]),
        ("Unix File Permission Commands", "Programming", [
            ("chmod", True), ("chown", True), ("permit", False)
        ]),
        ("Unix Process Commands", "Programming", [
            ("ps", True), ("kill", True), ("terminate", False)
        ]),
        ("Unix Network Commands", "Programming", [
            ("ping", True), ("traceroute", True), ("netmap", False)
        ]),
        ("Unix Text Processing", "Programming", [
            ("awk", True), ("extract", False), ("sed", True)
        ]),

        # Docker & Containers
        ("Docker Commands", "Programming", [
            ("run", True), ("deploy", False), ("build", True)
        ]),
        ("Docker Compose Commands", "Programming", [
            ("up", True), ("down", True), ("start", True)
        ]),
        ("Kubernetes Components", "Programming", [
            ("Pod", True), ("Container", False), ("Node", True)
        ]),
        ("Docker Image Commands", "Programming", [
            ("pull", True), ("push", True), ("upload", False)
        ]),
        ("Docker Network Types", "Programming", [
            ("bridge", True), ("connect", False), ("host", True)
        ]),

        # Web Technologies
        ("HTTP Status Codes", "Programming", [
            ("404", True), ("600", False), ("200", True)
        ]),
        ("HTTP Methods", "Programming", [
            ("GET", True), ("POST", True), ("FETCH", False)
        ]),
        ("HTTP Headers", "Programming", [
            ("Content-Type", True), ("Authorization", True), ("Permission", False)
        ]),
        ("REST API Principles", "Programming", [
            ("Stateless", True), ("Cacheable", True), ("Sequential", False)
        ]),
        ("WebSocket Events", "Programming", [
            ("open", True), ("connect", False), ("close", True)
        ]),

        # CSS
        ("CSS Properties", "Programming", [
            ("display", True), ("transparency", False), ("visibility", True)
        ]),
        ("CSS Display Values", "Programming", [
            ("block", True), ("inline", True), ("visible", False)
        ]),
        ("CSS Position Values", "Programming", [
            ("absolute", True), ("relative", True), ("floating", False)
        ]),
        ("CSS Selectors", "Programming", [
            ("class", True), ("id", True), ("name", False)
        ]),
        ("CSS Flexbox Properties", "Programming", [
            ("justify-content", True), ("center-items", False), ("align-items", True)
        ]),

        # Data Structures & Algorithms
        ("Data Structures", "Programming", [
            ("Stack", True), ("Deck", False), ("Queue", True)
        ]),
        ("Tree Types", "Programming", [
            ("Binary Tree", True), ("Ternary Tree", False), ("AVL Tree", True)
        ]),
        ("Sorting Algorithms", "Programming", [
            ("Quick Sort", True), ("Merge Sort", True), ("Hybrid Sort", False)
        ]),
        ("Search Algorithms", "Programming", [
            ("Binary Search", True), ("Index Search", False), ("Linear Search", True)
        ]),
        ("Graph Algorithms", "Programming", [
            ("Dijkstra's Algorithm", True), ("Breadth-First Search", True), ("Depth-Last Search", False)
        ]),

        # Programming Paradigms
        ("Object-Oriented Programming Concepts", "Programming", [
            ("Encapsulation", True), ("Hiding", False), ("Inheritance", True)
        ]),
        ("Functional Programming Concepts", "Programming", [
            ("Pure Functions", True), ("Static Functions", False), ("Higher-Order Functions", True)
        ]),
        ("SOLID Principles", "Programming", [
            ("Single Responsibility", True), ("Unified Purpose", False), ("Open-Closed", True)
        ]),
        ("Design Patterns", "Programming", [
            ("Singleton", True), ("Observer", True), ("Watcher", False)
        ]),
        ("Agile Methodologies", "Programming", [
            ("Scrum", True), ("Kanban", True), ("Waterfall", False)
        ]),

        # Additional Programming (50 more)
        ("C++ STL Containers", "Programming", [
            ("vector", True), ("arraylist", False), ("map", True)
        ]),
        ("Java Collection Interfaces", "Programming", [
            ("List", True), ("Set", True), ("Array", False)
        ]),
        ("Regular Expression Metacharacters", "Programming", [
            ("\\d", True), ("\\n", False), ("\\w", True)
        ]),
        ("TypeScript Features", "Programming", [
            ("Interfaces", True), ("Types", True), ("Classes", True)
        ]),
        ("GraphQL Query Types", "Programming", [
            ("query", True), ("mutation", True), ("action", False)
        ]),
        ("Redis Data Types", "Programming", [
            ("String", True), ("Hash", True), ("Object", False)
        ]),
        ("AWS Services", "Programming", [
            ("EC2", True), ("Lambda", True), ("Compute", False)
        ]),
        ("Testing Frameworks (JavaScript)", "Programming", [
            ("Jest", True), ("Mocha", True), ("TestJS", False)
        ]),
        ("NPM Commands", "Programming", [
            ("install", True), ("run", True), ("execute", False)
        ]),
        ("Vim Commands", "Programming", [
            (":wq", True), (":save", False), (":q!", True)
        ]),
        ("Webpack Concepts", "Programming", [
            ("Loaders", True), ("Converters", False), ("Plugins", True)
        ]),
        ("OAuth Grant Types", "Programming", [
            ("Authorization Code", True), ("Implicit", True), ("Direct Access", False)
        ]),
        ("JSON Web Token Parts", "Programming", [
            ("Header", True), ("Payload", True), ("Footer", False)
        ]),
        ("API Authentication Methods", "Programming", [
            ("API Key", True), ("Basic Auth", True), ("Password", False)
        ]),
        ("Continuous Integration Tools", "Programming", [
            ("Jenkins", True), ("TravisCI", True), ("BuildBot", False)
        ]),
        ("Package Managers", "Programming", [
            ("npm", True), ("pip", True), ("get", False)
        ]),
        ("Code Review Practices", "Programming", [
            ("Pull Requests", True), ("Code Comments", True), ("Code Approval", False)
        ]),
        ("Security Vulnerabilities", "Programming", [
            ("SQL Injection", True), ("XSS", True), ("Buffer Leak", False)
        ]),
        ("Encryption Algorithms", "Programming", [
            ("AES", True), ("RSA", True), ("SHA512", False)
        ]),
        ("Linux Distributions", "Programming", [
            ("Ubuntu", True), ("Debian", True), ("RedHawk", False)
        ]),
        ("Shell Scripting", "Programming", [
            ("Bash", True), ("Zsh", True), ("Cmd", False)
        ]),
        ("API Response Formats", "Programming", [
            ("JSON", True), ("XML", True), ("YAML", False)
        ]),
        ("Web Frameworks (Python)", "Programming", [
            ("Django", True), ("Flask", True), ("Rocket", False)
        ]),
        ("Database Normalization", "Programming", [
            ("1NF", True), ("2NF", True), ("0NF", False)
        ]),
        ("Microservices Patterns", "Programming", [
            ("API Gateway", True), ("Circuit Breaker", True), ("Service Mesh", False)
        ]),
        ("Message Queue Systems", "Programming", [
            ("RabbitMQ", True), ("Kafka", True), ("QueueMQ", False)
        ]),
        ("GraphQL Schema Types", "Programming", [
            ("Query", True), ("Mutation", True), ("Action", False)
        ]),
        ("Binary Operations", "Programming", [
            ("AND", True), ("OR", True), ("NAND", True)
        ]),
        ("Big O Notation Complexities", "Programming", [
            ("O(1)", True), ("O(n)", True), ("O(0)", False)
        ]),
        ("Network Protocols", "Programming", [
            ("TCP", True), ("UDP", True), ("XTP", False)
        ]),
        ("Cloud Computing Models", "Programming", [
            ("IaaS", True), ("PaaS", True), ("DaaS", False)
        ]),
        ("Mobile App Frameworks", "Programming", [
            ("React Native", True), ("Flutter", True), ("AppJS", False)
        ]),
        ("IDE Features", "Programming", [
            ("Syntax Highlighting", True), ("Code Completion", True), ("Auto-Compile", False)
        ]),
        ("Software Licenses", "Programming", [
            ("MIT", True), ("GPL", True), ("FREE", False)
        ]),
        ("Cache Strategies", "Programming", [
            ("LRU", True), ("FIFO", True), ("LIFO", True)
        ]),
        ("Load Balancing Algorithms", "Programming", [
            ("Round Robin", True), ("Least Connections", True), ("First Available", False)
        ]),
        ("Semantic Versioning", "Programming", [
            ("MAJOR", True), ("MINOR", True), ("PATCH", True)
        ]),
        ("API Design Styles", "Programming", [
            ("REST", True), ("GraphQL", True), ("SOAP", True)
        ]),
        ("Serverless Platforms", "Programming", [
            ("AWS Lambda", True), ("Azure Functions", True), ("Cloud Run", False)
        ]),
        ("Code Smells", "Programming", [
            ("Long Method", True), ("Duplicate Code", True), ("Messy Code", False)
        ]),
    ]

    # Movies (80)
    movie_questions = [
        ("Christopher Nolan Films", "Movies", [
            ("Inception", True), ("Arrival", False), ("Tenet", True)
        ]),
        ("Quentin Tarantino Films", "Movies", [
            ("Pulp Fiction", True), ("No Country for Old Men", False), ("Django Unchained", True)
        ]),
        ("Stanley Kubrick Films", "Movies", [
            ("2001: A Space Odyssey", True), ("Alien", False), ("The Shining", True)
        ]),
        ("Steven Spielberg Films", "Movies", [
            ("Jaws", True), ("The Godfather", False), ("E.T.", True)
        ]),
        ("Martin Scorsese Films", "Movies", [
            ("Goodfellas", True), ("The Departed", True), ("Scarface", False)
        ]),
        ("Wes Anderson Films", "Movies", [
            ("The Grand Budapest Hotel", True), ("Her", False), ("Moonrise Kingdom", True)
        ]),
        ("Marvel Cinematic Universe", "Movies", [
            ("Iron Man", True), ("Man of Steel", False), ("Black Panther", True)
        ]),
        ("Star Wars Original Trilogy", "Movies", [
            ("A New Hope", True), ("The Phantom Menace", False), ("Return of the Jedi", True)
        ]),
        ("Pixar Films", "Movies", [
            ("Toy Story", True), ("Shrek", False), ("Finding Nemo", True)
        ]),
        ("Best Picture Oscar Winners", "Movies", [
            ("The Godfather", True), ("The Shawshank Redemption", False), ("Schindler's List", True)
        ]),
        ("James Bond Actors", "Movies", [
            ("Sean Connery", True), ("Clint Eastwood", False), ("Daniel Craig", True)
        ]),
        ("Disney Renaissance Films", "Movies", [
            ("The Little Mermaid", True), ("Cinderella", False), ("Beauty and the Beast", True)
        ]),
        ("The Dark Knight Trilogy", "Movies", [
            ("Batman Begins", True), ("The Dark Knight", True), ("Batman Forever", False)
        ]),
        ("Harry Potter Films", "Movies", [
            ("Philosopher's Stone", True), ("The Cursed Child", False), ("Goblet of Fire", True)
        ]),
        ("Lord of the Rings Trilogy", "Movies", [
            ("Fellowship of the Ring", True), ("The Hobbit", False), ("Return of the King", True)
        ]),
        ("Alfred Hitchcock Films", "Movies", [
            ("Psycho", True), ("Vertigo", True), ("Casablanca", False)
        ]),
        ("Coen Brothers Films", "Movies", [
            ("Fargo", True), ("The Big Lebowski", True), ("Zodiac", False)
        ]),
        ("Ridley Scott Films", "Movies", [
            ("Blade Runner", True), ("2001: A Space Odyssey", False), ("Gladiator", True)
        ]),
        ("Francis Ford Coppola Films", "Movies", [
            ("The Godfather", True), ("Goodfellas", False), ("Apocalypse Now", True)
        ]),
        ("Denis Villeneuve Films", "Movies", [
            ("Arrival", True), ("Interstellar", False), ("Blade Runner 2049", True)
        ]),
        ("Greta Gerwig Films (Director)", "Movies", [
            ("Lady Bird", True), ("Little Women", True), ("Frances Ha", False)
        ]),
        ("Star Trek Films (Original Cast)", "Movies", [
            ("The Motion Picture", True), ("The Voyage Home", True), ("First Contact", False)
        ]),
        ("Back to the Future Trilogy", "Movies", [
            ("Back to the Future", True), ("Back to the Future Part II", True), ("Back in Time", False)
        ]),
        ("Terminator Films (Cameron)", "Movies", [
            ("The Terminator", True), ("Terminator 2", True), ("Terminator 3", False)
        ]),
        ("Jurassic Park Films (Original Trilogy)", "Movies", [
            ("Jurassic Park", True), ("Jurassic World", False), ("The Lost World", True)
        ]),
        ("Matrix Films", "Movies", [
            ("The Matrix", True), ("The Matrix Reloaded", True), ("The Matrix Revived", False)
        ]),
        ("Indiana Jones Films (Original Trilogy)", "Movies", [
            ("Raiders of the Lost Ark", True), ("Temple of Doom", True), ("Kingdom of the Crystal Skull", False)
        ]),
        ("Die Hard Films", "Movies", [
            ("Die Hard", True), ("Die Hard with a Vengeance", True), ("Live Free or Die", False)
        ]),
        ("Rocky Films", "Movies", [
            ("Rocky", True), ("Rocky IV", True), ("Creed III", False)
        ]),
        ("Mission: Impossible Films", "Movies", [
            ("Mission: Impossible", True), ("Fallout", True), ("Protocol", False)
        ]),
        ("Alien Franchise (Ridley Scott)", "Movies", [
            ("Alien", True), ("Aliens", False), ("Prometheus", True)
        ]),
        ("Mad Max Films (George Miller)", "Movies", [
            ("Mad Max", True), ("Fury Road", True), ("Beyond the Wasteland", False)
        ]),
        ("Batman Films (Tim Burton)", "Movies", [
            ("Batman", True), ("Batman Returns", True), ("Batman Forever", False)
        ]),
        ("Spider-Man Films (Sam Raimi)", "Movies", [
            ("Spider-Man", True), ("Spider-Man 2", True), ("The Amazing Spider-Man", False)
        ]),
        ("X-Men Films (Bryan Singer)", "Movies", [
            ("X-Men", True), ("X2", True), ("X-Men: Apocalypse", False)
        ]),
        ("Ocean's Trilogy", "Movies", [
            ("Ocean's Eleven", True), ("Ocean's Twelve", True), ("Ocean's Seven", False)
        ]),
        ("Bourne Films (Matt Damon)", "Movies", [
            ("The Bourne Identity", True), ("The Bourne Supremacy", True), ("The Bourne Legacy", False)
        ]),
        ("Planet of the Apes (Reboot Series)", "Movies", [
            ("Rise of the Planet of the Apes", True), ("War for the Planet of the Apes", True), ("Battle for the Planet of the Apes", False)
        ]),
        ("Fast & Furious Films (Vin Diesel)", "Movies", [
            ("The Fast and the Furious", True), ("2 Fast 2 Furious", True), ("Fast Five Hundred", False)
        ]),
        ("Toy Story Films", "Movies", [
            ("Toy Story", True), ("Toy Story 2", True), ("Toy Story 4", True)
        ]),
        ("Shrek Films", "Movies", [
            ("Shrek", True), ("Shrek 2", True), ("Shrek 5", False)
        ]),
        ("How to Train Your Dragon Films", "Movies", [
            ("How to Train Your Dragon", True), ("The Hidden World", True), ("Rise of Berk", False)
        ]),
        ("Ice Age Films", "Movies", [
            ("Ice Age", True), ("The Meltdown", True), ("Continental Divide", False)
        ]),
        ("Kung Fu Panda Films", "Movies", [
            ("Kung Fu Panda", True), ("Kung Fu Panda 2", True), ("Kung Fu Panda 4", False)
        ]),
        ("Despicable Me Films", "Movies", [
            ("Despicable Me", True), ("Despicable Me 2", True), ("Minions 2", False)
        ]),
        ("Academy Award for Best Director", "Movies", [
            ("Kathryn Bigelow won in 2010", True), ("Sofia Coppola won in 2004", False), ("Jane Campion won in 2022", True)
        ]),
        ("Films Set in Space", "Movies", [
            ("Interstellar", True), ("Gravity", True), ("The Martian Chronicles", False)
        ]),
        ("Films About Artificial Intelligence", "Movies", [
            ("Ex Machina", True), ("Her", True), ("Automata", True)
        ]),
        ("Films Based on Stephen King", "Movies", [
            ("The Shawshank Redemption", True), ("The Green Mile", True), ("Misery Loves Company", False)
        ]),
        ("Films Directed by Women", "Movies", [
            ("Wonder Woman (Patty Jenkins)", True), ("The Hurt Locker (Kathryn Bigelow)", True), ("Mad Max: Fury Road (Greta Gerwig)", False)
        ]),
        ("Animated Films (Non-Disney/Pixar)", "Movies", [
            ("Spirited Away", True), ("How to Train Your Dragon", True), ("Moana", False)
        ]),
        ("Films with Al Pacino", "Movies", [
            ("The Godfather", True), ("Scarface", True), ("Goodfellas", False)
        ]),
        ("Films with Robert De Niro", "Movies", [
            ("Taxi Driver", True), ("Raging Bull", True), ("Scarface", False)
        ]),
        ("Films with Tom Hanks", "Movies", [
            ("Forrest Gump", True), ("Cast Away", True), ("The Shawshank Redemption", False)
        ]),
        ("Films with Leonardo DiCaprio", "Movies", [
            ("Titanic", True), ("The Revenant", True), ("The Aviator", True)
        ]),
        ("Films with Meryl Streep", "Movies", [
            ("The Devil Wears Prada", True), ("Sophie's Choice", True), ("Erin Brockovich", False)
        ]),
        ("Films with Denzel Washington", "Movies", [
            ("Training Day", True), ("Glory", True), ("The Departed", False)
        ]),
        ("Films with Cate Blanchett", "Movies", [
            ("Blue Jasmine", True), ("Carol", True), ("The Hours", False)
        ]),
        ("James Cameron Films", "Movies", [
            ("Titanic", True), ("Avatar", True), ("Interstellar", False)
        ]),
        ("Guillermo del Toro Films", "Movies", [
            ("Pan's Labyrinth", True), ("The Shape of Water", True), ("The Orphanage", False)
        ]),
        ("Bong Joon-ho Films", "Movies", [
            ("Parasite", True), ("Snowpiercer", True), ("Train to Busan", False)
        ]),
        ("Edgar Wright Films", "Movies", [
            ("Shaun of the Dead", True), ("Hot Fuzz", True), ("28 Days Later", False)
        ]),
        ("Taika Waititi Films", "Movies", [
            ("Jojo Rabbit", True), ("Thor: Ragnarok", True), ("Hunt for the Wilderpeople", True)
        ]),
        ("Jordan Peele Films", "Movies", [
            ("Get Out", True), ("Us", True), ("Candyman", False)
        ]),
        ("Ari Aster Films", "Movies", [
            ("Hereditary", True), ("Midsommar", True), ("The Witch", False)
        ]),
        ("A24 Films", "Movies", [
            ("Moonlight", True), ("Lady Bird", True), ("The Grand Budapest Hotel", False)
        ]),
        ("Film Noir Classics", "Movies", [
            ("The Maltese Falcon", True), ("Double Indemnity", True), ("Casablanca", True)
        ]),
        ("Silent Film Era", "Movies", [
            ("The Cabinet of Dr. Caligari", True), ("Metropolis", True), ("Gone with the Wind", False)
        ]),
        ("French New Wave Films", "Movies", [
            ("Breathless", True), ("The 400 Blows", True), ("Amélie", False)
        ]),
        ("Italian Neorealism Films", "Movies", [
            ("Bicycle Thieves", True), ("Rome, Open City", True), ("Life is Beautiful", False)
        ]),
        ("Akira Kurosawa Films", "Movies", [
            ("Seven Samurai", True), ("Rashomon", True), ("Crouching Tiger, Hidden Dragon", False)
        ]),
        ("Wong Kar-wai Films", "Movies", [
            ("In the Mood for Love", True), ("Chungking Express", True), ("Hero", False)
        ]),
        ("Pedro Almodóvar Films", "Movies", [
            ("All About My Mother", True), ("Talk to Her", True), ("The Secret in Their Eyes", False)
        ]),
        ("Lars von Trier Films", "Movies", [
            ("Dancer in the Dark", True), ("Melancholia", True), ("The Hunt", False)
        ]),
        ("Michael Haneke Films", "Movies", [
            ("Amour", True), ("The White Ribbon", True), ("Force Majeure", False)
        ]),
        ("Park Chan-wook Films", "Movies", [
            ("Oldboy", True), ("The Handmaiden", True), ("Parasite", False)
        ]),
        ("Terrence Malick Films", "Movies", [
            ("The Tree of Life", True), ("The Thin Red Line", True), ("The Revenant", False)
        ]),
        ("Paul Thomas Anderson Films", "Movies", [
            ("There Will Be Blood", True), ("Boogie Nights", True), ("No Country for Old Men", False)
        ]),
    ]

    # Music (80)
    music_questions = [
        ("Beatles Albums", "Music", [
            ("Abbey Road", True), ("Dark Side of the Moon", False), ("Sgt. Pepper's", True)
        ]),
        ("Pink Floyd Albums", "Music", [
            ("The Wall", True), ("Led Zeppelin IV", False), ("Dark Side of the Moon", True)
        ]),
        ("Taylor Swift Albums", "Music", [
            ("1989", True), ("Lemonade", False), ("Folklore", True)
        ]),
        ("David Bowie Albums", "Music", [
            ("The Rise and Fall of Ziggy Stardust", True), ("The Wall", False), ("Let's Dance", True)
        ]),
        ("Queen Songs", "Music", [
            ("Bohemian Rhapsody", True), ("Stairway to Heaven", False), ("We Will Rock You", True)
        ]),
        ("Metallica Albums", "Music", [
            ("Master of Puppets", True), ("Appetite for Destruction", False), ("The Black Album", True)
        ]),
        ("Radiohead Albums", "Music", [
            ("OK Computer", True), ("The Bends", True), ("Kid B", False)
        ]),
        ("Nirvana Albums", "Music", [
            ("Nevermind", True), ("Ten", False), ("In Utero", True)
        ]),
        ("Led Zeppelin Albums", "Music", [
            ("Led Zeppelin IV", True), ("Physical Graffiti", True), ("The Wall", False)
        ]),
        ("Rolling Stones Albums", "Music", [
            ("Sticky Fingers", True), ("Exile on Main St.", True), ("Rumours", False)
        ]),
        ("Michael Jackson Albums", "Music", [
            ("Thriller", True), ("Purple Rain", False), ("Bad", True)
        ]),
        ("Prince Albums", "Music", [
            ("Purple Rain", True), ("1999", True), ("Thriller", False)
        ]),
        ("Bob Dylan Albums", "Music", [
            ("Highway 61 Revisited", True), ("Born to Run", False), ("Blood on the Tracks", True)
        ]),
        ("Bruce Springsteen Albums", "Music", [
            ("Born to Run", True), ("Born in the U.S.A.", True), ("Thunder Road", False)
        ]),
        ("Fleetwood Mac Albums", "Music", [
            ("Rumours", True), ("Tapestry", False), ("Tusk", True)
        ]),
        ("The Who Albums", "Music", [
            ("Tommy", True), ("Who's Next", True), ("Quadrophenia 2", False)
        ]),
        ("U2 Albums", "Music", [
            ("The Joshua Tree", True), ("Achtung Baby", True), ("The Unforgettable Fire 2", False)
        ]),
        ("Kendrick Lamar Albums", "Music", [
            ("good kid, m.A.A.d city", True), ("The College Dropout", False), ("To Pimp a Butterfly", True)
        ]),
        ("Kanye West Albums", "Music", [
            ("The College Dropout", True), ("My Beautiful Dark Twisted Fantasy", True), ("Take Care", False)
        ]),
        ("Drake Albums", "Music", [
            ("Take Care", True), ("Views", True), ("The College Dropout", False)
        ]),
        ("Beyoncé Albums", "Music", [
            ("Lemonade", True), ("1989", False), ("Beyoncé", True)
        ]),
        ("Adele Albums", "Music", [
            ("21", True), ("25", True), ("19", True)
        ]),
        ("Amy Winehouse Albums", "Music", [
            ("Back to Black", True), ("21", False), ("Frank", True)
        ]),
        ("Stevie Wonder Albums", "Music", [
            ("Songs in the Key of Life", True), ("Innervisions", True), ("What's Going On", False)
        ]),
        ("Marvin Gaye Albums", "Music", [
            ("What's Going On", True), ("Let's Get It On", True), ("Songs in the Key of Life", False)
        ]),
        ("Miles Davis Albums", "Music", [
            ("Kind of Blue", True), ("A Love Supreme", False), ("Bitches Brew", True)
        ]),
        ("John Coltrane Albums", "Music", [
            ("A Love Supreme", True), ("Giant Steps", True), ("Kind of Blue", False)
        ]),
        ("Johnny Cash Albums", "Music", [
            ("At Folsom Prison", True), ("American IV: The Man Comes Around", True), ("Highway 61 Revisited", False)
        ]),
        ("Dolly Parton Songs", "Music", [
            ("Jolene", True), ("9 to 5", True), ("Crazy", False)
        ]),
        ("Elvis Presley Songs", "Music", [
            ("Hound Dog", True), ("Johnny B. Goode", False), ("Jailhouse Rock", True)
        ]),
        ("The Beach Boys Albums", "Music", [
            ("Pet Sounds", True), ("Surf's Up", True), ("Smile", True)
        ]),
        ("Simon & Garfunkel Albums", "Music", [
            ("Bridge Over Troubled Water", True), ("Bookends", True), ("American Pie", False)
        ]),
        ("Elton John Albums", "Music", [
            ("Goodbye Yellow Brick Road", True), ("Captain Fantastic", True), ("Tapestry", False)
        ]),
        ("Billy Joel Albums", "Music", [
            ("The Stranger", True), ("52nd Street", True), ("Piano Man 2", False)
        ]),
        ("Joni Mitchell Albums", "Music", [
            ("Blue", True), ("Court and Spark", True), ("Tapestry", False)
        ]),
        ("Carole King Albums", "Music", [
            ("Tapestry", True), ("Blue", False), ("Music", True)
        ]),
        ("AC/DC Albums", "Music", [
            ("Back in Black", True), ("Highway to Hell", True), ("Master of Puppets", False)
        ]),
        ("Black Sabbath Albums", "Music", [
            ("Paranoid", True), ("Master of Reality", True), ("Back in Black", False)
        ]),
        ("Iron Maiden Albums", "Music", [
            ("The Number of the Beast", True), ("Powerslave", True), ("Paranoid", False)
        ]),
        ("Guns N' Roses Albums", "Music", [
            ("Appetite for Destruction", True), ("Use Your Illusion I", True), ("Master of Puppets", False)
        ]),
        ("Foo Fighters Albums", "Music", [
            ("The Colour and the Shape", True), ("There Is Nothing Left to Lose", True), ("Nevermind", False)
        ]),
        ("Green Day Albums", "Music", [
            ("Dookie", True), ("American Idiot", True), ("Nevermind", False)
        ]),
        ("Blink-182 Albums", "Music", [
            ("Enema of the State", True), ("Dookie", False), ("Take Off Your Pants and Jacket", True)
        ]),
        ("Red Hot Chili Peppers Albums", "Music", [
            ("Blood Sugar Sex Magik", True), ("Californication", True), ("Ten", False)
        ]),
        ("Pearl Jam Albums", "Music", [
            ("Ten", True), ("Vs.", True), ("Nevermind", False)
        ]),
        ("Soundgarden Albums", "Music", [
            ("Superunknown", True), ("Badmotorfinger", True), ("Nevermind", False)
        ]),
        ("R.E.M. Albums", "Music", [
            ("Automatic for the People", True), ("Out of Time", True), ("Document", True)
        ]),
        ("Coldplay Albums", "Music", [
            ("Parachutes", True), ("A Rush of Blood to the Head", True), ("X&Y", True)
        ]),
        ("Muse Albums", "Music", [
            ("Absolution", True), ("Black Holes and Revelations", True), ("Showbiz", True)
        ]),
        ("Arctic Monkeys Albums", "Music", [
            ("Whatever People Say I Am, That's What I'm Not", True), ("AM", True), ("Favourite Worst Nightmare", True)
        ]),
        ("The Strokes Albums", "Music", [
            ("Is This It", True), ("Room on Fire", True), ("Angles", True)
        ]),
        ("OutKast Albums", "Music", [
            ("Stankonia", True), ("Speakerboxxx/The Love Below", True), ("The Miseducation of Lauryn Hill", False)
        ]),
        ("A Tribe Called Quest Albums", "Music", [
            ("The Low End Theory", True), ("Midnight Marauders", True), ("The Chronic", False)
        ]),
        ("Wu-Tang Clan Albums", "Music", [
            ("Enter the Wu-Tang (36 Chambers)", True), ("Wu-Tang Forever", True), ("The Chronic", False)
        ]),
        ("Nas Albums", "Music", [
            ("Illmatic", True), ("It Was Written", True), ("The Chronic", False)
        ]),
        ("Jay-Z Albums", "Music", [
            ("Reasonable Doubt", True), ("The Blueprint", True), ("Illmatic", False)
        ]),
        ("Eminem Albums", "Music", [
            ("The Marshall Mathers LP", True), ("The Eminem Show", True), ("The Slim Shady LP", True)
        ]),
        ("Lauryn Hill Albums (Solo)", "Music", [
            ("The Miseducation of Lauryn Hill", True), ("The Score", False), ("MTV Unplugged No. 2.0", True)
        ]),
        ("Aretha Franklin Songs", "Music", [
            ("Respect", True), ("Think", True), ("Natural Woman", True)
        ]),
        ("Nina Simone Songs", "Music", [
            ("Feeling Good", True), ("I Put a Spell on You", True), ("Respect", False)
        ]),
        ("Billie Holiday Songs", "Music", [
            ("Strange Fruit", True), ("God Bless the Child", True), ("Summertime", True)
        ]),
        ("Frank Sinatra Songs", "Music", [
            ("My Way", True), ("New York, New York", True), ("Fly Me to the Moon", True)
        ]),
        ("Ella Fitzgerald Albums", "Music", [
            ("Ella and Louis", True), ("Ella Fitzgerald Sings the Cole Porter Songbook", True), ("Kind of Blue", False)
        ]),
        ("Louis Armstrong Songs", "Music", [
            ("What a Wonderful World", True), ("Hello, Dolly!", True), ("My Way", False)
        ]),
        ("Duke Ellington Compositions", "Music", [
            ("Take the 'A' Train", True), ("Mood Indigo", True), ("Round Midnight", False)
        ]),
        ("Thelonious Monk Compositions", "Music", [
            ("Round Midnight", True), ("Blue Monk", True), ("Take Five", False)
        ]),
        ("Dave Brubeck Songs", "Music", [
            ("Take Five", True), ("Blue Rondo à la Turk", True), ("So What", False)
        ]),
        ("Herbie Hancock Albums", "Music", [
            ("Head Hunters", True), ("Maiden Voyage", True), ("A Love Supreme", False)
        ]),
        ("Chick Corea Albums", "Music", [
            ("Return to Forever", True), ("Light as a Feather", True), ("Head Hunters", False)
        ]),
        ("Daft Punk Albums", "Music", [
            ("Discovery", True), ("Random Access Memories", True), ("Cross", False)
        ]),
        ("Justice Albums", "Music", [
            ("Cross", True), ("Audio, Video, Disco", True), ("Discovery", False)
        ]),
        ("The Chemical Brothers Albums", "Music", [
            ("Dig Your Own Hole", True), ("Surrender", True), ("Play", False)
        ]),
        ("Moby Albums", "Music", [
            ("Play", True), ("18", True), ("Dig Your Own Hole", False)
        ]),
        ("Aphex Twin Albums", "Music", [
            ("Selected Ambient Works 85-92", True), ("Richard D. James Album", True), ("Play", False)
        ]),
        ("Björk Albums", "Music", [
            ("Homogenic", True), ("Post", True), ("Vespertine", True)
        ]),
        ("Portishead Albums", "Music", [
            ("Dummy", True), ("Third", True), ("Homogenic", False)
        ]),
        ("Massive Attack Albums", "Music", [
            ("Blue Lines", True), ("Mezzanine", True), ("Dummy", False)
        ]),
    ]

    # TV Shows (60)
    tv_questions = [
        ("Breaking Bad Episodes", "TV Shows", [
            ("Pilot", True), ("The Red Wedding", False), ("Ozymandias", True)
        ]),
        ("Game of Thrones Houses", "TV Shows", [
            ("Stark", True), ("Blackwood", False), ("Lannister", True)
        ]),
        ("The Office (US) Characters", "TV Shows", [
            ("Michael Scott", True), ("Leslie Knope", False), ("Dwight Schrute", True)
        ]),
        ("Friends Characters", "TV Shows", [
            ("Ross Geller", True), ("Barney Stinson", False), ("Chandler Bing", True)
        ]),
        ("Stranger Things Seasons", "TV Shows", [
            ("Season 1 takes place in 1983", True), ("Season 2 takes place in 1987", False), ("Season 3 takes place in 1985", True)
        ]),
        ("The Sopranos Characters", "TV Shows", [
            ("Tony Soprano", True), ("Walter White", False), ("Christopher Moltisanti", True)
        ]),
        ("The Wire Characters", "TV Shows", [
            ("Jimmy McNulty", True), ("Omar Little", True), ("Tony Soprano", False)
        ]),
        ("Mad Men Characters", "TV Shows", [
            ("Don Draper", True), ("Peggy Olson", True), ("Tony Soprano", False)
        ]),
        ("The Simpsons Characters", "TV Shows", [
            ("Homer Simpson", True), ("Peter Griffin", False), ("Bart Simpson", True)
        ]),
        ("South Park Characters", "TV Shows", [
            ("Eric Cartman", True), ("Homer Simpson", False), ("Kenny McCormick", True)
        ]),
        ("Seinfeld Characters", "TV Shows", [
            ("Jerry Seinfeld", True), ("George Costanza", True), ("Chandler Bing", False)
        ]),
        ("Parks and Recreation Characters", "TV Shows", [
            ("Leslie Knope", True), ("Michael Scott", False), ("Ron Swanson", True)
        ]),
        ("Brooklyn Nine-Nine Characters", "TV Shows", [
            ("Jake Peralta", True), ("Leslie Knope", False), ("Amy Santiago", True)
        ]),
        ("The Good Place Characters", "TV Shows", [
            ("Eleanor Shellstrop", True), ("Chidi Anagonye", True), ("Michael Scott", False)
        ]),
        ("Arrested Development Characters", "TV Shows", [
            ("Michael Bluth", True), ("George Michael Bluth", True), ("George Costanza", False)
        ]),
        ("Community Characters", "TV Shows", [
            ("Jeff Winger", True), ("Abed Nadir", True), ("Michael Bluth", False)
        ]),
        ("30 Rock Characters", "TV Shows", [
            ("Liz Lemon", True), ("Jack Donaghy", True), ("Leslie Knope", False)
        ]),
        ("It's Always Sunny in Philadelphia Characters", "TV Shows", [
            ("Dennis Reynolds", True), ("Charlie Kelly", True), ("Jerry Seinfeld", False)
        ]),
        ("Curb Your Enthusiasm Characters", "TV Shows", [
            ("Larry David", True), ("Jerry Seinfeld", False), ("Cheryl David", True)
        ]),
        ("Veep Characters", "TV Shows", [
            ("Selina Meyer", True), ("Gary Walsh", True), ("Leslie Knope", False)
        ]),
        ("Silicon Valley Characters", "TV Shows", [
            ("Richard Hendricks", True), ("Erlich Bachman", True), ("Michael Bluth", False)
        ]),
        ("The Crown Seasons", "TV Shows", [
            ("Season 1 covers Elizabeth's early reign", True), ("Season 2 covers the Diana era", False), ("Season 3 changes the cast", True)
        ]),
        ("Westworld Characters", "TV Shows", [
            ("Dolores Abernathy", True), ("Maeve Millay", True), ("Daenerys Targaryen", False)
        ]),
        ("Black Mirror Episodes", "TV Shows", [
            ("San Junipero", True), ("White Christmas", True), ("The Red Wedding", False)
        ]),
        ("Doctor Who Doctors", "TV Shows", [
            ("David Tennant played the Tenth Doctor", True), ("Matt Smith played the Twelfth Doctor", False), ("Peter Capaldi played the Twelfth Doctor", True)
        ]),
        ("Sherlock Episodes", "TV Shows", [
            ("A Study in Pink", True), ("The Reichenbach Fall", True), ("Elementary", False)
        ]),
        ("The X-Files Characters", "TV Shows", [
            ("Fox Mulder", True), ("Dana Scully", True), ("Jimmy McNulty", False)
        ]),
        ("Twin Peaks Characters", "TV Shows", [
            ("Dale Cooper", True), ("Laura Palmer", True), ("Rust Cohle", False)
        ]),
        ("True Detective Season 1 Characters", "TV Shows", [
            ("Rust Cohle", True), ("Marty Hart", True), ("Dale Cooper", False)
        ]),
        ("Fargo Characters", "TV Shows", [
            ("Lester Nygaard", True), ("Lorne Malvo", True), ("Rust Cohle", False)
        ]),
        ("Better Call Saul Characters", "TV Shows", [
            ("Jimmy McGill", True), ("Kim Wexler", True), ("Walter White", False)
        ]),
        ("Succession Characters", "TV Shows", [
            ("Logan Roy", True), ("Kendall Roy", True), ("Don Draper", False)
        ]),
        ("The Mandalorian Characters", "TV Shows", [
            ("Din Djarin", True), ("Grogu", True), ("Luke Skywalker", True)
        ]),
        ("The Boys Characters", "TV Shows", [
            ("Billy Butcher", True), ("Homelander", True), ("Tony Stark", False)
        ]),
        ("Watchmen Characters", "TV Shows", [
            ("Angela Abar", True), ("Looking Glass", True), ("Rorschach", True)
        ]),
        ("The Handmaid's Tale Characters", "TV Shows", [
            ("Offred/June", True), ("Serena Joy", True), ("Daenerys", False)
        ]),
        ("Fleabag Characters", "TV Shows", [
            ("Fleabag", True), ("The Priest", True), ("Phoebe Waller-Bridge", False)
        ]),
        ("Atlanta Characters", "TV Shows", [
            ("Earn Marks", True), ("Paper Boi", True), ("Donald Glover", False)
        ]),
        ("BoJack Horseman Characters", "TV Shows", [
            ("BoJack Horseman", True), ("Princess Carolyn", True), ("Todd Chavez", True)
        ]),
        ("Rick and Morty Characters", "TV Shows", [
            ("Rick Sanchez", True), ("Morty Smith", True), ("Homer Simpson", False)
        ]),
        ("The Marvelous Mrs. Maisel Characters", "TV Shows", [
            ("Midge Maisel", True), ("Susie Myerson", True), ("Fleabag", False)
        ]),
        ("Ozark Characters", "TV Shows", [
            ("Marty Byrde", True), ("Wendy Byrde", True), ("Walter White", False)
        ]),
        ("Narcos Characters", "TV Shows", [
            ("Pablo Escobar", True), ("Javier Peña", True), ("Tony Montana", False)
        ]),
        ("Mindhunter Characters", "TV Shows", [
            ("Holden Ford", True), ("Bill Tench", True), ("Fox Mulder", False)
        ]),
        ("Peaky Blinders Characters", "TV Shows", [
            ("Thomas Shelby", True), ("Arthur Shelby", True), ("Tony Soprano", False)
        ]),
        ("The Last of Us Characters", "TV Shows", [
            ("Joel", True), ("Ellie", True), ("Rick Grimes", False)
        ]),
        ("The Walking Dead Characters", "TV Shows", [
            ("Rick Grimes", True), ("Daryl Dixon", True), ("Joel", False)
        ]),
        ("Lost Characters", "TV Shows", [
            ("Jack Shephard", True), ("John Locke", True), ("Fox Mulder", False)
        ]),
        ("House Characters", "TV Shows", [
            ("Gregory House", True), ("James Wilson", True), ("Dana Scully", False)
        ]),
        ("Grey's Anatomy Characters", "TV Shows", [
            ("Meredith Grey", True), ("Derek Shepherd", True), ("Gregory House", False)
        ]),
        ("Scrubs Characters", "TV Shows", [
            ("J.D.", True), ("Turk", True), ("Gregory House", False)
        ]),
        ("The Big Bang Theory Characters", "TV Shows", [
            ("Sheldon Cooper", True), ("Leonard Hofstadter", True), ("Ross Geller", False)
        ]),
        ("How I Met Your Mother Characters", "TV Shows", [
            ("Ted Mosby", True), ("Barney Stinson", True), ("Chandler Bing", False)
        ]),
        ("New Girl Characters", "TV Shows", [
            ("Jess Day", True), ("Nick Miller", True), ("Ted Mosby", False)
        ]),
        ("Modern Family Characters", "TV Shows", [
            ("Phil Dunphy", True), ("Claire Dunphy", True), ("Michael Scott", False)
        ]),
        ("Schitt's Creek Characters", "TV Shows", [
            ("David Rose", True), ("Alexis Rose", True), ("Fleabag", False)
        ]),
        ("The Marvelous Mrs. Maisel Time Period", "TV Shows", [
            ("Set in the 1950s", True), ("Set in the 1960s", True), ("Set in the 1970s", False)
        ]),
        ("Chernobyl Characters", "TV Shows", [
            ("Valery Legasov", True), ("Boris Shcherbina", True), ("Walter White", False)
        ]),
        ("Band of Brothers Characters", "TV Shows", [
            ("Richard Winters", True), ("Lewis Nixon", True), ("Rick Grimes", False)
        ]),
        ("The Pacific Characters", "TV Shows", [
            ("Eugene Sledge", True), ("Robert Leckie", True), ("Richard Winters", False)
        ]),
    ]

    # History (50)
    history_questions = [
        ("World War II Battles", "History", [
            ("Battle of Stalingrad", True), ("Battle of Waterloo", False), ("Battle of Midway", True)
        ]),
        ("Seven Wonders of the Ancient World", "History", [
            ("The Great Pyramid of Giza", True), ("The Colosseum", False), ("The Hanging Gardens of Babylon", True)
        ]),
        ("US Presidents", "History", [
            ("Abraham Lincoln", True), ("Benjamin Franklin", False), ("George Washington", True)
        ]),
        ("World War I Battles", "History", [
            ("Battle of the Somme", True), ("Battle of Verdun", True), ("Battle of Stalingrad", False)
        ]),
        ("Ancient Egyptian Pharaohs", "History", [
            ("Tutankhamun", True), ("Cleopatra", True), ("Nebuchadnezzar", False)
        ]),
        ("Roman Emperors", "History", [
            ("Julius Caesar", True), ("Augustus", True), ("Alexander the Great", False)
        ]),
        ("American Revolutionary War Battles", "History", [
            ("Battle of Bunker Hill", True), ("Battle of Yorktown", True), ("Battle of Gettysburg", False)
        ]),
        ("Civil Rights Movement Leaders", "History", [
            ("Martin Luther King Jr.", True), ("Malcolm X", True), ("Abraham Lincoln", False)
        ]),
        ("Cold War Events", "History", [
            ("Cuban Missile Crisis", True), ("Berlin Wall Construction", True), ("Vietnam War End", True)
        ]),
        ("Renaissance Artists", "History", [
            ("Leonardo da Vinci", True), ("Michelangelo", True), ("Picasso", False)
        ]),
        ("French Revolution Events", "History", [
            ("Storming of the Bastille", True), ("Reign of Terror", True), ("Battle of Waterloo", False)
        ]),
        ("Magna Carta Clauses", "History", [
            ("Signed in 1215", True), ("Signed in 1066", False), ("Limited the power of the King", True)
        ]),
        ("Declaration of Independence Signers", "History", [
            ("John Hancock", True), ("Benjamin Franklin", True), ("Alexander Hamilton", False)
        ]),
        ("Silk Road Trading Cities", "History", [
            ("Samarkand", True), ("Beijing", True), ("London", False)
        ]),
        ("Age of Exploration Navigators", "History", [
            ("Christopher Columbus", True), ("Ferdinand Magellan", True), ("James Cook", True)
        ]),
        ("Mongol Empire Leaders", "History", [
            ("Genghis Khan", True), ("Kublai Khan", True), ("Attila the Hun", False)
        ]),
        ("American Civil War Battles", "History", [
            ("Battle of Gettysburg", True), ("Battle of Antietam", True), ("Battle of Bunker Hill", False)
        ]),
        ("Industrial Revolution Inventions", "History", [
            ("Steam Engine", True), ("Telegraph", True), ("Telephone", True)
        ]),
        ("Napoleonic Wars Battles", "History", [
            ("Battle of Waterloo", True), ("Battle of Austerlitz", True), ("Battle of Gettysburg", False)
        ]),
        ("Byzantine Empire Emperors", "History", [
            ("Justinian I", True), ("Constantine XI", True), ("Julius Caesar", False)
        ]),
        ("Medieval Crusades", "History", [
            ("First Crusade began in 1096", True), ("Jerusalem was captured in 1099", True), ("Crusades ended in 1066", False)
        ]),
        ("Hundred Years' War Battles", "History", [
            ("Battle of Agincourt", True), ("Battle of Crécy", True), ("Battle of Waterloo", False)
        ]),
        ("Spanish Conquistadors", "History", [
            ("Hernán Cortés", True), ("Francisco Pizarro", True), ("Christopher Columbus", False)
        ]),
        ("Ottoman Empire Sultans", "History", [
            ("Suleiman the Magnificent", True), ("Mehmed II", True), ("Genghis Khan", False)
        ]),
        ("Enlightenment Philosophers", "History", [
            ("John Locke", True), ("Voltaire", True), ("Socrates", False)
        ]),
        ("American Founding Fathers", "History", [
            ("Thomas Jefferson", True), ("James Madison", True), ("Abraham Lincoln", False)
        ]),
        ("Victorian Era Inventions", "History", [
            ("Telegraph", True), ("Telephone", True), ("Television", False)
        ]),
        ("Meiji Restoration Japan", "History", [
            ("Began in 1868", True), ("Ended the Shogunate", True), ("Began in 1945", False)
        ]),
        ("Russian Tsars", "History", [
            ("Peter the Great", True), ("Ivan the Terrible", True), ("Vladimir Putin", False)
        ]),
        ("Space Race Achievements", "History", [
            ("Sputnik 1 launched in 1957", True), ("First human in space in 1961", True), ("Moon landing in 1965", False)
        ]),
        ("Ancient Greek Philosophers", "History", [
            ("Socrates", True), ("Plato", True), ("Voltaire", False)
        ]),
        ("Aztec Empire", "History", [
            ("Capital was Tenochtitlan", True), ("Conquered by Cortés", True), ("Located in Peru", False)
        ]),
        ("Inca Empire", "History", [
            ("Located in Peru", True), ("Conquered by Pizarro", True), ("Capital was Tenochtitlan", False)
        ]),
        ("Ancient Greece City-States", "History", [
            ("Athens", True), ("Sparta", True), ("Rome", False)
        ]),
        ("Persian Empire Kings", "History", [
            ("Cyrus the Great", True), ("Darius I", True), ("Alexander the Great", False)
        ]),
        ("Protestant Reformation Leaders", "History", [
            ("Martin Luther", True), ("John Calvin", True), ("Pope Leo X", False)
        ]),
        ("Thirty Years' War", "History", [
            ("Fought from 1618-1648", True), ("Primarily in Central Europe", True), ("Fought from 1914-1918", False)
        ]),
        ("Scientific Revolution Scientists", "History", [
            ("Galileo Galilei", True), ("Isaac Newton", True), ("Albert Einstein", False)
        ]),
        ("Manhattan Project", "History", [
            ("Developed the atomic bomb", True), ("Led by Robert Oppenheimer", True), ("Ended World War I", False)
        ]),
        ("Vietnam War Events", "History", [
            ("Tet Offensive in 1968", True), ("Gulf of Tonkin Incident", True), ("Pearl Harbor Attack", False)
        ]),
        ("Korean War Events", "History", [
            ("Began in 1950", True), ("38th Parallel Division", True), ("Ended in 1975", False)
        ]),
        ("Fall of the Berlin Wall", "History", [
            ("Occurred in 1989", True), ("Symbolized end of Cold War", True), ("Built in 1989", False)
        ]),
        ("9/11 Terrorist Attacks", "History", [
            ("Occurred on September 11, 2001", True), ("World Trade Center destroyed", True), ("Pentagon not affected", False)
        ]),
        ("Arab Spring", "History", [
            ("Began in 2010", True), ("Started in Tunisia", True), ("Ended in 1989", False)
        ]),
        ("Brexit", "History", [
            ("UK voted to leave EU in 2016", True), ("Became official in 2020", True), ("Scotland voted to leave UK", False)
        ]),
        ("Apartheid in South Africa", "History", [
            ("Ended in 1994", True), ("Nelson Mandela was imprisoned", True), ("Occurred in Zimbabwe", False)
        ]),
        ("Cuban Revolution", "History", [
            ("Led by Fidel Castro", True), ("Occurred in 1959", True), ("Che Guevara was not involved", False)
        ]),
        ("Irish Potato Famine", "History", [
            ("Occurred in 1845-1852", True), ("Caused mass emigration", True), ("Occurred in Scotland", False)
        ]),
        ("Treaty of Versailles", "History", [
            ("Ended World War I", True), ("Signed in 1919", True), ("Ended World War II", False)
        ]),
        ("D-Day Invasion", "History", [
            ("Occurred on June 6, 1944", True), ("Allied invasion of Normandy", True), ("Invasion of Pearl Harbor", False)
        ]),
    ]

    # Science (50)
    science_questions = [
        ("Nobel Prize Categories", "Science", [
            ("Physics", True), ("Mathematics", False), ("Chemistry", True)
        ]),
        ("Planets with Moons", "Science", [
            ("Jupiter", True), ("Mercury", False), ("Saturn", True)
        ]),
        ("Chemical Elements", "Science", [
            ("Helium", True), ("Electricium", False), ("Oxygen", True)
        ]),
        ("Nobel Prize Winners in Physics", "Science", [
            ("Albert Einstein", True), ("Charles Darwin", False), ("Marie Curie", True)
        ]),
        ("States of Matter", "Science", [
            ("Solid", True), ("Liquid", True), ("Gas", True)
        ]),
        ("Parts of the Human Brain", "Science", [
            ("Cerebrum", True), ("Cerebellum", True), ("Medulla", True)
        ]),
        ("Types of Clouds", "Science", [
            ("Cumulus", True), ("Stratus", True), ("Nebula", False)
        ]),
        ("DNA Nucleotides", "Science", [
            ("Adenine", True), ("Thymine", True), ("Uracil", False)
        ]),
        ("Layers of Earth's Atmosphere", "Science", [
            ("Troposphere", True), ("Stratosphere", True), ("Mesosphere", True)
        ]),
        ("Newton's Laws of Motion", "Science", [
            ("Law of Inertia", True), ("Law of Acceleration", True), ("Law of Relativity", False)
        ]),
        ("Taxonomic Ranks", "Science", [
            ("Kingdom", True), ("Phylum", True), ("Division", False)
        ]),
        ("Parts of a Cell", "Science", [
            ("Nucleus", True), ("Mitochondria", True), ("Vacuole", True)
        ]),
        ("Types of Rocks", "Science", [
            ("Igneous", True), ("Sedimentary", True), ("Metamorphic", True)
        ]),
        ("Greenhouse Gases", "Science", [
            ("Carbon Dioxide", True), ("Methane", True), ("Nitrogen", False)
        ]),
        ("Human Body Systems", "Science", [
            ("Circulatory", True), ("Respiratory", True), ("Metabolic", False)
        ]),
        ("Electromagnetic Spectrum", "Science", [
            ("Visible Light", True), ("Ultraviolet", True), ("Sound Waves", False)
        ]),
        ("Organelles in Eukaryotic Cells", "Science", [
            ("Endoplasmic Reticulum", True), ("Golgi Apparatus", True), ("Flagellum", True)
        ]),
        ("Types of Chemical Bonds", "Science", [
            ("Ionic", True), ("Covalent", True), ("Nuclear", False)
        ]),
        ("Blood Types", "Science", [
            ("A", True), ("B", True), ("C", False)
        ]),
        ("Phases of Mitosis", "Science", [
            ("Prophase", True), ("Metaphase", True), ("Anaphase", True)
        ]),
        ("Noble Gases", "Science", [
            ("Helium", True), ("Neon", True), ("Nitrogen", False)
        ]),
        ("Fundamental Forces of Nature", "Science", [
            ("Gravity", True), ("Electromagnetic", True), ("Nuclear Fusion", False)
        ]),
        ("Types of Electromagnetic Radiation", "Science", [
            ("Gamma Rays", True), ("X-Rays", True), ("Sound Waves", False)
        ]),
        ("Darwin's Finches Adaptations", "Science", [
            ("Beak shape varies by food source", True), ("Found on Galápagos Islands", True), ("All have identical beaks", False)
        ]),
        ("Mendel's Laws of Inheritance", "Science", [
            ("Law of Segregation", True), ("Law of Independent Assortment", True), ("Law of Natural Selection", False)
        ]),
        ("Quantum Mechanics Principles", "Science", [
            ("Wave-Particle Duality", True), ("Uncertainty Principle", True), ("Law of Conservation of Matter", False)
        ]),
        ("Plate Tectonic Boundaries", "Science", [
            ("Convergent", True), ("Divergent", True), ("Transform", True)
        ]),
        ("Types of Volcanoes", "Science", [
            ("Shield", True), ("Composite", True), ("Cinder Cone", True)
        ]),
        ("Renewable Energy Sources", "Science", [
            ("Solar", True), ("Wind", True), ("Natural Gas", False)
        ]),
        ("Vitamin Classifications", "Science", [
            ("Water-Soluble", True), ("Fat-Soluble", True), ("Protein-Soluble", False)
        ]),
        ("Types of Neurons", "Science", [
            ("Sensory", True), ("Motor", True), ("Cardiac", False)
        ]),
        ("Photosynthesis Products", "Science", [
            ("Glucose", True), ("Oxygen", True), ("Carbon Dioxide", False)
        ]),
        ("Immune System Cells", "Science", [
            ("T Cells", True), ("B Cells", True), ("Red Blood Cells", False)
        ]),
        ("Enzyme Functions", "Science", [
            ("Catalyze reactions", True), ("Lower activation energy", True), ("Provide energy", False)
        ]),
        ("Properties of Water", "Science", [
            ("Cohesion", True), ("Adhesion", True), ("Compressibility", False)
        ]),
        ("Thermodynamic Laws", "Science", [
            ("First Law (Conservation of Energy)", True), ("Second Law (Entropy)", True), ("Third Law (Absolute Zero)", True)
        ]),
        ("Types of Galaxies", "Science", [
            ("Spiral", True), ("Elliptical", True), ("Irregular", True)
        ]),
        ("Atomic Particles", "Science", [
            ("Protons", True), ("Neutrons", True), ("Electrons", True)
        ]),
        ("Types of Chemical Reactions", "Science", [
            ("Synthesis", True), ("Decomposition", True), ("Combination", True)
        ]),
        ("Biomes", "Science", [
            ("Tundra", True), ("Desert", True), ("Rainforest", True)
        ]),
        ("Muscular System Muscle Types", "Science", [
            ("Skeletal", True), ("Smooth", True), ("Cardiac", True)
        ]),
        ("Digestive System Organs", "Science", [
            ("Stomach", True), ("Small Intestine", True), ("Large Intestine", True)
        ]),
        ("Respiratory System Parts", "Science", [
            ("Trachea", True), ("Bronchi", True), ("Alveoli", True)
        ]),
        ("Circulatory System Components", "Science", [
            ("Heart", True), ("Arteries", True), ("Veins", True)
        ]),
        ("Endocrine System Glands", "Science", [
            ("Pituitary", True), ("Thyroid", True), ("Pancreas", True)
        ]),
        ("Geological Time Periods", "Science", [
            ("Jurassic", True), ("Cretaceous", True), ("Triassic", True)
        ]),
        ("Types of Fossils", "Science", [
            ("Body Fossils", True), ("Trace Fossils", True), ("Living Fossils", True)
        ]),
        ("Astronomical Objects", "Science", [
            ("Stars", True), ("Planets", True), ("Nebulae", True)
        ]),
        ("Types of Stars", "Science", [
            ("Red Giant", True), ("White Dwarf", True), ("Black Hole", True)
        ]),
        ("Evolution Mechanisms", "Science", [
            ("Natural Selection", True), ("Genetic Drift", True), ("Mutation", True)
        ]),
    ]

    # Geography (40)
    geography_questions = [
        ("Countries in Africa", "Geography", [
            ("Kenya", True), ("Portugal", False), ("Morocco", True)
        ]),
        ("Countries in South America", "Geography", [
            ("Brazil", True), ("Mexico", False), ("Argentina", True)
        ]),
        ("Countries in Asia", "Geography", [
            ("Japan", True), ("Egypt", False), ("Thailand", True)
        ]),
        ("Countries that Border France", "Geography", [
            ("Spain", True), ("Portugal", False), ("Switzerland", True)
        ]),
        ("Capital Cities", "Geography", [
            ("Paris is the capital of France", True), ("Sydney is the capital of Australia", False), ("Tokyo is the capital of Japan", True)
        ]),
        ("Continents", "Geography", [
            ("Asia", True), ("Atlantis", False), ("Antarctica", True)
        ]),
        ("Oceans", "Geography", [
            ("Pacific", True), ("Atlantic", True), ("Southern", True)
        ]),
        ("Great Lakes", "Geography", [
            ("Superior", True), ("Michigan", True), ("Huron", True)
        ]),
        ("Longest Rivers", "Geography", [
            ("Nile", True), ("Amazon", True), ("Mississippi", True)
        ]),
        ("Highest Mountains", "Geography", [
            ("Mount Everest", True), ("K2", True), ("Kilimanjaro", True)
        ]),
        ("Countries in Europe", "Geography", [
            ("Germany", True), ("Turkey", False), ("Italy", True)
        ]),
        ("Island Nations", "Geography", [
            ("Japan", True), ("Indonesia", True), ("Philippines", True)
        ]),
        ("Landlocked Countries", "Geography", [
            ("Switzerland", True), ("Bolivia", True), ("Mongolia", True)
        ]),
        ("US States", "Geography", [
            ("California", True), ("Texas", True), ("New York", True)
        ]),
        ("Canadian Provinces", "Geography", [
            ("Ontario", True), ("Quebec", True), ("British Columbia", True)
        ]),
        ("Australian States", "Geography", [
            ("New South Wales", True), ("Victoria", True), ("Queensland", True)
        ]),
        ("Countries with the Largest Populations", "Geography", [
            ("China", True), ("India", True), ("Indonesia", True)
        ]),
        ("Countries with the Largest Land Areas", "Geography", [
            ("Russia", True), ("Canada", True), ("United States", True)
        ]),
        ("Deserts", "Geography", [
            ("Sahara", True), ("Gobi", True), ("Mojave", True)
        ]),
        ("Rainforests", "Geography", [
            ("Amazon", True), ("Congo", True), ("Daintree", True)
        ]),
        ("Peninsulas", "Geography", [
            ("Iberian", True), ("Arabian", True), ("Korean", True)
        ]),
        ("Straits", "Geography", [
            ("Strait of Gibraltar", True), ("Bosporus", True), ("Strait of Malacca", True)
        ]),
        ("Major Cities in the United States", "Geography", [
            ("New York City", True), ("Los Angeles", True), ("Toronto", False)
        ]),
        ("Major Cities in China", "Geography", [
            ("Beijing", True), ("Shanghai", True), ("Tokyo", False)
        ]),
        ("Major Cities in India", "Geography", [
            ("Mumbai", True), ("Delhi", True), ("Karachi", False)
        ]),
        ("Countries in the Middle East", "Geography", [
            ("Saudi Arabia", True), ("Iran", True), ("Pakistan", False)
        ]),
        ("Countries in Scandinavia", "Geography", [
            ("Sweden", True), ("Norway", True), ("Finland", True)
        ]),
        ("Countries in the Caribbean", "Geography", [
            ("Jamaica", True), ("Cuba", True), ("Bahamas", True)
        ]),
        ("Countries in Central America", "Geography", [
            ("Costa Rica", True), ("Panama", True), ("Mexico", False)
        ]),
        ("Countries that use the Euro", "Geography", [
            ("Germany", True), ("France", True), ("United Kingdom", False)
        ]),
        ("Countries in the United Kingdom", "Geography", [
            ("England", True), ("Scotland", True), ("Ireland", False)
        ]),
        ("Time Zones", "Geography", [
            ("GMT", True), ("EST", True), ("PST", True)
        ]),
        ("Major Airports", "Geography", [
            ("Heathrow", True), ("JFK", True), ("Charles de Gaulle", True)
        ]),
        ("UNESCO World Heritage Sites", "Geography", [
            ("Machu Picchu", True), ("Great Wall of China", True), ("Eiffel Tower", False)
        ]),
        ("Active Volcanoes", "Geography", [
            ("Mount Vesuvius", True), ("Mount St. Helens", True), ("Mount Rushmore", False)
        ]),
        ("Major Waterfalls", "Geography", [
            ("Niagara Falls", True), ("Victoria Falls", True), ("Angel Falls", True)
        ]),
        ("Countries that Border the Mediterranean Sea", "Geography", [
            ("Spain", True), ("France", True), ("Portugal", False)
        ]),
        ("Countries on the Equator", "Geography", [
            ("Ecuador", True), ("Kenya", True), ("Brazil", True)
        ]),
        ("Major Mountain Ranges", "Geography", [
            ("Himalayas", True), ("Andes", True), ("Alps", True)
        ]),
        ("Major Seas", "Geography", [
            ("Mediterranean Sea", True), ("Caribbean Sea", True), ("Dead Sea", True)
        ]),
    ]

    # Literature (30)
    literature_questions = [
        ("Shakespeare Plays", "Literature", [
            ("Hamlet", True), ("The Faerie Queene", False), ("Macbeth", True)
        ]),
        ("Aesop's Fables", "Literature", [
            ("The Tortoise and the Hare", True), ("The Ancient Cat and the Youthful Rat", False), ("The Fox and the Grapes", True)
        ]),
        ("Harry Potter Books", "Literature", [
            ("Philosopher's Stone", True), ("The Order of the Dragon", False), ("Goblet of Fire", True)
        ]),
        ("Lord of the Rings Characters", "Literature", [
            ("Gandalf", True), ("Dumbledore", False), ("Aragorn", True)
        ]),
        ("George Orwell Novels", "Literature", [
            ("1984", True), ("Brave New World", False), ("Animal Farm", True)
        ]),
        ("Jane Austen Novels", "Literature", [
            ("Pride and Prejudice", True), ("Wuthering Heights", False), ("Emma", True)
        ]),
        ("Charles Dickens Novels", "Literature", [
            ("Great Expectations", True), ("Oliver Twist", True), ("Jane Eyre", False)
        ]),
        ("Mark Twain Works", "Literature", [
            ("The Adventures of Tom Sawyer", True), ("Moby-Dick", False), ("Adventures of Huckleberry Finn", True)
        ]),
        ("Ernest Hemingway Novels", "Literature", [
            ("The Old Man and the Sea", True), ("The Great Gatsby", False), ("For Whom the Bell Tolls", True)
        ]),
        ("F. Scott Fitzgerald Novels", "Literature", [
            ("The Great Gatsby", True), ("This Side of Paradise", True), ("The Sun Also Rises", False)
        ]),
        ("Toni Morrison Novels", "Literature", [
            ("Beloved", True), ("The Color Purple", False), ("Song of Solomon", True)
        ]),
        ("Gabriel García Márquez Novels", "Literature", [
            ("One Hundred Years of Solitude", True), ("Love in the Time of Cholera", True), ("The House of the Spirits", False)
        ]),
        ("Virginia Woolf Novels", "Literature", [
            ("Mrs Dalloway", True), ("To the Lighthouse", True), ("Jane Eyre", False)
        ]),
        ("James Joyce Works", "Literature", [
            ("Ulysses", True), ("Dubliners", True), ("The Waste Land", False)
        ]),
        ("T.S. Eliot Poems", "Literature", [
            ("The Waste Land", True), ("The Love Song of J. Alfred Prufrock", True), ("Howl", False)
        ]),
        ("Emily Dickinson Poems", "Literature", [
            ("Because I could not stop for Death", True), ("Hope is the thing with feathers", True), ("The Raven", False)
        ]),
        ("Edgar Allan Poe Works", "Literature", [
            ("The Raven", True), ("The Tell-Tale Heart", True), ("Frankenstein", False)
        ]),
        ("Mary Shelley Novels", "Literature", [
            ("Frankenstein", True), ("Dracula", False), ("The Last Man", True)
        ]),
        ("Bram Stoker Novels", "Literature", [
            ("Dracula", True), ("Frankenstein", False), ("The Lair of the White Worm", True)
        ]),
        ("Lewis Carroll Works", "Literature", [
            ("Alice's Adventures in Wonderland", True), ("Peter Pan", False), ("Through the Looking-Glass", True)
        ]),
        ("J.M. Barrie Works", "Literature", [
            ("Peter Pan", True), ("The Little White Bird", True), ("Alice's Adventures in Wonderland", False)
        ]),
        ("C.S. Lewis Works", "Literature", [
            ("The Lion, the Witch and the Wardrobe", True), ("The Hobbit", False), ("The Chronicles of Narnia", True)
        ]),
        ("J.R.R. Tolkien Works", "Literature", [
            ("The Hobbit", True), ("The Lord of the Rings", True), ("The Chronicles of Narnia", False)
        ]),
        ("Roald Dahl Children's Books", "Literature", [
            ("Charlie and the Chocolate Factory", True), ("The Cat in the Hat", False), ("Matilda", True)
        ]),
        ("Dr. Seuss Books", "Literature", [
            ("The Cat in the Hat", True), ("Green Eggs and Ham", True), ("Charlotte's Web", False)
        ]),
        ("Agatha Christie Novels", "Literature", [
            ("Murder on the Orient Express", True), ("The Hound of the Baskervilles", False), ("And Then There Were None", True)
        ]),
        ("Arthur Conan Doyle Works", "Literature", [
            ("The Hound of the Baskervilles", True), ("A Study in Scarlet", True), ("Murder on the Orient Express", False)
        ]),
        ("Stephen King Novels", "Literature", [
            ("The Shining", True), ("It", True), ("The Stand", True)
        ]),
        ("Margaret Atwood Novels", "Literature", [
            ("The Handmaid's Tale", True), ("Oryx and Crake", True), ("Beloved", False)
        ]),
        ("Haruki Murakami Novels", "Literature", [
            ("Norwegian Wood", True), ("1Q84", True), ("The Wind-Up Bird Chronicle", True)
        ]),
    ]

    # Video Games (10)
    games_questions = [
        ("Nintendo Game Franchises", "Video Games", [
            ("Super Mario", True), ("Sonic the Hedgehog", False), ("The Legend of Zelda", True)
        ]),
        ("PlayStation Exclusive Franchises", "Video Games", [
            ("God of War", True), ("Halo", False), ("The Last of Us", True)
        ]),
        ("Grand Theft Auto Games", "Video Games", [
            ("GTA V", True), ("GTA: San Andreas", True), ("GTA: London", False)
        ]),
        ("Call of Duty Games", "Video Games", [
            ("Modern Warfare", True), ("Black Ops", True), ("Battlefield", False)
        ]),
        ("Super Smash Bros Characters (Original)", "Video Games", [
            ("Mario", True), ("Sonic", False), ("Link", True)
        ]),
        ("Pokémon Generations", "Video Games", [
            ("Generation I (Red/Blue)", True), ("Generation II (Gold/Silver)", True), ("Generation X", False)
        ]),
        ("Final Fantasy Games", "Video Games", [
            ("Final Fantasy VII", True), ("Final Fantasy X", True), ("Final Fantasy XVII", False)
        ]),
        ("The Elder Scrolls Games", "Video Games", [
            ("Skyrim", True), ("Oblivion", True), ("Dragon Age", False)
        ]),
        ("Assassin's Creed Games", "Video Games", [
            ("Assassin's Creed II", True), ("Assassin's Creed: Brotherhood", True), ("Prince of Persia", False)
        ]),
        ("Dark Souls Series", "Video Games", [
            ("Dark Souls", True), ("Dark Souls III", True), ("Demon's Souls", True)
        ]),
    ]

    # Combine all questions
    all_questions = (
        programming_questions +
        movie_questions +
        music_questions +
        tv_questions +
        history_questions +
        science_questions +
        geography_questions +
        literature_questions +
        games_questions
    )

    # Format into JSON structure
    for question_text, category, statements in all_questions:
        question = {
            "question_text": question_text,
            "category": category,
            "difficulty": "medium",
            "statements": [
                {
                    "text": stmt[0],
                    "is_true": stmt[1],
                    "order": idx + 1,
                    "ghost_only": idx == 2  # Third statement is ghost-only
                }
                for idx, stmt in enumerate(statements)
            ]
        }
        questions.append(question)

    return {"questions": questions}

if __name__ == "__main__":
    print("Generating 500 haunting race questions...")
    data = create_questions()

    output_file = "haunting_race_questions.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\n✓ Generated {len(data['questions'])} questions")
    print(f"✓ Written to {output_file}")

    # Show breakdown by category
    from collections import Counter
    categories = [q['category'] for q in data['questions']]
    breakdown = Counter(categories)

    print("\nQuestions by category:")
    for category, count in sorted(breakdown.items(), key=lambda x: x[1], reverse=True):
        print(f"  {category}: {count}")
