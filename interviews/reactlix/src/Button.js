export const Button = ({ children, onClick }) => {
  return (
    <button className="genre" onClick={onClick}>
      {children}
    </button>
  );
};
