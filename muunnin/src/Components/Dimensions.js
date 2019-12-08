import React, {useState, useEffect} from 'react';

//Funktio moduuli komponenttien skaalautumiseen
export function Dimensions() {

  const [dimensions, setDimensions] = useState({height: window.innerHeight, width: window.innerWidth});

  const resizeWindow = () => {
    setDimensions(window.innerHeight, window.innerWidth);
  }

  useEffect(() => {
    window.addEventListener('resize', resizeWindow);
    return () => {
        window.removeEventListener('resize', resizeWindow);
    }
}, []);

  return (
    dimensions
  );
}