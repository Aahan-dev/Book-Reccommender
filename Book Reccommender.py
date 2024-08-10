class BookRecommendationSystem:
    def __init__(self):
        """Initialize the book recommendation system with a sample dataset."""
        self.books = [
            {"title": "To Kill a Mockingbird", "genre": "Fiction", "author": "Harper Lee"},
            {"title": "1984", "genre": "Dystopian", "author": "George Orwell"},
            {"title": "Pride and Prejudice", "genre": "Romance", "author": "Jane Austen"},
            {"title": "The Great Gatsby", "genre": "Fiction", "author": "F. Scott Fitzgerald"},
            {"title": "Moby Dick", "genre": "Adventure", "author": "Herman Melville"},
            {"title": "War and Peace", "genre": "Historical", "author": "Leo Tolstoy"},
            {"title": "The Catcher in the Rye", "genre": "Fiction", "author": "J.D. Salinger"},
            {"title": "Brave New World", "genre": "Dystopian", "author": "Aldous Huxley"},
        ]

    def recommend_by_genre(self, genre):
        """
        Recommend books based on the specified genre.

        Args:
            genre (str): The genre to filter books by.

        Returns:
            list: A list of recommended book titles.
        """
        recommended = [book['title'] for book in self.books if book['genre'].lower() == genre.lower()]
        return recommended

    def recommend_by_author(self, author):
        """
        Recommend books by a specific author.


        Args:
            author (str): The author's name to filter books by.


        Returns:
            list: A list of recommended book titles.
        """
        recommended = [book['title'] for book in self.books if book['author'].lower() == author.lower()]
        return recommended


    def run(self):
        """Run the book recommendation system."""
        print("Welcome to the Book Recommendation System!")
       
        while True:
            print("\nChoose a recommendation method:")
            print("1. By Genre")
            print("2. By Author")
            print("3. Exit")


            