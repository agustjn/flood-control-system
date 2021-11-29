<template>
<h1> 
    Meeting Point View
</h1>
<Map/>
    

</template>


<script>
import Map from '../map/Map'
export default { 
    name:'meeting-index',
    components:{Map},
    data() {  
        return { 
            points: [ ],
            errors:[ ]
        }
    },
    async created() { 
        const response = await fetch("https://admin-grupo3.proyecto2021.linti.unlp.edu.ar/api/points/all");
        const data = await response.json();
        console.log(data);
    }


}
</script>


<style>

</style>