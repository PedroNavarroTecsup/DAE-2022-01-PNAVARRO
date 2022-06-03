import React from 'react';
import PosHeader from '../components/PosHeader.js';
import PosCategorias from '../components/PosCategorias.js';
import PosMesas from '../components/PosMesas';
import PosPlatos from '../components/PosPlatos';
import PosBoleta from '../components/PosBoleta';

const PosPos = () => {
	const mesaSeleccionada ={id:'1',nro:'1'};
	return (
		<>
			<PosHeader />
			<main className="pos-container">
				<PosCategorias />
				<section className="tabla">
					<PosMesas />
					<div className="pedido">
						<PosPlatos />
						<PosBoleta objMesa={mesaSeleccionada}/>
					</div>
				</section>
			</main>
		</>
	);
};

export default PosPos;
