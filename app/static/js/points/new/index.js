import { Map } from '../../MapSingleMaker.js';

const submitHandler = (event, map) =>{
    if (!map.maker){
        event.preventDefault();
        alert('Debes seleccionar una ubicación en el mapa.');
    }
    else{
        latlng = map.maker.getLatLng();
        document.getElementById('coordinates_lat').setAttribute('value', latlng.lat);
        document.getElementById('coordinates_long').setAttribute('value', latlng.lng);

    }
}

window.onload = () =>{
    const map= new Map({
        selector: 'mapid',
        addSearch: true
    });
    const form = document.getElementById('create-point-form');

    form.addEventListener('submit', (event) => submitHandler(event, map));
}