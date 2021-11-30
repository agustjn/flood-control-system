<template>
<h1> 
    Meeting Point View
</h1>
<<<<<<< HEAD
=======
<Map/>
    

>>>>>>> parent of 5ebcf97... Puntos de encuentro con su mapa andando
</template>


<script>
export default { 
<<<<<<< HEAD
    
=======
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


>>>>>>> parent of 5ebcf97... Puntos de encuentro con su mapa andando
}
</script>


<style>

</style>