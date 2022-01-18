<template>
 <h1> 
     Estadisticas vista
     
 </h1>
 <div>
     {{info}}
     </div>
</template>


<script>

import axios from 'axios'
export default { 
    

data (){
    return {
        info: null
    }
},
mounted (){
    axios
        .get('http://127.0.0.1:5000/api/stadistics/')
        .then(response => (this.info = response))
}
}
</script>


<style>

</style>