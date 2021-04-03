import { useEffect, useState } from "react";
import "./App.css";
import axios from "axios";

interface IResponse {
  foo: string;
  input: string;
}

function App() {
  const [response, setResponse] = useState<IResponse>();

  useEffect(() => {
    axios.all([axios("/foo"), axios("/bar/3")]).then(([res1, res2]) => {
      console.log(res1, res2);
      setResponse({ foo: res1.data.foo, input: res2.data.input });
    });
  }, []);

  return (
    <div className="app">
      <div>
        <h1>{response?.foo}</h1>
        <h1>{response?.input}</h1>
      </div>
    </div>
  );
}

export default App;
