export const Input = ({ name, label, value, onChange }) => {
  return (
    <div>
      <label htmlFor={name} id={`${name}-label`}>
        {label}
      </label>
      <input
        min="0"
        max="10"
        step="0.5"
        id={name}
        type="number"
        value={value}
        onChange={onChange}
        data-testid={name}
      />
    </div>
  );
};
