<template>

<h1> 

    Flood Zones View
    
</h1>

<div class="container mt-4" v-if="isCreated">
    <Map :zones_data="zones" />
</div>
<div v-else>
    <h1>Cargando mapa..</h1>
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