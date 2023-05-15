from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# API endpoint to fetch movies by year
@app.route('/movies', methods=['GET'])
def fetch_movies():
    year = request.args.get('year')
    if year is None:
        return jsonify({'error': 'Year parameter is missing.'}), 400

    # WARNING: This code is intentionally vulnerable to SQL injection
    connection = sqlite3.connect('movies.db')
    cursor = connection.cursor()
    query = "SELECT title FROM movies WHERE year = '%s'" % year
    cursor.execute(query)
    movies = [row[0] for row in cursor.fetchall()]
    connection.close()
    
    return jsonify({'movies': movies})

# Function to retrieve movies from a given year
def get_movies_secure(year):
    connection = sqlite3.connect('movies.db')
    cursor = connection.cursor()
    cursor.execute("SELECT title FROM movies WHERE year = ?", (year,))
    movies = [row[0] for row in cursor.fetchall()]
    connection.close()
    return movies

# API endpoint to fetch movies by year
@app.route('/movies2', methods=['GET'])
def fetch_movies_secure():
    year = request.args.get('year')
    if year is None:
        return jsonify({'error': 'Year parameter is missing.'}), 400

    try:
        year = int(year)
    except ValueError:
        return jsonify({'error': 'Year parameter must be an integer.'}), 400

    movies = get_movies_secure(year)
    return jsonify({'movies': movies})

if __name__ == '__main__':
    app.run()
