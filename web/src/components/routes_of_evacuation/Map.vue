<template>
  <l-map style="height: 400px" :zoom="zoom" :center="center">
    <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>

            <!-- <div v-for="(point, index) in points_data" :key="index">
            <l-marker :lat-lng="formatCoordinates(point)" name="Hi!!" v-on:click="eventOnClick">
                <l-tooltip>
                    <ul>
                        <li><strong>{{ point.name }}</strong></li>
                        <li><strong>{{ point.address }}</strong></li>
                        <li><strong>{{ point.phone }}</strong></li>
                        <li><strong>{{ point.email }}</strong></li>
                    </ul>                    
                </l-tooltip>
            </l-marker> -->
            <l-polyline v-for="(route, index) in routes_data" :lat-lngs="formatRouteCoordinates(route)" color="red" :key="index"></l-polyline>
                           <div v-for="(route, index)  in routes_data" :key="index">
                 <div v-for="(data, index2) in route" :key="index2">
                    <l-popup v-if="evaluatePopup(index, route.coordinates)" :content="asd" :key="index" />
                 </div>

             </div>
            <!-- </div> -->
  </l-map>
 
</template>

<script>
// import { LMap, LTileLayer, LMarker, LTooltip, LPolyline } from "@vue-leaflet/vue-leaflet";
import { LMap, LTileLayer, LPolyline } from "@vue-leaflet/vue-leaflet";


export default {
  components: {
    LMap,
    LTileLayer,
    LPolyline
  },
  props: ["points_data", "routes_data", "email", "name", "phone" ],
  data() {
    return {
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      attribution:
        '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      zoom: 13,
      center: [-34.9214, -57.9544],
      markerLatLng: [51.504, -0.159],
      address: "",
      show:false
    };
  },
  methods: {
    formatCoordinates(point) {
      return [point.coordinates_latitude, point.coordinates_longitude];
    },
    formatRouteCoordinates(route){  
      const coords = [];
      for (const coor in route.coordinates) {  
        coords.push(Object.values(route.coordinates[coor])); // Object.values() convierte el objeto en array [-34,..., -54,...]
      }
      return coords;
    },
    evaluatePopup(index, coordinates){ 
      console.log(index==0 || index==coordinates.length);

      return index==0 || index==coordinates.length
    }
  },
};
</script>
