<template>
  <h1 class="title">Denunciar</h1>
  <form
    v-on:submit.prevent="submitDenuncia">
    <div style="width: 50%; float: left">
      <div>
        <label class="form-label" for="">Titulo: </label>
        <input
          class="form-input"
          type="text"
          placeholder="titulo"
          v-model="form.title"
        />
      </div>
      <div>
        <label class="form-label" for="">Categoria: </label>

        <select v-model="form.category">
          <option disabled value="">seleccione categoria</option>
          <option>Alcantarillas</option>
          <option>Basura</option>
          <option>Otros</option>
        </select>
      </div>
      <div>
        <span>Descripción: </span>
        <textarea
          v-model="form.description"
          placeholder="ingrese una descripción de la denuncia"
        ></textarea>
      </div>
      <div>
        <label class="form-label" for="">Nombre: </label>
        <input
          class="form-input"
          type="text"
          placeholder="nombre"
          v-model="form.first_name"
        />
      </div>
      <div>
        <label class="form-label" for="">Apellido: </label>
        <input
          class="form-input"
          type="text"
          placeholder="apellido"
          v-model="form.last_name"
        />
      </div>
      <div>
        <label class="form-label" for="">Telefono: </label>
        <input
          class="form-input"
          type="text"
          placeholder="telefono"
          v-model="form.phone"
        />
      </div>
      <div>
        <label class="form-label" for="">E-mail: </label>
        <input
          class="form-input"
          type="text"
          placeholder="mail"
          v-model="form.email"
        />
      </div>
    </div>
    <div style="height: 400px; width: 50%; float:right">
      <l-map
        v-if="showMap"
        :zoom="zoom"
        :center="center"
        :options="mapOptions"
        style="height: 80%"
        @update:center="centerUpdate"
        @update:zoom="zoomUpdate"
        @click="addMarker"
      >
        <l-tile-layer :url="url" :attribution="attribution" />
        <l-marker :lat-lng="withPopup" v-model="coordinates">
          <l-popup>
            <div @click="innerClick">I am a popup</div>
          </l-popup>
        </l-marker>
      </l-map>
    </div>
    <div>
      <button type="submit" class="btn btn-primary">Generar denuncia</button>
    </div>
  </form>
</template>

<script>
import { latLng } from "leaflet";
import { LMap, LTileLayer, LMarker, LPopup } from "@vue-leaflet/vue-leaflet";
import axios from "axios";

export default {
  name: "Example",
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LPopup,
  },
  data() {
    return {
      coordinates: [],
      form: {
        title: "",
        category: "",
        description: "",
        coordinates: "",
        first_name: "",
        last_name: "",
        phone: "",
        email: "",
      },
      zoom: 13,
      center: [-34.9214, -57.9544],
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      withPopup: {},

      currentZoom: 11.5,
      currentCenter: latLng(),

      mapOptions: {
        zoomSnap: 0.5,
      },
      showMap: true,
    };
  },
  methods: {
    zoomUpdate(zoom) {
      this.currentZoom = zoom;
    },
    centerUpdate(center) {
      this.currentCenter = center;
    },

    innerClick() {
      alert("Click!");
    },

    addMarker(e) {
      // this.form.coordinates_latitude = e.latlng["lat"];
      // this.form.coordinates_longitude = e.latlng["lng"];
      this.form.coordinates = e.latlng["lat"] + "," + e.latlng["lng"];
      console.log(this.form.coordinates);
      
      //var mark = {};
      //mark = {id:1, coordinates: [e.latlng['lat'],e.latlng['lng']]};
      //console.log(mark);
      // console.log(e.latlng);
      // console.log(this.withPopup);

      this.withPopup = latLng(e.latlng["lat"], e.latlng["lng"]);
    },

    submitDenuncia() {
      axios
        .post("https://admin-grupo3.proyecto2021.linti.unlp.edu.ar/api/report/", this.form)
        .catch((error) => {
          // error.response.status
          console.log(error);
        });
    },
  },
};
</script>
