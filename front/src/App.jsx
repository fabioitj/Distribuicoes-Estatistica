import { useState, useEffect } from 'react'
import './App.css'
import axios from "axios"
import AccordionDemo from './components/accordion';
import CircularProgress from '@mui/material/CircularProgress';


function App() {

  const [continuas, setContinuas] = useState([]);
  const [discretas, setDiscretas] = useState([]);

  useEffect(() => {
    axios.get("https://flask-production-bd7a.up.railway.app/distribuicoes")
      .then((response) => {
        console.log(response.data);
        setContinuas(response.data[0].func);
        setDiscretas(response.data[1].func);
      });
  }, []);

  return (
      continuas.length == 0 || discretas.length == 0 ? (
        <CircularProgress color='inherit'/>
      ) : (
          <div className='distribuicoes'>
            <div className='continuas' style={{ display: 'flex', gap: '1rem', flexDirection: 'column', height: '100%' }}>
              <h3>Contínuas</h3>
              <AccordionDemo key={0} graphs={continuas}/>
            </div>
            <div className='discretas' style={{ display: 'flex', gap: '1rem', flexDirection: 'column', height: '100%' }}>
              <h3>Discretas</h3>
              <AccordionDemo key={1} graphs={discretas}/>
            </div>
          </div>
      )
  )
}

export default App
