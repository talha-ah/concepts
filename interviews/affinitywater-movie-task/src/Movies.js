import { React } from 'react';

import { MovieCard } from './MovieCard';

export const Movies = ({ movies }) => {
  return (
    <div className="movie">
      {movies.map((movie, i) => (
        <MovieCard key={i} movie={movie} />
      ))}
    </div>
  );
};
