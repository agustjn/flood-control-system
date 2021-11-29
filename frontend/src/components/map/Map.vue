<template>
  <l-map style="height: 400px" :zoom="zoom" :center="center">
    <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>

            <div v-for="(point, index) in points_data" :key="index">
            <l-marker :lat-lng="formatCoordinates(point)" name="Hi!!" v-on:click="eventOnClick">
                <l-tooltip>
                    <ul>
                        <li><strong>{{ point.name }}</strong></li>
                        <li><strong>{{ point.address }}</strong></li>
                        <li><strong>{{ point.phone }}</strong></li>
                        <li><strong>{{ point.email }}</strong></li>
                    </ul>                    
                </l-tooltip>
            </l-marker>
            </div>
  </l-map>
</template>

<script>
import { LMap, LTileLayer, LMarker, LTooltip } from "@vue-leaflet/vue-leaflet";

export default {
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LTooltip,
  },
  props: ["points_data", "email", "name", "phone" ],
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
    eventOnClick() { 
        this.address = "123"
    }
  },
};
</script>
