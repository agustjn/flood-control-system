import L from 'leaflet'

const getMap = async() => {  
    const container = await document.getElementById("map");
    var map = L.map('map').setView([51.505, -0.09], 13);
    console.log(map);
    console.log(container);
 
}

getMap();

