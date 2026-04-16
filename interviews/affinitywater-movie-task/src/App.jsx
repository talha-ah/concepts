import { useEffect, useState } from 'react';

// you may add functionality to these functions, but please use them
import { fetchGenres, fetchMovies } from './api';
import './styles.css'; // have a look at this file and feel free to use the classes

import { Movies } from './Movies';
import { Genres } from './Genres';

import { Input } from './Input';
import { Button } from './Button';

export default function App() {
  const [movies, setMovies] = useState([]);
  const [genres, setGenres] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // fetch movies and genres
    fetchData();
  }, []);

  const fetchData = async () => {
    // fetch movies and genres (can be done in separate methods)
    // Can be done using a custom hook as well (useFetch)

    const moviesRes = await fetchMovies();
    const genresRes = await fetchGenres();

    if (!moviesRes.ok) return;
    if (!genresRes.ok) return;

    const movies = await moviesRes.json();
    const genres = await genresRes.json();

    setMovies(
      movies.map((movie) => ({
        ...movie,
        genres: genres.filter((g) => movie.genre_ids.includes(g.id)),
      }))
    );
    setGenres(genres);
    setLoading(false);
  };

  // As we don't have filter on the api side, we need to filter the movies on the client side
  // and istead of fetching the movies for every genre, we can fetch them once and filter them
  const [filteredMovies, setFilteredMovies] = useState([]);
  const [selectedGenres, setSelectedGenres] = useState([]);

  // Filter movies by rating
  const [rating, setRating] = useState(0);

  useEffect(() => {
    // Using the genre list added above,
    // add a multiple genres filter using checkboxes.
    // The user should have the ability to toggle movies depending on all of its assigned genres.
    // For example if 'Action' and 'Drama' genres are selected, listed movies must have both 'Action' and 'Drama' genres.

    // If no genre is selected, all movies should be listed.
    if (selectedGenres.length === 0) {
      setFilteredMovies(movies.filter((m) => m.vote_average >= rating));
      return;
    }

    // Filter movies by selected genres
    setFilteredMovies(
      movies.filter((movie) => {
        return selectedGenres.every(
          (genre) =>
            movie.genre_ids.includes(genre.id) && movie.vote_average >= rating
        );
      })
    );

    // Dependencies
  }, [movies, selectedGenres, rating]);

  const handleGenreSelect = (genre) => {
    // add or remove genre from selectedGenres

    // If the genre is already selected, remove it
    if (selectedGenres.findIndex((g) => g.id === genre.id) !== -1) {
      setSelectedGenres(selectedGenres.filter((g) => g.id !== genre.id));
      return;
    }

    // otherwise add it
    setSelectedGenres([...selectedGenres, genre]);
  };

  const handleGenreReset = () => {
    // reset genres
    setSelectedGenres([]);
  };

  const handleRatingChange = ({ target: { value } }) => {
    setRating(value);
  };

  return (
    <div>
      <h1>
        <span>
          <span role="img" aria-label="Popcorn emoji">
            🍿
          </span>{' '}
          Now playing
        </span>
      </h1>
      <div>
        {loading ? (
          <div>Loading...</div>
        ) : (
          <div>Showing {filteredMovies.length} movies</div>
        )}

        <Genres
          genres={genres}
          onSelect={handleGenreSelect}
          selectedGenres={selectedGenres}
        />

        <div
          style={{
            margin: '1rem 0',
          }}
        >
          <Button onClick={handleGenreReset}>Reset</Button>
        </div>

        <div
          style={{
            margin: '1rem 0',
          }}
        >
          <Input
            name="rating"
            value={rating}
            label="Minimum rating"
            onChange={handleRatingChange}
          />
        </div>

        <Movies movies={filteredMovies} />
      </div>
    </div>
  );
}
