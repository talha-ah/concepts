import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

import App from './App';

describe('Filter test', () => {
  it('renders filter input', async () => {
    const user = userEvent.setup();

    // Arrange
    render(<App />);

    // Act
    screen.findByLabelText('Minimum rating');

    // Assert
    expect(screen.getByTestId('rating')).toHaveValue(0);

    // Act
    await user.type(screen.getByTestId('rating'), '7');

    // Assert
    expect(screen.getByTestId('rating')).toHaveValue(7);
  });
});
