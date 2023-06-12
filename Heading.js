import React from 'react'
import { ReactDOM } from 'react-dom/client'
import App from './firstapp/src/App'

ReactDOM.createRoot(
    document.querySelector('#root')
).render(<App/>)


function Heading(){
    let title = "This is some heading text";
    return(
      <h1>{title}</h1>
    );
  };

  