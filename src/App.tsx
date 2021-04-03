import { useEffect } from "react";
import "./App.css";
import axios from "axios";

function App(): JSX.Element {
  useEffect(() => {
    console.log("hello world");
  }, []);

  return (
    <div className="app">
      <h3>Hello</h3>
    </div>
  );
}

export default App;
