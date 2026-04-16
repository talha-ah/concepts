import React from 'react';

export const MovieCard = ({ movie }) => {
  const formatGenres = (genres) => {
    let genresString = '';

    for (let i = 0; i < genres.length; i++) {
      genresString += genres[i].name;

      if (i < genres.length - 2) {
        genresString += ', ';
      } else if (i === genres.length - 2) {
        genresString += ' and ';
      }
    }

    return genresString;
  };

  return (
    <div className="movie-card">
      <img
        src={`https://image.tmdb.org/t/p/w500${movie.poster_path}`}
        alt="movie poster"
        className="movie-image"
      />
      <div className="movie-info">
        <h2 className="movie-title">{movie.title}</h2>
        <p className="movie-content">{movie.overview}</p>
        <span className="movie-meta">Rating: {movie.vote_average}/10</span>
        <span className="movie-meta">Popularity: {movie.popularity}</span>

        <span className="movie-meta">Genres: {formatGenres(movie.genres)}</span>
      </div>
    </div>
  );
};
