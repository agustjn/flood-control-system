<template>
  
  <l-map :zoom="zoom" :center="center" style="height: 500px; width: 100%">
  <l-tile-layer :url="url" :attribution="attribution"/>
    <div v-for="(zone, index) in zones_data" :key="index">
    <l-polygon :lat-lngs="zone.coordinates" name="h" :color="zone.colour" :fill="true" :fillColor="zone.colour" :fillOpacity="0.5" />
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
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
    };
  },
};
</script>
