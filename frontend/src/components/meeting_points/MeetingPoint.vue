<template>
<h1> 
    Meeting Point View
</h1>

<div class="container mt-4" v-if="isCreated">
    <Map :points_data="points" />
</div>
<div v-else>
    <h1>Cargando mapa..</h1>
</div>

    

</template>


<script>
import Map from '../map/Map'
export default { 
    name:'meeting-index',
    components:{Map},
    data() {  
        return { 
            points: [ ],
            errors:[ ],
            mapIsCreated: false
        }
    },
    async created() { 
        const response = await fetch("https://admin-grupo3.proyecto2021.linti.unlp.edu.ar/api/points/all");
        const data = await response.json();
        this.points = data;
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