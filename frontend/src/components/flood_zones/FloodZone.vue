<template>

<h1> 
    Zonas Inundables
</h1>

<div class="container mt-4" v-if="isCreated">
    <Map :zones_data="zones" />
</div>
<div v-else>
    <h1>Cargando mapa..</h1>
</div>
<br>
<div>
    <table class="table" style="width: 800px; height: 200px;  margin-left: auto; margin-right: auto;">
        <thead>
            <tr>
                <th scope="col">#</th>
                <th scope="col">Nombre</th>
                <th scope="col">Color</th>
                <th scope="col">Opciones</th>
            </tr>
        </thead>
        <tbody v-for="(zone, index) in zones" :key="index" >
            <tr>
                <th scope="row">{{index}}</th>
                <th>{{zone.name}}</th>
                <th :style="{backgroundColor:zone.colour}"></th>
                <th><router-link to="" class="btn btn-primary" > Ver zona </router-link></th>
            </tr>
        </tbody>
    </table>
</div>
</template>


<script>
import Map from './Map'
export default { 
    name:'zones-index',
    components:{Map},
    data() {  
        return { 
            zones: [ ],
            errors:[ ],
            mapIsCreated: false
        }
    },
    async created() { 
        const response = await fetch("https://admin-grupo3.proyecto2021.linti.unlp.edu.ar/api/flood_zones/all");
        const data = await response.json();
        this.zones = data.zonas;  //hago esto porque la api me lo devuelve como zonas[adentro 0{id...}]
        this.mapIsCreated = true;        
        
        
        
    },
    computed: {  
         isCreated () {  
            return this.mapIsCreated;
        }
    },

}
</script>


<style>

</style>