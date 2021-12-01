<template>
  <div v-for="(zone , index) in zones_data" :key="index">
    <div v-for="(cord , index) in zone.coordinates" :key="index">
       
    </div>  
  </div>  


  <l-map :zoom="zoom" :center="center" style="height: 500px; width: 100%">
  <l-tile-layer :url="url" :attribution="attribution"/>
    <div v-for="(zone, index) in zones_data" :key="index">
    <l-polygon :lat-lngs="zone.coordinates" name="h" :color="polygon.color"/>
    </div>
  </l-map>
</template>

<script>
import { LMap, LTileLayer, LPolygon } from "@vue-leaflet/vue-leaflet";

 
export default {
  name: "Zones",
  components: {
    LMap,
    LTileLayer,
    LPolygon
  },
  props: ["zones_data"],
  data() {
    return {
      zoom: 12,
      center: [-34.92145, -57.95453],
      polygon: {
        latlngs: [
          [47.2263299, -1.6222],
          [47.21024000000001, -1.6270065],
          [47.1969447, -1.6136169],
          [47.18527929999999, -1.6143036],
          [47.1794457, -1.6098404],
          [47.1775788, -1.5985107],
          [47.1676598, -1.5753365],
          [47.1593731, -1.5521622],
          [47.1593731, -1.5319061],
          [47.1722111, -1.5143967],
          [47.1960115, -1.4841843],
          [47.2095404, -1.4848709],
          [47.2291277, -1.4683914],
          [47.2533687, -1.5116501],
          [47.2577961, -1.5531921],
          [47.26828069, -1.5621185],
          [47.2657179, -1.589241],
          [47.2589612, -1.6204834],
          [47.237287, -1.6266632],
          [47.2263299, -1.6222]
        ],
        color: "#ff00ff",
      },
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
    };
  },
};
</script>
