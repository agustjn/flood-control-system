//constantes
const initialLat = -34.9187;
const initialLng = -57.956;
const mapLayerUrl = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';

export function Map({selector, addSearch}){
    let marker;
    let map;

    initializeMap(selector);

    if(addSearch){
        addSearchControl();
    };

    map.addEventListener('click', (e) => {addMarker(e.latlng)});

    //creacion del mapa
    function initializeMap(selector){
        map = L.map(selector).setView([initialLat, initialLng], 13);
        L.tileLayer(mapLayerUrl).addTo(map);
    };

    //comportamiento
    function addMarker({coordinates_lat, coordinates_long}) {
        if (marker) {
            marker.remove();
        };

        marker = L.marker([coordinates_lat, coordinates_long]).addTo(map);
    };

    function addSearchControl() {
        L.control.scale().addTo(map);
        let searchControl = new L.esri.Controls.Geosearch().addTo(map);

        let results = new L.LayerGroup().addTo(map);

        searchControl.on('results', (data) => {
            results.clearLayers();

            if (data.results.lenght > 0) {
                addMarker(data.results[0].latlng);
            }
        });
    };

}