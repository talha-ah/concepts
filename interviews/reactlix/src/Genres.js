import React from 'react';

import { Genre } from './Genre';

export const Genres = ({ genres, onSelect, selectedGenres }) => {
  return (
    <div className="genres-list">
      {genres.map((genre) => (
        <Genre
          genre={genre}
          key={genre.id}
          onSelect={onSelect}
          selected={selectedGenres.findIndex((g) => g.id === genre.id) !== -1}
        />
      ))}
    </div>
  );
};
