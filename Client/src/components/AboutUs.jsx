import React from 'react'
import './style.css'
import SovereignKingMS from '../assets/SovereignKingMS.jpg'

const AboutUs = () => {
  return (
    <div className='section'>
      <div className='text'>
        <h1>Sobre nosotros</h1>
        <p>Sovereign King Motor Sports es una empresa ficticia originada en base a una asignación de la asignatura desarrollo de software I. Se encuentra a cargo
          de <font style={{color: '#039257'}}>Juan Jose Rojas, Wilson Andres Mosquera y Mateo Duque.</font> Se trata de un servicio web para un concesionario de autos electricos,
          donde clientes, gerentes, vendedores y jefes de taller pueden acceder para realizar acciones especificas. Su utilidad se basa en la
          facilidad para el manejo de cuestiones como el inventario, donde el proceso se automatiza en cierta medida gracias a los scripts.
        </p>
      </div> 
        <img src={SovereignKingMS} className='SKMS'/>
    </div>
  )
}

export default AboutUs