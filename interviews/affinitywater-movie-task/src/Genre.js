export const Genre = ({ genre, onSelect, selected }) => {
  return (
    <div>
      <input
        id={genre.id}
        type="checkbox"
        className="genre"
        name={genre.name}
        checked={selected}
        onChange={() => onSelect(genre)}
      />
      <label htmlFor={genre.id}>{genre.name}</label>
    </div>
  );
};
