import { render, screen } from '@testing-library/react';

import { MovieCard } from './MovieCard';

describe('Movie details', () => {
  it('should display all given details about the movie', () => {
    // Arrange
    const movie = {
      adult: false,
      backdrop_path: '/srYya1ZlI97Au4jUYAktDe3avyA.jpg',
      genre_ids: [14, 28, 12],
      genres: ['Adventure', 'Fantasy', 'Action'],
      id: 464052,
      original_language: 'en',
      original_title: 'Wonder Woman 1984',
      overview:
        'Wonder Woman comes into conflict with the Soviet Union during the Cold War in the 1980s and finds a formidable foe by the name of the Cheetah.',
      popularity: 2407.318,
      poster_path: '/8UlWHLMpgZm9bx6QYh0NFoq67TZ.jpg',
      release_date: '2020-12-16',
      title: 'Wonder Woman 1984',
      video: false,
      vote_average: 7,
      vote_count: 3437,
    };

    // Act
    render(<MovieCard movie={movie} />);

    // Assert
    expect(screen.getByText('Rating: 7/10')).toBeInTheDocument();
    expect(screen.getByText('Wonder Woman 1984')).toBeInTheDocument();
    expect(screen.getByText('Popularity: 2407.318')).toBeInTheDocument();
    expect(screen.getByRole('img')).toHaveAttribute(
      'src',
      'https://image.tmdb.org/t/p/w500/8UlWHLMpgZm9bx6QYh0NFoq67TZ.jpg'
    );
  });
});
