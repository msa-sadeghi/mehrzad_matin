import { useRef } from "react";

function App() {
  const inputRef = useRef(null);
  return (
    <>
      <input ref={inputRef} type="text" name="" id="" />
      <button
        onClick={() => {
          inputRef.current.focus();
        }}
      >
        clickme
      </button>
    </>
  );
}

export default App;
