import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { useEffect } from 'react'
import axios from "axios"


function App() {

  const [beta, setBeta] = useState("");
  const [cauchy, setCauchy] = useState("");
  const [pareto, setPareto] = useState("");
  const [triangular, setTriangular] = useState("");
  const [gumbel, setGumbel] = useState("");

  useEffect(() => {
      axios.get("http://127.0.0.1:5000/distribuicoes")
        .then((response) => {
          console.log(response.data);
          // const newBeta = "data:image/png;base64, " + response.data;
          // console.log(newBeta);
          // setBeta(newBeta);
        });
  }, []);

  return (
    <>
      <img src={beta} style={{ backgroundColor: "red", width: '200px', height: 'auto'}}/>
      <img src={beta} style={{ backgroundColor: "red", width: '200px', height: 'auto'}}/>
      <img src={beta} style={{ backgroundColor: "red", width: '200px', height: 'auto'}}/>
      <img src={beta} style={{ backgroundColor: "red", width: '200px', height: 'auto'}}/>
      <img src={beta} style={{ backgroundColor: "red", width: '200px', height: 'auto'}}/>
    </>
  )
}

export default App
