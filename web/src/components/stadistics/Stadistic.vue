<template>
 <h1> 
     Estadisticas vista
     <div class="container mt-4" v-if="isCreated">
         <div class="card text-white bg-info mb-3" v-for="(denuncia, index) in info" :key="index">
             <p class="card-text" addCategory(denuncia.category)>
            Denuncias: <strong>{{denuncia}}</strong>
          </p>
        </div>
        {{respuesta}}
        <Doughnuts :denuncias_data="info" />
        <div class="container mt-5">
      <div class="card text-white bg-info mb-3" v-for="(denuncia, index) in info" :key="index">
        <div class="card-header">"informacion de muestra"</div>
        <div class="card-body">
          <h5 class="card-title">{{denuncia.category}} </h5>
          <p class="card-text">
            Descripcion: <strong>{{denuncia.description}}</strong>
          </p>
          <p>Estado: <strong>{{denuncia.status}}</strong> </p>
        </div>
      </div>
</div>
        
        
        
    </div>
    <div v-else>
        <h1>Cargando datos..</h1>
        <div class="d-flex justify-content-center">
          <div class="spinner-border" role="status">
            <span class="sr-only"></span>
          </div>
        </div>
    </div>
 </h1>

</template>


<script>

import axios from 'axios'
// import Doughnuts from './Doughnuts'
export default { 
    

data (){

    return {
        info: [],
        isCreatedInfo: false,
        resultado:{}
        
    }
},
async created (){
    // const response =
     axios
        .get('http://127.0.0.1:5000/api/stadistics/')
        .then(response => (this.info = response.data))
        // const data = await response.json();
        // this.info = data;
        this.resultado = addCategory();
    
        this.isCreatedInfo=true;
    // const dataOfCategory = await this.info.json();
    // this.arrCategoria = dataOfCategory;
    // const localizarTodasLasInstancias = (propiedad,valor) => {return data.filter( element => {
    //     return element[propiedad] === valor;
    // })}
    // console.log('todas');
    // console.log(localizarTodasLasInstancias('category', 2));
},
computed:{
    isCreated(){
        return this.isCreatedInfo;
    }



},
methods:{
    addCategory(categoria){
        
        // if (category in this.resultado):
        //      this.resultado[category]=+ 1;
        //  else:
        //      this.resultado[category]=1;
                
                
    }
}
}
</script>


<style>

</style>