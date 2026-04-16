import { render, screen } from '@testing-library/react';

import App from './App';

describe('renders App successfully', () => {
  it('Render app', async () => {
    // Arrange
    render(<App />);

    // Assert
    expect(screen.getByText('Now playing')).toBeInTheDocument();
  });
});
